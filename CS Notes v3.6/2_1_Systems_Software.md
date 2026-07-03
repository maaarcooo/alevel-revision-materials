# 1.2.1 Systems Software

## Operating Systems

An **operating system (OS)** is a collection of programs that work together to provide an **interface between the user and the computer hardware**. It enables the user to communicate with the computer and perform low-level tasks involving the management of computer memory and resources. Operating systems are essential in devices such as laptops, mobile phones and games consoles. Examples of desktop operating systems include Windows and macOS, while mobile operating systems include iOS and Android.

The main functions of an operating system are:

| Function | Description |
|---|---|
| **Memory management** | Allocating and deallocating primary memory using paging, segmentation and virtual memory |
| **Resource management** | Scheduling CPU time fairly between processes |
| **File management** | Handling storage, retrieval and manipulation of files and folders, providing a GUI of the file system |
| **Input/Output management** | Using device drivers to allow the OS to interact with hardware |
| **Interrupt management** | Handling and processing interrupt signals in a timely manner |
| **Utility software** | Providing tools such as disk defragmenter, backup, file compression, disk cleanup, file encryption and formatting |
| **Security** | Providing features such as firewalls, virus scanning, file encryption and password-protected user accounts with restricted permissions |
| **User interface** | Providing interaction visually through a **graphical user interface (GUI)** or text-based through a **command-line interface (CLI)** |
| **Platform for software** | Allowing application software access to system resources (e.g. granting a game access to the GPU and network card) |

The OS sits between the application software layer and the hardware, mediating all communication. When a user opens multiple applications, the OS decides how much memory to allocate to each, when and for how long each gets to use the CPU, and how to handle data being read from or written to storage.

---

## Memory Management

Computer memory must be **shared fairly** between multiple programs and applications. Often, main memory is not large enough to store all programs being used at once. The OS ensures main memory is shared efficiently through **paging**, **segmentation** and **virtual memory**.

Benefits of memory management include enabling **multitasking** (allowing multiple programs to run at once) and maintaining **security** (preventing programs from accessing memory reserved for other programs).

### Paging

**Paging** is a method of dividing primary memory into **equal-sized blocks** called **pages**. Programs are made up of a certain number of equally-sized pages, which can be swapped between main memory and the hard disk as needed. When an application is launched, its data is moved from the hard disk into pages for faster access. As users switch between applications, memory is dynamically allocated: pages are taken away from inactive applications and granted to active ones.

Paging can lead to **internal fragmentation**. Because pages are fixed-size, the last page of a program may not be fully utilised. For example, a 200 KB file divided into four 64 KB pages leaves the fourth page with only 8 KB used and 56 KB wasted. This unused space within a page cannot store unrelated data, so over time pockets of wasted space accumulate across memory.

### Segmentation

**Segmentation** is the splitting of memory into **logical-sized divisions** called **segments**, which **vary in size**. These segments are representative of the **structure and logical flow of the program**, with segments allocated to blocks of code such as conditional statements, loops, or different types of data (e.g. a video editing application may have separate segments for video data, audio data and effects).

Segmentation is more space-efficient because it only allocates the amount of space an application actually needs. However, it can lead to **external fragmentation**: as segments are allocated and deallocated over time, physical gaps appear in memory that reduce the maximum size of new segments that can be created.

### Virtual Memory

**Virtual memory** uses a section of the hard drive to act as an extension of RAM when main memory is insufficient to store all programs being used. Sections of programs that are **not currently in use** are temporarily moved into virtual memory through paging, freeing up RAM for other programs. This creates an **illusion of larger memory** and enables applications to continue multitasking.

However, accessing data in virtual memory is **considerably slower** compared to RAM. Solid-state drives are faster than traditional hard-disk drives, but neither approach the speed of RAM. Over-reliance on virtual memory can lead to performance issues.

*(Beyond source: Virtual memory is not to be confused with virtual storage, which refers to storing files in the cloud.)*

### Disk Thrashing

The key problem with these memory management techniques is **disk thrashing**. This occurs when pages are swapped **too frequently** between the hard disk and main memory. The computer appears to "freeze" because more time is spent transferring pages than actually executing the program. This issue becomes progressively worse as virtual memory fills up.

