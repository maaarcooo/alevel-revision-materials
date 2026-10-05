---
name: improve-materials
description: Improve an existing flashcard deck or revision note in this repository in place. Use when asked to fix, extend, tidy, re-check or update a deck or note that already exists here, or to fold new source material into one. For a subtopic that has no deck or note yet, use flashcard-generator or revision-notes-generator first, then apply this procedure.
---

# Improve Existing Materials

This repository keeps one living copy of each deck and note. An improvement edits that copy. It never creates a second version, a dated copy or a renamed file.

## Process

1. **Read what is there.** Read the whole deck and the matching note for the subtopic, not only the lines you were asked about. They share a name: `<subject>/flashcards/<n>. <topic>/<n.m> <subtopic>.txt` and `<subject>/notes/<n>. <topic>/<n.m> <subtopic>.md`.
2. **Read the specification section.** The note's **Specification** line names it (OCR H446 for Computer Science, AQA 7408 for Physics). The specification decides what belongs, what it is called and how deep to go.
3. **Read any source material you were given**, in full. Source notes are copyrighted: keep them in `sources/` (ignored by git) and never commit them.
4. **Decide each change** using the rules below, then edit the files in place.
5. **Keep the deck and the note in step.** A correction to a fact goes in both.
6. **Run the check** and fix everything it reports:
   ```bash
   python3 scripts/check_decks.py
   ```
   It must end with `0 decks with errors, 0 duplicate questions`.
7. **Record the change.** Add an entry at the top of `CHANGELOG.md` under the date, saying what changed and why. List every correction of a fact.
8. **Commit** with one commit per topic, staging the changed files by name.

## What counts as an improvement

- **Correct** anything that is wrong. The specification outranks the source notes: where a source is wrong and you are confident of the right version, write the right version and record the fix. Where you are not confident, leave the content out and say so.
- **Add** a fact, term or worked card only when the specification requires it or an exam question could plainly ask it, and only when you are confident the exam board accepts it.
- **Remove** trivia, case-study figures, content beyond the specification, and cards that repeat another card.
- **Reword** a card that is ambiguous, has more than one right answer, or gives away another card's answer.
- **Do not** rewrite cards that are already correct and clear. Changing a question's wording breaks its link to a learner's review history in apps that match cards by text, so only reword where the card is better for it.

## Deck rules

These add to the card style rules in `skills/flashcard-generator/SKILL.md`, which still apply.

- One card per line, `Question | Answer`, with exactly one pipe on the line and a space on each side. No blank lines. The file ends with a newline.
- Maths in LaTeX between dollar signs. Write a modulus as `\lvert x \rvert`, never with pipe characters.
- Cards follow the order of the specification.
- A reverse card has the form `<definition> — what term is this? | <term>` and sits directly after the definition it reverses. Only key terms get one.
- A list answer has at most three items. Split longer lists.
- No yes/no or true/false answers, and no fill-in-the-blank cards.
- Bundle or split, not both: a card that only restates two neighbouring cards is removed.
- No em dashes in answers. Use a colon or a comma.
- Put a worked card (a calculation, a trace, a scenario) directly after the fact it applies. Check the arithmetic.

## One deck owns each idea

An idea that appears in several topics is defined in one deck, the one whose specification section owns it. Other decks may only ask what is specific to their own context. Before adding a definition, search the subject for it:

```bash
grep -rn -i "<term>" computer-science/flashcards
```

Settled owners for ideas that cross topics:

| Computer Science | Owner |
|---|---|
| Opcode and operand, processor pipelining | 1.1 |
| Parallel processing | 1.2 |
| Operating system functions, device drivers, scheduling and time slices | 2.1 |
| Utilities, translators, the assembler | 2.2 |
| Assembly language, mnemonics, addressing modes | 2.4 |
| Object-oriented terms | 2.5 |
| Encryption and hashing | 3.1 |
| JavaScript syntax | 3.4 |
| Primitive data types and casting | 4.1 |
| Definitions of data structures, traversal orders, hash tables and collisions | 4.2 |
| Abstraction | 6.1 |
| Top-down design, hierarchy charts | 6.3 |
| Programming constructs, recursion, subroutines, variables, parameter passing, IDE features | 7.1 |
| Problem decomposition, divide and conquer, data mining, heuristics, pipelining as a method | 7.2 |
| Big O, searching, sorting, path finding | 8.1 |
| Algorithms on data structures: pointer values, checks and steps | 8.2 |

| Physics | Owner |
|---|---|
| The electron volt and unit conversions | 1.1 |
| Precision, accuracy, repeatability, reproducibility | 1.2 |
| Photon energy, the Planck constant, the neutrino hypothesis | 2.1 |
| Exchange particles | 2.3 |
| Wave-particle duality, the de Broglie wavelength | 2.5 |
| The principle of superposition | 3.2 |
| Coherence and path difference | 3.3 |
| The diffraction grating equation | 3.4 |
| Scalars, vectors and resolving | 4.1 |
| Displacement, speed, velocity and acceleration | 4.3 |
| Newton's second law in terms of momentum, impulse | 4.5 |
| Kinetic and gravitational potential energy | 4.6 |
| Hooke's law and elastic strain energy | 4.7 |
| Thermistors | 5.2 |
| The potential divider | 5.3 |

When a new overlap turns up, settle it by the specification, move the definition to the owner, and add the row here.

## Checking against mark schemes

The specification says what to cover. The mark schemes say which wording earns the mark. A mark-scheme pass compares one topic's cards with the credited answers.

1. **Get the papers.** For Physics, download the topic questions and mark schemes into `sources/` (ignored by git, never commit them):
   ```bash
   python3 scripts/pull_mark_schemes.py waves "3. Waves"
   ```
   Each PDF is saved with a plain-text copy for searching. Sets M, N and P are AQA papers. Sets A to D mix in other boards, so do not rely on them alone.
2. **Read the mark schemes for the topic** next to the decks. Definitions and "explain" answers matter most, because marks depend on their wording. Calculations rarely need changing.
3. **Change a card** when its wording would not earn the mark, when the mark scheme rejects it (look for "do not allow", "reject" and "insufficient"), or when it is wrong.
4. **Add a card** when a mark scheme point comes up that no card covers and the specification section includes it.
5. **Leave a card alone** when it already says what the mark scheme credits in other words.

Status: Physics topics 2 and 3 have had this pass. The other Physics topics and all of Computer Science have not.

## Note rules

These add to `skills/revision-notes-generator/SKILL.md`.

- The first heading is `# <n.m> <Subtopic name>`, the same as the file name.
- The next line is `**Specification (<board and code> <section>):** <what the section requires>`.
- No horizontal rules. No number or letter prefixes on headings below the title.
- No "check" flags and no "beyond source" labels in a finished note. Resolve the doubt, then state the fact plainly or remove it.
- Do not name the source notes in the text.
- The note ends with a summary table of key terms or key equations.

## Reporting

Finish by listing, in chat: the files changed, every fact corrected (old and new), anything you left out because you were not confident, and the final line of the check.
