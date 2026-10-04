# 1.4.3 Boolean Algebra

## Boolean Logic Fundamentals

**Boolean logic** is a system of logic based on binary values used in computer science and electronics to make logical decisions. Boolean operators evaluate to either **TRUE** (1) or **FALSE** (0), never both. Inputs and outputs are represented by letters (A, B, C, etc.).

**Boolean algebra** is a related but distinct concept: it is a mathematical system used to manipulate and simplify Boolean expressions. Boolean logic provides the underlying principles; Boolean algebra provides the rules for transformation.

### Operator Precedence

When evaluating expressions with multiple operators, a fixed precedence applies (analogous to BIDMAS in arithmetic):

1. **Brackets** (highest, evaluated first)
2. **NOT**
3. **AND**
4. **OR** (lowest)

Brackets override the default order. Inside brackets, the same NOT > AND > OR precedence applies.

**Example:** NOT (TRUE AND FALSE) evaluates the bracket first: TRUE AND FALSE = FALSE, then NOT FALSE = TRUE.

---

## Logic Gates and Truth Tables

A **logic gate** is a visual representation of a Boolean operation as a circuit element. A **truth table** shows every possible permutation of inputs and the corresponding output for a given Boolean expression.

### The Four Required Gates

| Operation | Gate | Symbols | Behaviour |
|---|---|---|---|
| **Conjunction** | AND | $A \wedge B$, $A.B$ | TRUE only when **both** inputs are TRUE |
| **Disjunction** | OR | $A \vee B$, $A + B$ | TRUE when **at least one** input is TRUE |
| **Negation** | NOT | $\neg A$, $\overline{A}$ | Inverts the input (TRUE becomes FALSE, FALSE becomes TRUE) |
| **Exclusive disjunction** | XOR | $A \oplus B$, $A \underline{\vee} B$ | TRUE when **exactly one** input is TRUE (inputs differ) |

### Truth Tables

**AND (Conjunction)**

| A | B | $A \wedge B$ |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

AND can be thought of as binary multiplication: the output is 1 only when both inputs are 1. AND has the next highest precedence after NOT.

**OR (Disjunction)**

| A | B | $A \vee B$ |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

OR can be thought of as binary addition (capped at 1): the output is 1 if at least one input is 1. OR has the lowest precedence.

**NOT (Negation)**

| A | $\neg A$ |
|---|---|
| 0 | 1 |
| 1 | 0 |

NOT is a unary operator (one input). It has the highest precedence of all Boolean operators.

**XOR (Exclusive Disjunction)**

| A | B | $A \oplus B$ |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

XOR differs from OR only when both inputs are TRUE: OR outputs 1, XOR outputs 0.

### Combining Boolean Operations

Boolean operators are combined to form complex expressions, just as arithmetic operators are combined in mathematics. Truth tables for compound expressions are built by evaluating intermediate columns step by step.

**Worked example:** Construct the truth table for $\neg(A \wedge (B \vee C))$.

| A | B | C | $B \vee C$ | $A \wedge (B \vee C)$ | $\neg(A \wedge (B \vee C))$ |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 1 | 0 | 1 |
| 0 | 1 | 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 | 1 | 0 |
| 1 | 1 | 0 | 1 | 1 | 0 |
| 1 | 1 | 1 | 1 | 1 | 0 |

Method: evaluate the innermost bracket first ($B \vee C$), then apply the next operation ($A \wedge ...$), then apply the outer NOT.

**Worked example (from circuit):** Given a circuit where A and B feed an AND gate producing D, and then D and C feed a XOR gate producing X, the expression is $X = (A \wedge B) \oplus C$.

| A | B | C | D = $A \wedge B$ | X = $D \oplus C$ |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 1 |
| 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

---

## Karnaugh Maps

A **Karnaugh map (K-map)** is a visual tool for simplifying Boolean expressions. It works by grouping together terms with common factors, making it easy to identify and eliminate redundant variables. K-maps are used in digital logic design to minimise the number of gates in a circuit.

### Creating a 2-Variable K-Map

For two variables A and B, the K-map is a 2x2 grid. One variable labels the rows, the other labels the columns. Each cell corresponds to one row of the truth table.

**Layout:** Place A across the top (columns: 0, 1) and B down the side (rows: 0, 1). Each cell contains the output value for that combination.

