# 1.2.4 Types of Programming Language

## 1.2.4 a) Programming Paradigms

**Programming paradigms** are different approaches to using a programming language to solve a problem. They are established conventions and practices that dictate how programs are structured and developed. Different paradigms are suited to different tasks, and the paradigm used depends on the type of problem that needs solving. Most programming languages such as Python support more than one paradigm.

Paradigms fall into two broad categories: **imperative** and **declarative**.

| Category | Paradigm | Description | Example Languages | Key Concepts |
|---|---|---|---|---|
| Imperative | **Procedural** | A subtype of imperative, structured around procedure calls using a sequence of step-by-step instructions | C, Go, Rust, Pascal, Python, Logo | Procedures, function calls, structured programming |
| Imperative | **Object-Oriented** | Organises code around "objects" (combining data and functionality) rather than functions | Java, C#, Swift, Python, Delphi | Classes, inheritance, polymorphism, encapsulation |
| Declarative | **Functional** | Built around reusing a set of functions that form the core of the program, closely linked to mathematics | Haskell, C#, Java | Function calls, function composition |
| Declarative | **Logic** | Defines a set of facts and rules based on the problem; queries are used to find answers | Prolog | Facts, rules, queries |

**Imperative** programming paradigms use code that clearly specifies the actions to be performed. The programmer defines the exact steps the computer must follow.

**Declarative** programming focuses on stating the desired result rather than the exact series of instructions needed to achieve it. The programming language determines how best to obtain the result, and the details of how it is obtained are abstracted from the user. Declarative programming is common in expert systems and artificial intelligence.

### Strengths and Weaknesses of Paradigms

| Paradigm | Strengths | Weaknesses |
|---|---|---|
| Procedural | Efficient execution of straightforward tasks; clear top-to-bottom flow of control; easy to implement for algorithms; strong emphasis on step-by-step procedure execution | Can become unwieldy for large programs; lack of modularity can lead to code redundancy; not ideal for applications with complex states or behaviours; difficulty managing and scaling the system as it grows |
| Object-Oriented | Enhances modularity with encapsulation; enables real-world modelling using objects; code reuse through inheritance; polymorphism allows flexibility in interface design | Can lead to unnecessary complexity; inefficiency due to overhead (e.g. memory for objects); not always intuitive for all types of problems; misuse can lead to overly complex inheritance hierarchies |
| Assembly | Direct control over hardware; optimised performance due to low-level operations; transparent understanding of how the machine operates; potential for very efficient code | Extremely steep learning curve; hardware-specific, leading to a lack of portability; tedious and error-prone due to manual memory management; difficult to write, debug, and maintain large programs |

New paradigms arise, and existing ones adapt in response to changes in computing and software challenges.

---

## 1.2.4 b) Procedural Programming

**Procedural programming** is one of the most widely used paradigms as it can be applied to a wide range of problems and is relatively easy to write and interpret. It is a type of imperative programming that uses a sequence of instructions which may be contained within procedures. These instructions are carried out in a step-by-step manner. However, it is not possible to solve all kinds of problems with procedural languages, or it may be inefficient to do so.

Procedural languages use traditional **data types** such as integers and strings which are built into the language, and also provide **data structures** like dictionaries and arrays.

It focuses on grouping code into **functions** and **procedures** to promote reuse and improve clarity. Variables are used to hold the program's **state**, while **control structures** (like selection and iteration) determine the **flow of execution** throughout the program.

### Structured Programming

**Structured programming** is a popular subsection of procedural programming in which the control flow is given by four main programming structures:

**Sequence** means code is executed line-by-line, from top to bottom.

**Selection** means a certain block of code is run if a specific condition is met, using IF statements.

**Iteration** means a block of code is executed a certain number of times or while a condition is met. Iteration uses FOR, WHILE or REPEAT UNTIL loops.

**Recursion** means functions are expressed in terms of themselves. Functions are executed, calling themselves, until a certain condition known as a **base case** (which does not call the function) is met.

Procedural programming is therefore suited to problems that can easily be expressed as a series of instructions using the constructs above.

### Core Programming Concepts

