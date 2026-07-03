# 6.5 Thinking Concurrently

## Concurrent Thinking

**Concurrent thinking** is the problem-solving mindset that allows you to identify parts of a problem where concurrency can be applied. It is built on the idea of **concurrent processing** but applies to human reasoning rather than computer execution. The goal is to spot patterns and related subtasks within a problem that can be worked on within the same time frame, rather than completing one task entirely before starting the next.

**Example -- recording car data.** You are asked to (1) record the number plate and (2) record the colour of every car that passes. A sequential approach would record all number plates first, then go back and record all colours. The concurrent thinking approach records both the number plate and the colour of each car before moving to the next. The two subtasks are related (they concern the same car), so handling them together is more efficient.

To determine which parts of a problem can be tackled at the same time, you must first assess which parts are **related**. Related sections of a problem can often be solved simultaneously and therefore handled concurrently. Parts that are unrelated or independent are also candidates, since they have no dependencies preventing them from progressing in parallel.

### Dependencies

**Dependencies** are tasks that rely on other tasks in order to either start or complete. When dependencies exist between subtasks, those subtasks cannot be executed concurrently -- they must follow the required order.

**Example 1 -- house construction.** A roofer cannot put a roof on a house if the walls are not fully built, and the walls cannot be built unless the foundation is in place. Each stage depends on the previous one.

**Example 2 -- tax calculation.** A person's taxes cannot be calculated until all of their income has been input and all deductibles have been accounted for. The final calculation depends on the completeness of earlier input.

When dependencies do not exist between data sets or subtasks, they can be processed concurrently or in parallel. For example, when running a **batch program** on a set of data (such as climate data analysis or departmental finances), if the data sets do not relate to, rely on, or interact with each other, they can be run in **parallel on multiple cores**, increasing time efficiency and maximising resource usage. If multiple different batch programs need to be run, they can be **interchanged and pipelined** using concurrent processing on the same processor, allowing multiple programs to make progress in a shorter time frame.

---

## Concurrent Processing vs Parallel Processing

### Concurrent Processing

**Concurrent processing** allows multiple processes or tasks to run on a **single processor** by giving each process a **fraction of time** (a **time slice**) and control over the processor before swapping to another process. The tasks appear to execute simultaneously, but in reality they are executed **sequentially** -- the rapid switching between tasks creates the illusion of simultaneous execution because human perception cannot detect the microsecond-level swaps.

**Example -- virus scan and game.** Without time slicing, a user who wants to play a game while a virus scan is running must wait until the scan completes. With concurrent processing, the virus scan is allocated a few microseconds of execution time, then the game is allocated a few microseconds, and the processor alternates between them. The effect looks simultaneous to the user.

### Parallel Processing

**Parallel processing** is where **multiple processors** (or multiple cores) are used to complete more than one task **at the same time**. Unlike concurrent processing, tasks genuinely execute simultaneously rather than being interleaved.

Modern programs such as photo and video editing software and AAA games make use of parallel computing to complete multiple tasks at the same time, improving running speed and maximising resource usage and efficiency. **GPUs** (graphical processing units) exploit parallel processing to render 3D objects quickly by splitting the computations of a scene between multiple cores.

### Comparison

| | Concurrent Processing | Parallel Processing |
|---|---|---|
| **Processors** | Single processor | Multiple processors / cores |
| **Execution** | Tasks interleaved via time slicing | Tasks run at the same time |
| **Simultaneity** | Apparent (illusion) | Genuine |
| **Mechanism** | Scheduler allocates time slices and swaps between processes | Each process runs on its own core |
| **Use case** | Multiple programs sharing one CPU (e.g. OS multitasking) | Computationally intensive tasks split across cores (e.g. rendering, data analysis) |

---

## Benefits and Drawbacks of Concurrent Processing

| Benefits | Drawbacks |
|---|---|
| Increased program **throughput** -- the number of tasks completed in a given time frame is increased (e.g. ten programs could each be half-finished versus only two running to completion sequentially) | With **large numbers of users or processes** involving high quantities of computation, individual processes take longer to complete because each is allocated only a limited time slice |
| **Less time wasted waiting** for user input or I/O -- the processor can swap to another task and wait for an **operating system interrupt** before swapping back to the waiting task | There is an **overhead** in coordinating and switching between processes (**context switching**), which reduces overall program throughput |
| | Not all tasks are suited to being broken up and performed concurrently -- some tasks have sequential dependencies that prevent concurrent execution |

*(Beyond source: the overhead referred to here is called **context switching** -- saving and restoring the state (registers, program counter, etc.) of each process when the processor swaps between them.)*

---

## Benefits and Drawbacks of Parallel Processing

| Benefits | Drawbacks |
|---|---|
| Speeds up **repetitive calculations on large data sets** (e.g. image or video editing) by splitting processes over several processors | Different processors running programs simultaneously may need to **communicate**, leading to overhead and delays |
| **GPUs** can render 3D objects quickly by splitting scene computations between multiple cores | Some tasks may run faster or be **optimised for a single processor** rather than multiple processors |
| Multiple different programs or browser web pages can run on different processors at the same time | |

---

## Worked Example -- Flight Simulator (4 marks)

**Question:** A flight simulator lets a user control a simulated aeroplane in an environment with different weather conditions and additional planes. Explain what is meant by "concurrent processing" and describe one example of how the simulator could use it.

**Model answer structure:**

1. **Definition [1 mark]:** Concurrent processing is where multiple processes are allocated time slices of processor time and are pipelined to allow multiple processes to make progress in the same time frame.
2. **State the example [1 mark]:** The user's plane moving independently of other planes or weather conditions.
3. **Explain how it acts concurrently [1 mark]:** Individual planes or weather systems do not always interact with each other, allowing them to operate as separate processes that can be interleaved.
4. **Explain why concurrency is needed [1 mark]:** This allows multiple objects and events to occur in the program "at the same time" and react to different events as they arise.

**Examiner tip:** When answering concurrency questions, always (1) state your example, (2) explain how it acts concurrently, and (3) explain why it is necessary that it is concurrent.

**Examiner tip:** Some operating system scheduling algorithms can **prioritise** certain concurrent processes over others, meaning larger or higher-priority processes could finish sooner.

---

## Key Terms Summary

| Term | Definition |
|---|---|
| **Concurrent thinking** | The problem-solving mindset of identifying parts of a problem that can be tackled within the same time frame |
| **Concurrent processing** | Multiple processes running on a single processor by allocating each a time slice, appearing simultaneous but executing sequentially |
| **Parallel processing** | Multiple processes running at the same time on multiple processors or cores |
| **Time slice** | A small fraction of processor time allocated to a process before the scheduler swaps to the next |
| **Dependencies** | Tasks that rely on other tasks to start or complete, preventing concurrent execution |
| **Throughput** | The number of tasks completed in a given time frame |
| **Context switching** | *(Beyond source)* The overhead of saving and restoring process state when swapping between tasks |
