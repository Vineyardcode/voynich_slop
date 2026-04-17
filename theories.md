# Voynich Manuscript — Comprehensive Theory Catalog

Compiled from: Voynich Ninja forum (Theories & Solutions, 7 pages, ~200+ threads),
Wikipedia, Cipher Mysteries (ciphermysteries.com), Reddit r/voynich, and academic sources.

Probability scores reflect community consensus, statistical evidence, and compatibility
with known physical/codicological facts (C14 dating 1404–1438, Italian provenance indicators,
two scribal hands, Currier A/B language split, low character entropy ~1.92 bits).

**Scoring key:**
- **1/10** — Debunked or fundamentally incompatible with established facts
- **2/10** — Extreme speculation, no supporting evidence
- **3/10** — Interesting but fails basic tests
- **4/10** — Some merit but major unresolved problems
- **5/10** — Plausible but undemonstrated
- **6/10** — Moderate support, survives some scrutiny
- **7/10** — Strong support from multiple evidence lines
- **8/10** — High compatibility with known facts, few objections

NOTE: No theory has ever been independently verified. All scores are relative.
A "high" score means "less implausible" — not "probably correct."

---

## A. MACRO-THEORIES: What IS the manuscript?

### A1. Cipher of a European Natural Language
**Probability: 5/10**
The 20th-century consensus position (NSA/Friedman team, Tiltman). Text encodes
a natural language (Latin, Italian, German, etc.) via some cipher algorithm.
- **For:** VMS has Zipfian word distribution, semantic clustering (Montemurro & Zanette 2013),
  topic-illustration correlation (Sterneck et al. 2021).
- **Against:** No known period cipher reproduces the VMS statistical fingerprint.
  Simple substitution excluded (wrong letter frequencies). Polyalphabetic ciphers produce
  flatter distributions. Character-level conditional entropy (h2 ≈ 2) is far below
  natural language (3–4). Bowern & Lindemann (2021) found VMS inconsistent with
  substitution or polyalphabetic ciphers.
- **Source:** Friedman (1950s), D'Imperio (1978), Pelling (2006), Bowern & Lindemann (2021)
- **Forum:** Ongoing discussion, no consensus solution achieved

### A2. Verbose/Complex Cipher
**Probability: 5/10**
A cipher where single plaintext letters map to multi-character groups (e.g. "ol", "aiin").
Includes the Naibbe cipher (2025) which demonstrated a historically plausible verbose
substitution cipher can produce VMS-like statistical properties from Latin/Italian.
- **For:** Naibbe cipher (magnesium, Voynich Ninja) published in Cryptologia (2025),
  reproduces many VMS statistical features. Explains verbose character groups.
  Compatible with 15th-century methods.
- **Against:** Proof of concept only — author explicitly does not claim it IS the cipher.
  No actual decipherment produced. Still struggles with some features (exact entropy match).