| Concept | Explanation | Example |
|---|---|---|
| Variables | Storing data values that can change | `x = 10` |
| Constants | Storing values that remain unchanged | `PI = 3.1415` |
| Selection | Decision-making constructs | `if x > 5: print("Greater")` |
| Iteration | Using loops to repeat actions | `for i in range(3): print(i)` |
| Sequence | Executing statements sequentially | `x = 5` then `y = x + 10` |
| Subroutines | Organising code into reusable parts | `def greet(name): return "Hello, " + name` |
| String Handling | Operations on character strings | `name.upper()` |
| File Handling | Reading from and writing to files | `with open('file.txt', 'w') as file: file.write("Hello")` |
| Boolean Operators | Logical operations | `x > 5 and y < 10` |
| Arithmetic Operators | Basic mathematical operations | `sum_value = x + y` |

### Worked Example: Library Late Fees

This example demonstrates procedural design with modular functions:

```
const DAILY_CHARGE = 1

function calculateFee(days_overdue)
  IF days_overdue > 0 THEN
    RETURN days_overdue * DAILY_CHARGE
  ELSE
    RETURN 0
  ENDIF
END function

function calculateTotalFee(books)
  var total_fee = 0
  FOR each days_overdue IN books
    total_fee = total_fee + calculateFee(days_overdue)
  ENDFOR
  RETURN total_fee
END function

var books = [7, 3, 0, 10]
var total_fee = calculateTotalFee(books)
PRINT "Total Late Fee:", total_fee
```

This is well designed because two smaller functions are better than one larger function: `calculateFee` handles a single book, and `calculateTotalFee` iterates over an array of books, demonstrating modularity, reuse, and separation of concerns.

---

## 1.2.4 c) Assembly Language

**Assembly language** is the next level up from machine code and is part of a family of **low-level languages**. It is converted to machine code using an **assembler** when executed.

Assembly language uses **mnemonics** (abbreviations for machine code instructions) rather than binary, which makes it easier to use than direct machine code. Each mnemonic is represented by a numeric code.

The commands that assembly language uses are **processor-specific** as it directly interacts with the CPU's **special purpose registers**. This allows for direct interaction with hardware, so assembly language is useful in **embedded systems**.

Typically, each instruction in assembly language is equivalent to almost one line of machine code.

Assembly language sits between high-level languages (like Python, Java) and machine code (binary). Each type of computer CPU has its specific assembly language. The levels of abstraction from most to least abstract are: high-level interpreted languages (Python, JavaScript), high-level compiled languages (C, C++), assembly code, machine code (hexadecimal representations of binary), and binary code (not human-readable).

### Little Man Computer (LMC) Instruction Set

The **Little Man Computer (LMC)** is a hypothetical computer model used for understanding the fundamental operations and mechanics of a computer. It has key elements like memory, a calculator, an accumulator, and an instruction set.

| Mnemonic | Instruction | Function | Alternative Mnemonics |
|---|---|---|---|
| **ADD** | Add | Add the value at the given memory address to the value in the Accumulator | |
| **SUB** | Subtract | Subtract the value at the given memory address from the value in the Accumulator | |
| **STA** | Store | Store the value in the Accumulator at the given memory address | STO |
| **LDA** | Load | Load the value at the given memory address into the Accumulator | LOAD |
| **INP** | Input | Allows the user to input a value which will be held in the Accumulator | IN, INPUT |
| **OUT** | Output | Prints the value currently held in the Accumulator | |
| **HLT** | Halt | Stops the program, preventing the rest of the code from executing | COB, END |
| **DAT** | Data | Creates a flag with a label at which data is stored | |
| **BRZ** | Branch if zero | Branches to a given address if the value in the Accumulator is zero (conditional branch) | BZ |
| **BRP** | Branch if positive | Branches to a given address if the value in the Accumulator is positive or zero (conditional branch) | BP |
| **BRA** | Branch always | Branches to a given address no matter the value in the Accumulator (unconditional branch) | BR |

### LMC Example 1: Add Two Numbers

