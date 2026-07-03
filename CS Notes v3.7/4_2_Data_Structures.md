# 1.4.2 Data Structures

## Arrays

An **array** is an ordered, static set of elements of a single data type. Arrays have a fixed size that cannot change at runtime. A **1D array** is a linear array. Unless stated otherwise, arrays are **zero-indexed** (the first element is at position 0).

```
oneDimensionalArray = [1, 23, 12, 14, 16, 29, 12]
print(oneDimensionalArray[3])
>> 14
```

Elements are accessed by index: `arrayName[index]`. Elements can be modified by assigning a new value: `arrayName[index] = newValue`. The length can be found with `len(arrayName)`.

### 2D Arrays

A **2D array** can be visualised as a table. When navigating a 2D array, you go **down the rows** first, then **across the columns** to find a position. This is the reverse of finding a set of coordinates.

```
twoDimensionalArray = [[23, 28, 90, 38, 88, 23, 47],
                       [ 1, 23, 12, 14, 16, 29, 12]]
print(twoDimensionalArray[1][3])   // row 1, column 3
>> 14
```

### 3D Arrays

A **3D array** can be visualised as a multi-page spreadsheet and thought of as multiple 2D arrays. Selecting an element uses the syntax `threeDimensionalArray[z][y][x]`, where **z** is the array number, **y** is the row number, and **x** is the column number.

```
threeDimensionalArray = [[[12,8],[9,6,19]],[[241,89,4,1],[19,2]]]
print(threeDimensionalArray[0][1][2])
>> 19
```

---

## Records

A **record** is a row in a file and is made up of **fields**. Records are used in databases. A record is declared by defining a named data type containing typed fields:

```
fighterDataType = record
    integer   ID
    string    FirstName
    string    Surname
end record
```

To create and access a record, first declare a variable of the record type, then use **dot notation** to access individual fields:

```
fighter : fighterDataType
fighter.FirstName       // accesses the FirstName field
```

In Python, records are typically implemented using a class with an `__init__` method that initialises the fields. In Java, a class with private fields, a constructor, and getter/setter methods is used.

---

## Lists

A **list** is a data structure consisting of a number of ordered items where items can occur more than once. Lists are similar to 1D arrays and elements are accessed in the same way. The key differences from arrays are:

- List values are stored **non-contiguously** (they do not have to be stored next to each other in memory, unlike arrays).
- Lists can contain elements of **more than one data type**, unlike arrays.
- Lists are **dynamic** (they can grow and shrink in size).

### List Operations

| Operation | Example | Description |
|---|---|---|
| `isEmpty()` | `List.isEmpty()` → `False` | Checks if the list is empty |
| `append(value)` | `List.append(15)` | Adds a new value to the end of the list |
| `remove(value)` | `List.remove(23)` | Removes the value the first time it appears in the list |
| `search(value)` | `List.search(38)` → `False` | Searches for a value in the list |
| `length()` | `List.length()` → `7` | Returns the length of the list |
| `index(value)` | `List.index(23)` → `0` | Returns the position of the item |
| `insert(position, value)` | `List.insert(4, 25)` | Inserts a value at a given position |
| `pop()` | `List.pop()` → `12` | Returns and removes the last value in the list |
| `pop(position)` | `List.pop(3)` | Returns and removes the value at the given position |

---

## Tuples

A **tuple** is an ordered set of values of any type. A tuple is **immutable**: elements cannot be added, removed, or changed once it has been created. Tuples are initialised using **regular brackets** (parentheses) instead of square brackets.

```
tupleExample = ("Value1", 2, "Value3")
print(tupleExample[0])
>> Value1

tupleExample[0] = "ChangedValue"
>> Syntax Error
```

Elements are accessed by index in the same way as arrays, but any attempt to modify a value produces an error.

---

## When to Use Each Structure

| Structure | When to Use | Example Use Cases |
|---|---|---|
| **Array** | A fixed-size collection where random access by index is needed. Efficient for index access but less efficient for dynamic resizing or mid-collection insertion/removal. | Student grades, lookup tables, pixel grids |
| **Record** | A group of related data forming a single entity with different attributes/fields. | Customer record, student record, product record |
| **List** | A dynamic collection that may change in size. Provides flexibility for adding, removing, and modifying elements. | Shopping list, to-do list, contact list |
| **Tuple** | A fixed collection of values that must not change after creation. | Storing coordinates, returning multiple values from a function |

---

## Linked Lists

