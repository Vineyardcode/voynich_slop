#!/usr/bin/env python3
"""
Download all Voynich Manuscript folios and their EVA transcriptions.

Sources:
  - Images: Beinecke Library (Yale) via IIIF Image API
  - Transcription: ZL IVTFF v3b from voynich.nu (EVA alphabet)

Output: folios/ directory with pairs of files per folio:
  - {folio}.png   (manuscript page image, ~2000px)
  - {folio}.txt   (EVA transcription from ZL)
"""

import json
import io
import os
import re
import sys
import time
import urllib.request
from pathlib import Path

# ── Configuration ───────────────────────────────────────────────────────────

MANIFEST_URL = "https://collections.library.yale.edu/manifests/2002046"
ZL_URL = "https://www.voynich.nu/data/ZL3b-n.txt"
IIIF_SIZE = "!2000,2000"   # fit inside 2000×2000 keeping aspect ratio
OUTPUT_DIR = Path("folios")
DELAY_BETWEEN_DOWNLOADS = 0.5  # seconds, be respectful to Beinecke servers

# ── Helpers ─────────────────────────────────────────────────────────────────

def download(url, retries=3, delay=2):
    """Download URL content with retries and exponential backoff."""
    for attempt in range(retries):
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": "VoynichResearch/1.0"}
            )
            with urllib.request.urlopen(req, timeout=120) as resp:
                return resp.read()
        except Exception as e:
            if attempt < retries - 1:
                wait = delay * (attempt + 1)
                print(f"  Retry {attempt+1}/{retries} for {url}: {e}")
                time.sleep(wait)
            else:
                raise


