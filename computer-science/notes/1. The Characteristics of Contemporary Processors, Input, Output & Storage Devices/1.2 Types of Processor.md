# 1.1.2 Types of Processor

## RISC and CISC Processors

Every processor has an **instruction set**, the complete collection of instructions it can execute. Instruction sets vary between processors, and processors fall into two design philosophies: **RISC** and **CISC**.

### RISC (Reduced Instruction Set Computer)

A **Reduced Instruction Set Computer (RISC)** processor uses a **smaller instruction set** made up of simpler, uniform-length instructions. Each instruction takes **one clock cycle** to execute, which makes RISC processors well **suited to pipelining** (overlapping the fetch-decode-execute stages of successive instructions).

Because each instruction does less work, the **compiler must do more work** to translate high-level code into machine code, generating **more instructions** for any given task. This means RISC programs **take up more space in memory (RAM)**.

RISC processors have **fewer addressing modes**, **fewer transistors**, **require less power**, and **cost less to manufacture**. They are typically used in **smartphones and tablets**.

**Example: multiplying two values X and Y on a RISC processor**

```
LDA  R1, X
LDA  R2, Y
MULT R1, R2
STO  R1, X
```

Four separate instructions are needed: load each operand into a register, multiply, then store the result.

### CISC (Complex Instruction Set Computer)

A **Complex Instruction Set Computer (CISC)** processor uses a **larger instruction set** containing more complex, variable-length instructions. The design aim is to accomplish tasks in **as few lines of assembly code as possible**. These complex instructions are **built into the hardware**.

Because individual instructions do more work, they can **take more than one clock cycle** to execute, making CISC **not well suited to pipelining**. However, the compiler has **less work** to do and programs occupy **less space in memory**.

CISC processors have **more general-purpose registers**, **more addressing modes**, **more transistors**, **require more power**, and **cost more to manufacture**. They are typically used in **laptops and desktop computers**.

*(Beyond source: historically CISC was the dominant design. Over time many desktop processors adopted RISC-like internal micro-operations while retaining a CISC-compatible instruction set, blurring the boundary.)*

**Example: the same multiply operation on a CISC processor**

```
MULT A, B
```

A single instruction handles the load, multiply, and store operations internally.

### RISC vs CISC Comparison

| Aspect | RISC | CISC |
|---|---|---|
| Instruction set | Smaller, simpler instructions | Larger, more complex instructions |
| Clock cycles per instruction | One | Multiple |
| Pipelining | Suited | Not suited |
| Compiler complexity | More complicated (generates more instructions) | Less complicated |
| Memory usage | Programs take up more space | Programs take up less space |
| General-purpose registers | Fewer | More |
| Addressing modes | Fewer | More |
| Transistor count | Fewer | More |
| Power consumption | Lower | Higher |
| Manufacturing cost | Lower | Higher |
| Typical use | Smartphones, tablets | Laptops, desktops |

### Compatibility

A program written for a RISC processor **will not run on a CISC processor**, and vice versa, because the instruction sets are fundamentally different. A program written for one RISC processor **will not necessarily run on another RISC processor** either, since different RISC processors may implement different instruction sets.

---

## Graphics Processing Unit (GPU)

### What is a GPU?

A **Graphics Processing Unit (GPU)** is a specialised processor responsible for **processing graphics**, reducing the load on the CPU. While **CPUs are general-purpose processors**, **GPUs are designed specifically for graphics** and contain **hundreds or thousands of smaller processing cores** that work in **parallel**.

GPUs are a type of **co-processor**: a secondary processor designed to supplement the activities of the primary processor (the CPU). It is not possible to use only a GPU, as the **CPU assigns tasks to the GPU**.

GPUs have **built-in circuitry or instructions for common graphics operations** and can perform **an instruction on multiple pieces of data at one time**. This makes them faster than CPUs at tasks like transforming points in a polygon or shading pixels. The GPU can be **part of a discrete graphics card** or **embedded directly in the CPU**.

### Uses of GPUs Beyond Graphics

GPUs excel at any task that involves performing the same operation across large datasets in parallel:

**3D modelling** involves rendering lighting effects, textures, and shadows, all of which benefit from parallel computation.

**Data modelling** uses GPUs to handle large datasets and complex operations such as sorting and filtering, since many calculations can run simultaneously.

