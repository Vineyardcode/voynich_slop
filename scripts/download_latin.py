#!/usr/bin/env python3
"""Download proper Latin texts to replace English ones in latin_texts/"""

import urllib.request
import re
import html
import os
import time

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'latin_texts')

def fetch_clean(url):
    """Fetch URL and strip HTML to get clean text."""
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = urllib.request.urlopen(req).read().decode('latin-1')
    # Remove script/style
    data = re.sub(r'<script[^>]*>.*?</script>', '', data, flags=re.DOTALL|re.IGNORECASE)
    data = re.sub(r'<style[^>]*>.*?</style>', '', data, flags=re.DOTALL|re.IGNORECASE)
    # Replace <br> and <p> with newlines
    data = re.sub(r'<br\s*/?>', '\n', data, flags=re.IGNORECASE)
    data = re.sub(r'<p[^>]*>', '\n', data, flags=re.IGNORECASE)
    data = re.sub(r'</p>', '\n', data, flags=re.IGNORECASE)
    # Strip all other tags
    data = re.sub(r'<[^>]+>', '', data)
    # Decode HTML entities
    data = html.unescape(data)
    # Clean up whitespace
    lines = data.strip().split('\n')
    lines = [l.strip() for l in lines]
    cleaned = []
    for l in lines:
        if l:
            cleaned.append(l)
    return '\n'.join(cleaned)


def extract_latin_body(text):
    """Extract just the Latin content, removing navigation/headers."""
    lines = text.split('\n')
    # Find first line starting with [ (section marker)
    start = 0
    for j, line in enumerate(lines):
        if line.startswith('[') and len(line) > 1 and (line[1].isdigit() or line[1] == ' '):
            start = j
            break
    # Find last navigation line
    end = len(lines)
    for j in range(len(lines)-1, -1, -1):
        if 'The Latin Library' in lines[j] or 'The Classics Page' in lines[j]:
            end = j
            break
    return '\n'.join(lines[start:end])


def download_caesar():
    """Download Caesar's De Bello Gallico, Books 1-7."""
    print('Downloading Caesar De Bello Gallico...')
    book_names = ['PRIMVS', 'SECVNDVS', 'TERTIVS', 'QVARTVS',
                  'QVINTVS', 'SEXTVS', 'SEPTIMVS']
    all_text = ''
    for i in range(1, 8):
        url = f'https://www.thelatinlibrary.com/caesar/gallic/gall{i}.shtml'
        print(f'  Liber {book_names[i-1]}...')
        text = fetch_clean(url)
        body = extract_latin_body(text)
        all_text += f'\n\nLIBER {book_names[i-1]}\n\n{body}'
        time.sleep(0.5)

    outpath = os.path.join(OUTPUT_DIR, 'caesar.txt')
    with open(outpath, 'w', encoding='utf-8') as f:
        f.write('C. IVLI CAESARIS COMMENTARIORVM DE BELLO GALLICO\n')
        f.write('Source: The Latin Library (thelatinlibrary.com)\n')
        f.write('Language: Latin\n\n')
        f.write(all_text.strip())
        f.write('\n')
    print(f'  Written to {outpath} ({len(all_text)} chars)')


def download_pliny():
    """Download Pliny the Elder's Naturalis Historia, Books 1-5 (what's available)."""
    print('Downloading Pliny Naturalis Historia...')
    all_text = ''
    for i in range(1, 6):
        url = f'https://www.thelatinlibrary.com/pliny.nh{i}.html'
        print(f'  Book {i}...')
        try:
            text = fetch_clean(url)
            body = extract_latin_body(text)
            if not body.strip():
                # Some pages may format differently - just take all content
                body = text
            all_text += f'\n\nLIBER {i}\n\n{body}'
        except Exception as e:
            print(f'  Error fetching book {i}: {e}')
        time.sleep(0.5)

    outpath = os.path.join(OUTPUT_DIR, 'pliny.txt')
    with open(outpath, 'w', encoding='utf-8') as f:
        f.write('C. PLINII SECVNDI NATVRALIS HISTORIA\n')
        f.write('Source: The Latin Library (thelatinlibrary.com)\n')
        f.write('Language: Latin\n\n')
        f.write(all_text.strip())
        f.write('\n')
    print(f'  Written to {outpath} ({len(all_text)} chars)')


def download_vulgate_genesis():
    """Download Vulgate Genesis in Latin."""
    print('Downloading Vulgate Genesis...')
    url = 'https://www.thelatinlibrary.com/bible/genesis.shtml'
    text = fetch_clean(url)
    body = extract_latin_body(text)
    if not body.strip():
        body = text

    outpath = os.path.join(OUTPUT_DIR, 'vulgate_genesis.txt')
    with open(outpath, 'w', encoding='utf-8') as f:
        f.write('BIBLIA SACRA VVLGATAE EDITIONIS - GENESIS\n')
        f.write('Source: The Latin Library (thelatinlibrary.com)\n')
        f.write('Language: Latin\n\n')
        f.write(body.strip())
        f.write('\n')
    print(f'  Written to {outpath} ({len(body)} chars)')


if __name__ == '__main__':
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    download_caesar()
    download_pliny()
    download_vulgate_genesis()
    print('\nDone! All Latin texts downloaded.')
