# 6.2 Thinking Ahead

## Inputs and Outputs

**Thinking ahead** means considering the different components of a problem and how they will be handled before implementation begins. This allows developers to anticipate difficulties that may arise during use and design strategies to make programs easy and intuitive.

All computational problems consist of **inputs** that are processed to produce **outputs**.

**Inputs** are any data required to solve the problem, usually entered by the user or passed as a parameter to a subroutine. When identifying inputs, consider:

- The **data type** of each input
- The **order** in which data is input
- The **method of input** (e.g. keyboard, card reader, touch screen)
- The **size and format** of the data

**Outputs** are the results passed back once inputs have been processed. Outputs are not limited to on-screen display. Output data can be visual, audio, or physical, and may require devices such as a printer, speaker, or cash dispenser.

When identifying outputs, consider:

- What data is returned (a value, an index, a boolean, a message, or nothing)
- The data type and format of the output
- The output device used to relay results to the user

**Design approach:** designers typically start by determining the required outputs based on user requirements, then work backwards to identify the inputs needed and the processing required to produce those outputs.

### Worked Example: ATM Program

| Inputs | Outputs |
|---|---|
| Transaction type (deposit, balance check, or withdrawal) | If deposit: display total amount entered on screen |
| Card details, captured via magnetic stripe card reader | If balance check: display total account balance on screen |
| PIN, entered via keypad | If withdrawal: dispense correct amount of cash |
| | Print receipt to confirm transaction |
| | Speaker provides verbal feedback throughout |

**Input devices:** touch screen, magnetic stripe card reader, keypad.
**Output devices:** monitor, cash dispenser, printer, speakers.

### Formal Definition Format

Inputs and outputs can be defined formally using a structured format:

```
Name: LinearSearch
Input: A list of integers my_list = (i₁, i₂, i₃, ..., iₙ)
Output: The index of the element as an integer
```

If inputs and outputs are not explicitly defined, creating the algorithm becomes harder and can cause errors when unexpected events occur.

---

## Preconditions

**Preconditions** are requirements/conditions that must be met before a program or subroutine can execute successfully. If preconditions are not met, the program will fail to execute, crash, or return an invalid answer.

Specifying preconditions means a subroutine can safely expect the arguments passed to it to meet certain criteria. **Arguments** are the values passed into the parameters of a subroutine.

### Where Preconditions Are Enforced

Preconditions can be handled in two ways:

| Approach | How it works | Advantages | Drawbacks |
|---|---|---|---|
| **Tested within the code** | The subroutine itself checks that conditions are met before proceeding | Prevents crashes from invalid input without relying on the user; the program handles validation automatically | Increases the length and complexity of the code; more time needed to debug and maintain |
| **Specified in documentation** | Conditions are stated in the documentation accompanying the subroutine; it is the user's/caller's responsibility to ensure inputs meet requirements | Reduces program length and complexity; saves development and maintenance time | Relies on the caller reading and following the documentation; no protection if they do not |

### Example 1: Precondition Tested in Code (Stack Pop)

The `pop()` function removes the last item added to a stack. Its precondition is that the stack must not be empty (i.e. `top > 0`):

```
function pop():
    if top = 0 then
        print "No items in the stack."
    else:
        element = stack[top]
        top = top - 1
    endif
endfunction
```

Without this check, popping from an empty stack would produce an error and crash the program.

### Example 2: Precondition in Documentation (Factorial)

The `factorial` function can only be called on non-negative integers. Rather than checking this within the code, the precondition is specified in the documentation.

> ⚠ Check: the source first describes this as "positive numbers" then as "non-negative". The correct precondition is **non-negative integers** (n >= 0), since 0! = 1 is defined.

### Example 3: Binary Search Preconditions

```
Name: BinarySearch
Inputs: A list of integers my_list (i₁, i₂, i₃, i₄, ..., iₙ)
Outputs: The index of the element as an integer
Preconditions: length of my_list > 0, type(my_list) = int, list must be sorted
```

If an unordered list is passed to a binary search, it will fail to execute correctly.

### Common Preconditions

