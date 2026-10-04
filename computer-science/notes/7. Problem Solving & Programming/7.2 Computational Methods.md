# 2.2.2 Computational Methods

## Features That Make a Problem Solvable by Computational Methods

A **computable** problem is one that can be solved using an algorithm within a **finite, realistic amount of time**. Problems suitable for computational solutions typically involve clearly defined **inputs**, **outputs**, and **calculations** or logical operations.

Not all problems are computable. Ethical, social, or cultural problems (e.g. determining whether a loan should be approved, improving employee morale) may involve human judgement that algorithms could oversimplify or misinterpret. The first step in problem solving is identifying whether or not a computational approach is appropriate.

Even when a problem is theoretically computable, it may be **impractical** to solve due to the resources or time required. Practical constraints include **processing power**, **speed**, and **memory**. For example, calculating Pi to a billion decimal places is computable in theory but demands impractical computational resources on current hardware. Similarly, running complex machine learning models on a regular laptop may be constrained by limited processing power and memory.

**Advances in technology** have expanded the range of problems that can be solved computationally. Genome sequencing, for instance, has become faster and more affordable due to improvements in hardware and algorithms.

| Problem | Computational? | Justification |
|---|---|---|
| Inventory not updated in real time | Yes | Real-time syncing achievable through algorithms |
| High employee turnover | No | Root causes are cultural/managerial, not algorithmic |
| Incorrectly sorted delivery products | Yes | Sorting algorithms can optimise placement |
| Long customer service wait times | Yes | Queue algorithms can improve response times |
| Poor delivery route optimisation | Yes | Routing algorithms exist for this specific problem |
| Inadequate marketing strategies | No | Requires creative, human-centric solutions |

---

## Problem Recognition

**Problem recognition** is determining that a problem exists and clearly identifying what it is. Stakeholders state their requirements for the finished product, and this information is used to clearly define the problem and the **system requirements**.

Requirements may be defined by:

- Analysing **strengths and weaknesses** of the current approach to solving the problem
- Considering **types of data** involved, including inputs, outputs, stored data, and data volumes

Not all identified problems should or can be solved with software. For example, a slow online checkout process can be addressed computationally (rewriting code to reduce steps, reorganising page layout). In contrast, low employee morale caused by unrealistic targets and lack of support is a cultural and psychological issue requiring human-centric solutions such as revised management practices, team-building, and counselling, even if software tools may assist with recording and analysing data.

**Exam-style example:** A GP surgery's online booking system has slow response times during peak hours (08:00-09:00), causing abandoned bookings. The big problem (slow response time) can be decomposed into sub-problems: peak-hour bottlenecks indicating scalability issues, delayed confirmation screens pointing to inefficient processing, poor user experience damaging trust, and abandoned bookings preventing patients from seeking care. All of these sub-problems are computational and can be addressed through software solutions.

---

## Problem Decomposition

**Problem decomposition** is the process of continually breaking down a large problem into smaller sub-problems until each can be represented as a **self-contained subroutine**. This reduces the complexity of the problem by splitting it into smaller, more understandable sections.

Programmers use decomposition to:

- Break problems into manageable parts
- Identify steps, parts, or processes involved
- Identify **reusable components** that can be implemented using **pre-coded modules or libraries**, saving coding and testing time
- Split tasks between programmers or teams

Before decomposing, it is often useful to apply **abstraction** to the problem first, removing non-essential elements so that programmers can focus on critical aspects. For example, when addressing a slow booking system, a programmer would ignore cosmetic elements like colour schemes and focus on performance metrics such as server response time and database query efficiency.

**Benefits of decomposition:**

- **Easier project management:** Different teams can be assigned sections according to their specialisms, with modules individually designed, developed, and tested before being combined.
- **Parallel development:** Multiple parts of the project can be developed simultaneously, enabling faster delivery.
- **Simpler debugging:** Errors are easier to identify, locate, and fix within individual modules. Without decomposition, testing can only occur once the entire application is complete, making it hard to pinpoint errors.

*(Beyond source: Top-down design, covered in 2.2.1, is a direct example of problem decomposition applied as a design methodology.)*

---

## Use of Divide and Conquer

**Divide and conquer** is a problem-solving strategy that breaks a problem down through three stages:

1. **Divide** - The problem is halved (or reduced) in size with every iteration.
2. **Conquer** - Each sub-problem is solved independently, often **recursively**.
3. **Merge** (also called **Combine**) - The solutions to the sub-problems are recombined to form the final solution.

### Binary Search Example

Binary search is a classic application of divide and conquer. The middle value of a sorted list is compared to the search value. If the search value is smaller, the upper half is discarded and the lower half is recursively searched. If the search value is larger, the lower half is discarded and the upper half is searched. This continues until the value is found or the list is reduced to one element (meaning the value does not exist in the list).

Other applications include **quick sort** and **merge sort**.

### Decrease and Conquer

The principle of divide and conquer also applies to problems where the size is reduced by **less than half** in every iteration. This variant is sometimes called **Decrease and Conquer**.

### Time Complexity

Because the problem size is halved with each iteration, the number of recursive calls is $\log_2(n)$. Algorithms using divide and conquer therefore have a time complexity of **$O(\log n)$** for the search/division step.

### Task Parallelism

**Task parallelism** occurs when several tasks or sub-tasks are carried out **concurrently** to speed up overall completion time. For example, on a factory assembly line, different components can be assembled simultaneously by different teams. In software, once a problem is divided into independent sub-problems, separate teams can work on each concurrently.

### Benefits and Drawbacks

| Benefits | Drawbacks |
|---|---|
| Greatly simplifies complex problems by halving the problem size each iteration | Not all problems can be broken down and solved independently |
| Makes programs more time-efficient | Can cause **stack overflow** if recursion is used, crashing the program |
| Sub-problems can make effective use of **cache memory** | Large recursive programs are very difficult to trace |

---

## Use of Abstraction

**Abstraction** is the removal of unnecessary detail to simplify a problem and allow focus on only the essential components.

### Representational Abstraction

**Representational abstraction** involves removing excessive details to simplify a problem. Problems may be reduced until they resemble previously solved problems, allowing **pre-programmed modules and libraries** to be used rather than coding from scratch. This lets programmers focus on the **core aspects** of the solution.

### Levels of Abstraction

Using **levels of abstraction** allows a large, complex project to be split into simpler component parts. Individual components can be handled by different teams, with details about other layers **hidden**. This makes projects more manageable.

### Abstraction by Generalisation

**Abstraction by generalisation** groups together different sections of a problem with **similar underlying functionality**. This allows segments to be coded together and **reused**, saving time.

### Abstract Thinking

Once a problem has been abstracted into levels, **abstract thinking** is required to represent real-world entities with computational elements such as **tables** and **variables**.

### Real-World Examples of Abstraction

- **Computer games:** Users see a realistic environment and responses to their actions, but do not need to know the complex algorithms controlling NPCs. Abstraction keeps the game fun while hiding implementation complexity.
- **Cooking with a recipe:** A recipe that instructs a user to "brown" an ingredient applies abstraction. The user does not need to understand the chemistry of the Maillard reaction, only the desired output.
- **Driving a car:** The driver uses a key/button to start the engine and pedals to accelerate/stop, without needing to understand the mechanics of internal combustion or electric motors.

---

## Problem Solving Strategies

### Backtracking

**Backtracking** is an algorithmic problem-solving technique, often implemented **recursively**, used when there is insufficient information to find a solution directly or when there are many possible solution paths.

It works by **methodically visiting each path** and **building a solution incrementally**. If a path is found to be invalid at any point, the algorithm **backtracks to the previous stage** and explores an alternate path. This continues until a valid solution is found or all paths have been exhausted.

**Depth-first graph traversals** are an example of backtracking.

**Maze analogy:** A maze is solved by visiting each path. If a path leads to a dead end, the solver returns to the most recent junction where there are unexplored paths and tries a different route.

Backtracking is also useful when **traversing data structures** such as trees or graphs, which have multiple paths that can lead to the desired solution. In a binary search tree, backtracking helps return from leaf nodes (dead ends) so that other subtrees can be explored.

Backtracking is ideal for solving **logic problems** but is **not ideal for strategic problems**.

| Benefits | Drawbacks |
|---|---|
| Guaranteed to find a solution if one exists | Not ideal for strategic problems |
| Easy to implement and use | Can have high time complexity depending on the problem |
| Can be applied to a variety of logic problems | Not always the most efficient method when many solutions exist |
| Comprehensively explores all possible paths | Can consume a lot of memory |
| | May not find the **best** solution, only **a** solution |
| | Often requires a complete search of the entire solution space |

