# 1.1.1 Structure and Function of the Processor

## 1.1.1 Components of a Processor

The **processor (CPU)** is responsible for processing all data within the computer. It executes instructions which allow programs to run. It is made up of several key components: the Arithmetic and Logic Unit, the Control Unit, registers, and buses.

### The Arithmetic and Logic Unit (ALU)

The **ALU (Arithmetic and Logic Unit)** performs all **arithmetical and logical operations**.

**Arithmetical operations** include all mathematical operations such as addition, subtraction, multiplication, and division on fixed or floating point numbers. **Logical operations** include Boolean logic operations such as AND, OR, NOT, and XOR.

The ALU is made up of several sub-components:

| Sub-component | Function |
|---|---|
| **Arithmetic circuit** | Carries out arithmetic operations (addition, subtraction, multiplication, division) |
| **Logic circuit** | Carries out logic operations (AND, OR, NOT, XOR) |
| **Registers** | Additional registers within the ALU that can store data during operations |
| **Status flags** | Indicate conditions such as an **overflow flag** (value too large for the register) or a **zero flag** (result is zero) |
| **Buses** | Transport data around the ALU and to other parts of the CPU |

### The Control Unit (CU)

The **Control Unit (CU)** is the component of the processor which **directs the operations of the CPU**. It decodes instructions, controls data movement within the CPU, and generates timing signals to coordinate operations.

Its jobs include:

- Controlling and coordinating the activities of the CPU
- Managing the flow of data between the CPU and other devices
- Accepting the next instruction
- Decoding instructions
- Storing the resulting data back in memory
- Generating timing signals and controlling the other units of the computer

### Registers

**Registers** are **small memory cells** that operate at a **very high speed**. They are used to **temporarily store data** for a **single specific purpose** and have a **faster access speed** than RAM or secondary storage. All arithmetic, logical, and shift operations occur in these registers.

| Register | Abbreviation | Purpose |
|---|---|---|
| **Program Counter** | PC | Holds the **address** of the **next instruction** to be executed |
| **Accumulator** | ACC | Stores the **results from calculations**, or values after they have been inputted/loaded or calculated in the ALU |
| **Memory Address Register** | MAR | Holds the **address** of a memory location that **is to be read from or written to** |
| **Memory Data Register** | MDR | **Temporarily stores data** that has been **read** from memory or data that needs to be **written** to memory |
| **Current Instruction Register** | CIR | Holds the **current instruction** being executed, divided up into **operand** and **opcode**. The instruction is loaded here before being split and decoded |

### Buses

**Buses** are a set of **parallel wires** which connect **two or more components** inside the CPU. There are three buses in the CPU: the **data bus**, the **control bus**, and the **address bus**. These buses collectively are called the **system bus**.

The **width of the bus** is the **number of parallel wires** the bus has. The width of the bus is **directly proportional** to the **number of bits** that can be transferred **simultaneously** at any given time. Buses are typically 8, 16, 32, or 64 wires wide.

There are also a number of other internal buses within the CPU which transport data between different areas of the processor.

#### Data Bus

The **data bus** is a **bi-directional** bus (bits can be carried in both directions). It is used for transporting **data and instructions** between components.

#### Address Bus

The **address bus** transmits **memory addresses** specifying where data is to be sent to or retrieved from. The width of the address bus is proportional to the **number of addressable memory locations**.

> ⚠ Check: the Save My Exams source describes the address bus as carrying addresses "to/from the CPU and RAM," implying bi-directionality. Standard A-Level treatment is that the address bus is **unidirectional** (CPU sends addresses to memory/devices to specify which location to access).

#### Control Bus

The **control bus** is a **bi-directional** bus used to transmit **control signals** between internal and external components. It coordinates the use of the address and data buses and provides status information between system components.

The control signals include:

| Signal | Purpose |
|---|---|
| **Bus request** | Shows that a device is requesting the use of the data bus |
| **Bus grant** | Shows that the CPU has granted access to the data bus |
| **Memory write** | Data is written into the addressed location using this bus |
| **Memory read** | Data is read from a specific location to be placed onto the data bus |
| **Interrupt request** | Shows that a device is requesting access to the CPU |
| **Clock** | Used to synchronise operations |

| Bus | Direction | Purpose |
|---|---|---|
| Data Bus | Bi-directional | Carries data and instructions between CPU and memory/devices |
| Address Bus | Unidirectional | Carries memory addresses from CPU to memory/devices |
| Control Bus | Bi-directional | Carries control signals to coordinate operations |

### Assembly Language

**Assembly code** uses **mnemonics** to represent instructions (e.g. ADD represents addition). This is a simplified way of representing **machine code**.

Each instruction is divided into two parts in the **Current Instruction Register (CIR)**:

- The **opcode** specifies the **type of instruction** to be executed (e.g. ADD, LDA, STA).
- The **operand** contains the **data** or the **address of the data** upon which the operation is to be performed.

In machine code, the instruction format also includes an **addressing mode** field within the operation code section, which specifies how the operand is used.

*(Beyond source: Assembly language is the language used in the Little Man Computer (LMC) model, covered in more detail in 1.2.4 Types of Programming Languages.)*

---

## 1.1.1 The Fetch-Decode-Execute Cycle

The **fetch-decode-execute cycle (FDE cycle)** is the **sequence of operations** that the CPU goes through repeatedly to process instructions. There are three stages: fetching, decoding, and executing.

### Fetch Phase

1. The **PC** is loaded with the address of the first instruction (e.g. 0).
2. The address from the **PC** is copied to the **MAR**.
3. The address from the **MAR** is sent across the **address bus**, with an instruction to read the data sent across the **control bus**.
4. The instruction held at that address in memory is sent down the **data bus** to the **MDR**.
5. **Simultaneously**, the contents of the **PC** are incremented by 1.
6. The value held in the **MDR** is copied to the **CIR**.

### Decode Phase

1. The contents of the **CIR** are split into **opcode** and **operand**.
2. This is sent to the **CU** to be decoded (interpreted).

### Execute Phase

The decoded instruction is executed. Which registers are used depends on the instruction being executed:

| Instruction | Registers/Components Used | What Happens |
|---|---|---|
| **INP** (Input) | ACC | The inputted value is stored in the ACC |
| **OUT** (Output) | ACC | The value currently in the ACC is outputted |
| **LDA** (Load) | MAR, MDR, ACC | The data is sent across the data bus from RAM (from the address in the MAR) to the MDR, then to the ACC |
| **STA** (Store) | ACC, MDR, MAR | The value from the ACC is sent to the MDR, then across the data bus to RAM at the address held in the MAR |
| **ADD/SUB** | ALU, ACC | Values are passed to the ALU, the operation is carried out, and the result is stored in the ACC |
| **BRA/BRZ/BRP** (Branch) | ALU, PC | The comparison takes place in the ALU. If the branch condition is met, the PC is updated to the branch target address |

### Worked Example: Register Values During STA

Given the LMC instruction `STA count` where the accumulator holds 9 and `count` refers to memory location 16:

- **ACC** holds the value 9
- **MDR** receives the value 9 from the ACC (data can only be sent to memory from the MDR)
- **MAR** holds the value 16 (the memory address where data is being stored)
- The value 9 is then sent from the MDR across the data bus to memory location 16

**Exam tip:** When answering register questions, always state the specific values held in each register based on the question context, not just which registers are involved.

---

## 1.1.1 Factors Affecting CPU Performance

There are three factors that affect CPU performance: **clock speed**, **number of cores**, and the **amount and type of cache memory**.

### Clock Speed

The **clock speed** is determined by the **system clock**, an electronic device which **generates signals**, switching between 0 and 1. All processor activities begin on a **clock pulse**, and each CPU operation starts as the clock changes from 0 to 1. Each one of these transitions is called a **state change**.

A state change can represent one fetch-decode-execute cycle, although some instructions take more than one cycle. **Clock speed** is a measure of **how many state changes the CPU performs per second**. One cycle per second equals 1 Hz. A typical computer may have a clock speed of 2.3 GHz, which is approximately 2.3 billion cycles per second.

A higher clock speed means the CPU can **execute more instructions per second** and therefore carry out tasks more quickly.

### Number of Cores

A **core** is an **independent processor** (processing unit within the CPU) that is able to run its own fetch-execute cycle. A computer with multiple cores can complete **more than one** fetch-execute cycle at any given time. Processors can be **dual core** (2), **quad core** (4), **octa core** (8), or have even more cores.

Each core normally runs at the same speed. Tasks are carried out more quickly using a multicore processor because each core can carry out its own task, known as **parallel processing**. However, a dual core processor is **not twice as fast** as a single core processor because:

- There is time spent **organising tasks between the cores**.
- **Not all programs** are designed to utilise multiple cores efficiently.
- **Some tasks cannot be split** between cores, so additional cores provide no speed benefit for those tasks.

### Cache Memory

**Cache memory** is the **CPU's onboard memory** and is part of **primary storage**. It is used to store **frequently used data and instructions**. Instructions fetched from main memory are copied to the cache, so if required again, they can be accessed more quickly. As cache fills up, unused instructions are replaced.

Cache is **closer to the CPU than RAM** and therefore **faster to retrieve data from**. The more cache available, the more data can be stored close to the CPU, which speeds up performance.

The cache is split into different **levels**, each differing in size and speed:

| Cache Level | Properties |
|---|---|
| **Level 1 (L1)** | Very fast memory cells with a small capacity (2-64 KB). One L1 cache per core |
| **Level 2 (L2)** | Relatively fast memory cells with a medium capacity (256 KB - 2 MB). Shared between cores, slower than L1 |
| **Level 3 (L3)** | Much larger and slower memory cells. Sits on the motherboard (unlike L1 and L2 which are on the CPU die) |

---

## 1.1.1 Pipelining

**Pipelining** is the process of completing the fetch, decode, and execute stages of **three separate instructions simultaneously**, holding appropriate data in a **buffer** in close proximity to the CPU until it is required. While one instruction is being executed, another can be decoded and another fetched.

Pipelining aims to reduce the amount of the CPU which is kept **idle**. It is separated into two types:

- **Instruction pipelining**: separating out the instruction into fetching, decoding, and executing stages that can overlap across different instructions.
- **Arithmetic pipelining**: breaking down the arithmetic operations and overlapping them as they are performed.

### Pipeline Stages

|  | Fetch | Decode | Execute |
|---|---|---|---|
| Step 1 | Instruction A | | |
| Step 2 | Instruction B | Instruction A | |
| Step 3 | Instruction C | Instruction B | Instruction A |
| Step 4 | Instruction D | Instruction C | Instruction B |

### How Pipelining Improves Performance

- **Reduces latency**: the CPU is **not idle** while waiting for the next instruction, which **increases the speed of execution**.
- The next instruction is fetched while the current one is being decoded or executed.
- **All parts of the processor** can be used at any instance in time.

In the case of a **branch instruction**, the pipeline must be **flushed** (cleared), because the pre-fetched and pre-decoded instructions may no longer be the correct ones to execute. This reduces the efficiency gains of pipelining when branches are frequent.

---

## 1.1.1 Computer Architecture

### Von Neumann Architecture

**Von Neumann architecture** includes the basic components of the computer and processor (single control unit, ALU, registers, and memory units) in which a **shared memory** and **shared data bus** is used for **both data and instructions**. Von Neumann architecture is built on the **stored program concept**, meaning instructions and data are stored in the same memory in the same format.

Key features:

- **Single set of buses** (data, address, control) connecting the CPU to memory and I/O.
- **Memory (RAM)** stores both data and instructions for processing, divided into cells each accessible by their address. Memory is a linear/sequential array of bytes.
- Both data and instructions are stored in the **same format**.
- Single Control Unit, ALU, and special registers within the CPU.

### Harvard Architecture

**Harvard architecture** has **physically separate memories** for instructions and data, with **separate buses** for each. It is more commonly used with **embedded processors**.

This separation is useful because:

- Memories can have **different characteristics** (e.g. instructions may be **read-only**, while data may be **read-write**).
- You can **optimise the size** of individual memory cells and their buses depending on needs (e.g. the instruction memory can be designed to be larger so a larger word size can be used for instructions).
- Instructions and data can be **fetched in parallel** because they use separate buses, so one does not interfere with the other.

### Architecture Comparison

| Feature | Von Neumann | Harvard |
|---|---|---|
| Memory organisation | Unified (shared) | Separated |
| Buses | Single set | Separate sets for instructions and data |
| Address space | Shared | Distinct |
| Control units | Single | Separate |
| Typical usage | Most modern general-purpose computers | Specialised embedded systems |

### Advantages Comparison

| Advantages of Von Neumann | Advantages of Harvard |
|---|---|
| **Cheaper to develop** as the control unit is easier to design | **Quicker execution** as data and instructions can be fetched in parallel |
| Programs can be **optimised in size** (data and instructions share the same memory) | Memories can be **different sizes**, which can make more efficient use of space |

### Contemporary Processing

**Contemporary processors** use a **combination of Harvard and Von Neumann architecture**. Von Neumann architecture is used when working with data and instructions in **main memory** (shared memory, shared bus), but Harvard architecture is used to divide the **cache** into separate **instruction cache** and **data cache**, allowing parallel access at the cache level.

Contemporary processors also incorporate several additional performance features:

| Feature | Explanation |
|---|---|
| **Virtual cores / Hyperthreading** | A physical core can act as two virtual cores, allowing more threads to be processed |
| **Multiple cores** | Each core acts as a separate processing unit |
| **Onboard graphics** | Built-in circuitry for graphics processing |
| **Performance boosting mode** | The clock speed can be temporarily increased for a performance boost |
| **Out of Order Execution** | Instructions can be executed before earlier ones if they are ready and do not depend on prior results |
| **Super Scalar** | Multiple instructions can be executed simultaneously within a single core |

**Exam tip:** You will not be asked about specific aspects of contemporary processor architecture beyond those listed above. However, you may be asked to show awareness of how contemporary processors differ from a pure Von Neumann architecture in more open-ended questions.