| | A=0 | A=1 |
|---|---|---|
| **B=0** | output for (A=0,B=0) | output for (A=1,B=0) |
| **B=1** | output for (A=0,B=1) | output for (A=1,B=1) |

### 3-Variable and 4-Variable K-Maps

For three variables, one variable takes the rows and two variables share the columns (or vice versa). For four variables, two variables share the rows and two share the columns.

**Gray code ordering is essential.** Adjacent columns (and rows) must differ by exactly one bit, including wraparound from the last column back to the first. The standard column ordering for two-variable headers is: 00, 01, 11, 10 (not 00, 01, 10, 11).

**3-variable example layout (variables A, B, C):**

|  | AB=00 | AB=01 | AB=11 | AB=10 |
|---|---|---|---|---|
| **C=0** | | | | |
| **C=1** | | | | |

**4-variable example layout (variables A, B, C, D):**

|  | AB=00 | AB=01 | AB=11 | AB=10 |
|---|---|---|---|---|
| **CD=00** | | | | |
| **CD=01** | | | | |
| **CD=11** | | | | |
| **CD=10** | | | | |

### Simplification Using K-Maps

**Step-by-step method:**

1. **Fill the map:** From the truth table (or by evaluating each minterm of the expression), place 1s and 0s into the corresponding K-map cells.
2. **Group the 1s:** Draw rectangular groups around adjacent 1s. Rules for grouping:
   - Groups must be **rectangular** (including squares).
   - Group sizes must be a **power of 2** (1, 2, 4, 8 cells).
   - Groups should be **as large as possible**.
   - Use **as few groups as possible** to cover all 1s.
   - **Overlapping is allowed** (and often necessary).
   - The grid **wraps around** in all directions (top-bottom, left-right).
3. **Read each group:** For each group, identify which variables remain constant across all cells in the group. Variables that change within the group are eliminated. A variable that is always 1 in the group appears un-negated; a variable that is always 0 appears negated.
4. **Combine with OR:** The simplified expression is the OR of all group terms (sum of products).

### K-Map Filling Example (3 Variables)

**Fill a K-map for:** $\neg A \wedge \neg B \wedge C \;\vee\; \neg A \wedge B \wedge \neg C \;\vee\; A \wedge \neg B \wedge C \;\vee\; A \wedge B$

Split at each OR to get four subterms, then place a 1 in every cell where that subterm is TRUE:

- $\neg A \wedge \neg B \wedge C$: A=0, B=0, C=1 → cell (C=1, AB=00) = 1
- $\neg A \wedge B \wedge \neg C$: A=0, B=1, C=0 → cell (C=0, AB=01) = 1
- $A \wedge \neg B \wedge C$: A=1, B=0, C=1 → cell (C=1, AB=10) = 1
- $A \wedge B$: A=1, B=1 (C irrelevant) → cells (C=0, AB=11) and (C=1, AB=11) = 1

Completed K-map (remaining cells are 0):

|  | AB=00 | AB=01 | AB=11 | AB=10 |
|---|---|---|---|---|
| **C=0** | 0 | 1 | 1 | 0 |
| **C=1** | 1 | 0 | 1 | 1 |

### K-Map Grouping Example (3 Variables)

Given the following pre-filled K-map, find groups and write the simplified expression:

|  | AB=00 | AB=01 | AB=11 | AB=10 |
|---|---|---|---|---|
| **C=0** | 1 | | 1 | 1 |
| **C=1** | 1 | | 1 | 1 |

**Group 1 (size 4):** Columns AB=11 and AB=10, both rows. A is always 1; B and C both change. Represents **A**.

**Group 2 (size 4, wraparound):** Columns AB=00 and AB=10, both rows. B is always 0; A and C both change. Represents $\neg B$.

**Simplified:** $A \vee \neg B$

### K-Map Worked Example (PMT 3-Variable)

The PMT source provides this truth table for a K-map simplification exercise:

| A | B | C | Y |
|---|---|---|---|
| 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 |

K-map:

|  | AB=00 | AB=01 | AB=11 | AB=10 |
|---|---|---|---|---|
| **C=0** | 1 | 0 | 1 | 1 |
| **C=1** | 0 | 0 | 0 | 1 |

Three groups can be identified:

- **Vertical group** (column AB=10, both rows): A=1, B=0, C changes. Represents $A \wedge \neg B$.
- **Horizontal group** (row C=0, cells AB=00 and AB=10, wrapping around): C=0, B=0, A changes. Represents $\neg B \wedge \neg C$.
- **Horizontal group** (row C=0, cells AB=11 and AB=10): C=0, A=1, B changes. Represents $A \wedge \neg C$.