---

### Data Mining

**Data mining** is the process of analysing large sets of data (**big data**), typically collected from a **variety of sources**, to identify **patterns**, **outliers**, or **correlations** that are not immediately obvious to humans. It uses **algorithms and statistical methods** to extract valuable insights.

Insights from data mining can be used to make **predictions about the future based on previous trends**, making it a useful tool for **business and marketing decisions**. For example, data mining can reveal which products are bought at certain times of the year, helping shops prepare enough stock in advance.

Data mining has also been used to reveal insights about people's **shopping habits and preferences** based on their personal information, informing marketing techniques.

**Industry examples:**

- **Retail:** Algorithms analyse purchase history and browsing behaviour for customised product suggestions (e.g. Amazon recommendations).
- **Healthcare:** Healthcare records are analysed to predict disease outbreaks or patient admissions (e.g. anticipating flu cases for resource allocation).
- **Finance:** Machine learning models trained on historical data identify suspicious transactions in real-time (e.g. credit card fraud detection).
- **Automotive:** Vehicle sensor data predicts when parts are likely to fail, enabling proactive maintenance (e.g. Tesla battery monitoring).
- **Entertainment:** Viewer preferences and behaviour drive content recommendations (e.g. Netflix targeting shows to specific audiences).

**Legal considerations:** As data mining often involves handling **personal data**, it must comply with the **General Data Protection Regulation (GDPR)**.

**Complexities:** Data mining requires knowledge of complex algorithms for data sorting, pattern recognition, and anomaly detection. It demands significant maintenance and expertise, and specialist data engineers and data scientists are in short supply.

| Benefits | Drawbacks |
|---|---|
| Identifies patterns and trends not immediately obvious to humans | Requires very powerful computers with significant processing power |
| Helps organisations make better future predictions | Inaccurate data produces inaccurate results |
| Ensures demand is met during busy periods, staying ahead of competition | May spot patterns/trends but cannot explain the reasons behind them |

---

### Heuristics

**Heuristics** are a **non-optimal, "rule-of-thumb"** approach to problem-solving used to find an **approximate solution** when the standard (optimal) solution is unreasonably **time-consuming or resource-intensive** to find. The solution found is **not perfectly accurate or complete**, but the focus is on finding a quick solution that is **"good enough"**.

Heuristics are used for **intractable problems** (problems whose optimal solutions take an unreasonably long time to find), such as the **Travelling Salesman Problem** and the **A\* algorithm** for pathfinding and graph traversal. They are also used in **machine learning** and **language recognition**.

**Trade-off between speed and accuracy:** Heuristic methods find solutions more quickly than exhaustive searching but do not guarantee the quickest or most optimal result. A heuristic algorithm can get stuck in a **local optimum**, where a solution appears to be the best in its neighbourhood but is not the globally best solution.

| Benefits | Drawbacks |
|---|---|
| Usually finds a solution close to the best available | Does not guarantee finding the optimal solution |
| Saves time by not investigating every possibility | Requires careful consideration of the accuracy-time trade-off |
| Practical and easily implemented | Incorrect heuristic values can lead to inaccurate solutions |

---

### Performance Modelling

**Performance modelling** uses **mathematical methods** to simulate and test the behaviour of a system before it is used in the real world, eliminating the need for true performance testing. It provides a **cheaper**, **less time-consuming**, and **safer** method of testing applications.

This is particularly useful for **safety-critical computer systems** (such as those used on aircraft) where it is not safe to do a real trial run before implementation. Results help companies judge the **capabilities of a system**, how it will cope in different environments, and whether it is **safe to implement**.

In software development, performance modelling can be integrated into:

- The **design phase** to make architectural decisions
- The **testing phase** to simulate real-world scenarios and measure performance

It uses metrics such as **response time** and **throughput** to identify potential **bottlenecks**, allowing developers to address issues before they affect end users.

**Application examples:**

- **Database optimisation:** Simulating different architectures and query strategies to find the most efficient setup, including selecting indexing strategies and estimating response times under varying loads.
- **Caching mechanisms:** Modelling how different caching strategies perform to determine optimal cache sizes and assess hit/miss ratios and latency improvements.
- **Energy efficiency:** Estimating power consumption under different usage patterns for mobile or embedded, battery-powered devices.

