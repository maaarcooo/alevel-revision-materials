# 2.1.3 Thinking Procedurally

**Specification coverage:** 2.1.3 a) Identify the components of a problem | b) Identify the components of a solution to a problem | c) Determine the order of the steps needed to solve a problem | d) Identify sub-procedures necessary to solve a problem

---

## Identifying the Components of a Problem

**Thinking procedurally** means breaking a problem down into smaller parts that are individually easier to understand and easier to design. It is a core computational thinking skill that simplifies the task of writing a program.

### Abstraction

Before decomposing, irrelevant detail must first be stripped away. **Abstraction** is the act of removing unimportant details from a real-world problem and focusing only on the details that will form part of the solution.

Examples of abstraction in everyday computing:

| Scenario | What is abstracted away |
|---|---|
| Modelling a garden or football pitch | Individual blades of grass are replaced by a green mesh or image. Higher-fidelity simulations model more detail at the cost of greater processing power. |
| Saving a file | The user does not need to know how the OS writes data to disk or manages paging/segmentation in RAM. |
| Sending an email | The user does not need to know which protocols are used, how data is formatted, or what handshaking occurs. |
| Downloading content | Security checks (digital certificates, signatures, protocols) are hidden from the user. |

### Problem Decomposition

**Problem decomposition** is the process of continually breaking a large, complex problem down into smaller sub-problems that can be solved more easily. Benefits of decomposition:

- The problem becomes more **feasible to manage**.
- Work can be **divided between a team** according to each person's skill set.
- Each sub-problem is simpler to **test and maintain**, particularly through **unit testing**.
- Sub-problems that are **self-contained** and **well documented** make it easier to find and fix errors.
- Subroutines can be **reused** rather than rewriting code.

**Example: adventure game.** An adventure game could be decomposed into Characters, Adventures, and Enemies. Each of these is then decomposed further (e.g. Characters splits into Characters' Interactions and Characters' Appearance).

**Example: teacher calculating student grades.** Identifying the components of this problem means asking questions such as: how many classes are there? How many students? What grades are possible? How many assessments? If statistical analysis is needed, further components emerge: are assessments categorised by difficulty? Does question format (multiple choice vs. written) affect results?

### Top-Down Design (Stepwise Refinement)

**Top-down design** is the standard method for decomposing large problems. It breaks a problem into major tasks, then breaks each major task into smaller sub-tasks. Each sub-task is broken down until it can be solved by a single subroutine or module.

Key properties:

- **Higher levels** of the hierarchy give an overview of the problem.
- **Lower levels** specify detailed components.
- Each lowest-level sub-task should be **unable to be broken down further**, **easily solved**, and **clear in purpose**.
- The goal is to structure a program into **small, manageable tasks** that can be delegated to different developers.

**Book reservation system example (hierarchy):**

```
Level 1: Book reservation system problem
Level 2: Borrower input | Process request | Confirm request
Level 3: Borrower name | Book details | Collection location | Check book availability | Print estimated arrival date | Display account details
```

Each Level 3 component represents a single task that can be implemented as one subroutine.

---

## Identifying the Components of a Solution

Once the problem components are identified, the matching **solution components** must be identified. Where decomposition broke the problem down, this stage builds back up toward a working solution by deciding how each lowest-level component will be implemented.

### Procedural Abstraction

**Procedural abstraction** means using a procedure to execute a sequence of instructions that achieves a specific goal. Each identified component of the problem is turned into a procedure (or function) with defined inputs and outputs.

> **Examiner tip:** "Procedure" in this context does not strictly mean a subroutine that returns no value. It refers to any **unit of computation that performs a single task**. A **function** returns a value, whereas a procedure (in the strict sense) does not.

### Technical Details to Consider

When designing each solution component, the programmer must evaluate:

| Consideration | Examples |
|---|---|
| Input/output data types | Integer, real/float, string, boolean |
| Data structures required | Array, list, dictionary, linked list, hash table |
| Libraries required | Statistics module, math module |
| Output format | Array, list, dictionary, formatted output string |
| Data transformations and constructs | Multiplication, division, for loop, while loop, select/case |
| Algorithm efficiency | Does the algorithm need to be O(n) or better? |

### Worked Example: Book Reservation System

Each Level 3 component from the decomposition above can be mapped to a concrete implementation:

**Borrower name** could be implemented as a procedure `getName()`. It checks whether the user is signed in. If signed in, the borrower's name is retrieved by querying the library database using the borrower's ID. If not signed in, the user is redirected to a registration or sign-in page.

**Book details** could be implemented as a function that takes a book name entered in a text field, displays matching books stocked by the libraries, and returns the **ISBN** of the selected book (an ISBN is easier to handle programmatically than a string title).

