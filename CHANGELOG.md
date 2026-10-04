# Changelog

What changed in the materials, newest first, followed by a note on where the content
came from.

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
  measurement uncertainty, the intensity of light after one polariser, the moment of an
  angled force, and rubber listed as a ductile material.

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
