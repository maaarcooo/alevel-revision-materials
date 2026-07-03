# 6.1 Thinking Abstractly

## The Nature of Abstraction

**Abstraction** is the process of removing unnecessary details from a problem to arrive at a representation that consists of only the key features needed to implement a solution. It is one of the most important principles in computer science and a critical part of **computational thinking**.

Examples of abstraction include modelling a real-life object, environment, action, sequence of actions, or concept. Implementations include simulators (e.g. car or flight simulators), representations of buildings in programs or games, and maps of bus or train routes.

A specific example is the London Underground map. Travellers do not need to know the geographical layout of the routes, only that boarding at stop A will transport them to stop B. The real geographical map is far more complex, but the abstracted version removes all detail irrelevant to the traveller's goal of navigating between stations.

### Types of Abstraction

**Representational abstraction** involves analysing what is relevant to a given scenario and simplifying a problem based on that analysis. Only the details that matter to the problem at hand are retained.

**Abstraction by generalisation** involves grouping together similarities within a problem to identify what kind of problem it is. This allows problems to be categorised as being of a particular type, so a common solution can be applied to all problems in that category.

**Data abstraction** hides details about how data is being stored. Programmers can use abstract data structures such as stacks and queues without concerning themselves with how these structures are implemented at a lower level. Programmers do not generally need to worry how primitive data types (integers, strings, booleans) are stored and represented in a computer. These implementations are hidden to make creating programs easier.

Data structures such as queues are actually modified arrays, which in turn are collections of variables, which are collections of bytes, which are collections of bits, which are collections of flip-flops. A programmer does not need to worry about any of this underlying implementation, only that they can add to and remove data from a queue.

**Procedural abstraction** means programmers can perform operations (such as pushing and popping items to and from a stack) without any knowledge of the code used to implement that functionality. It models what a subroutine does without considering how it is done. Once a procedure has been coded, it can be reused as a **black-box**. Procedural abstraction is also used in decomposition.

### Levels of Abstraction

Very large, complex problems make use of **multiple levels of abstraction**, where each level performs a different role. The highest levels are closest to the user and are usually responsible for providing an interface for the user to interact with hardware. The lowest levels are responsible for actually performing tasks through the execution of machine code.

## The Need for Abstraction

Abstraction allows non-experts to make use of a range of systems or models by hiding information that is too complex or irrelevant to the system's purpose.

In software development, abstraction enables more efficient design because programmers can focus on elements that need to be built into the software rather than worrying about unnecessary details. This reduces the time needed on the project. Removing wasteful details early on also prevents the program from becoming unnecessarily large.

Abstraction in the context of languages allows developers to focus on solving the problem rather than worrying about the technical details. An analogy: a car driver does not need to know how the engine or mechanics of the car work in order to drive it. Similarly, a programmer does not need to know all of the underlying technical complexity to create complex programs.

### Programming Language Abstraction

Programming languages are themselves an abstraction of other languages, separated into generations.

| Generation | Language Type | Description | Advantages | Disadvantages |
|---|---|---|---|---|
| 1st | Machine code (binary) | Programs written entirely in 0s and 1s | Directly executed by hardware | Time consuming, tedious, and error prone even for simple programs. Requires understanding of which binary codes perform which functions |
| 2nd | Assembly language | Uses mnemonics to represent groups of binary digits (e.g. 1011 might represent ADD) | Easier, quicker, and less error prone than machine code. The underlying 0s and 1s are abstracted away from the developer | Each processor has its own instruction set. Programs must be rewritten to run on a different processor family |
| 3rd | High-level languages (e.g. BASIC, FORTRAN, Python, Java, C) | Syntax parallels natural language. Long instruction sequences are abstracted into shorter instructions (e.g. `A = B * C` replaces many assembly lines) | Considerably easier to learn and use. Developers can ignore how data is stored in memory and how instructions are carried out in the processor. Made coding accessible to non-specialists | Must be translated (compiled/interpreted) before execution |