**Collection location** could be implemented as a function returning the user's chosen location. A **drop-down field** is preferred over a text entry field to prevent erroneous data (e.g. entering a location where no library exists).

**Check book availability** could be implemented as a function that queries the database for books matching the selected ISBN and returns `True` if available or `False` if on loan.

### Reusable Components

During this stage, it is useful to identify tasks that could be solved using an **existing module, subroutine, or library**. Spotting where reusable components apply reduces development complexity and is a direct benefit of top-down design. Once all solution components are implemented, they are combined to form the full working solution.

---

## Determining the Order of Steps

Once solution components exist, the **order in which operations are performed** must be determined. Getting this wrong causes errors or produces nonsensical behaviour.

### Data Dependencies and Sequencing

Some subroutines depend on data produced by other subroutines. Where such a dependency exists, the producing subroutine must execute first. Where no dependency exists, subroutines may be able to **execute simultaneously** (concurrently). Programmers must examine each subroutine's required inputs to decide which can run in parallel and which must run in sequence.

General sequencing principles:

- **Inputs must be collected before processing** can begin. In the book reservation system, none of the processing subroutines can execute without the user's input.
- **Inputs must be validated** before being passed to the next subroutine. Invalid data should not propagate through the system.
- Programmers must determine both the **order of execution** and **how subroutines interact** with each other (what data is passed between them).

### Enforcing Sensible Ordering

Programs must explicitly enforce ordering that humans take for granted. Examples:

- An adventure game should not allow users to access levels they have not yet unlocked.
- A food delivery app should not allow food selection before the user confirms their location, nor allow payment before the order is confirmed.

These constraints feel obvious but must be **explicitly coded** into the software.

### Worked Example: Grade Calculation Steps

Calculating student grades must follow a defined order:

1. **Calculate the grade for each assessment:** for each question, mark it and store the value, then sum the values of all marked questions.
2. **Calculate the average grade for each student** across all their assessments: add up the grade for each assessment, divide by the number of assessments, store the result.
3. **Repeat steps 1-2 for each class.**

---

## Identifying Sub-Procedures

Problems can be decomposed using tables and lists, but for larger problems these become unwieldy. **Diagrams** are preferred for visualising decomposition.

### Hierarchy Charts

A **hierarchy chart** is a diagram that shows how a problem has been decomposed. Properties:

- Each problem is divided into multiple sub-problems, which are further divided until they cannot be divided any more.
- The chart shows how **modules and subroutines relate to each other** using a **tree structure**.
- Hierarchy charts can be created on paper, digitally, or generated programmatically by software.

**Mobile phone example:** A mobile phone system decomposes into Voice Calls, Text Messages, and Contact Data Store. Voice Calls decomposes further into Vibrate, Receive Voice, Receive Data, Convert to Analogue, and Send Voice. Send Voice in turn decomposes into Capture Voice, Convert to Digital, and Transmit to Network.

### Worked Exam Question

**Scenario:** Mabel is writing a computer game where the main character avoids enemies across increasingly difficult levels. The user selects a character (name, gender), chooses a difficulty level (easy, normal, challenging), and controls the character with left/right movement and a space bar jump. Touching an enemy costs a life. The character must reach the end of the level without losing all lives. One sub-procedure handles user input. Describe three other sub-procedures (6 marks).

**Model answer:**

- A sub-procedure to **select a character** (name, gender, etc.) that presents the user with options when choosing a character. [2 marks]
- A sub-procedure to **choose a level** that gives the user a choice of difficulty (easy, medium, challenging) by taking user input. [2 marks]
- A sub-procedure to **handle losing lives**. If the character has fewer than 0 lives remaining, the game ends. [2 marks]

> **Examiner tip:** Basic input procedures such as moving left and right are not credit-worthy in this context, but showing the *output* of a left/right move (e.g. updating character position on screen) would be.

---

## Key Terms Summary

| Term | Definition |
|---|---|
| **Thinking procedurally** | Breaking a problem down into smaller parts that are easier to understand and design |
| **Abstraction** | Removing unimportant details from a real-world problem to focus on solution-relevant details |
| **Problem decomposition** | Continually breaking a large, complex problem into smaller sub-problems that can be solved more easily |
| **Top-down design / Stepwise refinement** | Decomposing a problem by breaking it into major tasks, then sub-tasks, until each sub-task is a single subroutine or module |
| **Procedural abstraction** | Using a procedure to execute a sequence of instructions to achieve a specific goal |
| **Hierarchy chart** | A tree-structured diagram showing how a problem is decomposed into modules and subroutines |
| **Function** | A subroutine that returns a value |
| **Procedure** | A subroutine that does not return a value (in the strict sense), or more broadly any unit of computation performing a single task |