**Simplified:** $Y = (A \wedge \neg B) \vee (\neg B \wedge \neg C) \vee (A \wedge \neg C)$

> ⚠ Check: the PMT source states the original unsimplified expression as $Y = (\neg A \wedge (\neg B \wedge \neg C)) \vee (A \wedge (\neg B \wedge C)) \vee (A \wedge (B \wedge \neg C)) \vee (A \wedge \neg(B \wedge \neg C))$, but the last term evaluates to 1 when A=1, B=1, C=1, giving Y=1 for that row, which contradicts the truth table showing Y=0. The truth table, K-map, and simplified expression are all mutually consistent; the stated original expression contains an error.

### K-Map Worked Example (4 Variables)

Given the 4-variable K-map:

|  | AB=00 | AB=01 | AB=11 | AB=10 |
|---|---|---|---|---|
| **CD=00** | 1 | 1 | 1 | 1 |
| **CD=01** | 1 | 1 | 1 | 1 |
| **CD=11** | 0 | 1 | 1 | 0 |
| **CD=10** | 0 | 1 | 1 | 0 |

**Group 1 (size 8):** The two middle columns (AB=01 and AB=11), all four rows. B is always 1 across this group; A, C, and D all change. Represents **B**.

**Group 2 (size 8):** The top two rows (CD=00 and CD=01), all four columns. C is always 0 across this group; A, B, and D all change. Represents $\neg C$.

These two groups cover all the 1s (with overlap).

**Simplified:** $B \vee \neg C$

---

## Simplifying Boolean Algebra

Boolean algebra provides rules for algebraically simplifying expressions. This is a more powerful method than K-maps and can simplify expressions that K-maps cannot handle.

### General Rules (Identity, Annulment, Idempotent, Complement)

**AND rules:**

| Rule | Expression | Name |
|---|---|---|
| Annulment | $X \wedge 0 = 0$ | AND with 0 always gives 0 |
| Identity | $X \wedge 1 = X$ | AND with 1 gives the original value |
| Idempotent | $X \wedge X = X$ | AND with itself gives itself |
| Complement | $\neg X \wedge X = 0$ | AND with its complement gives 0 |

**OR rules:**

| Rule | Expression | Name |
|---|---|---|
| Identity | $X \vee 0 = X$ | OR with 0 gives the original value |
| Annulment | $X \vee 1 = 1$ | OR with 1 always gives 1 |
| Idempotent | $X \vee X = X$ | OR with itself gives itself |
| Complement | $\neg X \vee X = 1$ | OR with its complement gives 1 |

> ⚠ Check: the Save My Exams source writes "X AND A = X" and "X OR A = X" for the idempotent rules; from context these mean X AND X = X and X OR X = X respectively, with "A" appearing to be a rendering error for "X".

### De Morgan's Laws

De Morgan's Laws allow a negation applied to an entire conjunction or disjunction to be distributed across the individual terms, with the operator switching:

$$\neg(A \wedge B) \equiv \neg A \vee \neg B$$

$$\neg(A \vee B) \equiv \neg A \wedge \neg B$$

**In words:** to negate a compound expression, negate each term individually and swap AND for OR (or OR for AND).

**Step-by-step application of** $\neg(A \wedge B) \equiv \neg A \vee \neg B$:

1. Change AND to OR: $\neg(A \vee B)$
2. Negate each term: $\neg(\neg A \vee \neg B)$
3. Negate the whole expression (to cancel the original outer NOT): $\neg\neg(\neg A \vee \neg B)$
4. Remove double negation: $\neg A \vee \neg B$

**Verification by truth table:**

| A | B | $A \wedge B$ | $\neg(A \wedge B)$ | $\neg A$ | $\neg B$ | $\neg A \vee \neg B$ |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 1 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 | 1 | 1 |
| 1 | 1 | 1 | 0 | 0 | 0 | 0 |

The final columns match, confirming equivalence.

**Practical significance:** De Morgan's Laws allow circuits to be built using only NAND gates or only NOR gates, which simplifies microprocessor manufacturing (e.g. flash memory construction).

### Distribution

Distribution describes how AND and OR interact with each other, analogous to factorising in arithmetic.

**Conjunction over disjunction (AND distributes over OR):**

