# A-Level Revision Materials

A collection of A-Level revision materials for **Computer Science** (OCR H446) and
**Physics** (AQA, AS topics). It contains Anki-ready flashcards, Markdown revision
notes, and pre-built Anki decks.

All content is AI-generated. The exact model and generator skill behind every set is
recorded in [VERSIONS.md](VERSIONS.md).

## Current materials

The newest set of each type lives at the repository root. Older sets are kept in
`archive/`.

| Subject | Flashcards | Notes |
|---------|-----------|-------|
| Computer Science | `CS Flashcards v3.6` (`flashcard-v3.6`, Opus 4.6 Thinking) | `CS Notes v3.6` (`notes-v3.6`, Opus 4.6 Thinking) |
| Physics (AS) | `Physics Flashcards v3.6 (AS)` (`flashcard-v3.6`, Opus 4.6 Thinking) | `Physics Notes v3.6 (AS)` (`notes-v3.6`, Opus 4.6 Thinking) |

| Content type | Format | Import |
|--------------|--------|--------|
| Flashcards | `.txt`, pipe-delimited (`Question \| Answer`) | Anki: Fields separated by `\|` |
| Notes | `.md` (Markdown) | Any editor, Obsidian, VS Code |
| Anki decks | `.apkg` | Anki: File > Import |

## Topic coverage (current sets)

### Computer Science

| Topic area | Flashcards v3.6 | Notes v3.6 |
|------------|:---------------:|:----------:|
| 1. Processors, Input, Output & Storage | ✓ | ✓ |
| 2. Software & Software Development | ✓ | ✓ |
| 3. Exchanging Data (compression, databases, networks, web) | ✓ | ✓ |
| 4. Data Types, Structures & Boolean Algebra | ✓ | ✓ |
| 5. Legal, Moral, Cultural & Ethical Issues | ✓ | ✓ |
| 6. Elements of Computational Thinking | ✓ | ✓ |
| 7. Programming Techniques & Computational Methods | ✓ | ✓ |
| 8. Algorithms | ✓ | ✓ |

The current CS flashcards are organised into per-topic folders (groups 1 to 8).
The current CS notes are stored as one Markdown file per subtopic with simplified
numbering.

### Physics (AS, topics 1-5)

| Topic | Flashcards v3.6 | Notes v3.6 |
|-------|:---------------:|:----------:|
| 1. Measurements & Their Errors | ✓ | ✓ |
| 2. Particles & Radiation | ✓ | ✓ |
| 3. Waves | ✓ | ✓ |
| 4. Mechanics & Materials | ✓ | ✓ |
| 5. Electricity | ✓ | ✓ |

Pre-built Anki decks are available for Waves and Mechanics & Materials in `Anki decks/`.

## Versioning

Versions follow the generator skill that created the material. Legacy sets generated
from hand-written prompt templates keep their original **v1** and **v2** labels.
Skill-era flashcards are named after the `flashcard-vX.Y` skill tag, and skill-era
notes are named after the `notes-vX.Y` skill tag. For example, both current
flashcard sets are **v3.6** because they were created with `flashcard-v3.6`, while
both current notes sets are **v3.6** because they were created with `notes-v3.6`.

Physics sets are tagged `(AS)` because they cover only the AS topics (1-5).

Full per-set detail (model, source blend, date) is in [VERSIONS.md](VERSIONS.md).

## Directory structure

```
alevel-revision-materials/
├── README.md
├── VERSIONS.md
├── LICENSE
├── CS Flashcards v3.6/             # current CS flashcards (topics 1-8)
│   └── 1..8 <topic>/               # subtopic cards + a "<n>. <topic> DEFS" file
├── CS Notes v3.6/                  # current CS notes (topics 1-8)
│   └── <topic>_<subtopic>.md        # one Markdown file per subtopic
├── Physics Flashcards v3.6 (AS)/   # current Physics flashcards (topics 1-5)
│   ├── 1..5 <topic>/               # subtopic cards
│   └── PMT Definitions/            # one DEFS aggregate per topic
├── Physics Notes v3.6 (AS)/        # current Physics notes (topics 1-5)
│   ├── 1..5 <topic>/               # subtopic notes
│   └── PMT Notes/                  # one NOTES aggregate per topic
├── Anki decks/                     # pre-built .apkg files
└── archive/                        # superseded versions, same topic-folder layout
    ├── CS Flashcards v1, v2, v3.4, v3.5
    ├── CS Notes v1, v2, v3.3
    ├── Physics Flashcards v1 (AS), v2 (AS), v3.3 (AS), v3.5 (AS)
    └── Physics Notes v1 (AS), v2 (AS), v3.2 (AS)
```

Most sets are organised into per-topic folders. The current CS notes are the exception:
they are stored as one Markdown file per subtopic. CS flashcards keep each topic's
definitions aggregate (`DEFS`) inside the topic folder. Physics keeps PMT aggregates in
separate `PMT Definitions` and `PMT Notes` folders. The oldest set, `CS Flashcards v1`,
keeps its three card sources (`CMB`, `PMT`, `SME`) as separate subfolders, since each
covers the same subtopics.

### Source variants and aggregates

- **CMB** Combine: content merged from both PMT and SME.
- **PMT** [Physics & Maths Tutor](https://www.physicsandmathstutor.com/).
- **SME** [Save My Exams](https://www.savemyexams.com/).
- **DEFS** A per-topic definitions aggregate (sourced from PMT).
- **NOTES** A per-topic note-style aggregate (sourced from PMT).

## How to use

### Anki decks

Install [Anki](https://apps.ankiweb.net/), then double-click an `.apkg` file in
`Anki decks/` or use File > Import.

### Text flashcards

The `.txt` files are pipe-delimited (`Question | Answer`). Import into Anki with File >
Import and set "Fields separated by: `|`", or use any flashcard app that accepts
CSV/text.

### Markdown notes

Open the `.md` files in any text editor, a Markdown viewer (VS Code, Obsidian, Typora),
or GitHub, or convert to PDF with pandoc.

## Syllabus alignment

- **OCR A-Level Computer Science** (H446)
- **AQA A-Level Physics** (AS topics 1-5)

Content may also help with other boards covering similar topics. Always verify against
the official specification.

## Contributing

Found an error? Open an issue identifying the file and the specific card or section,
and provide the correction with a source where possible.

## Credits

- **Content generation**: Anthropic's Claude (Sonnet 4.5, Opus 4.5, Opus 4.6 Thinking)
- **Generators**: [`notes-v3.6`](https://github.com/maaarcooo/claude-skills/releases/tag/notes-v3.6) from [revision-notes-generator](https://github.com/maaarcooo/claude-skills#revision-notes-generator) and [`flashcard-v3.6`](https://github.com/maaarcooo/claude-skills/releases/tag/flashcard-v3.6) from [anki-flashcard-generator](https://github.com/maaarcooo/claude-skills#anki-flashcard-generator)
- **Flashcard format**: compatible with [Anki](https://apps.ankiweb.net/)

---

*For educational use. Always verify information against official exam board
specifications and approved textbooks.*