```
INP         // Input the first number
STA 90      // Store the first number in memory location 90
INP         // Input the second number
ADD 90      // Add the number in memory location 90 to the accumulator
OUT         // Output the result
HLT         // End the program
DAT         // Memory location 90 for storing data
```

### LMC Example 2: Modulus (Remainder)

This program returns the remainder when num1 is divided by num2. In a high-level language, this would be a single instruction: MOD.

```
         INP
         STA num1
         INP
         STA num2
         LDA num1
positive STA num1       // branches to 'positive' flag,
         SUB num2       // subtracting num2 while the result
         BRP positive   // of num1 minus num2 is positive
         LDA num1
         OUT
         HLT
num1     DAT
num2     DAT
```

The loop repeatedly subtracts num2 from num1. When the result goes negative, BRP no longer branches, and the last positive value of num1 (the remainder) is loaded and output.

### LMC Example 3: Find the Largest of Three Numbers

This program inputs three numbers, determines the largest, and outputs it. It demonstrates **branching logic** and how comparisons are chained using SUB and BRP.

```
         INP
         STA 91
         INP
         STA 92
         INP
         STA 93

         LDA 91
         SUB 92
         BRP compare13   // If first >= second, compare first to third
         LDA 92
         SUB 93
         BRP output2     // If second >= third, output second
         LDA 93
         OUT
         HLT

compare13 LDA 91
         SUB 93
         BRP output1     // If first >= third, output first
         LDA 93
         OUT
         HLT

output1  LDA 91
         OUT
         HLT

output2  LDA 92
         OUT
         HLT
```

The program first checks if the first number is greater than or equal to the second. If so, it compares the first against the third. If not, it checks whether the second is greater than or equal to the third. The greatest value is loaded and output.

### LMC Worked Example: Thermostat Validation

A thermostat validates that a user's temperature setting is between 15 and 25 degrees Celsius inclusive. It outputs 1 for valid, 0 for invalid.

```
         INP
         STA tempSetting
         LDA tempSetting
         SUB minTemp
         BRP checkMax      // If tempSetting >= 15, check against max
         LDA invalidVal
         BRA end

checkMax LDA maxTemp
         SUB tempSetting
         BRP isValid        // If maxTemp - tempSetting >= 0, input is valid
         LDA invalidVal
         BRA end

isValid  LDA validVal

end      OUT
         HLT

validVal    DAT 1
invalidVal  DAT 0
minTemp     DAT 15
maxTemp     DAT 25
tempSetting DAT
```

The label `checkMax` marks the section that checks whether the temperature setting is less than or equal to the maximum (25). It is reached only after confirming the input is at least 15. If a user inputs 14, the output is 0 because 14 < 15 fails the first check and the program loads the invalid value without reaching `checkMax`. To expand the range to 30 degrees, change `maxTemp DAT 25` to `maxTemp DAT 30`.

---

## 1.2.4 d) Modes of Addressing Memory

Machine code instructions are made up of two parts: the **opcode** and the **operand**. The opcode specifies the instruction to be performed. The operand holds a value related to the data on which the instruction is to be performed.

In some cases, the operand may hold the actual value on which the instruction is to be executed, but more often it holds an address related to where the data is stored.

**Addressing modes** allow for a much greater number of locations for data to be stored, as the size of the operand would otherwise constrain the number of addresses that could be accessed.

It is the addressing mode that specifies how the operand should be interpreted. The **addressing mode is part of the opcode**. The instruction format is: `[Instruction | Addressing Mode] [Operand]`, where the instruction and addressing mode together form the opcode.

### The Four Addressing Modes

**Immediate Addressing**: The operand is the actual value upon which the instruction is to be performed, represented in binary. The data is part of the instruction itself.

Example: `MOV AX, 1234h` moves the immediate hex value 1234h directly into the AX register.

**Direct Addressing**: The operand gives the memory address which holds the value upon which the instruction is to be performed. Direct addressing is used in LMC.

Example: `MOV AX, [1234h]` takes the value stored in memory location 1234h and moves it to the AX register.

**Indirect Addressing**: The operand gives the address of a register which holds another address, where the data is located. This adds a level of indirection: the operand points to a location that itself contains the final address.

