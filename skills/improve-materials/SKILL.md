---
name: improve-materials
description: Improve an existing flashcard deck or revision note in this repository in place. Use when asked to fix, extend, tidy, re-check or update a deck or note that already exists here, or to fold new source material into one. For a subtopic that has no deck or note yet, use flashcard-generator or revision-notes-generator first, then apply this procedure.
---

# Improve Existing Materials

This repository keeps one living copy of each deck and note. An improvement edits that copy. It never creates a second version, a dated copy or a renamed file.

## Process

1. **Read what is there.** Read the whole deck and the matching note for the subtopic, not only the lines you were asked about. They share a name: `<subject>/flashcards/<n>. <topic>/<n.m> <subtopic>.txt` and `<subject>/notes/<n>. <topic>/<n.m> <subtopic>.md`.
2. **Read the specification section.** The note's **Specification** line names it (OCR H446 for Computer Science, AQA 7408 for Physics). Maths has decks only, one per section of OCR H240, named after the section number, and so has Further Maths, one per section of OCR H245 (Pure Core 4.01 to 4.10, Mechanics 6.01 to 6.06, Additional Pure 8.01 to 8.06). The specification decides what belongs, what it is called and how deep to go.
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
- **Use the repository's spellings**: `PD` and `EMF` in capitals with no full stops, `a.c.` and `d.c.` with them, and symbols as AQA's data and formulae sheet writes them ($F = BIl$, $T_{1/2} = 0.69RC$, time constant $RC$).
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
| Precision, accuracy, repeatability, reproducibility, parallax and zero errors | 1.2 |
| Photon energy, the Planck constant, the neutrino hypothesis | 2.1 |
| Alpha and beta particles and their decay equations, the range of the strong nuclear force | 2.1 |
| Electron capture | 2.3 |
| Exchange particles | 2.3 |
| Wave-particle duality, the de Broglie wavelength | 2.5 |
| Frequency and period, $f = \frac{1}{T}$ | 3.1 |
| The principle of superposition | 3.2 |
| Coherence and path difference | 3.3 |
| The diffraction grating equation | 3.4 |
| Scalars, vectors and resolving | 4.1 |
| Displacement, speed, velocity and acceleration | 4.3 |
| Newton's second law in terms of momentum, impulse | 4.5 |
| Kinetic and gravitational potential energy | 4.6 |
| Hooke's law and elastic strain energy | 4.7 |
| Conventional current | 5.1 |
| Thermistors | 5.2 |
| The potential divider | 5.3 |
| Radians, angular speed and $\omega = 2\pi f$, centripetal force and acceleration | 6.1 |
| Simple harmonic motion, the restoring force, amplitude and the equilibrium position of an oscillator | 6.2 |
| Damping, natural frequency, free and forced vibrations, resonance | 6.3 |
| Why an ideal gas has no potential energy, $Q = mc\Delta\theta$ and the units of $\Delta\theta$ | 6.4 |
| The gas constants and $k = \frac{R}{N_A}$, moles, molar mass and the Avogadro constant | 6.5 |
| The internal energy of an ideal gas, how gas molecules exert a pressure | 6.6 |
| Force fields, the inverse square law, where $r$ is measured from | 7.1 |
| What an equipotential surface is, and why equipotentials have no arrows | 7.2 |
| Comparing gravitational and electric fields, how $E$ varies with $r$ for a point charge | 7.4 |
| $\Delta W = Q\Delta V$, the equipotentials of electric fields, the sign of electric potential | 7.5 |
| How electrons move as a capacitor charges and discharges | 7.7 |
| The force on a charge moving in a magnetic field, the radius of its circular path | 7.8 |
| Magnetic flux and flux linkage | 7.9 |
| Mass-energy equivalence, $E = mc^2$ for all energy changes | 8.4 |
| Thermionic emission and the electron gun | 12.1 |

