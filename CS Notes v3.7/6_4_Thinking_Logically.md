# 6.4 Thinking Logically

## Decision Making in Problem Solving

A **decision** is a result reached after some consideration. When solving problems and designing programs, many decisions must be made at different stages, from high-level design choices down to individual lines of code.

Examples of decisions during software development include choosing the **programming paradigm**, the **programming language**, the **input and output devices** required, and how to interact with those devices.

To simplify decision making, begin by **limiting the possible solutions** to a feasible subset. When choosing a programming language, for instance, consider its suitability to the problem, whether it provides enough functionality, whether the developer is comfortable with it, and whether time constraints allow learning a new language.

Identifying where decisions will need to be made early in the process allows enough information to be gathered so that an **informed decision** can be made.

## Structured Programming and Decision Structures

Most languages use **structured programming** techniques built from three constructs:

| Construct | Description | Examples |
|-----------|-------------|----------|
| **Sequence** | Statements executed one after another in order | Assignment, output |
| **Selection** | The flow of control is directed based on a Boolean condition (also called **branching**) | `if/then/else`, `switch/case` |
| **Iteration** | A sequence of instructions is repeated based on a stopping Boolean condition | `for`, `while`, `do while`, `do until` |

The purpose of these constructs is to **aid the readability, understanding and maintainability** of code.

A **block-structured language** (e.g. Python) uses only these three constructs to control execution flow. Each block of code should have a **single entry and exit point** and should ideally minimise breaking out of iterative blocks. This prevents unintended consequences such as entering or leaving a subroutine early or branching unintentionally.

## Planning Algorithms to Identify Decision Points

Before coding, algorithms should be planned using **flowcharts**, **pseudocode**, or **structured English**.

| Planning Method | Strengths | Weaknesses |
|-----------------|-----------|------------|
| **Flowcharts** | Visually show the flow of control; decisions are clear and easy to follow (diamond-shaped icons with True/False branches) | Time-consuming to create |
| **Pseudocode** | More accurately mimics programming language constructs without syntax constraints; any clear expression is acceptable | Less visual than flowcharts |
| **Structured English** | Natural language alternative to pseudocode | More verbose and imprecise |

Languages have specific **syntax**, **constructs**, and **idiosyncrasies** that differ between them, making it challenging to create a solution that can immediately be implemented in another language. Language-independent planning tools help avoid this problem.

## Conditions That Affect the Outcome of a Decision

When making a decision, the outcome is determined by evaluating several key factors:

- **Effectiveness**: which option best solves the problem?
- **Convenience**: which option is easiest to implement?
- **Feasibility/Reasonability**: is the option realistic given available resources and constraints?

To make an appropriate decision, these conditions should be **evaluated and ordered from most important to least important**. By prioritising one factor over others (effectiveness vs convenience vs feasibility), the best approach for a given solution becomes clearer. The priority may vary depending on the **purpose of the software** and its **end-users**.

## Identifying Decision Points in Programs

Most errors in a program occur when evaluating a **Boolean condition**, whether in a sequence, iteration, or selection statement. Care must be taken when creating Boolean conditions, especially long, complex conditions involving **multiple clauses**.

Decisions in programs typically occur in two situations:

- **Selection statements**: `if/then/else` or `switch/case`, which evaluate a condition and direct the program down one of several paths
- **Iteration statements**: usually a `while` loop, which repeats a block of code until a stopping condition is met

## How Decisions Affect Flow Through a Program

Decisions are **Boolean conditions** encountered in selection and iteration structures. They **affect the flow of control** of a program by determining which path of execution is followed.

Different decisions produce completely different routes through a program. For example, designing a runner game requires deciding whether it will be endless or level-based, and each choice leads to an entirely different program structure.

Thinking logically also involves identifying where decisions need to be made **by the user** within the program, and planning the outcomes of each possible decision. The program follows a different route depending on the user's choice.

### if/then/else Example

An `if/then/else` chain evaluates conditions sequentially. Each `elseif` introduces another decision point that directs the program through a different set of statements:

```
if today == "Monday" then
    print("Monday message")
elseif today == "Tuesday" then
    print("Tuesday message")
elseif today == "Wednesday" then
    print("Wednesday message")
...
else
    print("Invalid day")
endif
```

### switch/case Example

A `switch/case` statement achieves the same result as a chain of `elseif` statements but is often cleaner when matching a single variable against many discrete values:

```
switch entry:
    case "Monday":
        print("Monday message")
    case "Tuesday":
        print("Tuesday message")
    ...
    default:
        print("Invalid day")
endswitch
```

Both structures are functionally identical: each case or branch is a separate decision point that directs execution to a different set of statements.

### Nested Selection and Iteration

Iteration and selection statements can be **nested**, where one decision structure sits inside another. This creates multiple layers of decision points that collectively determine the program's flow.

**Example: grade assignment using nested if statements inside a repeat loop**

