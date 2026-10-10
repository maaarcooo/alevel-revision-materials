# A-Level Revision Materials

Flashcard decks and revision notes for OCR A-Level Computer Science (H446) and AQA
A-Level Physics (7408). There is one living copy of each deck and each note, improved in
place. Marco studies from these and imports the decks into NeuroCards.

## Before changing a deck or a note

Read [skills/improve-materials/SKILL.md](skills/improve-materials/SKILL.md) and follow
it. It holds the procedure, the deck rules, which deck owns an idea that crosses topics,
how to check wording against mark schemes, and a status table of what each topic has
had done to it.

The folders under `skills/` are plain files in this repository, not skills that load by
themselves, so open the file.

- Card style: [skills/flashcard-generator/SKILL.md](skills/flashcard-generator/SKILL.md),
  currently `flashcard-v3.10`. It is kept identical to the copy in Marco's agent-skills
  repository and to the NeuroCards generation prompt. Change all three together.
- Note style: [skills/revision-notes-generator/SKILL.md](skills/revision-notes-generator/SKILL.md).

## What Marco has asked for

- Bring every deck up to the current card rules and to the exam board's wording. The
  specification decides what belongs and what it is called. Mark schemes and examiner
  reports decide which wording earns the mark.
- Edit the deck files directly. Do not send decks through a model API unless asked.
- Formula sheets: an important formula or rule keeps its card even when the exam
  supplies it, because candidates are expected to know it. The value of a supplied
  constant gets no card, and a complicated supplied result may be left out. This is a
  judgement for each card. Physics uses AQA's data and formulae sheet. OCR Computer
  Science has none. Marco's Maths board is OCR.
- No em dashes or semicolons on a card. A reverse card is
  `<definition> - what term is this? | <term>`, with a hyphen.

## Every change

- `python3 scripts/check_decks.py` must end `0 decks with errors, 0 duplicate questions`.
- A corrected fact goes in the deck and in the matching note.
- Add an entry at the top of `CHANGELOG.md`, listing every fact corrected.
- Update the status table in the improve-materials skill, and the counts in `README.md`
  when decks or cards are added or removed.
- One commit per topic, staging files by name. Commit or push only when Marco asks.
- `sources/` is copyrighted material that git ignores. Never commit it or move it.