| Maths | Owner |
|---|---|
| The discriminant and its conditions for roots (its use for a line and a circle is 1.3) | 1.2 |
| The binomial expansion and $\binom{n}{r}$ (binomial probabilities are 2.4) | 1.4 |
| Trigonometric identities, including $\cos^2 A$ and $\sin^2 A$ in terms of $\cos 2A$ | 1.5 |
| Exponential models and why $e^{kx}$ suits them | 1.6 |
| Standard derivatives, including $e^{kx}$, and tangents and normals to curves | 1.7 |
| Areas by integration and integration as the limit of a sum | 1.8 |
| The trapezium rule and rectangle bounds | 1.9 |
| Magnitude, direction and position vectors in general (their use for velocity and force is 3.2 and 3.3) | 1.10 |
| S.I. units, including the units of force and moment | 3.1 |
| Motion graphs, constant acceleration, calculus and vectors in kinematics, projectiles | 3.2 |
| Resolving, friction, connected particles and modelling terms such as particle, light and smooth | 3.3 |
| Moments and where the weight of a rod or lamina acts | 3.4 |
| Informal correlation, correlation and causation, outliers and their two rules | 2.2 |
| Mutually exclusive and independent events | 2.3 |
| Binomial conditions, mean and variance, the normal approximation to the binomial | 2.4 |
| The distribution of $\bar{X}$, Pearson's correlation coefficient and its tests | 2.5 |