High-level languages provide an abstraction for the machine code that is actually executed when a program runs. Each generation further abstracts the underlying complexity, allowing developers to build increasingly complex programs more quickly.

### TCP/IP Model as Layered Abstraction

The **TCP/IP model** is an abstraction for how networks function, separated into four layers: **Application**, **Transport**, **Internet**, and **Link**. Each layer deals with a different part of the communication process, and separating these stages makes them simpler to understand.

Each layer does not need to know how other layers work. Outgoing communication is visualised as going down these layers, while incoming information goes up. Compatibility between layers is ensured by agreeing on standards in advance. The TCP/IP model uses a set of **protocols** which means each layer can be dealt with individually, with details about other layers being hidden.

## The Difference Between Abstraction and Reality

Abstraction is a **simplified representation of reality**. The real world is very complex with many variables that factor into problems. The closer an implementation is to reality, the less abstract the solution becomes.

### Computational Representations of Reality

Real-world entities may be represented using computational structures such as tables and databases. Real-world values are often stored as variables.

**Object-oriented programming** uses objects, which are an abstraction for real-world entities. In OOP, abstraction considers the functionality, interface, and properties of entities. **Attributes** are an abstraction for the characteristics of an object, while **methods** are an abstraction for the actions a real-world object can perform.

### Examples: Maps and Navigation

An aerial view of a city with all its roads, junctions, and streets forms the basis of reality when navigating from point A to point B. When travelling by vehicle, greenspace and buildings are unnecessary detail. By removing these, a simplified map retaining only roads and junctions can be created.

This can be abstracted further into a graph: all junctions are represented as **graph nodes** and each road as an **edge** (or **arc**) between junctions. Constraints such as no left turnings can be represented by **directed edges**. The distance between junctions is represented by an appropriate **weight** on each edge.

The final product is a **weighted graph** to which graph theory and algorithms such as **Dijkstra's shortest path** or **A\* search** can be applied. Apps such as Google Maps or Uber use abstracted maps like this to calculate shortest routes. Additional factors such as traffic, roadworks, and weather conditions can also be incorporated for more accurate calculations.

### Examples: Physics and Games

Implementing the trajectory of a projectile (e.g. a ball or dart) or the physics of a snooker ball involves decisions about which real-world factors to include: gravity, air resistance, friction. The more factors included, the less abstract the model becomes.

**Pong** is an example of a highly abstracted game of tennis or badminton. The ball's momentum is constant and there are no extraneous factors such as friction or gravity.

## Devising an Abstract Model

When devising an abstract model for a given scenario, the following questions must be considered:

**What is the specific problem to be solved?** Can the problem be solved computationally? What are the key features of the problem? Can it be broken down into milestones?

**What elements will impact the solution?** Alternatively, if an element were removed, would it impact the solution in any way?

**How will the model be used?** What format does the model need? Consider factors such as convenience, affordability, and ease of access.

**Who will the model be used by?** How many people will use it? What level of expertise do they have in the relevant discipline?

**Which parts of the problem are relevant?** Based on the target audience and purpose of the model, remove sections not relevant to the problem. Remove details that would confuse the audience.

## Key Terms Summary

| Term | Definition |
|---|---|
| **Abstraction** | The process of removing unnecessary details to focus on the key features of a problem |
| **Representational abstraction** | Simplifying a problem by analysing what is relevant and removing what is not |
| **Abstraction by generalisation** | Grouping similarities to categorise a problem as a particular type, enabling a common solution |
| **Data abstraction** | Hiding details of how data is stored, allowing use of abstract data structures without knowing their implementation |
| **Procedural abstraction** | Modelling what a subroutine does without considering how it does it (black-box reuse) |
| **Levels of abstraction** | Layers from user-facing interfaces (highest) to machine code execution (lowest), each performing a different role |