| Technique | Description | Benefit | Drawback |
|---|---|---|---|
| **Paging** | Divides memory into fixed-sized blocks (pages) | Facilitates efficient memory management and enables virtual memory | Can lead to **internal fragmentation** (wasted space within pages) |
| **Segmentation** | Divides memory into variable-sized segments based on logical parts of a process | Allows intuitive, space-efficient memory access | Can result in **external fragmentation** (gaps between segments) |
| **Virtual memory** | Uses hard drive space as an extension of RAM | Allows more extensive programs to run and facilitates multitasking | Slower to access than physical memory, degrades performance if overused |

---

## Interrupts

**Interrupts** are **signals generated by software or hardware** to indicate to the processor that a process needs attention. Different types of interrupts have different **priorities**, and the OS must account for urgency when allocating processor time. Interrupts are stored in order of their priority within a **priority queue** in a special register known as the **interrupt register**. The OS ensures interrupts are serviced fairly through the **Interrupt Service Routine (ISR)**.

Examples of interrupts include a printer signalling completion of a print job, a peripheral signalling power failure, keyboard input, mouse movements, and division-by-zero errors.

### Types of Interrupts

| Type | Definition | Example |
|---|---|---|
| **Hardware interrupts** | Generated by external devices | Keyboard input, mouse movements, disk I/O requests |
| **Software interrupts** | Triggered by software or the operating system | Application requests to open a file, division by zero errors |
| **Trap interrupts** | Intentionally triggered by a program | Software debugging, handling unexpected error cases |

### Purpose and Role of Interrupts

Interrupts serve three key purposes: **real-time event handling** (responding to hardware errors and signals from input devices), **device communication** (alerts from external devices such as printer jams and network errors), and **multitasking** (suspending processing in one application so the user can switch to another).

### Interrupt Service Routine (ISR)

The processor checks the contents of the interrupt register **at the end of each Fetch-Decode-Execute (FDE) cycle**. The full process is:

1. **Interrupt Request (IRQ)**: An external device or software generates an interrupt signal. The interrupt controller passes this to the interrupt handler for assessment.
2. **Interrupt Acknowledge**: The interrupt handler determines whether the interrupt is of **higher priority** than the process currently being executed. If it is, the **current contents of the special purpose registers** (PC, MAR, MDR, CIR, ALU) in the CPU are temporarily **saved onto a stack**.
3. **ISR Lookup**: The processor fetches the corresponding ISR associated with the interrupt type.
4. **ISR Execution**: The processor loads the appropriate ISR into RAM and executes it. A **flag is set** to signal the ISR has begun.
5. **Interrupt Exit**: Once the interrupt has been serviced, the **flag is reset**. The interrupt queue is checked again for further interrupts of higher priority than the process that was originally being executed. If there are more priority interrupts, the process repeats from step 2. If there are no more (or remaining interrupts are of lower priority than the original process), the **contents of the stack are restored** back into the registers. The **FDE cycle resumes** as before.

### Interrupt Priority and Nesting

**Interrupt prioritisation** allows the processor to acknowledge and switch to resolving a higher-priority interrupt, even while already servicing another interrupt. Lower-priority ISRs may be temporarily suspended until the higher-priority ISR completes. This ability to handle **interrupts within interrupts** is called **nesting**. Proper management of nested interrupts avoids conflicts and ensures system stability.

---

## Scheduling

A core function of the OS is to ensure all sections of programs being run (known as **jobs**) receive a **fair amount of processing time**. This is achieved through **scheduling algorithms**, which decide which tasks to process, for how long, and in what order.

### Pre-emptive vs Non-Pre-emptive

| Category | Description | Examples |
|---|---|---|
| **Pre-emptive** | Jobs are actively made to start and stop by the OS. The CPU is allocated for **time-limited slots**, and currently running processes can be interrupted. | Round Robin, Shortest Remaining Time, Multi-level Feedback Queues |
| **Non-pre-emptive** | Once a job is started, it is left alone until it is completed (or switches to a waiting state). A process cannot be interrupted. | First Come First Served, Shortest Job First |

### Scheduling Algorithms

**Round Robin (RR)**: Each job is given a section of processor time called a **time slice (time quantum)** within which it is allowed to execute. Once every job in the queue has used its first time slice, the OS grants each job another equal slice. This continues until a job completes, at which point it is removed from the queue. If a process has not completed by the end of its time quantum, it is moved to the **back of the queue**. RR ensures every job gets attention, but **longer jobs take much longer** for completion due to their execution being split across multiple cycles. It also **does not account for job priority**.

