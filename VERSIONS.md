# Version History

This file is the single source of truth for how every set in this repository was
generated. The folder name alone cannot capture the model, so record changes here.

## Versioning scheme

- **v1 and v2** are the legacy "prompt era": generated from hand-written prompt
  templates before the generator skills existed. Their numbers are kept as-is.
- **v3.x** is the "skill era": the version number equals the minor version of the
  specific generator skill that produced the set. Flashcards follow the
  `flashcard-vX.Y` skill tag, and notes follow the `notes-vX.Y` skill tag.

Because the generator skills now version independently, matching folder labels do not
mean a shared repository release. For example, the current flashcards are `v3.6`
because they were generated with `flashcard-v3.6`, while the current notes are `v3.6`
because they were generated with `notes-v3.6`.

Current generator tags:

- Flashcards: [`flashcard-v3.6`](https://github.com/maaarcooo/claude-skills/releases/tag/flashcard-v3.6)
- Notes: [`notes-v3.6`](https://github.com/maaarcooo/claude-skills/releases/tag/notes-v3.6)

The newest set of each type lives at the repository root; everything older lives in
`archive/`. Physics sets are tagged `(AS)` because they cover the AS topics (1-5)
only.

## Re-numbering map

How each set was named before this re-versioning, and its name now. Sets marked
"(from local)" were added during this pass and did not previously exist in the
repository. Sets whose number is unchanged were only renamed for consistency.

### Flashcards

| Previous name | New name | Note |
|---------------|----------|------|
| CS Flashcards v1 | CS Flashcards v1 | number unchanged |
| CS Flashcards v2 | CS Flashcards v2 | number unchanged |
| CS Flashcards v4 | CS Flashcards v3.4 | renumbered to skill version |
| CS Flashcards v4re / "v4-regenerated" | _removed_ | abandoned Skill v3.4 run |
| CS Flashcards v5 | CS Flashcards v3.5 | archive, renumbered to skill version |
| CS "Flashcards v3.6" (from local) | CS Flashcards v3.6 | **current** |
| Physics Flashcards v1 | Physics Flashcards v1 (AS) | number unchanged |
| Physics Flashcards v2 | Physics Flashcards v2 (AS) | number unchanged |
| Physics Flashcards v3 | Physics Flashcards v3.3 (AS) | renumbered to skill version |
| Physics "Cards v5 (AS)" (from local) | Physics Flashcards v3.5 (AS) | renumbered to skill version |
| Physics "Cards v3.6" (from local) | Physics Flashcards v3.6 (AS) | **current** |

### Notes

| Previous name | New name | Note |
|---------------|----------|------|
| CS CMB Notes v1 | CS Notes v1 | number unchanged |
| CS CMB Notes v2 | CS Notes v2 | number unchanged |
| CS CMB Notes v3 | CS Notes v3.3 | archive, renumbered to skill version |
| CS "Notes v3.7" (from local) | CS Notes v3.6 | **current**, re-versioned to notes skill tag |
| Physics Gen Notes v1 (SME) | Physics Notes v1 (AS) | number unchanged |
| Physics Gen Notes v2 (Mix) | Physics Notes v2 (AS) | number unchanged |
| Physics Gen Notes v3 (Mix) | Physics Notes v3.2 (AS) | renumbered to skill version |
| Physics "Notes v3.7" (from local) | Physics Notes v3.6 (AS) | **current**, re-versioned to notes skill tag |

## Flashcards

| Version | Status | Generation method | Model | Source blend | Date |
|---------|--------|-------------------|-------|--------------|------|
| v1 | archive | `ankiFlashcardPrompt_v3` | Claude Sonnet 4.5 | CMB / PMT / SME | 2025 |
| v2 | archive | `ankiFlashcardPrompt_v4` | Claude Opus 4.5 | CMB / PMT defs | 2025 |
| v3.3 (Physics) | archive | anki-flashcard-generator Skill v3.3 | Claude Opus 4.5 (extended thinking) | PMT / defs | 22-01-2026 |
| v3.4 (CS) | archive | anki-flashcard-generator Skill v3.4 | Claude Opus 4.6 (extended thinking) | CMB / PMT defs | 2026 |
| v3.5 (CS) | archive | anki-flashcard-generator Skill v3.5 | Claude Opus 4.6 (extended thinking) | CMB / PMT defs | 2026 |
| v3.5 (Physics) | archive | anki-flashcard-generator Skill v3.5 | Claude Opus 4.6 (extended thinking) | PMT / defs | 16-06-2026 |
| v3.6 (CS) | **current** | anki-flashcard-generator Skill `flashcard-v3.6` | Claude Opus 4.6 Thinking | CMB / PMT defs | 2026 |
| v3.6 (Physics) | **current** | anki-flashcard-generator Skill `flashcard-v3.6` | Claude Opus 4.6 Thinking | PMT / defs / subtopics | 16-06-2026 |

## Notes

| Version | Status | Generation method | Model | Source blend | Date |
|---------|--------|-------------------|-------|--------------|------|
| v1 | archive | `revisionNotesPrompt_v1` | Claude Sonnet 4.5 (extended thinking) | CS: CMB / Physics: SME | 2025 |
| v2 | archive | `revisionNotesPrompt_v2` | Claude Opus 4.5 (extended thinking) | Mix / CMB | 2025 |
| v3.2 (Physics) | archive | revision-notes-generator Skill v3.2 | Claude Opus 4.5 (extended thinking) | Mix | 09-01-2026 |
| v3.3 (CS) | archive | revision-notes-generator Skill v3.3 | Claude Opus 4.5 (extended thinking) | CMB | 16-01-2026 |
| v3.6 (CS) | **current** | revision-notes-generator Skill `notes-v3.6` | Claude Opus 4.6 Thinking | CMB | 2026 |
| v3.6 (Physics) | **current** | revision-notes-generator Skill `notes-v3.6` | Claude Opus 4.6 Thinking | Mix | 15-06-2026 |

## Notes on specific versions

- **CS Flashcards has no v3.3.** It jumped from prompt-era v2 straight to Skill v3.4.
- **A v3.4 Physics regeneration never shipped.** Physics went v3.3 then v3.5 then v3.6.
- **v3.4-partial (CS, deleted).** A CS flashcard run was started on Skill v3.4 by
  mistake (intended v3.5), stopped midway with topic 6 missing, and saved locally as
  "v4-regenerated". It was superseded by v3.5 and removed from the repository.
- **CS Notes v3.3 was renumbered to the simplified scheme.** It was generated with full
  OCR specification numbering (1.1.1, 2.1.x) but was converted to simplified numbering
  (1.1 to 6.5) during reorganisation, to match the flashcards and the v1 notes.
- **Notes v3.6 replaces the temporary v3.7 label.** The revision-notes-generator
  release formerly referred to as v3.7 is now tracked as `notes-v3.6`, so current CS
  and Physics notes use the `v3.6` folder label.

## Source blend key

- **CMB** Combine: content merged from both PMT and SME.
- **PMT** [Physics & Maths Tutor](https://www.physicsandmathstutor.com/).
- **SME** [Save My Exams](https://www.savemyexams.com/).
- **defs** Definition-focused cards.