- The parameter list must not be empty (otherwise index out of bounds errors occur)
- Data may need to be of the same data type (otherwise invalid comparisons are made)
- The target/search value must be the same type as the list elements and cannot be empty
- For an O(n²) algorithm like bubble sort, a limit on input size may be needed to prevent excessive execution time

### Advantages of Specifying Preconditions

- When provided in documentation, the developer knows what checks are required before calling the subroutine
- When built into the subroutine, the program handles validation automatically, preventing the developer from needing to write additional checking code
- Defining preconditions (including inputs and outputs) makes subroutines more **reusable** and suitable for packaging into a library

### Worked Example: Furniture Planning Software

**Scenario:** Software lets users plan furniture positions in a room. Users enter room dimensions and choose furniture from a library, then view the room in 3D.

**Question:** Suggest two preconditions that must be met before the software will run.

**Answer:**
1. All room dimensions entered must be greater than 0.
2. Width, length, and height of the room must have been entered.

**Examiner tip:** stating "room dimensions" alone is not enough. You must provide a condition that can be evaluated, e.g. "greater than 0".

---

## Caching

**Cache** is the small, fast storage on a processor used to temporarily store frequently used data and instructions while a program is running.

**Caching** is the process of storing instructions or values in cache memory after they have been used, as they may be needed again. This avoids the slower process of retrieving them from secondary storage. Caching is usually performed automatically by the operating system, though some languages such as C allow direct manipulation of the underlying hardware.

### Web Caching

Web pages that a user frequently accesses are cached so that the next time they are visited, content loads without delay. Images and text do not need to be re-downloaded, which frees up bandwidth for other tasks on the network.

### Prefetching

**Prefetching** is a more advanced form of caching and thinking ahead. Algorithms predict which instructions are likely to be needed soon and load them into cache before they are actually fetched. This reduces the time spent waiting for instructions to be loaded from the hard disk into RAM.

### Benefits of Caching

- Faster access to frequently used data and instructions
- Reduces the need to retrieve data from slower secondary storage
- Web caching saves bandwidth by avoiding repeated downloads
- Prefetching further reduces wait times by anticipating future needs

### Drawbacks of Caching

- Prefetching algorithms can only provide an informed prediction; there is no guarantee the predicted instructions will actually be needed
- The effectiveness of caching depends on how well the caching algorithm manages the cache
- Larger caches take longer to search, and cache size limits how much data can be stored
- Can be difficult to implement, though performance gains are significant when done effectively

---

## Reusable Program Components

Commonly used functions and subroutines are packaged into **libraries** for reuse. Examples of library subroutines include printing, type casting, finding the maximum/minimum value of a list, and generating random numbers.

Teams working on large projects may also create their own libraries so that components used in multiple places can be reused. **Reusable components** include:

- Implementations of abstract data structures (queues, stacks, linked lists)
- Classes and subroutines
- Standard algorithms (quick sort, merge sort)

### Link to Decomposition

When designing software, the problem is **decomposed** (broken down into smaller, simpler tasks). This allows developers to think ahead about how each task can be solved and identify where previously developed or externally sourced components can be reused to simplify development.

### Benefits of Reusable Components

- **More reliable** than newly coded components, as they have already been tested and bugs dealt with
- **Saves time, money, and resources** during development
- Subroutines can be reused with different arguments to produce a variety of outputs
- Well-tested components can be **reused in future projects**, further reducing development costs
- Thoroughly tested and documented components reduce the need for additional testing

### Drawbacks of Reusable Components

- **Compatibility issues** may arise when integrating third-party components with existing software
- Components may need to be **modified** to work with the rest of the software, which can sometimes be more costly and time-consuming than developing them in-house

---

## Key Terms Summary

| Term | Definition |
|---|---|
| **Input** | Any data required to solve a problem, entered by the user or passed as a parameter |
| **Output** | The result passed back after inputs have been processed |
| **Precondition** | A requirement/condition that must be met before a subroutine can execute successfully |
| **Argument** | A value passed into the parameter of a subroutine |
| **Caching** | Storing frequently used data/instructions in cache memory for faster future access |
| **Prefetching** | Predicting which instructions will be needed and loading them into cache in advance |
| **Library** | A collection of pre-written, tested, reusable subroutines packaged for use across projects |
| **Decomposition** | Breaking a problem down into smaller, simpler sub-tasks |