**First Come First Served (FCFS)**: Jobs are processed in the **chronological order** in which they entered the queue. The process currently being worked on blocks all other processes until it completes. This is **straightforward to implement** but does not allocate processor time based on priority, meaning high-priority tasks must wait their turn. Performance suffers if a long process arrives before shorter ones.

**Multi-level Feedback Queues (MLFQ)**: This uses **multiple queues**, each ordered based on a **different priority**. Shorter and more critical tasks are processed first. All processes initially join the highest priority queue but trickle down to lower priority queues if they exceed the time quantum. This creates a prioritisation system where similar-sized tasks are grouped together. However, it is **difficult to implement** due to the complexity of deciding which job to prioritise and setting correct parameters (number of queues, ageing rules).

**Shortest Job First (SJF)**: The queue is ordered according to the **time required for completion**, with the shortest jobs serviced first. This is most suited to **batch systems** where shorter jobs are given preference to minimise waiting time. However, it requires the processor to **know or calculate how long each job will take**, which is not always possible. There is also a risk of **processor starvation** if short jobs keep being added to the queue, causing longer jobs to be perpetually delayed.

**Shortest Remaining Time (SRT)**: The queue is ordered according to the **time left for completion**, with jobs closest to finishing serviced first. This is a **pre-emptive version of SJF**: a time quantum is set, and if a task does not complete in time, it is re-queued. Before the next cycle, all processes are inspected and reordered by shortest remaining time. Again, there is a risk of **processor starvation** for longer jobs.

**Processor starvation** occurs when a particular process does not receive enough processor time to execute and be completed.

### Comparison of Scheduling Algorithms

| Algorithm | Type | Benefits | Drawbacks |
|---|---|---|---|
| **Round Robin** | Pre-emptive | All processes get a fair share of CPU time. Predictable. Good for time-sharing systems. | Choosing the right time quantum is difficult. High turnaround/waiting time for long processes. Does not consider priority. |
| **FCFS** | Non-pre-emptive | Simple and easy to implement. Fair in arrival order. | Poor performance if a long process arrives before shorter ones. High-priority tasks must wait their turn. |
| **MLFQ** | Pre-emptive | Smaller tasks prioritised. Creates a prioritisation system grouping similar-sized tasks. | More complex than other algorithms. Setting correct parameters is difficult. |
| **SJF** | Non-pre-emptive | Minimises waiting time. Efficient for short processes. | Requires knowing burst time in advance. Risk of processor starvation for longer jobs. |
| **SRT** | Pre-emptive | Ideal for short burst-time jobs. Can be aligned with CPU performance via time quantum. | Requires knowing burst time in advance. High context-switching overhead. Risk of processor starvation. |

The suitability of a scheduling algorithm depends on the specific scenario and system requirements. A drawback in one scenario may not be a drawback in another. For example, **Shortest Remaining Time** is used where completion of shorter tasks before others is preferred, while operating systems such as Windows typically use **multilevel feedback queues**.

---

## Types of Operating System

| Type | Description | Key Features | Examples |
|---|---|---|---|
| **Distributed** | Run across **multiple devices**, allowing the load to be spread across multiple processors when a task is run | Appears as a single unit to the user. Used for efficient task distribution and load balancing. | Hadoop (open-source, processes big data using multiple nodes) |
| **Embedded** | Built to perform a **small range of specific tasks**, catered towards a specific device | Limited functionality. Hard to update. Consumes **significantly less power** than other OS types. Runs a proprietary OS with simple functions. | Consumer appliances (microwaves, washing machines, coffee machines), in-car systems, IoT devices |
| **Multi-tasking** | Enables the user to carry out tasks **seemingly simultaneously** | Uses **time slicing** to switch quickly between programs and applications in memory | Windows, macOS, Linux |
| **Multi-user** | Multiple users make use of **one computer** (typically a supercomputer) | A **scheduling algorithm** must be used to ensure processor time is shared fairly. Risk of processor starvation without suitable scheduling. Provides data security and user privacy features. | Windows, macOS, Linux (supporting multiple user accounts) |
| **Real-time** | Designed to perform a task within a **guaranteed time frame** | Used in **time-critical** computer systems where a response within a certain time period is crucial to safety. Low latency is critical. | Management of control rods at a nuclear power station, self-driving cars, aerospace systems |

---

## BIOS

