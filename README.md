# A-Level Revision Materials

Flashcards and revision notes for **OCR A-Level Computer Science** (H446) and
**AQA A-Level Physics** (AS topics 1 to 5).

There is one copy of each deck and each note. They are improved in place, so there are
no version numbers in file or folder names. The history is in git, and
[CHANGELOG.md](CHANGELOG.md) records what changed and where the content came from.

All content is AI-generated and checked against the exam board specifications. Physics
topics 2 and 3 have also been checked against AQA mark schemes and examiner reports. Always verify anything
important against the official specification.

## What is here

| Subject | Decks | Cards | Notes |
|---------|------:|------:|------:|
| Computer Science (OCR H446, topics 1 to 8) | 26 | 1925 | 26 |
| Physics (AQA, AS topics 1 to 5) | 24 | 1303 | 24 |

Each subtopic has one flashcard deck and one note with the same name.

## Layout

```
alevel-revision-materials/
├── computer-science/
│   ├── flashcards/<n>. <topic>/<n.m> <subtopic>.txt
│   └── notes/<n>. <topic>/<n.m> <subtopic>.md
├── physics/
│   ├── flashcards/<n>. <topic>/<n.m> <subtopic>.txt
│   └── notes/<n>. <topic>/<n.m> <subtopic>.md
├── skills/        # the generator skills and the procedure for improving materials
├── scripts/       # check_decks.py, paper_digest.py, pull_mark_schemes.py
├── CHANGELOG.md
└── LICENSE
```

## Flashcards

Each deck is a plain text file with one card per line:

```
Question | Answer
```

- The only pipe on a line is the separator, with a space on each side.
- Maths is written in LaTeX between dollar signs, e.g. `$E_k = \frac{1}{2}mv^2$`.
- A reverse card (`<definition> — what term is this? | <term>`) directly follows the
  definition it reverses.

Import a deck into Anki with File > Import and "Fields separated by: Pipe", or into any
flashcard app that accepts delimited text, such as NeuroCards.

### How the decks are organised

- Cards follow the order of the specification within each deck.
- Each idea is defined in one deck only, the one whose specification section owns it.
  Other decks only ask about what is specific to their own context. For example,
  abstraction is defined in Computer Science 6.1, and the photon energy equations in
  Physics 2.1.
- Answers are short. An answer never contains the answer to another card.
- Worked cards (a calculation, a trace, a scenario) sit next to the fact they apply.

## Notes

Each note is a Markdown file whose title matches its file name. Below the title, a
**Specification** line states the board, the section numbers and what that section
requires. Notes end with a summary table of key terms or key equations.

## Checking the decks

```bash
python3 scripts/check_decks.py
```

This reports format errors (anything that would break an import) and questions that
appear more than once within a subject. Both counts should be zero before a change is
committed.

## Improving the materials

The procedure is in [skills/improve-materials/SKILL.md](skills/improve-materials/SKILL.md).
It covers how to check a change against the specification, which deck owns an idea that
appears in more than one topic, and how to record the change.

The generator skills used to produce new decks and notes from source material are in
`skills/flashcard-generator` and `skills/revision-notes-generator`.

## Earlier versions

Before October 2026 the repository kept every generated version side by side
(`CS Flashcards v3.6`, `Physics Notes v2 (AS)` and so on). Those folders, the separate
definitions decks, the per-topic PMT summaries and the pre-built Anki packages were
merged into the files here and then removed. They are still available at the
[`pre-baseline`](https://github.com/maaarcooo/alevel-revision-materials/tree/pre-baseline)
tag.

## Contributing

Found an error? Open an issue that names the file and the card or section, and give the
correction with a source where possible.

## Credits and licence

- **Content**: generated with Anthropic's Claude models, using the skills in `skills/`.
- **Licence**: CC BY 4.0, see [LICENSE](LICENSE).

For educational use. Always verify information against official exam board
specifications and approved textbooks.