```
Count ← 0
REPEAT
    INPUT Score[Count]
    IF Score[Count] >= 70 THEN
        Grade[Count] ← "A"
    ELSE
        IF Score[Count] >= 60 THEN
            Grade[Count] ← "B"
        ELSE
            IF Score[Count] >= 50 THEN
                Grade[Count] ← "C"
            ELSE
                IF Score[Count] >= 40 THEN
                    Grade[Count] ← "D"
                ELSE
                    IF Score[Count] >= 30 THEN
                        Grade[Count] ← "E"
                    ELSE
                        Grade[Count] ← "F"
                    ENDIF
                ENDIF
            ENDIF
        ENDIF
    ENDIF
    Count ← Count + 1
UNTIL Count = 30
```

Each nested `IF` statement is a decision point that affects which grade is assigned. The outer `REPEAT...UNTIL` loop is itself controlled by a decision (whether `Count` has reached 30). This nested structure is functionally identical to a chain of `elseif` statements.

## Boolean Conditions and Logical Operators

**Boolean conditions** evaluate to either True or False and are used to control selection and iteration. They are constructed using combinations of **comparison operators** and **logical operators**.

### Comparison Operators

| Operator | Meaning |
|----------|---------|
| `==` | Equal to |
| `>` | Greater than |
| `>=` | Greater than or equal to |
| `<` | Less than |
| `<=` | Less than or equal to |
| `!=` | Not equal to |

### Logical Operators

| Operator | Meaning |
|----------|---------|
| `AND` | Both conditions must be True |
| `OR` | Either or both conditions must be True |
| `NOT` | Inverts the condition (True becomes False) |
| `XOR` | Exactly one condition must be True (not both) |

### Worked Example: Compound Boolean Condition

A teenager wants to see a 15-rated film costing £8. They need to be at least 15 years old **and** have at least £8. This requires `AND` because both conditions must be satisfied simultaneously:

```
if age >= 15 AND money >= 8 then
    entry ← True
endif
```

If `OR` were used instead, a 10-year-old with £8 or a 16-year-old with no money could gain entry, which is not the intended logic.

### Worked Example: Identifying Decision Points in an Algorithm

The following pseudocode removes elements containing numeric digits from a list of strings. Each decision point is annotated:

```
i ← 0
valid_element ← True
while len(my_list) > 0:             // Decision 1: list must have ≥1 element
    valid_element ← True
    element ← str(my_list[i])
    for index in element             // Decision 2: iterate over each character
        if element[index] in ["0","1","2","3","4","5","6","7","8","9"] then
            valid_element ← False    // Decision 3: character is a digit
            break                    // Exit the for loop early
        endif
    next index
    if valid_element == False then   // Decision 4: remove element if invalid
        my_list.pop(i)
    endif
endwhile
```

**Decision points identified:**

- **While loop (Decision 1)**: the list must contain at least one element for the loop body to execute.
- **For loop (Decision 2)**: iterates over every character in the current element. The stopping condition is reaching the end of the string.
- **First if statement (Decision 3)**: checks whether each character is a numeric digit. If any single digit is found, the element is considered invalid, `valid_element` is set to False, and a `break` exits the for loop early.
- **Second if statement (Decision 4)**: if the element was found to contain a digit, it is removed from the list using `pop`.

> ⚠ Check: the source pseudocode has issues. The for loop iterates over `list_item`, which is undefined (it should be `element`). The digit check compares against integer literals `[1,2,3,...]` but the element was cast to a string, so the comparison should use string literals `["0","1","2",...]`. Additionally, `i` is never incremented for valid elements, meaning the while loop would run indefinitely if a valid element is at position 0. The corrected version above uses `element` and string digit literals, but the infinite-loop issue remains in the source algorithm. In an exam, be prepared to identify and explain such logic errors.

**Warning on `break` statements**: `break` instructions are powerful for controlling flow but can be misused and cause unintended problems if they bypass important logic. Use them carefully.

## Summary: Why Thinking Logically Matters

Thinking logically allows a developer to **plan and prepare for different scenarios** by providing foresight of the decisions made throughout an entire program. It involves:

- Identifying **where** decisions must be made (both by the developer and by the user)
- Determining the **logical conditions** that govern each decision
- Understanding **how** each decision affects the flow of control through the program
- Evaluating conditions by prioritising **effectiveness, convenience, and feasibility**

Good decision making is the key to solving problems effectively.

## Key Terms Summary

| Term | Definition |
|------|-----------|
| **Decision** | A result reached after consideration, producing a True/False outcome in code |
| **Selection (Branching)** | Directing program flow based on a Boolean condition (if/else, switch/case) |
| **Iteration** | Repeating instructions based on a stopping Boolean condition |
| **Boolean condition** | An expression that evaluates to True or False |
| **Sequence** | Executing statements one after another in order |
| **Block-structured language** | A language that uses only sequence, selection, and iteration to control flow |
| **Flowchart** | A visual diagram showing program flow; decisions shown as diamond shapes |
| **Pseudocode** | Language-independent algorithm notation with no fixed syntax |
| **Structured English** | Natural language description of an algorithm; more verbose than pseudocode |
| **Nested structures** | Selection or iteration statements contained within other selection or iteration statements |
