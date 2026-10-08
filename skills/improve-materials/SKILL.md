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
- A reverse card has the form `<definition> - what term is this? | <term>` and sits directly after the definition it reverses. Only key terms get one. A law, a principle, an Act or a description of when something happens is never reversed.
- A list answer has at most three items. Split longer lists.
- No yes/no or true/false answers, and no fill-in-the-blank cards.
- Bundle or split, not both: a card that only restates two neighbouring cards is removed.
- No em dashes or semicolons on a card. Use a comma, a colon, or two sentences.
- Put a worked card (a calculation, a trace, a scenario) directly after the fact it applies. Check the arithmetic. Each main equation candidates calculate with has one single-step worked card.
- No card for rearranging an equation that already has a card.
- No card for the value of a constant the exam supplies. For Physics that is everything under "Fundamental constants and values" on AQA's data and formulae sheet ($c$, $e$, $h$, $g$, $R$, $k$, $N_A$, the particle masses and specific charges, the atomic mass unit) and the rest energies in its particle table, along with values a question gives, such as the specific heat capacity of water. Equations on the sheet keep their cards, because candidates are expected to use them fluently, and so do the quark and lepton properties.

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
| Why an ideal gas has no potential energy, $Q = mc\Delta\theta$ and the units of $\Delta\theta$ | 6.4 |
| The gas constants and $k = \frac{R}{N_A}$ | 6.5 |
| The internal energy of an ideal gas, how gas molecules exert a pressure | 6.6 |

When a new overlap turns up, settle it by the specification, move the definition to the owner, and add the row here.

## Checking against mark schemes

The specification says what to cover. The mark schemes say which wording earns the mark, and the examiner reports say which wording loses it. A mark-scheme pass compares one topic's cards with both.

Source material lives in `sources/`, which git ignores. It is copyrighted: never commit it, and never move it out of `sources/`.

```
sources/<subject>/notes/<provider>/          # PMT, SME and Cognito note sets
sources/physics/papers/as/combined/          # AQA AS papers 2016 to 2025, question and mark scheme together
sources/physics/papers/as/cleaned/           # the examiner report for each paper
sources/physics/papers/as/raw/               # the separate papers the two folders above were built from
sources/physics/papers/topic-questions/      # topic-sorted questions and mark schemes
sources/computer-science/papers/alevel/combined/   # OCR H446 papers 2021 to 2025, question and mark scheme together
sources/computer-science/papers/as/combined/       # OCR H046 papers 2022 to 2025
sources/computer-science/papers/<level>/clean/     # the examiner report for each paper
sources/computer-science/papers/<level>/raw/       # the separate papers the folders above were built from
```

1. **Collect the topic's questions.** Print every question on the topic with its mark scheme and examiner comment:
   ```bash
   python3 scripts/paper_digest.py physics "polaris|stationary wave|coheren" > /tmp/waves.txt
   python3 scripts/paper_digest.py computer-science "normal form|foreign key" --paper 1 > /tmp/databases.txt
   ```
   Use a pattern of the topic's key terms. In Computer Science, Paper 1 covers topics 1 to 5 and Paper 2 covers topics 6 to 8, and data structures (4.2) come up in both. Add `--calculations` to include questions whose mark scheme is mostly working. For more Physics questions, `scripts/pull_mark_schemes.py waves "3. Waves"` downloads topic-sorted papers (sets M, N and P are AQA; sets A to D include other boards).
2. **Read them next to the decks.** Definitions and "explain" answers matter most, because marks depend on their wording. Calculations rarely need changing.
3. **Change a card** when its wording would not earn the mark, when the mark scheme or examiner report rejects it (look for "do not allow", "reject", "insufficient" and "common error"), or when it is wrong.
4. **Add a card** when a mark scheme point comes up that no card covers and the specification section includes it.
5. **Leave a card alone** when it already says what the mark scheme credits in other words.

Status: every topic in both subjects had this pass on 5 October 2026. Run it again for a topic when new papers are added to `sources/`, or when a deck is rewritten.

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