A **linked list** is a **dynamic data structure** used to hold an ordered sequence. The items do not have to be in contiguous memory locations. Each item is called a **node** and contains a **data field** alongside a **pointer field** (also called a link).

### Structure

| Index | Data | Pointer |
|---|---|---|
| 0 | 'Apple' | 2 |
| 1 | 'Pineapple' | 0 |
| 2 | 'Melon' | - |
| 3 | | |

**Start = 1, NextFree = 3**

The **data field** holds the actual value. The **pointer field** holds the address of the next item in the sequence. Two additional pointers are maintained: **Start** (the index of the first logical item) and **NextFree** (the index of the next available space).

### Traversing a Linked List

1. Check if the linked list is empty.
2. Begin at the index given by the Start pointer.
3. Output the data at the current node.
4. Follow the pointer to the next node.
5. Repeat until the pointer field is empty/null, signalling the end of the list.

Traversing the example above produces: `'Pineapple', 'Apple', 'Melon'`

### Adding a Node

To add 'Orange' after 'Pineapple':

1. Check there is free memory to insert data.
2. Place the new value at the NextFree position and increment NextFree.
3. Update the pointer of 'Pineapple' to point to the new node ('Orange') at position 3.
4. Set the pointer of 'Orange' to point to 'Apple' at position 0 (the node 'Pineapple' previously pointed to).
5. Traversal now produces: `'Pineapple', 'Orange', 'Apple', 'Melon'`

### Removing a Node

To remove 'Apple' from the original list:

1. Update the pointer of 'Pineapple' to point to 'Melon' at index 2 (bypassing 'Apple').
2. Traversal now produces: `'Pineapple', 'Melon'`

The node is **not truly removed** from memory; it is only ignored because no pointer references it. This wastes memory.

### Advantages and Disadvantages

- Values can easily be added or removed by editing pointers (no shifting of elements).
- Storing pointers requires **more memory** compared to an array.
- Items can **only be traversed sequentially** by following pointers; an item **cannot be directly accessed** by index (**no random access**), unlike arrays.

**Random access** is the ability to access a specific element directly given its index. This is possible in an array but not in a linked list.

---

## Graphs

A **graph** is a set of **vertices** (or **nodes**) connected by **edges** (or **arcs**). Graphs fall into three categories:

| Type | Description |
|---|---|
| **Directed graph** | Edges can only be traversed in one direction |
| **Undirected graph** | Edges can be traversed in both directions |
| **Weighted graph** | A cost/value is attached to each edge |

A graph can be both directed and weighted simultaneously.

### Adjacency Matrix

A 2D array where rows and columns represent nodes. For **unweighted** graphs, a 1 indicates an edge exists and a 0 indicates no edge. For **weighted** graphs, the weight value is stored in place of 1, and infinity (∞) represents no connection. An **undirected** graph produces a **symmetric** matrix. A **directed** graph is not necessarily symmetric because the direction of the edge determines which cell is filled.

Example (undirected, weighted):

|   | A  | B  | C  | D  | E  |
|---|----|----|----|----|---- |
| **A** | -  | 4  | 18 | 12 | -  |
| **B** | 4  | -  | 5  | -  | 8  |
| **C** | 18 | 5  | -  | 5  | -  |
| **D** | 12 | -  | -  | -  | 3  |
| **E** | -  | 8  | -  | 3  | -  |

### Adjacency List

Each node stores a list of its neighbours (and weights, if applicable).

```
A → {B:4, C:18, D:12}
B → {A:4, C:5, E:8}
C → {A:18, B:5, D:5}
D → {A:12, E:3}
E → {B:8, D:3}
```

A separate data structure (e.g. a dictionary) is needed to map node names to their row/column positions; the node data values themselves are not stored in the matrix.

### Comparison

| Adjacency Matrix Advantages | Adjacency List Advantages |
|---|---|
| Convenient to work with due to quicker access times | More space efficient for large, sparse networks |
| Easy to add nodes | Easier to add edges |

### Graph Traversal

**Breadth-first search (BFS)** visits all neighbours of a given vertex before moving on to their neighbours, layer by layer. It uses a **queue**:

1. Set the start node as the current node and add it to the visited list.
2. Enqueue all unvisited neighbours (left to right) into the queue.
3. Dequeue the front item, set it as the current node, add it to the visited list.
4. Repeat until the queue is empty.
5. Output the visited list.

**Depth-first search (DFS)** explores as far as possible along one path before backtracking. It uses a **stack**:

1. Set the start node as the current node and add it to the visited list.
2. Push all unvisited neighbours onto the stack.
3. Pop the top item, set it as the current node, add it to the visited list.
4. Repeat until the stack is empty.
5. Output the visited list.

*(Beyond source: When multiple unvisited neighbours exist, the order in which they are enqueued/pushed depends on the implementation. Exam mark schemes typically process neighbours in alphabetical or left-to-right order.)*

### Applications of Graphs

Graphs are used to model social networks, transport networks, and operating system processes.

---

## Stacks

A **stack** is a **last in first out (LIFO)** data structure. Items can only be added to or removed from the **top** of the stack. A stack is implemented using a **top pointer** that indicates where the next piece of data will be inserted.

Stacks are used to **reverse an action**, such as going back a page in web browsers or the undo function in applications.

A stack can be implemented as either a **static** or **dynamic** structure. Where the maximum size is known in advance, static stacks are preferred as they are easier to implement and make more efficient use of memory.

A **stack overflow** occurs when attempting to push an item onto a full stack. A **stack underflow** occurs when attempting to pop an item from an empty stack.

### Stack Operations

| Operation | Example | Description |
|---|---|---|
| `isEmpty()` | `Stack.isEmpty()` → `True` | Checks if the stack is empty by checking the top pointer |
| `push(value)` | `Stack.push("Nadia")` | Adds a new value to the top of the stack. Must check the stack is not full first. |
| `peek()` | `Stack.peek()` → `"Elijah"` | Returns the top value without removing it. Checks the stack is not empty first. |
| `pop()` | `Stack.pop()` → `"Elijah"` | Removes and returns the top value. Checks the stack is not empty first. |
| `size()` | `Stack.size()` → `2` | Returns the size of the stack |
| `isFull()` | `Stack.isFull()` → `False` | Checks if the stack is full by comparing the stack size to the top pointer |

When data is **pushed**, it is placed at the position of the top pointer, and the pointer increments by 1. When data is **popped**, it is returned from the top pointer position, and the pointer decrements by 1. The popped data is not necessarily erased from memory; the pointer simply moves to indicate it is no longer part of the stack, and the data can be overwritten later.

---

## Queues

A **queue** is a **first in first out (FIFO)** data structure. Items are added to the **end** (back/tail) of the queue and removed from the **front** (head) of the queue. Queues use two pointers: a **front pointer** and a **back pointer**.

A **queue overflow** occurs when attempting to enqueue an item into a full queue. A **queue underflow** occurs when attempting to dequeue an item from an empty queue.

Queues are commonly used in printers, keyboards, and simulators. There are three types: **linear queue**, **circular queue**, and **priority queue**.

### Queue Operations

| Operation | Example | Description |
|---|---|---|
| `enQueue(value)` | `Queue.enQueue("Nadia")` | Adds a new item to the end of the queue. Increments the back pointer. |
| `deQueue()` | `Queue.deQueue()` | Removes and returns the item from the front. Increments the front pointer. |
| `peek()` | `Queue.peek()` | Returns the front value without removing it |
| `isEmpty()` | `Queue.isEmpty()` → `False` | Checks if the queue is empty by comparing the front and back pointers |
| `isFull()` | `Queue.isFull()` → `False` | Checks if the queue is full by comparing the back pointer and queue size |

### Linear Queue

A **linear queue** is implemented using an array. Items are added to the next available space starting from the front. As items are dequeued, the addresses they occupied in the array **cannot be reused**, making a linear queue an inefficient use of memory.

```
enQueue(Task3)
Position: 0     1     2     3     4     5
Data:     Task1 Task2 Task3

deQueue()       // removes Task1
Position: 0     1     2     3     4     5
Data:           Task2 Task3

enQueue(Task4)
Position: 0     1     2     3     4     5
Data:           Task2 Task3 Task4
```

### Circular Queue

A **circular queue** solves the wasted-space problem of a linear queue. It is a static array with a fixed capacity. Once the rear pointer reaches the maximum size of the array, it **wraps around** to the front and stores values in previously freed positions, provided the queue is not full.

The rear pointer wraps using the formula: `rearPointer = (rearPointer + 1) MOD maxSize`

*(Beyond source: The front pointer wraps in the same way when dequeuing.)*

```
enQueue(Task7) with rearPointer at maxSize:
Position: 0     1     2     3     4     5
Data:     Task7       Task3 Task4 Task5 Task6
rearPointer: 0
```

