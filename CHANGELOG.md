# Changelog

What changed in the materials, newest first, followed by a note on where the content
came from.

## 2026-10-08: card rules brought up to date, and thermal physics added

Every deck was checked against the current card rules (flashcard-generator v3.10, the
rules tuned as the NeuroCards generation prompt). Physics now has 1510 cards in 27 decks
and Computer Science has 1952.

**New decks**

- Physics 6.4 Thermal Energy Transfer, 6.5 Ideal Gases and 6.6 Molecular Kinetic Theory
  Model, generated from the notes for those sections and then edited to the current
  rules. They have no revision notes yet.

**Punctuation**

- Reverse cards are written `<definition> - what term is this?`, with a hyphen where
  there was an em dash (272 cards).
- Semicolons in answers became full stops, colons or commas (91 answers). Code that
  needs its semicolons keeps them.

**Facts corrected**

- Physics 6.4: mean molecular kinetic energy is proportional to absolute temperature.
  The old answer said temperature.
- Physics 6.5: the temperature of a gas is related to the average kinetic energy of its
  molecules. The old answer said average speed.
- Physics 6.5: the Boyle's law graph of $p$ against $1/V$ confirms the law when it is a
  straight line through the origin. The old answer said a straight line.
- Computer Science 1.1: the width of the address bus determines the number of
  addressable locations, $2^n$ for $n$ bits. The old card and the note said proportional.
- Computer Science 2.2: semantic analysis detects errors in meaning. The old card and
  the note called them logic errors.

**Removed**

- Values the exam supplies: the constants on AQA's data and formulae sheet (Physics 2.1:
  $e$, $h$, the particle masses, specific charges and rest energies; 6.5: $R$ and $k$)
  and values a question gives (6.4: the specific heat capacity and latent heats of
  water). Equations on the sheet keep their cards.
- Reverse cards for laws, principles and Acts: Newton's laws, Ohm's law, Kirchhoff's
  laws, the gas laws, the principles of moments, superposition and conservation of
  momentum, De Morgan's law, and the four Acts in Computer Science 5.1.
- Cards that only rearrange an equation that has a card (Physics 2.4, 3.3 and 5.1).
- Repeats of another card (Physics 1.1, 4.3, 6.4, 6.5 and 6.6, Computer Science 4.2),
  and the named-scientist history cards in Physics 6.6, which the specification does
  not ask for.

**Added**

- A single-step worked card for each main equation that had none: 15 in Physics topics
  2 to 5, 7 in topic 6, and 7 binary and address-bus calculations in Computer Science.

**Reworded**

- Conditions moved into the question where the answer depends on them: photoelectric
  current against intensity (fixed frequency above the threshold), $W = p\Delta V$
  (constant pressure), and the energy balance for mixing (no energy lost).

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