Example: If BX contains the value 2000h, then `MOV AX, [BX]` moves the value from memory location 2000h to the AX register. This does not move 2000h into AX; it looks up what is stored at address 2000h and moves that value. When brackets `[ ]` surround a register in assembly language, it means to treat the value inside that register as a memory address and use the data at that address.

**Indexed Addressing**: An **index register** is used, which stores a certain value. The address of the operand is determined by adding the operand to the index register. This is necessary to add an **offset** in order to access data stored contiguously in memory, such as in arrays.

Example: If BX contains 0050h and SI has a base address 1000h, then `MOV AX, [BX + SI]` fetches data from effective address 1050h (1000h + 0050h) and moves it into AX.

### Addressing Modes Summary

| Mode | What the Operand Represents | Use Case |
|---|---|---|
| Immediate | The actual data value itself | Loading constants |
| Direct | The memory address holding the data | Simple memory access (used in LMC) |
| Indirect | The address of a register/location holding another address where the data is | Pointer-based access |
| Indexed | A value to be added to an index register to compute the effective address | Accessing elements in arrays or contiguous data |

### Worked Example: Register and Memory Trace

Given these instructions starting at address 1000, with initial register values AX=0000, BX=0003, DI=0002, CX=0010, and memory contents {0003: 5, 0005: 7, 0008: 0}:

```
1000: MOV AX, 8        // Immediate: AX = 8
1002: ADD AX, [BX]     // Indirect: BX=3, so add value at address 0003 (which is 5) to AX. AX = 8+5 = 13
1004: MOV [0008], AX   // Direct: store AX (13) at address 0008
1006: MOV CX, [BX+DI]  // Indexed: BX+DI = 3+2 = 5, so move value at address 0005 (which is 7) into CX
1008: HLT
```

After execution: AX = 13, memory address 0008 holds 13, and CX = 7.

The instruction at 1002 uses **indirect addressing** because the BX register's value (3) is treated as a memory address. The instruction at 1006 uses **indexed addressing** because it combines two register values (BX and DI) to compute the effective address (5).

---

## 1.2.4 e) Object-Oriented Programming

**Object-oriented programming (OOP)** is built around the idea of **classes**. A **class** is a template for an object and defines the **state** and **behaviour** of an object. State is given by **attributes**, which describe an object's properties. Behaviour is defined by the **methods** associated with a class, which describe the actions it can perform.

OOP is applicable to certain types of problem with lots of reusable components that have similar characteristics. It focuses on making programs that are reusable and easy to update and maintain.

### Instantiation

Classes can be used to create objects by a process called **instantiation**. An **object** is a particular instance of a class. A class can be used to create multiple objects with the same set of attributes and methods.

A class is usually associated with an entity. For example, a class called `Library` could have attributes `number_of_books` and `number_of_computers`, and methods `add_book` and `remove_book`. Similarly, `Book` could also be a class with attributes `reserved` and `onloan`, and methods `set_reserved` and `set_onloan`.

### Getters and Setters

A **setter** is a special method that sets the value of a particular attribute. For example, `set_reserved` would set the attribute `Reserved` to `True` when someone reserves a book.

A **getter** is a special method that retrieves the value of a given attribute.

Getters and setters exist to ensure attributes cannot be directly accessed and edited by users.

### Encapsulation

**Encapsulation** is the property of OOP where attributes are declared as **private** so they can only be altered by **public methods**. This makes code more reliable by protecting attributes from being directly accessed. Code for different classes can also be produced independently of others.

### Constructor

Every class must have a **constructor** method, which is called `new`. A constructor allows a new object to be created and defines its initial attribute values.

### Pseudocode Example: Book Class

```
class Book:
    private reserved
    private onLoan
    private author
    private title

    public procedure new(title, author, reserved, onLoan)
        title = givenTitle
        author = givenAuthor
        reserved = givenReserved
        onLoan = givenOnLoan
    end procedure

    public function set_reserved()
        reserved = True
    end function
end class
```

Creating a new object using the constructor:

```
myBook = new Book('Great Expectations', 'Charles Dickens', 'False', 'False')
```

Calling a setter on an object:

```
myBook.set_reserved()
```

