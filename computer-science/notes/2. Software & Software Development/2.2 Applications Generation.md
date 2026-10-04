# 1.2.2 Applications Generation

## Nature of Applications

Software is categorised as either **applications software** or **systems software**.

**Applications software** is designed to be used by the end-user to perform a specific task or tasks. Application software requires systems software in order to run. Examples include word processors (Microsoft Word, Google Docs), spreadsheet software (Microsoft Excel, Google Sheets), web browsers (Google Chrome, Firefox), database management systems (MySQL, Oracle), graphics manipulation (Adobe Photoshop, GIMP), presentation software (Microsoft PowerPoint, Keynote), email clients (Outlook, Thunderbird), video editing software (Adobe Premiere, Final Cut Pro), IDEs (Visual Studio, IntelliJ IDEA), and virtualisation software (VMware, VirtualBox).

**Systems software** is low-level software responsible for running the computer system smoothly, interacting with hardware, and providing a platform for applications software to run. The user does not directly interact with systems software, but it ensures high performance. Examples include library programs, utility programs, the operating system, and device drivers.

---

## Utilities

**Utilities** are a type of system software integral to ensuring the consistent, high performance of the operating system. Each utility program has a specific function linked to the maintenance of the OS. Utility software is designed to help analyse, configure, optimise, or maintain a computer, and supports the operating system rather than performing end-user tasks directly.

| Utility | Purpose | Detail |
|---|---|---|
| **Compression** | Reduce file sizes for storage or transmission | Operating systems provide utilities to compress and decompress files, commonly used when transmitting large files across the Internet or compressing scanned files. |
| **Disk defragmentation** | Rearrange files on a hard drive to improve access speed | As the hard disk fills, files become fragmented across different parts of the disk, slowing read/write times. The defragmenter rearranges contents into contiguous blocks so they can be accessed faster, improving performance. Modern SSDs generally do not require defragmentation. |
| **Antivirus / Security** | Detect, alert, and remove threats | Responsible for detecting potential threats to the computer (viruses, malware, spyware), alerting the user, and removing them. Monitors the system and controls activities to protect from threats. Examples: Norton, McAfee, Windows Defender. |
| **Automatic updating** | Keep the OS up to date | Ensures updates are automatically installed when the computer is restarted. Updates tackle bugs or security flaws, making the system less vulnerable to malware and hacking threats. |
| **Backup** | Create routine copies of files for recovery | Automatically creates copies of specific files selected by the user, at intervals also specified by the user. Enables file recovery in the event of power failure, malicious attack, or other accident. |
| **File management** | Organise, search, rename, and relocate files | Includes creating, deleting, moving, and renaming files and folders. Examples: Windows Explorer, macOS Finder. |
| **Device drivers** | Interface between hardware and the OS | Ensures the OS and programs can communicate with hardware without needing to know precise hardware details. The OS usually manages drivers, but users may sometimes need to update them. |
| **System cleanup** | Free up space by removing unnecessary files | Removes temporary files, system cache, unused applications, and other data that can slow the system. Examples: CCleaner, Disk Cleanup on Windows. |

---

## Open Source vs Closed Source

**Source code** is the human-readable code written by a programmer before it has been compiled into object code.

> ⚠ Check: the PMT source states "Source code is written by a programmer and refers to object code before it has been compiled." The standard treatment is that source code and object code are distinct things: source code is the human-readable code, and object code is the machine code output produced after compilation. Source code does not "refer to" object code.

Whether software is described as **open source** or **closed source** refers to whether or not the source code is accessible to the public.

| | Open Source | Closed Source |
|---|---|---|
| **Definition** | Source code can be used by anyone without a licence and is distributed with the source code. Users can view, modify, and distribute it. | Requires the user to hold an appropriate licence. Users cannot access the source code as the company owns the copyright licence. The source code is hidden and proprietary. |
| **Examples** | Linux, Apache HTTP Server | Microsoft Windows, Adobe Photoshop |
| **Typical use** | Collaborative projects, customisation, transparency | Businesses requiring polished products, professional support, intellectual property protection |

**Benefits and drawbacks to the user:**

| | Benefits | Drawbacks |
|---|---|---|
| **Open Source** | Often free to use. Can be modified and improved by anyone. Technical support from online community. Can be modified and sold on. Customisable and transparent. | Support may be insufficient or incorrect, with no official user manuals. Lower security as may not be developed in a controlled environment. May be less user-friendly, with compatibility issues and possible bugs. |
| **Closed Source** | Thorough, regular, well-tested updates. Company provides expert support and user manuals. High levels of security as developed professionally. More polished and consistent products. | Licence restricts how many people can use the software at once. Users cannot modify or improve the software themselves. Costly and less customisable. |

**Benefits and drawbacks to the creator:**