$$A \wedge (B \vee C) \equiv (A \wedge B) \vee (A \wedge C)$$

**Disjunction over conjunction (OR distributes over AND):**

$$A \vee (B \wedge C) \equiv (A \vee B) \wedge (A \vee C)$$

Think of AND as multiplication and OR as addition: $A \times (B + C) = (A \times B) + (A \times C)$.

### Association

The associative law states that the grouping of operands with the same operator does not affect the result. Brackets can be freely added, removed, or repositioned among identical operators.

$$( A \wedge B) \wedge C \equiv A \wedge (B \wedge C) \equiv A \wedge B \wedge C$$

$$(A \vee B) \vee C \equiv A \vee (B \vee C) \equiv A \vee B \vee C$$

### Commutation

The commutative law states that the order of operands around an operator does not matter.

$$A \wedge B \equiv B \wedge A$$

$$A \vee B \equiv B \vee A$$

### Double Negation

Negating a value twice returns the original value.

$$\neg\neg A \equiv A$$

### Absorption

*(Beyond source for PMT; present in Save My Exams worked example.)*

The absorption law states:

$$A \vee (A \wedge B) = A$$

$$A \wedge (A \vee B) = A$$

This is useful when simplification produces terms where one variable appears both standalone and within a conjunction/disjunction with another variable.

### Worked Example: Algebraic Simplification

**Simplify** $(A \vee B) \wedge (A \vee C)$

**Step 1 -- Distribution:** Expand like multiplying brackets (treating OR as addition, AND as multiplication):

$(A \vee B) \wedge (A \vee C) = (A \wedge A) \vee (B \wedge A) \vee (A \wedge C) \vee (B \wedge C)$

**Step 2 -- Idempotent rule:** $A \wedge A = A$:

$= A \vee (B \wedge A) \vee (A \wedge C) \vee (B \wedge C)$

**Step 3 -- Commutation:** Rewrite $B \wedge A$ as $A \wedge B$:

$= A \vee (A \wedge B) \vee (A \wedge C) \vee (B \wedge C)$

**Step 4 -- Absorption:** $A \vee (A \wedge B) = A$:

$= A \vee (A \wedge C) \vee (B \wedge C)$

**Step 5 -- Absorption again:** $A \vee (A \wedge C) = A$:

$= A \vee (B \wedge C)$

**Result:** $A \vee (B \wedge C)$

---

## D-Type Flip Flops

A **D-type flip flop** is a fundamental logic circuit used in digital circuits and computer memory. It is a type of **bistable** circuit (two stable states) that stores the value of one bit.

### Components

- **D (Data input):** the value to be stored
- **CLK (Clock input):** a regular pulse generated by the CPU used to coordinate components
- **Q (Output):** the stored value
- **$\overline{Q}$ (Inverted output):** the complement of Q (always the opposite of Q)

### Operation

The D-type flip flop is **positive edge triggered**, meaning the output Q can only change at a **rising edge** of the clock signal (when the clock transitions from 0 to 1).

**Clock signal terminology:** A clock pulse is a square wave that alternates between high and low. The transition from low to high is the **rising edge**; the transition from high to low is the **falling edge**.

**At each rising edge:**
- Q takes the current value of D
- $\overline{Q}$ takes the complement of D
- Q then holds ("remembers") this value until the next rising edge

**Between rising edges,** Q remains unchanged regardless of what D does. Changes to D between clock edges are ignored.

### Internal Structure

The D-type flip flop circuit is built from **four NAND gates**. You do not need to recall the internal gate arrangement for the exam, but you should understand the input-output behaviour.

### Use Cases

- **Registers:** sets of flip flops combined to store multi-bit values
- **Shift registers:** data shifted one position per clock cycle
- **Counters:** sequential counting circuits
- **Memory units:** fundamental building blocks of RAM
- **Synchronous circuits:** any circuit that requires data to change only at defined clock intervals

### Worked Example: Drawing Q Output

Given clock and D signal waveforms, draw Q by applying these rules:

1. Assume Q starts at the same level as D at the beginning.
2. Draw vertical dotted lines at each rising edge of the clock.
3. At each rising edge, Q adopts whatever value D has at that instant.
4. Between rising edges, Q holds its value, even if D changes.

---

## Adder Circuits

An **adder** is a logic circuit that adds together binary inputs and outputs the result in binary. There are two types: half adders and full adders.

### Half Adder