def ensure_pillow():
    """Make sure Pillow is available, install if missing."""
    try:
        from PIL import Image
        return Image
    except ImportError:
        print("Installing Pillow for JPEG→PNG conversion...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
        from PIL import Image
        return Image


# ── IIIF Manifest Parsing ──────────────────────────────────────────────────

def parse_manifest(manifest_json):
    """
    Extract (label, image_id) pairs from a IIIF v3 manifest.
    Returns list of tuples: [(label, image_id), ...]
    """
    manifest = json.loads(manifest_json)
    results = []

    for canvas in manifest.get("items", []):
        # Get label
        label_dict = canvas.get("label", {})
        label = None
        for lang_labels in label_dict.values():
            if lang_labels:
                label = lang_labels[0]
                break
        if not label:
            continue

        # Get image ID from canvas metadata
        image_id = None
        for meta in canvas.get("metadata", []):
            meta_label = ""
            for vals in meta.get("label", {}).values():
                if vals:
                    meta_label = vals[0]
                    break
            if meta_label == "Image ID":
                for vals in meta.get("value", {}).values():
                    if vals:
                        image_id = vals[0]
                        break
                break

        # Fallback: extract from rendering URL
        if not image_id:
            for rendering in canvas.get("rendering", []):
                rid = rendering.get("id", "")
                match = re.search(r"/iiif/2/(\d+)/", rid)
                if match:
                    image_id = match.group(1)
                    break

        if image_id and label:
            results.append((label, image_id))

    return results


def is_manuscript_folio(label):
    """True if label is an actual manuscript folio (not cover/spine/flyleaf)."""
    ll = label.lower()
    for skip in ["cover", "flyleaf", "spine", "binding"]:
        if skip in ll:
            return False
    return bool(re.search(r"\d+[rv]", ll))


def label_to_filename(label):
    """
    Convert a manifest label to a clean filename stem.
    Examples:
      "1r"                         → "f1r"
      "85v and 86r (foldout)"     → "f85v_86r_foldout"
      "89v (part) and 90r"        → "f89v_part_90r"
      "86v (part) (part of ...)"  → "f86v_part"
    """
    s = label.strip()
    # Normalize whitespace and parens
    s = re.sub(r"\s+", " ", s)
    s = s.replace("(", "").replace(")", "")
    s = re.sub(r"\s*part of [\w\- ]+foldout\s*", "", s)
    # Replace connectors
    s = s.replace(" and ", "_")
    s = s.replace(" ", "_")
    # Remove trailing underscores
    s = s.strip("_")
    # Prefix with 'f' if not already
    if not s.startswith("f"):
        s = "f" + s
    return s


# ── IVTFF Transcription Parsing ────────────────────────────────────────────

def parse_ivtff(text):
    """
    Parse an IVTFF file into a dict of { folio_key: [lines] }.
    folio_key is like "f1r", "f1v", "fRos", etc.
    """
    folios = {}
    current_key = None

    for line in text.splitlines():
        # Page header: <f1r>  or  <f1r> $I=H $Q=A ...
        m = re.match(r"^<(f\w+)>", line)
        if m:
            current_key = m.group(1)
            if current_key not in folios:
                folios[current_key] = []
            folios[current_key].append(line)
            continue

        # File-level comments/headers (before any folio)
        if current_key is None:
            continue

        folios[current_key].append(line)

    # Join each folio's lines
    return {k: "\n".join(v) for k, v in folios.items()}


def extract_folio_keys_from_label(label):
    """
    Extract possible IVTFF folio keys from a Beinecke manifest label.
    E.g. "85v and 86r (foldout)" → ["f85v", "f86r"]
         "1r"                    → ["f1r"]
         "Rosettes foldout"      → ["fRos"]
    """
    ll = label.lower()

    # Special case: Rosettes
    if "rosette" in ll:
        return ["fRos"]

    # Find all folio references: numbers followed by r or v, optionally with
    # a trailing digit for sub-pages (e.g. "67r1", "67r2")
    matches = re.findall(r"(\d+[rv]\d*)", ll)
    if matches:
        return ["f" + m for m in matches]

    return []


def find_transcription(label, transcriptions):
    """
    Find and combine transcriptions for all folio keys matching a manifest label.
    """
    keys = extract_folio_keys_from_label(label)
    parts = []
    for key in keys:
        if key in transcriptions:
            parts.append(transcriptions[key])
        else:
            # Try without trailing digits or with them
            # Some IVTFF files use f67r1, f67r2 for foldout panels
            for tk in sorted(transcriptions.keys()):
                if tk.startswith(key):
                    parts.append(transcriptions[tk])
    return "\n\n".join(parts) if parts else None


# ── Main ────────────────────────────────────────────────────────────────────

def main():
    Image = ensure_pillow()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # ── 1. Download and parse IIIF manifest ─────────────────────────────
    print("⏳ Downloading IIIF manifest from Beinecke Library...")
    manifest_data = download(MANIFEST_URL)
    all_items = parse_manifest(manifest_data)
    print(f"   Found {len(all_items)} items in manifest")

    # Filter to actual manuscript folios
    ms_folios = [(lbl, iid) for lbl, iid in all_items if is_manuscript_folio(lbl)]
    print(f"   Filtered to {len(ms_folios)} manuscript folios\n")

    # ── 2. Download and parse transcription file ────────────────────────
    print("⏳ Downloading ZL transcription (EVA, IVTFF v3b)...")
    zl_raw = download(ZL_URL)
    zl_text = zl_raw.decode("latin-1")
    transcriptions = parse_ivtff(zl_text)
    print(f"   Parsed {len(transcriptions)} folio transcriptions\n")

    # ── 3. Download images and write transcription files ────────────────
    total = len(ms_folios)
    downloaded = 0
    skipped = 0
    errors = 0

    for i, (label, image_id) in enumerate(ms_folios, 1):
        filename = label_to_filename(label)
        img_path = OUTPUT_DIR / f"{filename}.png"
        txt_path = OUTPUT_DIR / f"{filename}.txt"

        # Download image if not already present
        if not img_path.exists():
            img_url = (
                f"https://collections.library.yale.edu/iiif/2/"
                f"{image_id}/full/{IIIF_SIZE}/0/default.jpg"
            )
            print(f"[{i:3d}/{total}] ⬇  {label:30s}", end="", flush=True)
            try:
                img_data = download(img_url)
                img = Image.open(io.BytesIO(img_data))
                img.save(str(img_path), "PNG", optimize=True)
                w, h = img.size
                size_mb = img_path.stat().st_size / (1024 * 1024)
                print(f"  → {filename}.png  ({w}×{h}, {size_mb:.1f} MB)")
                downloaded += 1
            except Exception as e:
                print(f"  ✗ ERROR: {e}")
                errors += 1
                continue
            time.sleep(DELAY_BETWEEN_DOWNLOADS)
        else:
            print(f"[{i:3d}/{total}] ✓  {label:30s}  (already downloaded)")
            skipped += 1

        # Write transcription file
        transcription = find_transcription(label, transcriptions)
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(f"# Voynich Manuscript — Folio {label}\n")
            f.write(f"# EVA transcription (ZL IVTFF v3b)\n")
            f.write(f"# Source: voynich.nu — René Zandbergen\n")
            f.write(f"# Alphabet: EVA (European Voynich Alphabet)\n")
            if transcription:
                f.write(f"\n{transcription}\n")
            else:
                keys_tried = extract_folio_keys_from_label(label)
                f.write(f"\n# No transcription available for this folio\n")
                f.write(f"# Keys attempted: {', '.join(keys_tried)}\n")
                f.write(f"# (May be illustration-only, or use different key)\n")

    # ── Summary ─────────────────────────────────────────────────────────
    print(f"\n{'='*60}")
    print(f"Done!  {OUTPUT_DIR}/")
    print(f"  Downloaded : {downloaded}")
    print(f"  Skipped    : {skipped} (already existed)")
    print(f"  Errors     : {errors}")
    print(f"  Total folios: {total}")
    txt_count = len(list(OUTPUT_DIR.glob("*.txt")))
    png_count = len(list(OUTPUT_DIR.glob("*.png")))
    print(f"  PNG files  : {png_count}")
    print(f"  TXT files  : {txt_count}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