Circular queues use space more effectively than linear queues but are **harder to implement**.

### Priority Queue

*(Beyond source: A priority queue is a variant where each item has an associated priority. Items with higher priority are dequeued before items with lower priority, regardless of insertion order. Items of equal priority follow FIFO order. Priority queues are used in process scheduling by operating systems.)*

---

## Trees

A **tree** is a connected, undirected form of a graph. Trees have a **root node** at the top. Nodes are connected to other nodes using **branches** (also called edges or arcs), with lower-level nodes being the **children** of higher-level nodes.

### Tree Terminology

| Term | Definition |
|---|---|
| **Node** | An item in the tree |
| **Edge** (branch/arc) | Connects two nodes together |
| **Root** | The single node with no incoming edges (the top node) |
| **Child** | A node with incoming edges |
| **Parent** | A node with outgoing edges |
| **Subtree** | A subsection of a tree consisting of a parent and all its children |
| **Leaf** | A node with no children |
| **Height** | The number of edges from the root to the furthest leaf node |
| **Null pointer** | Indicates a node does not point to another node (e.g. no children) |

### Uses of Trees

Trees are used for managing folder structures, storing routing tables in routers, building binary search trees to speed up searching, and representing algebraic and Boolean expressions in expression trees.

### Binary Tree

A **binary tree** is a type of tree in which each node has a **maximum of two children** (a left child and a right child). Binary trees are commonly represented by storing each node with a **left pointer** and a **right pointer**, typically implemented using a 2D array:

| Index | Left Pointer | Data Value | Right Pointer |
|---|---|---|---|
| 0 | 1 | G | 3 |
| 1 | 2 | C | 4 |
| 2 | - | A | - |
| 3 | - | J | 5 |
| 4 | - | F | - |
| 5 | - | L | - |

This represents the tree: G is the root, with C (left) and J (right). C has children A (left) and F (right). J has child L (right).

### Traversing a Binary Tree

There are three **depth-first** methods and one **breadth-first** method. The **outline method** is a visual technique: draw an outline around the tree starting from the root, and record nodes when you pass them on the relevant side.

**Pre-order traversal** (Root, Left subtree, Right subtree): Nodes are recorded when passed on the **left** side. Used in prefix notation where the operator is written before the operands (e.g. `a + b` becomes `+ a b`).

For the tree with root 15, left subtree rooted at 9 (children 5 and 11), right subtree rooted at 20 (child 25):
Pre-order: **15, 9, 5, 7, 11, 10, 12, 20, 25, 34**

**In-order traversal** (Left subtree, Root, Right subtree): Nodes are recorded when passed **underneath**. This produces nodes in **sequential (sorted) order**.

In-order: **5, 7, 9, 10, 11, 12, 15, 20, 25, 34**

**Post-order traversal** (Left subtree, Right subtree, Root): Nodes are recorded when passed on the **right** side. Used in postfix notation where the operator is written after the operands.

Post-order: **7, 5, 10, 12, 11, 9, 34, 25, 20, 15**

**Breadth-first traversal**: Visit nodes level by level, left to right, starting from the root. For a tree with root 10, second level 6 and 15, third level 2, 8, 19, fourth level 4, 17, 21:
Breadth-first: **10, 6, 15, 2, 8, 19, 4, 17, 21**

### Adding Data to a Binary Tree

1. If the tree is empty, the new value becomes the root.
2. Compare the new value to the current node.
3. If smaller, move to the left child; if greater, move to the right child.
4. Repeat until an empty position is found; insert the new node there.

### Removing Data from a Binary Tree

Three cases:

**Case 1 - Leaf node (no children):** Simply remove the node.

**Case 2 - One child:** Replace the node with its child.

**Case 3 - Two children:** Find the **in-order successor** (the minimum value in the right subtree) or the maximum value in the left subtree. Replace the node with this value, then remove the successor from its original position.

---

## Binary Search Trees

A **binary search tree (BST)** is a rooted binary tree where nodes are **ordered** to optimise searching. In ascending order, nodes to the **left** of a subtree have values **lower** than the root, and nodes to the **right** have values **higher** than the root. This property applies recursively to every subtree.

### Inserting a Value

To insert the value 2 into a BST with root 10, left child 7 (with left child 1), right child 15 (with left child 12):

1. Compare 2 to 10: 2 < 10, go left.
2. Compare 2 to 7: 2 < 7, go left.
3. Compare 2 to 1: 2 > 1, go right.
4. Position is empty, so insert 2 as the right child of 1.