- **Source:** Greshko (2025, Cryptologia), Pelling (cipher structure analysis)
- **Forum:** Voynich Ninja — ["The Naibbe cipher"](https://www.voynich.ninja/thread-4848.html) (83 replies, 29,752 views, very active)

### A3. Constructed/Artificial Language
**Probability: 5/10**
Friedman's alternative hypothesis: VMS is written in an invented philosophical
or taxonomic language, predating Wilkins (1668) by two centuries.
- **For:** Over-regular paradigm structure (our Phase 1 analysis: paradigm fill at
  100th percentile vs shuffled controls). Hebrew-like agglutinative morphology that
  is "too regular" to be natural language. Suffix categories divide cleanly into
  bimodal classes. Category-based prefix structure (plant names sharing prefixes)
  would explain repetitive text.
- **Against:** No constructed language from before 1600 is known. Each category should
  share prefixes — not yet demonstrated convincingly. Low information per word is
  unusual for taxonomic systems. Tiltman (1967) found it a "cumbersome mixture of
  different kinds of substitution," not a clean system.
- **Source:** Friedman (1950), Tiltman (1967), Bowern & Lindemann (2021)
- **Forum:** Various threads, Jorge_Stolfi is a prominent proponent

### A4. Shorthand / Abbreviation System
**Probability: 5/10**
Text is heavily abbreviated natural language (Latin, vernacular) — like a pharmacist's
or physician's personal notation system.
- **For:** Our pre-phase analysis: 3/4 shorthand tests passed (frame-constant runs,
  section divergence, formulaic templates). Nicholas Gibbs (2017) proposed abbreviated
  Latin pharmacopoeia. VMS word entropy is low (~10 bits), consistent with compressed notation.
  Voynich Ninja threads: ["Lingua Volgare Shorthand"](https://www.voynich.ninja/thread-4513.html) (ginocaspari, 55 replies),
  ["Specialized shorthand and not a language"](https://www.voynich.ninja/thread-5200.html) (DerrickMay), ["The Voynich-Ms as a
  concatenation of abbreviations"](https://www.voynich.ninja/thread-4008.html) (Helmut Winkler, 69 replies, 45K views).
  Tironian shorthand hypothesis tested structurally (CorwinFr, 2026).
- **Against:** Slot dependence (NMI = 0.4164) is too high for pure abbreviation —
  the system encodes grammatical relationships. Gibbs's specific proposal was widely
  rejected as incomplete/circular.
- **Source:** Feely (1943), Gibbs (2017), ginocaspari (Lingua Volgare), CorwinFr (Tironian)
- **Forum:** Voynich Ninja — multiple active threads

### A5. Hoax / Meaningless Text
**Probability: 4/10**
The text is deliberate gibberish, produced mechanically or by copying/recombining
meaningless elements. Purpose: fraud (sell to Rudolf II), intellectual prank,
or art project.
- **For:** Gordon Rugg (2003) showed Cardan grille + table can produce VMS-like
  text. Schinner (2007) found statistical properties more consistent with stochastic
  generation than natural language. Timm & Schinner (2019) showed self-citation
  process reproduces VMS features. Gaskell & Bowern (2022) found human-produced
  gibberish has similar unusual properties. VMS character entropy anomalously low.
- **Against:** Montemurro & Zanette (2013) found semantic clustering unlikely in a hoax.
  Sterneck et al. (2021) found text clusters match illustration topics. Cardan grille
  invented c. 1550, postdates VMS by 100+ years. Bowern dismisses pure gibberish.
  The manuscript is physically expensive (240 vellum pages) — excessive for a hoax.
  Rugg argues it could be done but hasn't proved it WAS done.
- **Source:** Rugg (2003, 2016), Schinner (2007), Timm & Schinner (2019), Gaskell & Bowern (2022)
- **Forum:** Voynich Ninja — ["Just a hoax?"](https://www.voynich.ninja/thread-5230.html) (Tessa9, 35 replies), ["Speculative fraud hypothesis"](https://www.voynich.ninja/thread-4877.html)
  (dexdex, 92 replies, 29K views), ["How could you prove that VM is gibberish?"](https://www.voynich.ninja/thread-5051.html) (Rafal, 28 replies)

### A6. Steganographic Vehicle
**Probability: 3/10**
The visible text is camouflage; the real message is hidden in spacing, letter
positions, illustrations, or other inconspicuous features.
- **For:** Trithemius described steganography in 1499, contemporary with VMS.
  Could explain why text "looks like language" but resists decipherment.
- **Against:** Text and letters are NOT on a regular grid, making Cardan grille
  extraction impractical. Hard to prove or disprove. No one has extracted a
  convincing hidden message.
- **Source:** D'Imperio (1978)
- **Forum:** Voynich Ninja — ["Segmented Steganography"](https://www.voynich.ninja/thread-5121.html) (R. Sale)

### A7. Glossolalia / Outsider Art / Visionary Writing
**Probability: 2/10**
The text was produced in a trance state, inspired by visions (like Hildegard von Bingen's
Lingua Ignota), automatic writing, or mental illness.
- **For:** Kennedy & Churchill (2004) noted the obsessive, trance-like nature of the
  illustrations. Would explain resistance to decipherment.
- **Against:** Statistical structure is too consistent for automatic writing.
  The manuscript shows careful planning (quire structure, bifolio arrangement).
  Two scribal hands suggest collaboration, not individual trance.
  Theory is "virtually impossible to prove or disprove" (Wikipedia).
- **Source:** Kennedy & Churchill (2004)

### A8. Visual Code / No Text
**Probability: 2/10**
The glyphs are not text at all but visual symbols encoding astronomical/astrological
positions, musical notation, or mathematical relationships.
- **For:** Antonio García Jiménez (Voynich Ninja, 1,699 replies, 1M+ views — the
  most-viewed theory thread) proposes visual code interpretation.
- **Against:** Text has clear word-level and character-level statistical structure
  consistent with SOME kind of encoding, not arbitrary symbol placement.
  Zipfian distribution is hard to produce from non-linguistic symbols.
- **Forum:** Voynich Ninja — ["No text, but a visual code"](https://www.voynich.ninja/thread-2384.html) (Antonio García Jiménez,
  170 pages, enormously active but divisive)

---

## B. LANGUAGE IDENTIFICATION THEORIES

### B1. Latin (plain, abbreviated, or encoded)
**Probability: 5/10**
The underlying language is Latin — the lingua franca of 15th-century Europe.
Multiple variants: abbreviated Latin, vowelless Latin, Latin via verbose cipher.
- **For:** Expected language for a 15th-century medical/botanical text. Naibbe cipher
  demonstrates Latin can produce VMS-like output. Month names on zodiac pages are
  Latin-script with Romance-language spelling.
- **Against:** No convincing full-text decipherment. Vowelless Latin tested extensively
  (farmerjohn, Voynich Ninja, 139 replies) without breakthrough.
- **Forum:** ["Can VM be written in vowelless Latin?"](https://www.voynich.ninja/thread-758.html) (farmerjohn, 139 replies, 108K views),
  ["VMS to pseudo-latin"](https://www.voynich.ninja/thread-5072.html) (bi3mw)

### B2. Italian / Proto-Romance
**Probability: 4/10**
Gerard Cheshire (2019) proposed "proto-Romance" language. Others propose Italian dialects.
Caspari & Faccini (2025) proposed Lingua Volgare shorthand encoding Italian.
- **For:** Zodiac month labels suggest Romance-language spelling. Italian provenance
  (binding, stylistic analysis). Naibbe cipher also works with Italian input.
- **Against:** Cheshire's work was retracted by University of Bristol, criticized as
  circular by Ars Technica and multiple experts. "Proto-Romance" is not a recognized
  linguistic category in the way Cheshire uses it.
- **Source:** Cheshire (2019, retracted), Caspari & Faccini (2025)
- **Forum:** Voynich Ninja — ["Lingua Volgare Shorthand"](https://www.voynich.ninja/thread-4513.html) (ginocaspari, 55 replies)

### B3. German / Bavarian
**Probability: 4/10**
The underlying language is a German dialect, possibly Bavarian/Alemannic.
JoJo_Jost's active theory thread on Voynich Ninja.
- **For:** Russian mathematical analysis (Keldysh Institute, 2016) identified
  German/Danish as statistically feasible donor language. Some herbal traditions
  link to central European practices. VMS may have central European provenance.
  Month names could have Germanic influence.
- **Against:** Italian provenance indicators (binding, codicology). The Keldysh
  paper discarded spaces, which Pelling notes is anachronistic (spaces weren't
  removed from ciphertexts until 50–100 years later).
- **Source:** Keldysh Institute (2016), JoJo_Jost
- **Forum:** Voynich Ninja — ["Why and how the text could be Bavarian"](https://www.voynich.ninja/thread-5312.html) (JoJo_Jost,
  154 replies, 15K views), ["Could incantations explain some problems"](https://www.voynich.ninja/thread-5161.html) (JoJo_Jost)

### B4. Hebrew / Judaeo-Greek
**Probability: 4/10**
Various proposals that the underlying language is Hebrew, or a Jewish-language hybrid.
- **For:** Kondrak & Hauer (2018, U of Alberta) used AI to identify Hebrew as most
  likely language (alphagram-encoded). Our own Phase 1 analysis found Hebrew-like
  agglutinative morphology with mishkal patterns. Hannig (2020) proposed "special
  Hebrew." geoffreycaveney proposed both Judaeo-Greek (221 replies, 160K views)
  and later Middle English. LisaFaginDavis discussed Hebrew proposals (69 replies, 62K views).
- **Against:** Kondrak's medieval manuscript experts were "not convinced." Our analysis
  found the morphology is TOO regular for natural Hebrew — it's a constructed system
  possibly inspired by Hebrew grammar. Labels prefer prefixes (73% vs 50% text) —
  opposite of Hebrew noun prediction.
- **Source:** Kondrak & Hauer (2018), Hannig (2020), geoffreycaveney, Torsten
- **Forum:** Voynich Ninja — ["geoffreycaveney's Judaeo-Greek theory"](https://www.voynich.ninja/thread-2697.html) (221 replies, 160K views),
  ["Anyone seen this proposed solution yet? More Hebrew..."](https://www.voynich.ninja/thread-3250.html) (LisaFaginDavis, 69 replies)

### B5. Greek
**Probability: 3/10**
Ruby Novacna's ongoing theory thread, among others.
- **For:** Active research thread with visual/glyph comparisons.
- **Against:** Greek script is well-known; glyph shapes don't match standard Greek.
  Statistical properties not demonstrated to match.
- **Forum:** Voynich Ninja — ["Ruby's Greek Thread"](https://www.voynich.ninja/thread-3904.html) (218 replies, 73K views)

### B6. Old Czech / Slavic
**Probability: 3/10**
Various proposals linking VMS to Czech, Slovenian, or other Slavic languages.
Elena Konovalova proposed Old Czech technical manual.
Cvetka Kocjan proposed Slovenian.
- **For:** Georg Baresch (earliest confirmed owner) was from Prague. Bohemian provenance
  for at least part of the ownership chain. Some illustrations potentially linked
  to central European herbal traditions.
- **Against:** C14 dating and stylistic analysis point to Italian origin, predating
  Baresch by 200 years. No convincing decipherment.
- **Source:** Konovalova, Cvetka Kocjan
- **Forum:** Voynich Ninja — ["Cvetka's Slovenian Theory Thread"](https://www.voynich.ninja/thread-4758.html) (107 replies, 33K views),
  ["Voynich Manuscript - a technical manual in Old Czech"](https://www.voynich.ninja/thread-3895.html)

### B7. Arabic / Persian / Syriac
**Probability: 3/10**
Various proposals for Semitic/Middle Eastern origin.
- **For:** Bowern & Lindemann (2021) found Zipfian frequency proportions similar
  to Semitic and Iranian languages. JustAnotherTheory proposed "Arabic/Persian-inspired
  women's health manual." Active thread on Arabic/Syriac reading of F1R.
  Baresch's 1637 letter suggested the text may relate to Egyptian medicine.
- **Against:** Glyph shapes don't match Arabic/Persian/Syriac scripts. Codicology
  and binding are European. C14 parchment is European vellum.
- **Forum:** Voynich Ninja — ["Three arguments in favor of an Arabic/Persian-inspired
  women's health manual"](https://www.voynich.ninja/thread-5219.html) (JustAnotherTheory), ["Help with Arabic/Syriac Reading of F1R"](https://www.voynich.ninja/thread-5516.html)

### B8. Chinese / East Asian ("Monosyllabic Tonal Language")
**Probability: 3/10**
Originally proposed by Georg Baresch (1639 letter to Kircher: "some man of quality
went to oriental parts" and brought back knowledge "buried in this book in the same
script"). Jacques Guy (linguist) revived the idea; Jorge Stolfi developed it into the
most detailed version. Vonfelt (2014) found statistical resonance with Mandarin pinyin.
dashstofsk's 43-page thread (2025) is the most comprehensive modern discussion.

**Stolfi's detailed formulation (thread-4746, Jun 2025):**
Not specifically Chinese — any monosyllabic tonal language from the Sino-Tibetan,
Tai-Kadai, or Austronesian families. An educated European merchant/traveler spent years
in "oriental parts," met local scholars with books on medicine/botany, couldn't read the
local script, so had a local Reader dictate aloud while the Author wrote phonetic
transcription. The Author invented a new script because Latin alphabet was inadequate
for the tonal phoneme inventory — designed for speed (pull-strokes, combination of 2-3
simple strokes per glyph). A separate Scribe (probably Northern Italian, from Genoa or
Venice) later clean-copied the draft onto vellum. The Scribe was not the Author, didn't
know the language, and took liberties with illustrations (nymphs, fortifications, jars
— hence the Italian codicological fingerprint). Different VMS sections = transcriptions
of different "Chinese" books. The Herbal section was created last by elaborating Pharma
plant-part drawings into full plants (with fake details). Stolfi suspects the Starred
Paragraphs section is the "true Rosetta Stone" because he believes he knows which
source book it was copied from (not disclosed).

**Key statistical argument (Stolfi/ReneZ):**
Monosyllabic tonal languages (Vietnamese, Mandarin) have syllable structure with ordered
slots (onset consonant, glide, vowel, coda, tone marker) — each slot drawn from a small
inventory. This produces low character-level entropy (h2 ≈ 2, matching VMS) while
maintaining normal word-level entropy (~10 bits). ReneZ showed daiin→da3 ("he/she"),
chol→cho4=shi ("to be"), chor→cho2=shi ("period of time") — VMS word endings as tone
markers. MarcoP measured Vietnamese VIQR conditional entropy ≈ 2.2, close to VMS.

- **For:** (1) Explains low character entropy: slot-structured monosyllabic words with
  small per-slot inventories = exactly the VMS LOOP grammar pattern. (2) VMS word-level
  entropy ~10 bits is normal for NL. (3) Explains why a new alphabet was invented:
  tonal encoding needs custom script. (4) Explains word-ending regularities: tone
  markers (a small set of word-final characters — "exactly what we are seeing"). (5)
  Explains doubled words (common in Chinese compound formation). (6) Explains Currier
  A/B: different source books or dictation sessions. (7) Explains Starred Paragraphs
  format. (8) 43-page active discussion with substantive statistical engagement.
- **Against:** (1) No material evidence of Chinese/Asian contact in the VMS (no Asian
  imagery, inscriptions, or objects). (2) Historical plausibility is "very challenging"
  (ReneZ) — limited European travel to East Asia pre-1440. (3) Codicology is entirely
  European (Italian vellum, European binding). (4) Why no marginal notes in Latin?
  (oshfdk). (5) Koen G: Voynichese is not a romanization — it's "loosely based on
  medieval Latin script and some numerals" — no known precedent for Europeans inventing
  a wholly new script for a foreign language (they always romanize). (6) No convincing
  continuous text translations. (7) Labels don't consistently match plant images
  across different occurrences (oshfdk). (8) Vowel-consonant alternation in VMS is NOT
  clearly present like it is in East Asian syllable structure (ReneZ). (9) Probability 2→3
  for statistical interest; still historically near-implausible.
- **Source:** Baresch (1639), Jacques Guy, Jorge Stolfi, Vonfelt (2014), dashstofsk,
  ReneZ, MarcoP, Koen G
- **Forum:** Voynich Ninja — ["The 'Chinese' Theory: For and Against"](https://www.voynich.ninja/thread-4746.html) (dashstofsk,
  43 pages, ~400+ replies, 105K+ views)

### B9. Celtic Languages (Irish, Lepontic, etc.)
**Probability: 2/10**
Doireannjane proposed Phonetic Irish; newamauta proposed Lepontic/Cisalpine Celtic;
Petrasti proposed a Celtic theory.
- **For:** Active research with glyph-phonetic mappings attempted. Multiple independent
  Celtic proposals suggest something draws researchers to this family.
- **Against:** Celtic scripts of the 15th century are well-documented and don't
  resemble Voynichese. No convincing continuous text translations.
- **Forum:** Voynich Ninja — ["Voynich through Phonetic Irish"](https://www.voynich.ninja/thread-5032.html) (Doireannjane, 400 replies,
  77K views), ["Doireann's theory of Lepontic/Cisalpine Celtic"](https://www.voynich.ninja/thread-4543.html) (newamauta, 25 replies),
  ["Petrasti's Celtic Theory"](https://www.voynich.ninja/thread-4961.html) (58 replies)

### B10. Turkish / Turkic
**Probability: 2/10**
Ahmet Ardıç claimed VMS encodes Old Turkic phonetics. Calgary engineer theory
(widely covered in media).
- **For:** Extensive media coverage. Detailed glyph-to-sound mapping proposed.
- **Against:** Widely criticized by Voynich Ninja community and Koen Gheuens.
  Resembles goropism (Sun Language Theory). Circular methodology — finds Turkish
  words by looking for them.
- **Source:** Ardıç (2018–2024)
- **Forum:** Voynich Ninja — ["Calgary engineer believes he's cracked the mysterious
  Voynich Manuscript"](https://www.voynich.ninja/thread-2318.html) (663 replies, 462K views — highest reply count on the forum,
  overwhelmingly critical)

### B11. Nahuatl / New World Language
**Probability: 1/10**
Tucker & Talbert (2013) proposed Nahuatl based on plant identifications from
Mesoamerica. Jacinto Gimenez proposed Nahuatl diary.
- **For:** Some visual similarity between VMS plants and New World species (disputed).
- **Against:** C14 dates to 1404–1438, decades before Columbus. Nahuatl specialist
  M. Pharao Hansen rejected the proposed readings as "pure speculation." European
  codicology and binding. Radio carbon dating alone effectively kills this.
- **Source:** Tucker & Talbert (2013), Pharao Hansen (2018 rebuttal)
- **Forum:** Voynich Ninja — ["Voynich revealed, diary of a Nahuatl"](https://www.voynich.ninja/thread-4050.html) (Jacinto Gimenez, 27 replies)

### B12. Landa / Khojki / Sindhi
**Probability: 2/10**
Sukhwant Singh proposed the Landa Khojki script family (ancestor of Khudabadi,
Gurmukhi, Sindhi scripts).
- **For:** Some gallows characters resemble Khojki glyphs. Abugida (vowel-modifying)
  structure could explain some VMS word patterns.
- **Against:** No established 15th-century contact between Western European
  manuscript production and Punjab region scribal traditions. Codicology is European.
- **Forum:** Voynich Ninja — ["Is the VM written in Landa Khojki script?"](https://www.voynich.ninja/thread-3530.html) (De1m0s, 22 replies)

### B13. Korean
**Probability: 1/10**
Hangul-based theory.
- **For:** Hangul does have some structural similarities in glyph composition.
- **Against:** Hangul was invented in 1443, at the very end of or after VMS
  production period. No mechanism for Korean script to reach Europe. Entirely
  speculative.
- **Forum:** Voynich Ninja — ["Korean Solution"](https://www.voynich.ninja/thread-5045.html) (rikforto, 14 replies, received with skepticism)

### B14. Enochian / Encrypted Book of Enoch
**Probability: 2/10**
Radim Dobeš proposes the VMS is an encrypted version of the Book of Enoch.
- **For:** Active thread with detailed analysis attempted. John Dee (historical VMS
  connection) was involved with Enochian language.
- **Against:** Dee connection to VMS is speculative. Enochian language postdates VMS.
  No convincing systematic decipherment.
- **Forum:** Voynich Ninja — ["Voynich is encrypted ENOCH"](https://www.voynich.ninja/thread-5388.html) (Radim Dobeš, 80 replies, 9K views)

### B15. Middle English
**Probability: 2/10**
geoffreycaveney proposed Middle English after his earlier Judaeo-Greek theory.
- **For:** Detailed glyph mapping attempted.
- **Against:** Month labels have Romance/Italian not English spelling. English
  provenance doesn't align with Italian codicological evidence.
- **Forum:** Voynich Ninja — ["geoffreycaveney's Middle English theory"](https://www.voynich.ninja/thread-3521.html) (136 replies, 88K views)

---

## C. AUTHORSHIP THEORIES

### C1. Roger Bacon (1214–1294)
**Probability: 1/10**
Wilfrid Voynich's original proposal and the lens through which the MS was first studied.
- **Against:** Definitively refuted by C14 dating (1404–1438). Bacon died 110+ years
  before the parchment was made. Widely discarded.

### C2. John Dee / Edward Kelley
**Probability: 2/10**
Dee and Kelley were in Bohemia in the 1580s and had connections to Rudolf II.
- **For:** Circumstantial: Dee owned Bacon manuscripts, lived in Prague, knew Rudolf's court.
- **Against:** Dee's meticulous diaries don't mention the VMS. C14 dates the parchment
  to over a century before Dee and Kelley were active (though old vellum could
  theoretically be reused).
- **Source:** Voynich's original proposal, widely discussed

### C3. Giovanni Fontana (c. 1395–1455)
**Probability: 4/10**
North Italian engineer/inventor known to have used cipher systems.
- **For:** Correct time period. North Italian. Used cryptographic systems in his own
  works. His cipher is documented as a "simple, rational cipher, based on signs
  without letters or numbers."
- **Against:** His known ciphers are simpler than VMS. No direct link established.
- **Source:** Wikipedia, D'Imperio (1978)

### C4. Antonio Averlino/Filarete (c. 1400–1469)
**Probability: 3/10**
Nick Pelling's proposal from "The Curse of the Voynich" (2006). North Italian
architect/polymath connected to Milan.
- **For:** Correct geographic/temporal fit. Renaissance polymath with access to
  relevant knowledge. Detailed historical argument in Pelling's book.
- **Against:** Pelling himself has backed away from strong commitment. Requires
  a post-1450 dating which conflicts with the lower range of C14 dates.
- **Source:** Pelling (2006)

### C5. Raphael Mnishovsky (1580–1644)
**Probability: 2/10**
The friend of Marci who reported the Bacon connection. Known cryptographer who
invented a cipher he claimed was uncrackable (c. 1618).
- **For:** Had motive and means. Could have made Baresch an "unwitting test subject."
- **Against:** C14 dating predates him by 150+ years. Would require old vellum reuse.

### C6. Wilfrid Voynich (Modern Forgery)
**Probability: 2/10**
Voynich fabricated the MS to sell as a lost Roger Bacon manuscript.
- **For:** Had knowledge, means, and financial motive as book dealer.
- **Against:** C14 dating of the PARCHMENT to 1404–1438 is very difficult to fake.
  Discovery of Baresch's letter (1999) establishes the MS existed by the 1630s.
  McCrone Associates confirmed period-consistent inks and pigments.
  proto57 (Rich SantaColoma) has the most detailed modern forgery argument on
  Voynich Ninja (482 replies, 82K views) but the community is largely unconvinced.
- **Forum:** Voynich Ninja — ["The Modern Forgery Hypothesis"](https://www.voynich.ninja/thread-5008.html) (proto57, 482 replies, 82K views)

### C7. Giovanni Aurispa (1376–1459)
**Probability: 2/10**
Rustandi proposed the Italian humanist and manuscript collector.
- **For:** Correct period. Collected Greek manuscripts.
- **Against:** No direct evidence linking him to cipher creation or the VMS.
- **Forum:** Voynich Ninja — ["I've found the author of Voynich manuscript. He was Giovanni
  Aurispa."](https://www.voynich.ninja/thread-4168.html) (Rustandi, 51 replies, 32K views)

### C8. Hartmann Schedel (1440–1514)
**Probability: 2/10**
JustAnotherTheory proposed Schedel may have possessed the VMS.
- **For:** Correct broad period. Known collector and author.
- **Against:** Speculative connection with no documentary evidence.
- **Forum:** Voynich Ninja — ["Was Hartmann Schedel in possession of the VMS?"](https://www.voynich.ninja/thread-5307.html) (17 replies)

---

## D. CONTENT/PURPOSE THEORIES

### D1. Pharmaceutical / Herbal Manual
**Probability: 7/10**
The manuscript is a pharmacopoeia — a reference for plant-based medicines.
This is the MOST widely accepted purpose theory.
- **For:** Herbal section (majority of MS) depicts plants with root systems, a
  standard format for herbals. Pharmaceutical section has jars/containers consistent
  with apothecary texts. Our own pre-phase analysis: 3/4 shorthand tests support
  pharmaceutical notation. The overall structure matches a pharmacopoeia.
  Touwaide (specialist) confirmed binding is characteristic of Italian work.
- **Against:** Most plant illustrations don't match known species (may be stylized
  or composite). Labels don't function like typical herbal indices.
  If it's just a pharmaceutical manual, why encrypt it?
- **Source:** Baresch (1637 letter), most codicological assessments

### D2. Women's Health / Gynecological Manual
**Probability: 5/10**
The "balneological" section with naked women in pools/baths relates to
women's medical practices, possibly conception, pregnancy, and bathing cures.
- **For:** Naked female figures in baths are consistent with medieval gynecological
  texts and bath-cure traditions. JustAnotherTheory proposed "Arabic/Persian-inspired
  women's health manual." fabmas proposed "guide to conception and pregnancy."
  Surayya munir isah proposed "manual for female leadership and social health."
- **Against:** Naked figures could represent many things (astrological concepts,
  philosophical diagrams). The connection to gynecology is more assumed than demonstrated.
- **Forum:** Voynich Ninja — ["Three arguments in favor of Arabic/Persian women's health manual"](https://www.voynich.ninja/thread-5219.html),
  ["Viewing the MS as a guide to conception and pregnancy"](https://www.voynich.ninja/thread-5079.html) (fabmas, 19 replies),
  ["The Balneological section: A manual for female leadership and social health?"](https://www.voynich.ninja/thread-5276.html)

### D3. Alchemical Treatise
**Probability: 4/10**
The MS represents alchemical knowledge — coded to protect trade secrets.
- **For:** Georg Baresch (first known owner) was an alchemist. The pharmaceutical
  section containers resemble alchemical vessels. Secrecy motivation for encryption.
- **Against:** Typical alchemical manuscripts use known alchemical symbols, not
  entirely new scripts. The herbal section doesn't match typical alchemical content.

### D4. Astronomical / Astrological Manual
**Probability: 4/10**
The zodiac and cosmological sections suggest astrological content.
- **For:** Clear zodiac symbols present. Circular diagrams consistent with astronomical
  charts. Month labels in Latin script. ["Cosmic Comparison Theory"](https://www.voynich.ninja/thread-4822.html) (R. Sale, 19 replies).
- **Against:** Only a portion of the MS is astronomical. The astronomical diagrams
  are crude and don't match any known medieval astronomical tradition precisely.
- **Forum:** Voynich Ninja — ["Cosmic Comparison Theory"](https://www.voynich.ninja/thread-4822.html) (R. Sale), ["Zodiac labels"](https://www.voynich.ninja/thread-4829.html) (takrobat),
  ["Foil Q9f67r1- Stations of the Moon"](https://www.voynich.ninja/thread-4487.html) (BessAgritianin)

### D5. Charlatan's Prop
**Probability: 4/10**
The MS was created as an impressive-looking but meaningless prop to impress/deceive
patrons, possibly to sell to Rudolf II.
- **For:** Rafal's active thread (50 replies). An unintelligible-but-impressive manuscript
  could be used to claim hidden knowledge. 600 ducats supposedly paid by Rudolf.
  The text doesn't NEED to mean anything for this to work.
- **Against:** Extremely expensive production (vellum, illustrations) for a prop.
  No parallel example of this scale is known from the period. Statistical structure
  is more elaborate than a prop would need.
- **Forum:** Voynich Ninja — ["Voynich Manuscript as a charlatan's prop"](https://www.voynich.ninja/thread-5465.html) (Rafal, 50 replies, 4K views)

### D6. Espionage / Key Cipher
**Probability: 2/10**
The VMS was created for espionage and requires an external key to decode.
- **For:** Milan's diplomatic cipher tradition was active in this period. Mark Knowles
  has extensively researched connections between VMS authorship and Milanese
  diplomatic ciphers on Cipher Mysteries.
- **Against:** No key has ever been found. Lost-key theories are unfalsifiable.
  The length and illustrated nature of the MS is unusual for intelligence material.
- **Forum:** Voynich Ninja — ["The Voynich is for espionage and uses a key cipher"](https://www.voynich.ninja/thread-4999.html) (Ransom)

### D7. Copy of an Older Manuscript
**Probability: 5/10**
The VMS we have is a COPY of an older, possibly partly illegible original. This
could explain some of the text oddities (garbled copying, loss of meaning).
- **For:** JoJo_Jost's hypothesis (46 replies). Could explain why text seems structured
  but resists decipherment (copy errors accumulated). Explains why illustrations
  are sometimes crude (copied without full understanding). Retracing evidence
  (Bernd's thread, 326 replies, 88K views) supports multiple layers of work.
  Stolfi's "Book Switch Theory" (146 replies, 15K views) is related.
- **Against:** Doesn't address what the ORIGINAL was. Copy-only theory doesn't
  explain the cipher system itself.
- **Forum:** Voynich Ninja — ["copy of an older, barely legible manuscript?"](https://www.voynich.ninja/thread-4996.html) (JoJo_Jost, 46
  replies), ["[split] Retracer Thread"](https://www.voynich.ninja/thread-4740.html) (Bernd, 326 replies, 88K views),
  ["The Book Switch Theory"](https://www.voynich.ninja/thread-5035.html) (Jorge_Stolfi, 146 replies)

### D8. Lullian / Combinatorial Machine
**Probability: 3/10**
Walter Mandron proposes the MS encodes a Lullian-style combinatorial system
(based on Ramon Llull's logical/philosophical machines).
- **For:** Lullian combinatorics were well-known in the 15th century. Could
  explain the over-regular, paradigmatic structure we found. Circular diagrams
  might represent combinatorial wheels.
- **Against:** Lullian texts have their own well-documented format — they don't
  look like the VMS. No convincing mapping demonstrated.
- **Forum:** Voynich Ninja — ["The Lullian Apophatic Machine"](https://www.voynich.ninja/thread-5466.html) (Walter Mandron, 19 replies)

### D9. Beekeeping Manual
**Probability: 1/10**
- **Forum:** Voynich Ninja — ["A Beekeeping-Based Hypothesis"](https://www.voynich.ninja/thread-4799.html) (えすじーけけ, 6 replies)
- **Against:** Extremely niche, no supporting evidence.

### D10. Music / Lyrics
**Probability: 1/10**
- **Forum:** Voynich Ninja — ["lyrics and music?"](https://www.voynich.ninja/thread-4689.html) (extent_of_foxes, 14 replies)
- **Against:** No musical notation features identified.

### D11. Map / Travel Record
**Probability: 2/10**
Rosette page (f86v) as a map. Kaybo proposed "Iberian-African Voyage Record."
- **For:** Fold-out rosette page does resemble a map to some viewers.
- **Against:** Most map interpretations are pareidolic. Kaybo's theory (34 replies)
  received mixed reception.
- **Forum:** Voynich Ninja — ["The Voynich Manuscript as an Iberian-African Voyage Record"](https://www.voynich.ninja/thread-5001.html)
  (Kaybo, 34 replies), "Voynich Manuscript - folio 86v - A Map"

---

## E. META-THEORIES / STRUCTURAL

### E1. Two-Language/Bilingual System
**Probability: 6/10**
The MS contains two different encoding systems (Currier's Language A and Language B).
- **For:** Well-established since Prescott Currier's analysis. Two different scribes
  confirmed. Language A appears in herbal/pharmaceutical, Language B in
  balneological/astrological sections. Bowern & Lindemann (2021) confirm the split.
  Our analysis shows section divergence (JSD = 0.1975) supporting distinct sub-systems.
  Keldysh Institute proposed bilingual Romance-Germanic mixture.
- **Against:** Could be two dialects, two registers, or two scribes with different
  habits rather than genuinely different languages.
- **Source:** Currier (1976), Bowern & Lindemann (2021)

### E2. Numeric/Cipher System with Numbers Embedded
**Probability: 3/10**
Various proposals that some characters (i, q, d, y) represent numbers.
- **For:** oeesordy proposed i,q,d,y = 1,4,8,9 respectively. "A Numeric Solution"
  (Legit, 22 replies).
- **Against:** No systematic decipherment produced. Character frequency distributions
  don't match number distributions.
- **Forum:** Voynich Ninja — ["i,q,d,y are numbers"](https://www.voynich.ninja/thread-5491.html) (oeesordy), ["A Numeric Solution"](https://www.voynich.ninja/thread-5204.html) (Legit)

### E3. MHTamdgidi "Elephant in the Room"
**Probability: 3/10**
Behrooz Tamdgidi's extensive theory involving multi-layered structural analysis.
- **For:** Very detailed work. 256 replies, 36K views — indicates sustained
  engagement and effort.
- **Against:** Complexity of the proposal has not led to verified translations.
  Community reception is mixed.
- **Forum:** Voynich Ninja — ["Elephant in the Room Solution Considerations"](https://www.voynich.ninja/thread-5160.html)
  (MHTamdgidi_(Behrooz), 256 replies, 36K views)

### E4. Data Matrix / Tabular Structure
**Probability: 2/10**
almarture proposes the manuscript functions as a data matrix.
- **Forum:** Voynich Ninja — ["The manuscript as a data matrix"](https://www.voynich.ninja/thread-5297.html) (9 replies)

### E5. Conlang + Glossolalia Hybrid
**Probability: 3/10**
oeesordy proposes "daiin" is pronounced (Conlang theory, 17 replies).
- **Forum:** Voynich Ninja — ["Conlang, Glossolalia, daiin pronounced"](https://www.voynich.ninja/thread-5562.html) (oeesordy, 17 replies)

---

## F. DECIPHERMENT CLAIMS (SPECIFIC)

### F1. Stephen Bax (2014) — Partial Decoding
**Probability: 3/10**
Proposed partial decoding of specific plant names using phonetic values derived
from star names and plant identifications.
- **For:** Systematic methodology. A few readings are superficially plausible.
  Our Phase 57 tested Bax/Vogt proposals.
- **Against:** Only a handful of words "decoded." Readings are contested. Cannot
  extend to continuous text. Bax died before completing the work.
- **Source:** Bax (2014, academia.edu)

### F2. Dr. Michael Hoffmann — "Voynich decoded completely"
**Probability: 2/10**
Claims complete decoding, reading text as Latin vowel sequences.
- **For:** Published extensively (173 replies, 143K views on Voynich Ninja).
- **Against:** Readings are unconvincing ("te ea exta ore uni eum"). Claims "no letters,
  no language, only visual code" which contradicts statistical evidence.
- **Forum:** Voynich Ninja — ["Voynich decoded completely"](https://www.voynich.ninja/thread-2416.html) (173 replies, 143K views)

### F3. Alisa Gladyseva
**Probability: 2/10**
- **Forum:** Voynich Ninja — ["Alisa Gladyseva: Voynich manuscript is decoded"](https://www.voynich.ninja/thread-2821.html)
  (138 replies, 118K views)

### F4. Kris1212 — "Voynich Decoded"
**Probability: 2/10**
- **Forum:** Voynich Ninja — ["Voynich Decoded"](https://www.voynich.ninja/thread-4606.html) (284 replies, 110K views)

### F5. Monica Yokubinas Translation
**Probability: 2/10**
- **Forum:** Voynich Ninja — ["M. Yokubinas translation"](https://www.voynich.ninja/thread-2761.html) (114 replies, 86K views)

### F6. bi3mw — Translation of Folio 1r
**Probability: 2/10**
- **Forum:** Voynich Ninja — ["The Translation of The Voynich Manuscript: Folio 1r"](https://www.voynich.ninja/thread-4320.html)
  (66 replies, 44K views)

### F7. Yulia May's Solution
**Probability: 2/10**
- **Source:** Discussed on Cipher Mysteries (2017), JKP
- **Forum:** Voynich Ninja — ["Discussion of Yulia May's proposed solution"](https://www.voynich.ninja/thread-569.html) (70 replies, 68K views)

### F8. Tim King et al. Translation
**Probability: 2/10**
- **Forum:** Voynich Ninja — ["Tim King's et al. translation"](https://www.voynich.ninja/thread-2847.html) (37 replies, 35K views)

### F9. MarkWart — "Voynich manuscript is decoded"
**Probability: 2/10**
- **Forum:** Voynich Ninja — ["Voynich manuscript is decoded"](https://www.voynich.ninja/thread-3932.html) (44 replies, 58K views)

### F10. The Genoese Gambit (R. Sale)
**Probability: 2/10**
- **Forum:** Voynich Ninja — ["The Genoese Gambit"](https://www.voynich.ninja/thread-5570.html) (2 replies, recent)

### F11. Moravian Interpretation (BessAgritianin)
**Probability: 3/10**
Detailed folio-by-folio interpretations with Moravian context.
- **Forum:** Voynich Ninja — ["Foil14v- Acanthus Mollis Moravian Interpretation"](https://www.voynich.ninja/thread-5548.html) (11 replies),
  ["Foil116v -An Ancient Recipe"](https://www.voynich.ninja/thread-4480.html) (29 replies), ["Who is the author of VM?"](https://www.voynich.ninja/thread-4298.html) (36 replies)

---

## G. METHODOLOGY / PROCESS THEORIES

### G1. Strong Four-Phase System (Urtx13)
**Probability: 3/10**
Claims statistical evidence of a structured four-phase encoding system.
- **Forum:** Voynich Ninja — ["Strong evidence of a structured four-phase system"](https://www.voynich.ninja/thread-4650.html)
  (81 replies, 29K views)

### G2. K&A Testing at Scale (CorwinFr)
**Probability: 4/10**
CorwinFr (2026) tested Kelley & Augustine (?) approach at scale, found
structural patterns and Tironian shorthand connections.
- **Forum:** Voynich Ninja — ["Tested K&A at scale, found something, need your help"](https://www.voynich.ninja/thread-5553.html)
  (27 replies), ["Structural patterns in the VMS & Evaluating the Tironian shorthand
  hypothesis"](https://www.voynich.ninja/thread-5585.html) (21 replies) — both very recent and active

### G3. Polyphonic Cipher
**Probability: 2/10**
- **Forum:** Voynich Ninja — ["Polyphonic Cipher?"](https://www.voynich.ninja/thread-4628.html) (Dobri, 5 replies)

### G4. Bit-level Geometry (TheEnglishKiwi, Feb 2026)
**Probability: 2/10**
TheEnglishKiwi ("Ben", New Zealand, joined Feb 2026) claims a proprietary
"patent pending" engine uses MDL (Minimum Description Length) compression on
the raw UTF-8 bit stream of EVA transcriptions to discover the "true structural
building blocks" of Voynichese — prefixes, roots, and suffixes — without
human guesswork. The engine maps data into a "2D bit-array" and identifies
tokens by their "geometric centroid" rather than character identity. Includes
web-based tools (Pattern Decoder, Contextual Analyser, Word Shape Visualiser,
Translation Auditor). Key claim: 24-bit (3-char) chunks are the "mathematical
sweet spot" at ~63.2% compression, and that this proves the text is built from
tight trigram-level building blocks.

**CRITICAL PROBLEMS:**

1. **Foundational logical error (identified by nablator):** Compression
   performance does NOT prove linguistic structure. Different compression
   algorithms produce different tokenizations. A zip dictionary of English
   doesn't reveal "deep truth about building blocks." LZW, BPE, and MDL
   all segment differently — none is privileged as the "true" segmentation.
   The claim that "if the maths can make the dictionary smaller, the pattern
   is physically real" conflates statistical regularity with linguistic reality.

2. **Refuted by Jorge Stolfi at the theoretical level:** Natural languages
   cannot be factored as a simple L = A × B (prefix set × suffix set).
   Real morphology is a messy union of hundreds of sub-languages with
   semantic constraints, phonetic variations, and paradigm gaps. The
   "unbelievable → un-believe-able" example is cherry-picked; the engine
   cannot distinguish "-able" from "-ible" without knowing semantics that
   compression cannot access. Stolfi: "Math may provide a set of prefixes,
   cores, and suffixes that have certain favorable statistical properties,
   but it cannot prove that the Author thought of the words in terms of
   those parts."

3. **Compression ratio WORSE than existing methods (identified by Mauro):**
   Mauro's earlier Monte Carlo slot-grammar approach achieved 480,985 bits.
   TheEnglishKiwi's best (24-bit lens) achieved 688,640 bits — 43% WORSE.
   As nablator noted: "688640 > 480985 so no? Less bits is better compressed."
   If your novel method produces worse compression than a supervised
   slot-grammar, it is not finding "optimal" structure.

4. **Trigram result is not new:** The finding that 3-character chunks are
   important in Voynichese is well-established. Nablator: "trigrams are
   important is not new: you must include constraints at least at the trigram
   level if you want to generate good-looking pseudo-Voynichese." The
   "quick snapshot" output (ch-, qo-, sh-, che, aiin, hedy, etc.) reproduces
   exactly the patterns that have been known since Currier (1976) and Stolfi's
   paradigm tables. Nothing new is discovered.

5. **"Patent pending" / proprietary black box:** The engine is closed-source.
   The community cannot inspect the algorithm, verify the null controls, or
   reproduce results independently. Claims about "geometric centroids" and
   "2D bit-arrays" are vague marketing language — no mathematical specification
   is provided. For a method that claims mathematical proof, the inability to
   examine the proof is a fatal credibility problem.

6. **Overclaiming that was partially retracted:** Original post claimed the
   engine finds "a law of the language" and "proves exactly where the author(s)
   connected their building blocks." After pushback from Stolfi and nablator,
   TheEnglishKiwi conceded: "I was too enthusiastic to say 'it is the law of
   the language'" and "there is no proof of psychological intent from the
   author." The scoring reflects the retracted state, but the web tools still
   appear to present results with the original overconfident framing.

7. **Conflicts with our own analysis:** Our Phase 51 showed that 95.6% of
   "morphological MI" in Voynichese is explained by single-character transitions
   — the morphological labels (prefix, suffix, root) are convenient descriptions
   of character-level regularities, NOT independent phenomena. An MDL engine
   that "discovers" these same prefixes and suffixes is rediscovering the
   character bigram structure, not uncovering hidden morphemes. Our conditional
   entropy finding (H(char|prev) = 1.92 bits) already quantifies exactly how
   predictable the next character is given the previous one — this is the same
   information an MDL compressor captures, just expressed differently.

8. **Anthropomorphized mathematics:** Repeated claims that "maths has no brain
   and cannot be fooled" are misleading. MDL makes assumptions (e.g., the
   generative model family). If the wrong model family is applied (e.g.,
   concatenative morphology to a system that may be positional/templatic),
   MDL will find the best-fitting WRONG answer. Garbage-in, garbage-out
   applies to mathematical optimization exactly as to any other method.

**What the community said:**
- **nablator** (experienced analyst): Directly challenged core claims. "There is
  no law, only local preferences." "The performance of a given compression
  algorithm is not evidence of anything."
- **Jorge Stolfi** (prominent researcher): "I bet it does not [prove building
  blocks]." Demolished the theoretical assumptions with formal linguistic argument.
- **Mauro** (prior compression work): Politely noted superior compression from
  his own method, remained diplomatically open but unconvinced.
- **ThomasCoon**: Only positive response ("huge step forward"), but this was
  before the critical responses from Stolfi and nablator.

**Bottom line:** A proprietary black-box tool that achieves worse compression
than existing open methods, rediscovers known patterns, overclaims what
compression can prove, and was challenged at the theoretical level by two of
the forum's most knowledgeable members. The approach has some methodological
value in principle (MDL is a legitimate technique for unsupervised morphology
induction — see Goldsmith 2001), but the specific implementation and claims
are not credible as presented. TheEnglishKiwi accepted critique gracefully,
which suggests good faith, but the tool remains unverified.

- **Forum:** Voynich Ninja — ["Bit-level Geometry"](https://www.voynich.ninja/thread-5407.html) (17 replies, Feb-Mar 2026)

---

## H. SUMMARY: PROBABILITY RANKING

| Rank | Theory | Score | Key Factor |
|------|--------|-------|------------|
| 1 | Pharmaceutical/Herbal Manual (content) | 7/10 | Fits illustrations, structure, period |
| 2 | Two-language system (Language A/B) | 6/10 | Well-established statistical fact |
| 3 | Cipher of European natural language | 5/10 | Default hypothesis, no solution found |
| 4 | Verbose/Complex cipher (e.g. Naibbe) | 5/10 | Best proof-of-concept to date |
| 5 | Constructed/Artificial language | 5/10 | Explains over-regular structure |
| 6 | Shorthand/Abbreviation system | 5/10 | Our analysis partially supports |
| 7 | Copy of an older manuscript | 5/10 | Explains some oddities |
| 8 | Latin as underlying language | 5/10 | Expected for the period |
| 9 | Women's health manual (content) | 5/10 | Fits balneological section |
| 10 | Hoax/Meaningless text | 4/10 | Some statistical support, but expensive |
| 11 | Italian/Proto-Romance language | 4/10 | Italian provenance, but claims retracted |
| 12 | German/Bavarian language | 4/10 | Some statistical support |
| 13 | Hebrew/Judaeo-Greek | 4/10 | Morphological similarities but too regular |
| 14 | Giovanni Fontana (author) | 4/10 | Right place, right time, used ciphers |
| 15 | Alchemical treatise (content) | 4/10 | Baresch was alchemist |
| 16 | Astronomical/Astrological (content) | 4/10 | Zodiac sections present |
| 17 | Charlatan's prop | 4/10 | Possible but expensive |
| 18 | K&A / Tironian shorthand | 4/10 | Recent, promising methodology |
| 19 | Arabic/Persian/Syriac | 3/10 | Some Zipfian similarities |
| 20 | Greek | 3/10 | Active but unconvincing |
| 21 | Old Czech/Slavic | 3/10 | Ownership chain only |
| 22 | Steganography | 3/10 | Possible but unproven |
| 23 | Stephen Bax partial decoding | 3/10 | Few plausible readings, incomplete |
| 24 | Lullian machine | 3/10 | Interesting but undemonstrated |
| 25 | Averlino authorship | 3/10 | Post-1450 dating problematic |
| 26-30 | Various specific decipherments | 2/10 | None independently verified |
| 31-35 | Celtic, Turkish, Khojki, etc. | 1-2/10 | Insufficient evidence |
| — | Chinese / East Asian tonal language | 3/10 | Statistical interest, historical implausibility |
| 36 | Roger Bacon authorship | 1/10 | Refuted by C14 dating |
| 37 | Nahuatl / New World language | 1/10 | Pre-Columbian dating kills it |
| 38 | Korean | 1/10 | No contact mechanism |
| 39 | Beekeeping manual | 1/10 | No evidence |

---

## I. FORUM STATISTICS (Voynich Ninja — Most Active Theory Threads)

| Thread | Author | Replies | Views |
|--------|--------|---------|-------|
| [No text, but a visual code](https://www.voynich.ninja/thread-2384.html) | Antonio García Jiménez | 1,699 | 1,089,782 |
| [Calgary engineer (Turkish)](https://www.voynich.ninja/thread-2318.html) | Ahmet Ardıç | 663 | 462,169 |
| [The Modern Forgery Hypothesis](https://www.voynich.ninja/thread-5008.html) | proto57 | 482 | 81,928 |
| [Voynich through Phonetic Irish](https://www.voynich.ninja/thread-5032.html) | Doireannjane | 400 | 77,239 |
| [The 'Chinese' Theory](https://www.voynich.ninja/thread-4746.html) | dashstofsk | 397 | 105,486 |
| [Retracer Thread](https://www.voynich.ninja/thread-4740.html) | Bernd | 326 | 88,513 |
| [Voynich Decoded (Kris1212)](https://www.voynich.ninja/thread-4606.html) | Kris1212 | 284 | 109,878 |
| [Elephant in the Room](https://www.voynich.ninja/thread-5160.html) | MHTamdgidi | 256 | 36,262 |
| [geoffreycaveney's Judaeo-Greek](https://www.voynich.ninja/thread-2697.html) | geoffreycaveney | 221 | 159,702 |
| [Ruby's Greek Thread](https://www.voynich.ninja/thread-3904.html) | Ruby Novacna | 218 | 73,263 |
| [Voynich decoded completely (Hoffmann)](https://www.voynich.ninja/thread-2416.html) | Dr. Michael Hoffmann | 173 | 142,883 |
| [Why the text could be Bavarian](https://www.voynich.ninja/thread-5312.html) | JoJo_Jost | 154 | 15,418 |
| [The Book Switch Theory](https://www.voynich.ninja/thread-5035.html) | Jorge_Stolfi | 146 | 14,758 |
| [Can VM be vowelless Latin?](https://www.voynich.ninja/thread-758.html) | farmerjohn | 139 | 108,305 |
| [Alisa Gladyseva decoded](https://www.voynich.ninja/thread-2821.html) | bi3mw | 138 | 117,705 |
| [geoffreycaveney's Middle English](https://www.voynich.ninja/thread-3521.html) | geoffreycaveney | 136 | 87,797 |
| [M. Yokubinas translation](https://www.voynich.ninja/thread-2761.html) | -JKP- | 114 | 86,016 |
| [Cvetka's Slovenian Theory](https://www.voynich.ninja/thread-4758.html) | Cvetka | 107 | 33,351 |
| [Speculative fraud hypothesis](https://www.voynich.ninja/thread-4877.html) | dexdex | 92 | 29,788 |
| [The Naibbe cipher](https://www.voynich.ninja/thread-4848.html) | magnesium | 83 | 29,752 |
| [Voynich is encrypted ENOCH](https://www.voynich.ninja/thread-5388.html) | Radim Dobeš | 80 | 9,384 |

NOTE: Reply count does not correlate with plausibility. The most-replied threads
often reflect controversy or persistence rather than quality. The Naibbe cipher
thread (83 replies) has arguably the strongest methodology despite fewer replies
than many debunked proposals.

---

## H. CIPHER MYSTERIES DEEP-DIVE (Nick Pelling's Site + Comments)

Extracted 2026-04-14 from 7 Cipher Mysteries pages including ~2,250+ comments.
Sources: ciphermysteries.com/the-voynich-manuscript (main + 6 sub-pages).

### H1. Pelling's Core Model: Verbose Cipher of Truncated Text

Nick Pelling's primary hypothesis (developed in "The Curse of the Voynich", 2006):
- Plaintext is **abbreviated/truncated** natural language (Latin or Italian).
- Truncated text is then **enciphered via verbose cipher** — common bigrams/syllables
  map to multi-glyph tokens.
- **Two or more intermediate operations** are involved (Pelling uses "plural" deliberately).
- Layered: abbreviation → substitution → verbose expansion.
- Key quote: "Voynichese words have such low information content (highly formulaic,
  hence predictable), this has profound implications for the kind of text."
- Key quote: "People didn't start taking the spaces out of ciphertexts till the
  early sixteenth century (in Venice), so near-100% chance plaintext words map to
  Voynichese words."
- Pelling excludes **polyalphabetic ciphers** because VMS has MORE internal structure
  than normal languages, not less. Renaissance polyalphabetic ciphers (Alberti, 1467)
  postdate the VMS and destroy structure rather than preserve it.

### H2. Pelling's Positional Rules (MORE Specific Than Previously Catalogued)

Pelling describes Voynichese letters as "dancing to a tricky set of structural rules":
- **Gallows** appear preferentially as first letter of a **page** or **paragraph**
- **'s'** (EVA-s) preferentially appears as first letter of a **line**
- **'m'** or **'am'** preferentially appear as last letter of a **line**
- **'qo'** appears as first token of a **word**
- **'y'** or **'dy'** appear as last token of a **word**
- **Paired letters** cluster: 'ol', 'or', 'al', 'ar'
- Letters are **unrepeated** except: 'ee', 'eee', 'ii', 'iii'
- Key quote: "Its absence of randomness is possibly its most remarkable aspect."
- These are not just word-level patterns — they extend to **line-level** and
  **page/paragraph-level** positional effects.

NOTE: Our Phase 61/67 I*M*F slot-grammar model captures word-internal structure but
does NOT capture line-initial/line-final or page/paragraph-level positional effects.
This is a gap in our fingerprint battery.

### H3. Pelling's "qo-" Prefix Parsing

Pelling explicitly states (Theories page, 2014):
- "qo-" is a **free-standing prefix**, NOT part of the root word.
- "qokedy" should parse as **"qo-k-e-d-y"** (not "q-o-k-e-d-y").
- He suspects "qo-" enciphers **"lo" = "the"** (Italian definite article).
- "ok-" is a **completely different** verbose pair from "qo-".
  So "okedy" parses as **"ok-e-d-y"** (different cipher token).
- "y+gallows" pairs (e.g. "yk") form different cipher tokens than unpaired gallows.
  So "ykedy" parses as **"yk-e-d-y"**.

This has direct implications for EVA transcription parsing: the "correct" tokenization
may not be character-by-character but chunk-based with prefix separation.

### H4. Gallows as Non-Letter Structural Markers (Thomas Spande)

Thomas Spande contributed extensive gallows analysis across multiple articles:
- Gallows **frequencies change between folios written by the same scribe**.
  If gallows were consonants, their frequency should be roughly stable.
- Gallows may serve as **pilcrows/punctuation markers** rather than letters.
- Spande proposes gallows as "placeholders" dividing the alphabet into 4 quarters.
- Gallows cannot be constant consonants because their distribution is too variable.
- This is supported by J.K. Petersen's observation that distinctive tokens
  (including gallows) are common at paragraph beginnings.

Independently, commenter "Xenon" (2015) proposes that ALL VMS characters may be
**scribal abbreviation characters**, not cipher glyphs — matching ~15 to 1400s
European paleography forms. More complex glyphs are compound abbreviations of
2-3 standard forms.

### H5. The "o" Problem

Pelling (main page comments): EVA-o is "that rock that just about every
linguistic account of Voynichese will find itself cracked upon."
- Spande's vowel frequency analysis: "o" = 54 occurrences in 16 lines (f22v),
  "a" = only 24. No known natural language has this level of "o" dominance.
- Latin: e > a ≈ u >> o. Italian: a, e, i all more common than o.
- English: a, e both more common than o.
- No language Spande tested (Latin, Italian, English, Tamil, Urdu, Sinhala,
  Armenian) matches VMS "o" dominance.
- "o" might be a **structural element** (separator, null, space marker, period)
  rather than a phonemic character.
- Menno Knul wonders if "o" should be interpreted as a **full stop** or **slash**.

### H6. Rene Zandbergen's Enumeration / Numbering System Insight

Rene Zandbergen (the leading Voynich provenance researcher) describes VMS as
**"more like a numbering (or enumeration) system"**:
- VMS has fewer than 13,824 unique word types.
- This means **3 Greek letters** (24³ = 13,824) could encode every distinct word.
- Information content per VMS word is extremely low.
- This is compatible with a **nomenclator** model where each word encodes an
  index into a codebook rather than spelling out phonemes.

Commenter "David T" reinforces: low entropy means plaintext is **shorter**
than ciphertext (verbose encoding confirmed from information theory).

### H7. Mark Knowles: Partial Hoax Hypothesis (~60% Null, ~40% Real)

Mark Knowles proposes:
- ~60% of VMS text is **null/padding** (meaningless filler).
- ~40% contains **real encoded content**.
- **Labels** are encrypted differently from **sentence text**.
- If true, whole-corpus statistics are contaminated by mixture of signal + noise.
- This could explain why no single cipher model reproduces the full fingerprint:
  we're trying to match a blended distribution.

### H8. "Denke deutsch, schreibe Latein" Hypothesis (Commenter 'Peter')

German-thinking, Latin-writing model:
- Uses prefix abbreviations, combination abbreviations, Latin ending abbreviations.
- Hides 'E' (most common letter) in combination forms.
- Still a simple 1:1 encryption underneath the abbreviation layer.
- Compatible with known German marginalia in VMS (color codes: "rot", etc.)
- Compatible with Pelling's multi-layer model (German → Latin abbreviation → cipher).

### H9. Kevin Shaw: Rule-Governed Constructed Technical Language (Dec 2025)

Kevin Shaw published a monograph (late 2025) claiming VMS is a:
- **"Rule-governed constructed technical language"**
- Exhibits **hierarchical affix behaviour**: prefix–modifier–root–suffix
- Shows **semantic domain clustering**
- Aligns strongly with our Phase 67 slot grammar findings (I*M*F zones).

### H10. Russian Paper (Keldysh Institute): Mixture of Two Languages

Claimed VMS is a **"mixture of two natural languages — one Roman, one Germanic —
with vowels intentionally omitted."**
- Pelling dismissed it because the model requires discarding spaces, which
  contradicts his "spaces were preserved" argument.
- However, vowel omission + two-language mixture is an interesting model worth
  testing: an abjad-style encoding of a bilingual text.

### H11. Multiple Scribes Confirmed — Statistical Implications

Multiple evidence lines confirm at least 2 scribes:
- **Codicology page:** Two distinct handwriting styles (tight vs. loose).
- **Currier A/B:** Different statistical profiles in different sections.
- Spande: "Two scribes are at work but both seem to use the same abbreviations
  and cipher abbreviations."
- Tight scribe (f24r): "o" = 71 in 20 lines. Loose scribe (f22v): "o" = 54 in 16 lines.
  But proportions differ.
- **Implication:** If the two scribes produce different statistical fingerprints,
  our whole-corpus metrics are an average of two distinct distributions.
  This could explain some metric mismatches.

### H12. Patrick Lockerby: Abbreviated Latin Transcription

Lockerby (multiple comments, 2019) proposes a specific transcription key:
- VMS is **abbreviated Latin**, like compressed medieval text.
- 'oto-' transcribes as 'oleo-' (oil-related), 'oko' as 'olio' (as in 'folio').
- 'ota' = 'olea', 'oka' = 'olia'.
- Sometimes 'k' and 't' are interchangeable (spelling variation pre-printing press).
- Entire VMS is about **herbal preparations, especially oils, for use in baths**.
- Word 'anus' in VMS context means 'mature woman', not anatomical term.
- Claims translation of f1r first words: "This is a peractum with which you will
  assuredly perform the art of perfumes."

### H13. Don of Tallahassee: Prefix–Midfix–Suffix Decomposition

Don proposed (with "Voynich Lite" system) that VMS words consistently decompose
into **prefix–midfix–suffix** structure:
- 503 of 505 most common words (≥10 occurrences) successfully decompose.
- Uses 137 codes total: 103 for herbal ingredients, 34 for everything else.
- Proposes VMS is an **artificial apothecaries' shorthand**.
- Pelling's critique: The most common word ('daiin', 886 occurrences) would encode
  "1 minim's measure of macerated avens" — improbably specific for the most
  frequent word. Also: no word for "the" or "and" in Don's system.
- Nevertheless, the **structural decomposition** (prefix–midfix–suffix) aligns
  with our slot grammar findings.

### H14. Kortexneo / Mohamed Machkour: Positional Polyalphabetic (April 2026)

Brand new theory (posted April 2026 on Cipher Mysteries):
- **Pure positional polyalphabetic cipher**: 1-6 position shifting based on
  glyph position within word.
- Claims to yield **"consistent technical Latin (Padua, c. 1420)"**.
- Claims **100% reproducible** via online decoder at kortexneo.com.
- Published on Zenodo: DOI 10.5281/zenodo.19337911.
- Claims to find complete **four-stage spagyric recipe** structure (Nigredo,
  Albedo, Citrinitas, Rubedo) on folio 1r, typical of 15th-century Northern
  Italian alchemy schools.
- **Not yet evaluated.** Should be testable: if the decoder is mechanical, we
  can feed in VMS text and verify whether output is grammatical Latin.

---

## I. CODICOLOGICAL & DATING EVIDENCE (From Cipher Mysteries)

### I1. Parallel Hatching Dating

Source: ciphermysteries.com/the-voynich-manuscript/voynich-parallel-hatching
- Parallel hatching originated with **Florentine goldsmiths** working in niello, ~1440s.
- Spread to **Venice ~1450**, rest of Europe after.
- **Cross-hatching** (absent from VMS) appeared later.
- VMS earliest possible date from hatching evidence: **1440 (Florence) or 1450 (elsewhere)**.
- Lack of cross-hatching places VMS in range **1450–1480** most likely.
- Parallel hatching **died out after ~1500–1510**.
- Combined with C14 date (1404–1438 for vellum): VMS was likely produced
  **after 1440 but using older vellum stock** (not uncommon in period).
- Debated with D.N. O'Donovan about whether VMS hatching is truly Renaissance
  parallel hatching or an older technique — Pelling firmly supports the former.

### I2. Quire Numbers

Source: ciphermysteries.com/the-voynich-manuscript/voynich-quire-numbers
- Quire numbering uses **ugly hybrid of Arabic numerals and late medieval Latin
  abbreviations**: pm9, 29, 39... = primus, secundus, tertius...
- The "9" symbol represents **"-us" or "-um"** in Latin (standard medieval abbrev.).
- **4 different hands** identified in quire numbers (more than the 2 scribes of text).
- Numbering style is **unique** — no exact match found in any other manuscript.
- **Quire numbering** dates ~1450–1500. **Folio numbering** (different hand, different
  ink) dates ~1550. These are distinct from the text scribes.
- Pelling suspects quire numbers added **near Lake Constance** (southern German-speaking).
- **Sergio Toresella** (Italian herbal manuscript expert): "VMS manufactured
  1450–1460, was in France for a while, book itself comes from Italy, mysterious
  writing done in round humanistic style found only in Italy in second half of 1400s."

### I3. Codicology — Pages Out of Order

Source: ciphermysteries.com/the-voynich-manuscript/voynich-codicology
- Strong evidence that **pages are NOT in their original order**.
- Folio numbers likely wrong; bifolios potentially **upside down**; quires in wrong order.
- Water section: **f78v–f81r were originally adjacent** (water flows seamlessly
  between them in the illustrations).
- Pages scrambled through at least one rebinding.
- Original page layouts had a **consistent design aesthetic** — now disrupted.
- **Lisa Fagin Davis** (Oct 2025): New presentation on manuscript materiality with
  "BIG NEWS" about potential original structure. Confirmed only **one set of
  stitch-marks** (bound only once, contradicting multiple-rebinding theories, but
  pages could have been shuffled before that single binding).
- **Vladimir D**: Quire 9 (Q9) is **foreign to VMS book block** — worm holes on
  outer contour, missing captal attachment. May have been inserted from another source.
- **Barb**: Identified possible alchemical phases (Nigrido, Albido, Rubedo) in
  water section pages.
- Two distinct handwriting styles (tight vs. loose scribes) — see H11.
- Paints added in **multiple waves**: some original, heavy blue paint added
  **after binding**.

**Implication for computational analysis:** Any metric depending on sequential text
order (cross-page boundary entropy, section-level Zipf) may be corrupted by page
disorder. Our cross-boundary metrics should be interpreted with this caveat.

### I4. Agriculture Section

Source: ciphermysteries.com/the-voynich-manuscript/voynich-agriculture
- **Glen Claston's hypothesis**: Plant drawings encode secrets of herbal gardening,
  specifically pruning techniques.
- Book tradition: **Pietro Crescenzi's Ruralia Commoda** (~1305) — major agricultural
  treatise widely copied in period.
- **Filarete connection**: Antonio Averlino (Filarete) had lost herbal/"books of
  agriculture" — potential source text.
- Agriculture section plants don't match any known real plants well — possibly
  **composite or symbolic** rather than naturalistic.

### I5. Crossbow Dating Evidence

Source: ciphermysteries.com/the-voynich-manuscript/crossbow-article
- Crossbow depicted in VMS dated to **first half of 14th century** based on:
  - Recurve composite bow (Saracen influence)
  - Straight stock (early 14th century)
  - Right-angled trigger bar (14th century only)
- BUT: VMS vellum dated 1405–1438, so the crossbow image was likely **copied
  from an earlier source**.
- Pelling: zodiac roundel drawings are **"barely integrated"** with rest of
  manuscript — likely copied from pre-existing source material.
- **Implication:** Different VMS sections may derive from **different source texts**
  of different dates and possibly different languages. Supports treating sections
  independently in statistical analysis.

### I6. Marginalia and Provenance (From Comments Across Articles)

- German marginalia firmly established: color codes ("rot" = red), month names.
- **Occitan/Catalan** month names in zodiac sections (debated).
- f116v text — possible colophon, multiple competing readings.
- "de Tepenecz" inscription on f1r — Jacobus Horčický de Tepenec ownership.
- Manuscript was likely in:
  - **Northern Italy** (creation, 1450–1460)
  - Possibly **France** for a period (Toresella)
  - **Prague** (Rudolf II connection, early 1600s)
  - **Rome** (Kircher correspondence, 1660s)
  - **Villa Mondragone** (Jesuits, until ~1912)
  - **Wilfrid Voynich** (purchase ~1912)

---

## J. COMMUNITY CONSENSUS POINTS (Meta-Analysis of Comments)

From reviewing ~2,250 comments across Cipher Mysteries (2012–2026):

### What the serious researchers mostly agree on:
1. **VMS is genuine** (not a modern forgery) — C14 dating, paint analysis, binding
   construction all consistent with 15th-century origin.
2. **Two scribes** (Currier A/B) with consistent system but distinguishable hands.
3. **More structure than natural language**, not less — rules out simple polyalphabetic.
4. **Italian/Northern Italian provenance** for the physical manuscript.
5. **Not "just readable"** in any known language — Bax-style "just read it" approaches
   are rejected by serious researchers.
6. **Labels** behave differently from **running text** — should be analyzed separately.
7. **Multiple layers** of encoding are likely involved.
8. The **"o" problem** has no satisfactory explanation in any theory.
9. **EVA transcription** may impose incorrect character boundaries.

### What remains deeply contested:
1. **Source language**: Latin vs. Italian vs. German vs. something else.
2. **Cipher type**: verbose substitution vs. nomenclator vs. abbreviation system
   vs. constructed language vs. glossolalia.
3. **Whether gallows are phonemic** or structural/punctuation.
4. **Whether the text is meaningful** at all (hoax/gibberish minority view persists).
5. **The role of "qo-"**: prefix? article encoding? integral to root word?
6. **Page order**: how much disruption occurred and whether it can be reconstructed.

### Recurring failed approaches (cautionary patterns):
1. **Morse code mapping** — Thomas O'Neil spent years on VMS → Morse → Italian
   anagram system. Comprehensively refuted: any text of sufficient length can
   produce Italian words via unconstrained anagram selection from dot-dash totals.
   Ger Hungerink proved this by "decoding" his own grandfather's name using the
   same method. The system has no falsification criterion.
2. **Single-character substitution** — Repeatedly attempted, repeatedly fails.
   VMS character frequencies don't match any known language.
3. **"I can just read it"** — Dozens of claimants across 14 years of comments,
   all producing mutually incompatible "translations," none reproducible.
4. **Numerological/mystical approaches** — Multiple claimants, no testable predictions.
5. **Anagram-based decryption** — Nick Pelling: by subjective anagramming,
   "you can turn a great deal of nonsense text into words."

---

*Last updated: 2026-04-14*
*Sources: voynich.ninja/forum-58 (all 7 pages), en.wikipedia.org/wiki/Voynich_manuscript,
ciphermysteries.com (main VMS page + 6 sub-pages + ~2,250 comments), reddit.com/r/voynich,
project workspace analysis (DISCOVERIES.md, SYNTHESIS.md)*