The **Basic Input Output System (BIOS)** is a piece of **firmware** stored on a small memory chip on the motherboard. It is the **first program that runs** when a computer system is switched on. The **Program Counter (PC)** register points to the location of the BIOS upon each start-up.

The BIOS is responsible for running key tests before the operating system is loaded into memory:

- **POST (Power-On Self-Test)**: A diagnostic testing sequence that ensures all hardware (keyboards, disk drives) are correctly connected and functional. If errors are encountered, the BIOS will either halt the boot process or issue an error message.
- Checking the **CPU clock, memory and processor** are operational.
- Testing for **external memory devices** connected to the computer.

Only after these checks are completed can the OS be loaded into RAM from the hard disk. The program responsible for starting the operating system is called the **bootstrap/bootloader**. If the POST succeeds, the BIOS runs the **bootstrap loading sequence** to load the OS.

---

## Device Drivers

**Device drivers** are computer programs that enable **communication between the operating system and specific hardware devices** such as printers, graphics cards and network cards. When a piece of hardware is used (e.g. a keyboard), the device driver communicates this request to the OS, which then produces the relevant output (e.g. displaying a letter on screen). Device drivers bridge the gap between a major operating system and the embedded system software of hardware devices, making it possible to perform specific operations on the hardware (e.g. sending print commands and managing print jobs).

Device drivers are **specific to the computer's architecture**, so different drivers are needed for different device types such as smartphones, games consoles and desktop PCs. They are also **specific to the operating system** installed on the device. Most hardware manufacturers write their own device driver software, meaning a single OS may have several drivers installed for devices of the same type (e.g. multiple printer drivers).

*(Beyond source: Device drivers are an example of abstraction, as the user can interact with hardware without knowing the details of how communication works at a low level.)*

---

## Virtual Machines

A **virtual machine (VM)** is a **software-driven computer** that runs within a physical machine. It is a software implementation of a computer system that **mimics a complete computer system**, including virtual CPU, memory, storage and network interface. A physical machine can run multiple VMs using **hypervisor software**. Each VM behaves as a separate system with its own operating system and applications, independent of the host OS.

A VM provides an environment with a translator for **intermediate code** to run.

### Intermediate Code

**Intermediate code** is code that is halfway between machine code and object code. It is **independent of the processor architecture** so can be used across different machines and operating systems. Some languages (e.g. Java) compile to intermediate code (**bytecode**) instead of machine code. This bytecode is executed by a virtual machine (such as the **Java Virtual Machine**), allowing the same program to run on multiple platforms.

> ⚠ Check: the PMT source states intermediate code is "halfway between machine code and object code." Standard A-Level treatment describes intermediate code as halfway between **source code** and machine code, since object code and machine code refer to the same (or very similar) output of compilation.

### Uses of Virtual Machines

**Development and testing**: VMs are commonly used to create isolated development environments for programmers to test programs on different operating systems, saving both the time and money of purchasing multiple devices. VMs provide a **clean-slate system** with no other applications running, and VM management software can create VMs that emulate **older hardware**, allowing developers to build software compatible with a wider range of devices. Developers can test against various operating systems (macOS, Linux, Windows) for greater compatibility.

**Cross-platform and forwards compatibility**: Not all software runs on all operating systems. A Windows user could run a VM of macOS to access Mac-only software. Software often needs updating to work on the latest OS versions, so a user may need to run a VM of a **previous OS release** to use applications that have not received a forwards-compatibility update.

**Protection from malware**: Malware will affect the virtual machine rather than the host device, providing an isolated environment for safely working with potentially harmful code.

**Running incompatible software**: Programs specific to different operating systems or different versions of an OS can be run within a VM. A common example is games consoles being emulated on PCs via a virtual machine.

### Benefits and Drawbacks

| Benefits | Drawbacks |
|---|---|
| Allows software to run on different operating systems (cross-platform) | Uses system resources (CPU, RAM, storage) from the host machine |
| Supports running legacy applications on older operating systems | Performance is usually **slower** than running software directly on physical hardware |
| Provides isolated test environments for safe software testing | Can be complex to set up and manage |
| Enables execution of intermediate code (e.g. Java bytecode via JVM) | May require additional licences or activation payments for virtualised OSs |
| Multiple VMs can run on a single physical machine, improving hardware usage | Resource limits can cause crashes or lag if poorly configured |
| Easy to reset or rollback using snapshots | Not all hardware features can be virtualised accurately |