| | Benefits | Drawbacks |
|---|---|---|
| **Open Source** | Collaboration, community engagement, faster innovation | Less control over the software, burdened with requests from users |
| **Closed Source** | Greater control, revenue through sales, intellectual property protection | Slower innovation, full responsibility for updates and flaws |

Whether a user chooses open or closed source software depends on the **suitability of the software to the task**. The user must also consider **costs** (implementation, maintenance, training of staff, licence) and **functionality** (features available, ease of use).

---

## Translators

A **translator** is a program that converts high-level source code into low-level object code (machine code), which is then ready to be executed by a computer. There are three types of translator.

### Compiler

A **compiler** translates the entire high-level source code into machine code all at once, after carrying out a number of checks and reporting back any errors. The initial compilation process is longer than using an interpreter or assembler. If changes need to be made, the whole program must be recompiled.

Once compiled, the resulting machine code is specific to a particular processor type and operating system, so it can only be executed on certain devices. However, compiled code can be run without a translator being present. Compiled code executes faster than interpreted code because translation has already been completed.

### Interpreter

An **interpreter** translates and executes code line-by-line. It stops and produces an error if a line contains an error. Interpreters may initially appear faster than compilers as code is instantly executed, but overall execution is slower than running compiled code because the source must be re-translated each time the program runs.

This line-by-line approach makes interpreters useful for testing and debugging sections of code, as time is not wasted compiling the entire program before it has been fully debugged. Interpreted code requires an interpreter to be present on the device in order to run. However, code can be executed on a range of platforms as long as the right interpreter is available, making interpreted code more portable than compiled code.

### Assembler

**Assembly code** is a low-level language, considered to be the "next level up" from machine code. Assembly code is platform-specific because the instructions used are dependent on the instruction set of the processor.

An **assembler** translates assembly code into machine code. Each line of assembly code is equivalent to almost one line of machine code, so code is translated on approximately a one-to-one basis. Unlike interpreters and compilers that work with high-level languages, assemblers deal with low-level languages.

### Translator comparison

| Feature | Compiler | Interpreter | Assembler |
|---|---|---|---|
| **Input** | High-level source code | High-level source code | Assembly language (low-level) |
| **Translation method** | Translates all at once | Translates and executes line-by-line | Translates on near one-to-one basis |
| **Speed of translation** | Slower initial compilation | No separate compilation step | Fast (simple one-to-one mapping) |
| **Speed of execution** | Fast (pre-translated) | Slower (re-translated each run) | Fast (close to machine code) |
| **Error reporting** | Reports all errors after compilation | Stops at the first error encountered | Reports errors during assembly |
| **Translator needed at runtime?** | No | Yes | No |
| **Portability** | Low (platform-specific output) | High (runs on any platform with the interpreter) | Low (platform-specific) |
| **Best for** | Distribution of finished software | Testing and debugging during development | Low-level hardware programming |

*(Beyond source: common languages and their translators include C, C++, Swift (compiled), Python, JavaScript, Ruby, PHP (interpreted), and Assembly Language (assembled). Java is commonly compiled to bytecode, which is then interpreted or JIT-compiled by the JVM.)*

---

## Stages of Compilation

When a compiler is used, high-level code goes through four stages before it is turned into object code ready to be executed.

### Lexical Analysis

In the first stage, **whitespace and comments are removed** from the source code. The remaining code is then analysed for keywords, identifiers (names of variables and constants), operators, and separators. These are **replaced with tokens**, and information about each token (its type and associated identifier) is stored in a **symbol table**.

Token types include:

| Type | Examples |
|---|---|
| **Keywords** | `var`, `const`, `function`, `for`, `while`, `if`, `return` |
| **Identifiers** | Variable names, function names |
| **Operators** | `+`, `++`, `-`, `*`, `=`, `>` |
| **Separators** | `,`, `;`, `{`, `}`, `(`, `)` |

**Example:** The code:
```
while     flag  =  False:
      print  "not found";
      #terminates when item is found
```
becomes (after removing whitespace and the comment):
```
while flag =False:
      print"not found";
```
Each element is then tokenised and recorded in the symbol table.

### Syntax Analysis

In this stage, the tokens produced during lexical analysis are **analysed against the grammar and rules of the programming language**. This process is known as **parsing**, which checks each line of code is well-formed. Any tokens that break the rules of the language are **flagged as syntax errors** and added to a list of errors.

Examples of syntax errors: undeclared variable type, incomplete set of brackets, mismatched parentheses, missing semicolons, invalid characters (e.g. `$` in languages that do not permit it).

An **abstract syntax tree (AST)** is produced, which is a tree-based (graph-based) representation of the source code's structure. Further detail about identifiers is also added to the symbol table.