### Deleting a Value

The same three cases as removing from a binary tree apply (leaf node, one child, two children), as described in the Trees section above.

---

## Hash Tables

A **hash table** is an associative array coupled with a **hash function**. The hash function takes in data (a **key**) and produces an output (the **hash value**). The role of the hash function is to **map the key to an index** in the hash table. Each piece of data is mapped to a unique position using the hash function.

Hash tables provide **fast access to data** (constant time in the best case) because keys have a direct one-to-one relationship with the address at which they are stored. They are commonly used for **indexing**.

### Hashing Non-Integer Keys

When the key is alphanumeric rather than a simple integer, the hash function performs additional processing. For example, to hash the key "C6IA":

1. Convert each character to its ASCII value: C=67, 6=54, I=73, A=65.
2. Sum the values: 67 + 54 + 73 + 65 = 259.
3. Apply MOD with the table size: 259 MOD 97 = 65.
4. Store the data at position 65 in the hash table.

### Collisions

A **collision** occurs when two different inputs produce the same hash value. A good hashing algorithm should minimise collisions. Two methods for handling collisions:

**Linear probing:** When a collision occurs, check the next position in the hash table. If it is also occupied, continue checking sequentially (or at a fixed interval, e.g. every 3rd slot) until an empty position is found. To retrieve data after linear probing: hash the key, check the indexed position, and if the stored key does not match, continue checking subsequent positions until the key is found or an empty slot is reached (meaning the data is not in the table). Many collisions degrade performance because retrieval becomes closer to a linear search.

**Chaining:** Instead of storing data directly in the hash table, each position stores a pointer to a **linked list**. When a collision occurs, the new item is appended to the linked list at that position. Each node in the chain stores the key value, the data, and a pointer to the next node. To retrieve: hash the key, then traverse the linked list at that position until the matching key is found or the end of the list is reached.

Hash tables should always be designed with **extra capacity** beyond the expected number of entries to reduce collisions.

### Rehashing

**Rehashing** addresses performance degradation as a hash table fills up or accumulates many displaced items. A new (often larger) table is created, and every existing item is re-hashed and inserted into the new table. If the table size changes, the hashing algorithm must be modified to generate a larger range of hash values. Rehashing is also an opportunity to review the effectiveness of the hash function and collision-handling strategy.

### Adding Data

1. Hash the key to generate an index.
2. Check if the position is empty.
3. If empty, insert the data (storing the key alongside it).
4. If occupied, apply the collision resolution strategy (linear probing or chaining).

### Removing Data

1. Hash the key to generate an index.
2. Check if the data at that position matches the key.
3. If it matches, remove it (mark the address as available).
4. If it does not match, search using the collision resolution strategy until the key is found or confirmed absent.

### Traversing/Searching

1. Hash the key to generate an index.
2. Check the position for the target key.
3. If found, output the data.
4. If not found, search the overflow/chain until located or confirmed absent.

The main advantage of a hash table is that lengthy searches are not necessary; additional searching is only required when collisions have occurred.

---

## Key Terms Summary

| Term | Definition |
|---|---|
| **Array** | An ordered, static set of elements of a single data type |
| **Record** | A row in a file made up of fields |
| **List** | An ordered, dynamic collection of items that can contain multiple data types |
| **Tuple** | An ordered, immutable set of values of any type |
| **Linked list** | A dynamic data structure of nodes containing data and pointers |
| **Graph** | A set of vertices/nodes connected by edges/arcs |
| **Stack** | A LIFO data structure where items are added/removed from the top |
| **Queue** | A FIFO data structure where items are added at the back and removed from the front |
| **Tree** | A connected, undirected form of graph with a root node and hierarchical structure |
| **Binary tree** | A tree where each node has a maximum of two children |
| **Binary search tree** | A binary tree where nodes are ordered (left < root < right) |
| **Hash table** | An associative array coupled with a hash function for fast key-based access |
| **Collision** | When two different keys produce the same hash value |
| **Stack overflow** | Attempting to push onto a full stack |
| **Stack underflow** | Attempting to pop from an empty stack |
| **Queue overflow** | Attempting to enqueue into a full queue |
| **Queue underflow** | Attempting to dequeue from an empty queue |
| **LIFO** | Last In First Out |
| **FIFO** | First In First Out |
| **Random access** | The ability to access a specific element directly by index |