### Inheritance

**Inheritance** is a property of OOP where a class can inherit from another class. The **subclass** (or derived class) possesses all of the methods and attributes of the **superclass** (or parent class) and can have its own additional properties.

For example, a `Biography` class could inherit from `Book` and have its own attributes such as `Subject` and a shorter loan duration, but would still have `author` and `title`. This allows programmers to effectively reuse certain components and properties while making some changes.

Inheritance is expressed as:

```
class Biography inherits Book
```

### Polymorphism

**Polymorphism** is a property of OOP meaning objects can behave differently depending on their class. This can result in the same method producing different outputs depending on the object involved. There are two categories:

**Overriding** is redefining a method within a subclass and altering the code so that it functions differently and produces a different output.

**Overloading** is passing in different parameters into a method. Both forms produce different results depending on the scenario.

### Advantages of OOP

OOP allows for a high level of **reusability**, which makes it useful for projects where there are multiple components with similar properties. The properties of inheritance and polymorphism allow for this. Classes can also be used across multiple projects.

Encapsulation makes code more reliable by protecting attributes from being directly accessed. Code for different classes can be produced independently.

OOP requires **advance planning** to determine how the problem will be broken down into classes and how these will link to each other. A thorough design can produce a higher-quality piece of software with fewer vulnerabilities.

The **modular structure** used in OOP makes it easy to maintain and update.

There is a high level of **abstraction** and it is not necessary for programmers to know details about how code is implemented. Once classes have been created and tested, they can be reused as a **black box**, which saves time and effort.

### Disadvantages of OOP

OOP requires an alternative style of thinking, which can be difficult for programmers accustomed to other paradigms to pick up.

OOP is not suited to all types of problems. Where few components are reused, OOP may in fact result in a longer, more inefficient program.

OOP is generally unsuitable for smaller problems.

Inefficiency can arise due to overhead (e.g. memory for objects), and misuse can lead to overly complex inheritance hierarchies.

---

## Key Terms Summary

| Term | Definition |
|---|---|
| **Programming paradigm** | An approach to using a programming language to solve a problem |
| **Imperative** | Paradigm where code specifies the exact actions to be performed |
| **Declarative** | Paradigm where code states the desired result, not the steps |
| **Procedural** | Imperative paradigm using a sequence of step-by-step instructions in procedures |
| **Structured programming** | Subsection of procedural using sequence, selection, iteration, and recursion |
| **Base case** | The condition in recursion that does not call the function, stopping the recursion |
| **Assembly language** | Low-level language using mnemonics, converted to machine code by an assembler |
| **Mnemonic** | An abbreviation for a machine code instruction in assembly code |
| **Assembler** | Translates assembly language into machine code |
| **Opcode** | The part of a machine code instruction specifying the operation and addressing mode |
| **Operand** | The part of a machine code instruction related to the data or address |
| **Addressing mode** | Specifies how the operand in a machine code instruction should be interpreted |
| **Immediate addressing** | Operand is the actual data value |
| **Direct addressing** | Operand is the memory address of the data |
| **Indirect addressing** | Operand gives the address of a location holding another address where data resides |
| **Indexed addressing** | Effective address computed by adding the operand to the value in an index register |
| **Class** | A template for an object defining its attributes and methods |
| **Object** | A particular instance of a class |
| **Instantiation** | The process of creating an object from a class |
| **Attribute** | A property of an object that defines its state |
| **Method** | An action associated with a class that defines its behaviour |
| **Getter** | A method that retrieves the value of an attribute |
| **Setter** | A method that sets the value of an attribute |
| **Encapsulation** | Declaring attributes as private so they can only be accessed via public methods |
| **Constructor** | A method (called `new`) that creates a new object and sets its initial attribute values |
| **Inheritance** | A subclass inheriting all attributes and methods from a superclass |
| **Superclass** | The parent class from which other classes inherit |
| **Subclass** | The derived class that inherits from a superclass |
| **Polymorphism** | Objects behaving differently depending on their class |
| **Overriding** | Redefining a method in a subclass to produce different behaviour |
| **Overloading** | Passing different parameters into a method to produce different results |