**Semantic analysis** is also carried out at the syntax analysis stage, where logic mistakes within the program are detected. Examples of semantic errors: multiple declaration of the same identifier, use of undeclared identifiers.

### Code Generation

The abstract syntax tree produced in the syntax analysis stage is traversed and used to **generate machine code** (object code) that can be executed by the computer.

### Optimisation

This stage searches through the code for areas where it could be made more efficient. The aim is to **make the code faster to execute** and **reduce the memory required**, although this stage can significantly **add to the overall time taken for compilation**.

Insignificant, redundant parts of code are detected and removed. Repeated sections of code may be grouped and replaced with a more efficient piece of code that produces the same result. A common optimisation action is removing duplicate code (e.g. if an identical function is written twice, the compiler includes it only once in the object code).

There is a danger, however, that **excessive optimisation may alter the way the program behaves**.

---

## Linkers, Loaders and Use of Libraries

Most programs use external pieces of code, including subroutines and libraries from outside sources.

### Linkers

A **linker** is a piece of software responsible for linking external modules and libraries included within the code. It combines different code files and libraries into a single executable, resolving references between files. There are two types of linking:

**Static linking:** Modules and libraries are added directly into the main executable file. This increases the file size. Any external updates to modules and libraries will not affect the program, which means a specific version of a library can be guaranteed. The executable is self-contained.

**Dynamic linking:** Only the addresses (references) of modules and libraries are included in the file where they are referenced. When the program is run, the loader retrieves the required library or module from the specified address at runtime. Files remain small, and external updates feed through to the main file automatically without needing to rewrite the code. However, the library must be present on the system during execution.

| | Static Linking | Dynamic Linking |
|---|---|---|
| **File size** | Larger (libraries embedded) | Smaller (only references stored) |
| **Updates** | External updates do not affect program | External updates automatically apply |
| **Version control** | Specific library version guaranteed | Uses whatever version is currently installed |
| **Independence** | Self-contained executable | Requires libraries to be present at runtime |

### Loaders

**Loaders** are programs provided by the operating system. When a file is executed, the loader retrieves the program (or its required libraries/subroutines) from the given memory location and loads the executable file into memory so it can be run.

### Use of Libraries

**Libraries** are collections of pre-compiled, pre-written code (functions, classes, procedures, scripts) that can be incorporated within other programs using either static or dynamic linking. They are ready-to-use and error-free, saving time developing and testing modules. Libraries can be reused within multiple programs.

Libraries are often used to provide a specialised range of functions (e.g. mathematical, graphical) that would otherwise require significant time and effort to develop, saving programmers from having to "reinvent the wheel" and instead making use of others' expertise. Most programming languages come with **standard libraries** offering basic functionalities, and developers also have access to **third-party libraries** shared through package managers.

**Benefits of libraries:** Save development time and effort. Pre-tested and reliable, reducing errors. Reusable across different programs and projects. Popular libraries have strong community support and documentation.

**Drawbacks of libraries:** Dependency issues if a library is discontinued or not maintained. Compatibility issues with different library versions or systems. Using a large library for a small task can add unnecessary complexity and size (overhead) to the application.

---

## Key Terms Summary

| Term | Definition |
|---|---|
| **Applications software** | Software designed for end-users to perform specific tasks |
| **Systems software** | Low-level software that runs the computer system, interacts with hardware, and provides a platform for applications |
| **Utility software** | System software with a specific function linked to OS maintenance |
| **Open source software** | Software distributed with its source code, freely viewable, modifiable, and redistributable |
| **Closed source software** | Software where the source code is proprietary and hidden, requiring a licence to use |
| **Translator** | A program that converts source code into machine code |
| **Compiler** | Translates entire high-level source code into machine code at once |
| **Interpreter** | Translates and executes high-level code line-by-line |
| **Assembler** | Translates assembly language into machine code on a near one-to-one basis |
| **Lexical analysis** | First compilation stage: removes whitespace/comments, tokenises code, populates symbol table |
| **Syntax analysis** | Second compilation stage: checks tokens against language grammar, produces AST, detects syntax and semantic errors |
| **Code generation** | Third compilation stage: traverses AST to produce machine code |
| **Optimisation** | Fourth compilation stage: improves code efficiency by removing redundancy |
| **Linker** | Combines object files and libraries into a single executable |
| **Static linking** | Libraries embedded directly into the executable at compile time |
| **Dynamic linking** | Library addresses referenced at compile time, loaded at runtime |
| **Loader** | OS program that loads executables into memory for execution |
| **Library** | Collection of pre-compiled, reusable code modules |
| **Abstract syntax tree (AST)** | Tree-based representation of source code structure, produced during syntax analysis |
| **Symbol table** | Data structure storing information about identifiers and their associated tokens during compilation |
| **Parsing** | The process of checking each line of code is well-formed against language rules |