**Financial modelling** applies GPUs to risk modelling, option pricing, and scenario simulation, where many simulations can be run in parallel.

**Data mining** is the process of **analysing large amounts of data to find patterns**. The main computational tasks (sorting, searching, pattern recognition, statistical analysis, graph algorithms) are well suited to parallel execution.

**Complex numerical calculations** such as matrix multiplication and inversion can be decomposed and performed in parallel.

**Numerical simulations** in physics and engineering involve solving complex mathematical models, which can be parallelised.

**Solving differential equations** involves computations that can be distributed across many cores.

**Machine learning** involves **training a computer on a massive amount of data**, with extensive matrix multiplications and other computations that can be performed in parallel. After training, GPUs also speed up the process of **making predictions** on new data.

**Calculations on multiple data simultaneously** arise in scenarios like insurance pricing, risk modelling, and bill calculation, where the same formula must be applied to many data points at once.

### What Types of Task Are GPUs Suited For?

**Specialist instructions.** GPUs are designed to execute specialist instructions common in 3D graphics rendering, such as operations on matrices, vectors, and geometric transformations. These capabilities have been generalised over time, making GPUs suitable for a wide range of complex calculations beyond graphics.

**Multiple cores.** CPU cores are optimised for **serial processing**, whereas GPU cores are smaller but optimised for **parallel processing**. GPUs can perform many calculations simultaneously, making them ideal for tasks that can be broken into smaller independent parts, such as machine learning and large-scale data processing.

**SIMD processing.** **Single Instruction Multiple Data (SIMD)** describes processors with multiple processing elements that perform **the same operation on multiple data points simultaneously**. GPUs support SIMD because they were originally designed to perform identical operations on multiple pixels or vertices at once, a pattern common in image processing, simulations, and machine learning.

### Benefits of Using a GPU

**Parallel processing.** GPUs handle many tasks simultaneously because they are multicore processors.

**Speed.** Parallel processing accelerates tasks involving large datasets or complex computations.

**Efficiency.** GPUs perform more calculations per unit of power consumed compared to CPUs for parallel workloads, making them more energy efficient for suitable tasks.

---

## Multicore and Parallel Systems

### Multicore Processing

A **multicore system** has **more than one processing unit** within a single processor chip. Each core can **independently process instructions at the same time**. Cores can either work on the **same task** (completing it more quickly) or on **separate tasks** simultaneously.

*(Beyond source: common configurations include dual-core, quad-core, and octa-core processors.)*

### Parallel Processing

**Parallel processing** is the simultaneous execution of multiple processes or threads. It can be achieved in two ways: using **multiple cores** within a single CPU, or by using **more than one processor** together (for example, a CPU and a GPU working in combination).

**Parallel systems** can also exploit a single core by using **threading**, where multiple threads of execution are interleaved. However, multicore systems generally **perform better for larger projects** than single-core parallel (threaded) approaches.

### Benefits and Limitations of Parallel Processing

| Benefits | Limitations |
|---|---|
| **Speed.** Dividing a task into subtasks that execute simultaneously reduces total execution time. | **Limit on maximum speed.** Even with infinite processors, there is a limit to the speedup achievable if part of the program cannot be parallelised. |
| **Improved performance.** Simultaneous computation on different data subsets benefits machine learning, data mining, and scientific computing. | **Complex programming.** Writing parallel code is harder than serial code because tasks must be synchronised and data shared correctly. |
| **Better resource utilisation.** Multicore or multiple processors are used more effectively. | **Debugging difficulty.** Parallel programs are harder to debug due to the precise timing required for specific events. |
| **Problem solving.** Large, complex problems that lend themselves to decomposition can be solved more easily. | **Communication between processors.** Inter-processor communication can consume significant time and resources, potentially outweighing the benefits. |
| **Real-time applications.** Graphics rendering and other real-time tasks are more feasible and benefit significantly. | **Limited applicability.** Not all tasks can be parallelised and some must be executed serially. |

### Benefits of Multicore Processors

**Multitasking.** Each core can work on a different task, which is particularly effective when the user has multiple applications open at the same time.

**Background tasks.** On a single-core processor, a background task like an anti-malware scan can slow down the user's main task. A multicore processor can assign the background task to one core, reducing its impact on other work.

**Improved responsiveness.** If one program becomes unresponsive, it has less impact on overall system performance because other cores continue running their assigned tasks independently.
