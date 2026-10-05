# Changelog

What changed in the materials, newest first, followed by a note on where the content
came from.

## 2026-10-05: mark-scheme pass, the remaining topics

The same comparison was carried out for Physics topics 1, 4 and 5 (AQA AS papers 2016
to 2025) and for all eight Computer Science topics (OCR A-Level papers 2021 to 2025 and
AS papers 2022 to 2025), with the examiner reports for each. Most cards already said
what the mark schemes credit, so the changes are small. Physics now has 1316 cards and
Computer Science has 1951.

**Facts corrected**

- Physics 5.1: the resistance at a point on an I-V graph is V/I at that point. The old
  card gave 1/gradient, which the examiner reports name as a misconception for curves.
- Computer Science 1.3: magnetic storage represents bits by the orientation of
  magnetised regions. The old wording said polarised and unpolarised regions.
- Computer Science 4.2: a record is a data structure that groups fields of different
  data types under one identifier. The old card called it a row in a file, and the
  examiner reports say database-row answers lose the mark in programming questions.

**Reworded to match credited answers**

- Physics: why a filament lamp's resistance rises, and how the diameter of a wire is
  measured (readings at different points and orientations, anomalies rejected, mean
  calculated).
- Computer Science: the accumulator, why more RAM helps, SSD advantages, alpha testing,
  concurrent processing (no longer limited to one processor), and deleting a leaf from
  a binary search tree.
- Two fill-in-the-blank cards (1.3 and 6.1) rewritten as questions.

**Added**

- 13 Physics cards. Examples: the two conditions for equilibrium, thrust and drag
  explained with Newton's laws, thermistor self-heating, cells in parallel, and the
  micrometer zero error.
- 26 Computer Science cards. Examples: what the BIOS does at start-up, why compiled
  code protects intellectual property, spiral against waterfall, assembly against
  high-level languages, primary and foreign key uniqueness, layering as abstraction,
  one representation of zero in two's complement, arrays against lists, a RIPA power,
  the benefit of a global variable, and how a graph differs from a tree.

**Tools**

- `scripts/paper_digest.py` now takes the subject as its first argument and covers
  the Computer Science papers in `sources/computer-science/papers`.

## 2026-10-05: mark-scheme pass, Physics topics 2 and 3

The definition and explanation cards in Particles & Radiation and Waves were compared
with the credited answers in the AQA AS papers from 2016 to 2025, their examiner
reports, and AQA topic mark schemes. The notes were updated to match. Physics now has
1303 cards.

**Facts corrected**

- Polarisation: the oscillations are restricted to a single plane. The old wording
  said the plane was perpendicular to the direction of propagation, but the plane
  contains that direction.
- Single-slit diffraction: the subsidiary maxima get dimmer but stay the same width.
  The old card said they get narrower.
- Destructive interference gives zero amplitude only when the two amplitudes are equal.
- Electron diffraction: a beam of particles alone would give a single bright patch, not
  an even spread across the screen.
- Fluorescent tube: collisions excite the mercury atoms. The note said they ionise them.

**Reworded to match credited answers**

- Work function, the proton as the only stable baryon, how a theory is validated, how
  an emission spectrum is produced, resonant frequencies on a string, the functions of
  cladding, modal dispersion, the effect of pulse broadening, why a polarising filter
  reveals objects under water, and how to reduce uncertainty in the double-slit
  practical.

**Added**

- 23 cards for mark-scheme points that had no card. Examples: the ground state, why
  energy levels are negative, why nothing is emitted below the threshold frequency,
  how the stopping potential depends on frequency, how a beam of electrons ionises an
  atom, where electrons behave as waves in a diffraction tube, when the fringe spacing
  equation is valid, and how to reduce uncertainty in the diffraction grating practical.

**Tools**

- `scripts/paper_digest.py` prints the past-paper questions on a topic with their mark
  schemes and examiner comments. `scripts/pull_mark_schemes.py` downloads topic-sorted
  papers. Both work on `sources/`, which git ignores.
- `sources/` now has one layout: `<subject>/notes/<provider>` and `physics/papers`.
  The procedure is in `skills/improve-materials/SKILL.md`.

## 2026-10-04: baseline

The repository moved from many numbered versions kept side by side to one living copy
of each deck and note.

**Structure**

- New layout: `<subject>/flashcards` and `<subject>/notes`, with one file per subtopic.
- Version numbers removed from every file and folder name.
- Computer Science 2.4 and 2.5 are now separate decks and notes.
- Added `scripts/check_decks.py`, which checks deck format and finds repeated questions.

**Flashcards**

- Every deck was compared with all earlier versions of itself, with the source notes
  and with the specification. Cards that only existed in an older version were restored
  where they tested something the specification requires.
- The separate definitions decks were merged into the subtopic decks.
- Each idea is now defined in one deck. Repeats in other decks were removed or reworded
  to test only what is specific to that deck.
- Cards follow specification order.
- Removed: trivia, case-study figures, yes/no questions, fill-in-the-blank cards, and
  cards that restated two neighbouring cards.
- Added: worked cards (calculations, traces and scenarios) throughout.
- Errors copied from source material were corrected. Examples: the meaning of the
  PageRank damping factor, the year of the Malicious Communications Act (1988), the
  claim that every divide and conquer algorithm is O(log n), the definition of
  measurement uncertainty, the intensity of light after one polariser, the resolution
  of a micrometer, and rubber listed as a ductile material.
- The corrections were then checked against the OCR and AQA specifications and
  published mark schemes. Two of them turned out to be rewordings of statements that
  were already acceptable (the conditions for a couple and the moment of an angled
  force), so those now follow the wording of the AQA specification.

**Notes**

- Every note opens with a **Specification** line giving the board, section numbers and
  requirements.
- Physics: the per-topic PMT summaries were folded into the subtopic notes.
- Open "check" flags were resolved and the note corrected where the source was wrong.
- "Beyond source" labels were removed and the facts kept.
- Horizontal rules and numbered headings were removed.

**Result**

- Computer Science: 26 decks, 1925 cards, 26 notes.
- Physics: 24 decks, 1280 cards, 24 notes.
- The check reports no format errors and no repeated questions in either subject.

**Removed**

- The `archive/` folder, the numbered folders at the repository root, the Physics
  definitions decks and PMT summaries, the pre-built Anki packages, and `VERSIONS.md`.
  All of these remain available at the `pre-baseline` tag.

## Provenance

All content is AI-generated.

- **2025 to mid 2026.** Decks and notes were generated from Physics & Maths Tutor (PMT)
  and Save My Exams (SME) notes, first with hand-written prompts (versions 1 and 2) and
  then with the `flashcard-generator` and `revision-notes-generator` skills (versions
  3.2 to 3.8), using Claude Sonnet 4.5, Opus 4.5 and Opus 4.6. The full record of which
  model and skill produced which version is `VERSIONS.md` at the `pre-baseline` tag.
- **October 2026.** The baseline above was produced with Claude Opus 5.5 in Claude
  Code, by merging those versions and checking them against the source notes and the
  OCR H446 and AQA 7408 specifications.

The source notes are copyrighted and are not part of this repository.