| Further Maths | Owner |
|---|---|
| Exam command words: show that, verify, determine, hence, detailed reasoning | 4.1 |
| Roots of unity and the geometry of multiplying complex numbers | 4.2 |
| How three planes meet, from the determinant and consistency | 4.3 |
| The scalar and vector products, equations of lines and planes | 4.4 |
| Partial fraction forms (their integration is 4.8) | 4.5 |
| Hyperbolic definitions, identities and logarithmic forms (their inverses' derivatives are 4.8) | 4.7 |
| Simple harmonic motion and damping as differential equations, forming a differential equation from Newton's second law | 4.10 |
| Dimensions of mechanical quantities | 6.1 |
| Work, kinetic and elastic energy, power, including $\mathbf{F} \cdot \mathbf{x}$ and $\mathbf{F} \cdot \mathbf{v}$ and the sign of work or power | 6.2 |
| Impulse, restitution and collisions in one and two dimensions | 6.3 |
| Centres of mass, suspension, sliding and toppling | 6.4 |
| $v\frac{\mathrm{d}v}{\mathrm{d}x}$ and variable-force motion (the methods of solving are 4.10) | 6.6 |
| Recurrence relations, their auxiliary equations, limits and models (the steps of induction are 4.1) | 8.1 |
| Number bases, divisibility tests, congruences, Fermat's little theorem and the order of $a$ modulo $p$ | 8.2 |
| Group axioms, orders of elements, Lagrange's theorem, cyclic groups and isomorphism | 8.3 |
| Areas and volumes from the vector product and the scalar triple product (the products themselves are 4.4) | 8.4 |
| Sections, contours, partial derivatives, the Hessian and tangent planes | 8.5 |
| Reduction formulae, arc length and area of a surface of revolution | 8.6 |

Further Maths assumes A-level Maths, so its decks do not repeat what the Maths decks own,
such as the basic partial fractions or vector magnitudes.

When a new overlap turns up, settle it by the specification, move the definition to the owner, and add the row here.

## Checking against mark schemes

The specification says what to cover. The mark schemes say which wording earns the mark, and the examiner reports say which wording loses it. A mark-scheme pass compares one topic's cards with both.

Source material lives in `sources/`, which git ignores. It is copyrighted: never commit it, and never move it out of `sources/`.

```
sources/<subject>/notes/<provider>/       # PMT, SME and Cognito note sets
sources/<subject>/<level>/spec/spec.md    # the specification (alevel/ and as/), with data-booklet.md where there is one
sources/<subject>/<level>/papers/         # past papers, question and mark scheme together, e.g. 2024-jun-p1.md
sources/<subject>/<level>/reports/        # the examiner report for each paper, e.g. 2024-jun-p1-er.md
```

Physics is AQA 7408 and 7407 (A-level Papers 1, 2, 3A and 3BD), Computer Science OCR H446 and H046, Maths OCR H240 and H230, and Further Maths OCR H245 and H235 (Pure Core, Mechanics and Additional Pure only).

1. **Collect the topic's questions.** Print every question on the topic with its mark scheme and examiner comment:
   ```bash
   python3 scripts/paper_digest.py physics "polaris|stationary wave|coheren" > /tmp/waves.txt
   python3 scripts/paper_digest.py computer-science "normal form|foreign key" --paper 1 > /tmp/databases.txt
   ```
   Use a pattern of the topic's key terms. In Computer Science, Paper 1 covers topics 1 to 5 and Paper 2 covers topics 6 to 8, and data structures (4.2) come up in both. In Maths, Pure is all of A-level Paper 1 and Section A of every other paper, Statistics is Section B of A-level Paper 2 and of AS Paper 1, and Mechanics is Section B of A-level Paper 3 and of AS Paper 2, so choose the papers with `--paper` and keep only that section's questions. In Further Maths, A-level Papers 1 and 2 and AS Paper 1 are Pure Core, Paper 3 and AS Paper 3 are Mechanics, and Paper 5 and AS Paper 5 are Additional Pure. Add `--calculations` to include questions whose mark scheme is mostly working. For more Physics questions, `scripts/pull_mark_schemes.py waves "3. Waves"` downloads topic-sorted papers (sets M, N and P are AQA; sets A to D include other boards).
2. **Read them next to the decks.** Definitions and "explain" answers matter most, because marks depend on their wording. Calculations rarely need changing.
3. **Change a card** when its wording would not earn the mark, when the mark scheme or examiner report rejects it (look for "do not allow", "reject", "insufficient" and "common error"), or when it is wrong.
4. **Add a card** when a mark scheme point comes up that no card covers and the specification section includes it.
5. **Leave a card alone** when it already says what the mark scheme credits in other words.

Run it again for a topic when new papers are added to `sources/`, or when a deck is rewritten. The status table below says which topics have had it.

## Status

What each topic has had done to it. Update this table whenever a pass is finished or a deck is added.

| Topics | Card rules (flashcard-v3.10) | Mark-scheme pass | Notes |
|---|---|---|---|
| Computer Science 1 to 8 | 8 October 2026 | 5 October 2026 | Yes |
| Physics 1 to 5 | 8 October 2026 | 5 October 2026 against AS papers, 16 October 2026 against A-level papers | Yes |
| Physics 6.1 to 6.3 | Written to them on 10 October 2026 | 16 October 2026, against A-level papers | 16 October 2026 |
| Physics 6.4 to 6.6 | 8 October 2026 | 16 October 2026, against A-level papers | 16 October 2026 |
| Physics 7.1 to 7.10 | 10 October 2026 | 16 October 2026, against A-level papers | 16 October 2026 |
| Physics 8.1 to 8.4 | Written to them on 18 October 2026 | 19 October 2026, against A-level papers | 19 October 2026 |
| Physics 12.1 to 12.3 (Turning Points) | Written to them on 19 October 2026 | 19 October 2026, against A-level Paper 3BD | 19 October 2026 |
| Maths 1.1 to 1.10 (Pure) | Written to them on 19 October 2026 | 19 October 2026, against A-level Papers 1 to 3 and AS Papers 1 and 2 | Decks only |
| Maths 2.1 to 2.5 (Statistics) | Written to them on 19 October 2026 | 19 October 2026, against A-level Paper 2 and AS Paper 1 | Decks only |
| Maths 3.1 to 3.4 (Mechanics) | Written to them on 19 October 2026 | 19 October 2026, against A-level Paper 3 and AS Paper 2 | Decks only |
| Further Maths 4.1 to 4.10 (Pure Core) | Written to them on 23 October 2026 | 23 October 2026, against A-level Papers 1 and 2 and AS Paper 1 | Decks only |
| Further Maths 6.1 to 6.6 (Mechanics) | Written to them on 23 October 2026 | 23 October 2026, against A-level Paper 3 and AS Paper 3 | Decks only |
| Further Maths 8.1 to 8.6 (Additional Pure) | Written to them on 23 October 2026 | 23 October 2026, against A-level Paper 5 and AS Paper 5 | Decks only |

Every section of OCR H240 now has a deck (Mechanics ends at 3.04). Further Maths has
Pure Core and both of Marco's options, Mechanics (6.01 to 6.06) and Additional Pure (8.01
to 8.06). Its cards lean on recognising which method a question needs and
the steps of that method, with one single-step worked card for each routine calculation
such as a scalar product, a vector product or a matrix product. The whole Maths set was
copied into the NeuroCards catalog on 19 October 2026.

Every Physics topic now has decks and notes. Marco takes the Turning Points option, which
Paper 3BD examines. Its decks and notes sit in `12. Turning Points in Physics` folders,
numbered after specification section 3.12.

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