| Benefits | Drawbacks |
|---|---|
| Stress testing ensures a system can cope with large data volumes or many users | Outcomes are only as useful as the accuracy of the input data |
| Can predict problems and act on them before they occur in the real world | Incorrect model rules produce incorrect results |

---

### Pipelining

**Pipelining** is the process of carrying out **multiple instructions or tasks concurrently**, improving overall efficiency and performance. The output of one process becomes the **input of another**, resembling a **production line**.

To utilise pipelining:

1. **Break down the task** into individual sub-tasks.
2. **Arrange in sequential order** so that the output of one task becomes the input for the next.
3. **Allow multiple tasks to operate concurrently** rather than waiting for each to complete before starting the next.

*(Beyond source: Pipelining is also used in RISC processors where different stages of the Fetch-Decode-Execute cycle are performed simultaneously, as covered in 1.1.1.)*

**Pipelining in programming:** In languages such as Python and Java, pipelining involves chaining multiple instructions together. For example, a list of numbers can be squared in one step, then filtered for even values in the next, with each operation feeding into the next.

In Unix/Linux, the pipe symbol `|` is used to chain commands. For example:

```
grep "hello" docs | grep "world"
```

The first command searches for lines containing "hello" in a file called "docs". The pipe connects its output to the input of the second command, which filters for lines also containing "world". Data flows left to right through the pipeline.

**Exam-style example (car manufacturing):** In manufacturing, tasks like engine development, chassis development, and electronics planning can proceed concurrently once designs are drawn. However, some tasks must be sequential: painting can only occur after the body is welded, and final inspection must follow all other tasks.

---

### Visualisation

**Visualisation** presents data or concepts in a **graphical or visual form** that is easier for humans to understand. It makes it possible to **identify trends that were not otherwise obvious**, particularly in statistical data. Data may be represented as **graphs**, **trees**, **charts**, and **tables**.

Visualisation is used by businesses to spot patterns that inform business decisions.

**Example uses:**

- **Flowcharts:** Represent workflows or processes, mapping out each step to make it easier to predict outcomes. For example, visualising a complex e-commerce checkout process to ensure users cannot purchase out-of-stock items.
- **UML diagrams:** Provide a standard way to visualise a system's architecture, showing how classes and objects interact.
- **Wireframes:** Low-fidelity design plans representing the skeletal framework of a program or website, aiding layout planning and user experience design.

| Benefits | Drawbacks |
|---|---|
| Simplifies complex concepts for human understanding | Cannot explain **why** something is the way it is |
| Makes it easier to spot new trends and patterns | Different people may interpret visualisations differently |
| Helps programmers understand problems in a current system | The presentation format can influence understanding |

---

## Key Terms Summary

| Term | Definition |
|---|---|
| **Computable** | A problem that can be solved using an algorithm within a finite, realistic amount of time |
| **Problem recognition** | Determining that a problem exists and clearly identifying what it is |
| **Problem decomposition** | Continually breaking down a problem into smaller sub-problems until each can be represented as a self-contained subroutine |
| **Divide and conquer** | A strategy that divides a problem in half, solves sub-problems recursively, and merges/combines the solutions |
| **Decrease and conquer** | A variant of divide and conquer where the problem is reduced by less than half each iteration |
| **Representational abstraction** | Removing excessive details to simplify a problem |
| **Abstraction by generalisation** | Grouping sections of a problem with similar underlying functionality to enable code reuse |
| **Backtracking** | An algorithmic technique that builds solutions incrementally, abandoning invalid paths and returning to the last decision point |
| **Data mining** | Analysing large data sets to identify patterns, outliers, or correlations not immediately obvious |
| **Big data** | Very large data sets, typically collected from a variety of sources |
| **Heuristics** | A non-optimal, rule-of-thumb approach that finds an approximate "good enough" solution quickly |
| **Intractable problem** | A problem whose optimal solution takes an unreasonably long time to find |
| **Local optimum** | A solution that appears best in its neighbourhood but is not the globally optimal solution |
| **Performance modelling** | Using mathematical methods to simulate and test system behaviour before real-world deployment |
| **Pipelining** | Carrying out multiple tasks concurrently, where the output of one process becomes the input of the next |
| **Visualisation** | Presenting data or concepts in graphical form to aid human understanding and pattern identification |
| **Task parallelism** | Carrying out several tasks or sub-tasks concurrently to speed up overall completion time |