A **half adder** adds two single-bit inputs (A and B) and produces two outputs: **Sum (S)** and **Carry ($C_{out}$)**.

**Circuit construction:** one XOR gate (for Sum) and one AND gate (for Carry).

- $S = A \oplus B$
- $C_{out} = A \wedge B$

**Truth table:**

| A | B | $C_{out}$ | S |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 0 |

**Quick method:** for each row, add A + B and write the result as a 2-bit binary number. The high bit is $C_{out}$ and the low bit is S. For example, 1 + 1 = 2 = 10 in binary, so $C_{out}$ = 1 and S = 0.

The half adder is "half" because it has no carry input, so it cannot be used for multi-bit addition beyond the least significant bit.

### Full Adder

A **full adder** extends the half adder by adding a third input, **Carry in ($C_{in}$)**, allowing it to handle a carry from a previous stage.

**Circuit construction:** two XOR gates, two AND gates, and one OR gate. Equivalently, a full adder can be built from **two half adders and an OR gate**:
- First half adder: inputs A and B, producing intermediate Sum1 and Carry1
- Second half adder: inputs Sum1 and $C_{in}$, producing final S and Carry2
- OR gate: inputs Carry1 and Carry2, producing $C_{out}$

**Outputs:**
- $S = A \oplus B \oplus C_{in}$ (XOR of all three inputs)
- $C_{out}$ = 1 when at least two of A, B, $C_{in}$ are 1

**Truth table:**

| A | B | $C_{in}$ | $C_{out}$ | S |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 1 |
| 0 | 1 | 0 | 0 | 1 |
| 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 | 0 |
| 1 | 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 1 |

**Quick method:** for each row, add A + B + $C_{in}$ (possible results 0, 1, 2, or 3) and write the answer as a 2-bit binary number. The high bit is $C_{out}$ and the low bit is S. For example, 1 + 1 + 1 = 3 = 11 in binary, so $C_{out}$ = 1 and S = 1.

### Ripple Adder

Because full adders have a carry input, they can be **chained together** to form a **ripple adder** for multi-bit addition. To add two n-bit numbers, n full adders are connected in series, with the $C_{out}$ of each stage feeding the $C_{in}$ of the next. At each stage, one bit from each number is provided as input A and B. The $C_{in}$ of the first stage is set to 0 (or connected to a half adder).

To add two 4-bit binary numbers: chain 4 full adders, with each adder's carry output connected to the next adder's carry input. Each adder receives one bit from each of the two numbers being added.

---

## Key Rules Summary

| Law | AND form | OR form |
|---|---|---|
| **Identity** | $X \wedge 1 = X$ | $X \vee 0 = X$ |
| **Annulment** | $X \wedge 0 = 0$ | $X \vee 1 = 1$ |
| **Idempotent** | $X \wedge X = X$ | $X \vee X = X$ |
| **Complement** | $X \wedge \neg X = 0$ | $X \vee \neg X = 1$ |
| **Double negation** | $\neg\neg X = X$ | |
| **Commutation** | $A \wedge B = B \wedge A$ | $A \vee B = B \vee A$ |
| **Association** | $(A \wedge B) \wedge C = A \wedge (B \wedge C)$ | $(A \vee B) \vee C = A \vee (B \vee C)$ |
| **Distribution** | $A \wedge (B \vee C) = (A \wedge B) \vee (A \wedge C)$ | $A \vee (B \wedge C) = (A \vee B) \wedge (A \vee C)$ |
| **Absorption** | $A \wedge (A \vee B) = A$ | $A \vee (A \wedge B) = A$ |
| **De Morgan's 1** | $\neg(A \wedge B) = \neg A \vee \neg B$ | |
| **De Morgan's 2** | $\neg(A \vee B) = \neg A \wedge \neg B$ | |

## Key Circuit Summary

| Circuit | Inputs | Outputs | Gates used | Purpose |
|---|---|---|---|---|
| **D-type flip flop** | D, CLK | Q, $\overline{Q}$ | 4 NAND gates | Stores 1 bit; Q updates to D on rising clock edge |
| **Half adder** | A, B | S, $C_{out}$ | 1 XOR, 1 AND | Adds two 1-bit numbers |
| **Full adder** | A, B, $C_{in}$ | S, $C_{out}$ | 2 XOR, 2 AND, 1 OR | Adds two 1-bit numbers plus carry; chainable into ripple adder |
