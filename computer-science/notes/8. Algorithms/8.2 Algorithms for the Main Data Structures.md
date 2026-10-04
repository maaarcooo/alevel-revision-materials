# 8.2 Algorithms for the Main Data Structures

Each data structure has its own set of algorithms for manipulating the data it holds. You need to know the algorithms for stacks, queues (linear, circular, and priority), linked lists, and trees (including depth-first post-order and breadth-first traversal).

---

## Stacks

A **stack** is a **First In, Last Out (FILO)** data structure often implemented as an array. It uses a single pointer called the **top pointer**, which tracks the element currently at the top of the stack. The top pointer is initialised to **-1** because the first element occupies index 0, and a value of 0 would falsely suggest the stack contains an element.

### Stack Operations

| Operation | Name | Description |
|---|---|---|
| Check size | `size()` | Returns the number of elements |
| Check if empty | `isEmpty()` | Returns True if stack has no elements |
| Check if full | `isFull()` | Returns True if the stack has reached capacity |
| Return top element | `peek()` | Returns the top element without removing it |
| Add element | `push(element)` | Adds an element to the top of the stack |
| Remove top element | `pop()` | Removes and returns the top element |

### Stack Pseudocode

**size()** returns `top + 1` because array indexing starts at 0:

```
size()
    return top + 1
```

**isEmpty()** checks whether the top pointer is below 0:

```
isEmpty()
    if top < 0:
        return True
    else:
        return False
    endif
```

**isFull()** checks whether the stack has reached its maximum capacity:

```
isFull()
    if top + 1 == MAX_SIZE:
        return True
    else:
        return False
    endif
```

*(Beyond source: PMT's pseudocode omits the isFull() check entirely and also omits overflow checking in push(). The isFull() pseudocode and the overflow guard in push() below are drawn from the Save My Exams source and are essential for a complete implementation.)*

**peek()** returns the element at the top pointer position. It must check the stack is not empty first to avoid errors:

```
peek()
    if isEmpty():
        return error
    else:
        return A[top]
    endif
```

**push(element)** increments the top pointer then inserts the new element at that position. A full-stack check should be performed first:

```
push(element)
    if isFull():
        return error
    else:
        top += 1
        A[top] = element
    endif
```

**pop()** records the element at the top pointer, clears that position, decrements the top pointer, and returns the removed element. Must check the stack is not empty:

```
pop()
    if isEmpty():
        return error
    else:
        toRemove = A[top]
        A[top] = ""
        top -= 1
        return toRemove
    endif
```

### Stack Worked Example

Operations on a **3-element stack** (capacity 3), initially empty:

| Step | Operation | Action | Stack (bottom to top) | top | Output |
|---|---|---|---|---|---|
| 1 | `push(1)` | Insert 1 | [1] | 0 | -- |
| 2 | `push(5)` | Insert 5 | [1, 5] | 1 | -- |
| 3 | `push(4)` | Insert 4 | [1, 5, 4] | 2 | -- |
| 4 | `peek()` | View top | [1, 5, 4] | 2 | 4 |
| 5 | `pop()` | Remove 4 | [1, 5] | 1 | 4 |
| 6 | `isEmpty()` | Check empty | [1, 5] | 1 | False |
| 7 | `push(2)` | Insert 2 | [1, 5, 2] | 2 | -- |
| 8 | `push(3)` | Stack full | [1, 5, 2] | 2 | error |
| 9 | `pop()` | Remove 2 | [1, 5] | 1 | 2 |
| 10 | `pop()` | Remove 5 | [1] | 0 | 5 |

**Final output:** `4, 4, False, error, 2, 5`

Final stack state: `[1]` with top = 0.

### Stack Implementation (Python)

```python
class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def push(self, item):
        if not self.isFull():
            self.stack.append(item)
        else:
            print("Stack is full. Cannot push item:", item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            print("Stack is empty. Cannot pop item.")

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            print("Stack is empty. Cannot peek.")

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) == self.capacity
```

---

## Queues

A **queue** is a **First In, First Out (FIFO)** data structure. Items are added at the back and removed from the front. Like stacks, queues are often implemented using arrays but require **two pointers**: **front** and **back** (also called **rear**).

### Linear Queues

In a linear queue, `front` holds the position of the first element and `back` stores the **next available space** (PMT convention). An alternative convention initialises `rear = -1` so that `rear` points to the **last inserted item** (Save My Exams convention). Both are valid, and exam questions will specify which convention is in use.

#### Linear Queue Operations

| Operation | Name | Description |
|---|---|---|
| Check size | `size()` | Returns the number of elements |
| Check if empty | `isEmpty()` | Returns True if queue has no elements |
| Check if full | `isFull()` | Returns True if no space remains |
| Return front element | `peek()` | Returns the front element without removing it |
| Add element | `enqueue(element)` | Adds an element to the back of the queue |
| Remove front element | `dequeue()` | Removes and returns the front element |

#### Linear Queue Pseudocode (PMT convention: back = next available space)

In this convention, both `front` and `back` are initialised to 0. `back` always points to the first empty slot after the last element.

```
size()
    return back - front
```

```
isEmpty()
    if front == back:
        return True
    else:
        return False
    endif
```

```
peek()
    return A[front]
```

```
enqueue(element)
    if isFull():
        return error
    else:
        A[back] = element
        back += 1
    endif
```

```
dequeue()
    if isEmpty():
        return error
    else:
        toDequeue = A[front]
        A[front] = ""
        front += 1
        return toDequeue
    endif
```

#### Linear Queue Pseudocode (Save My Exams convention: rear = last item)

In this convention, `front = 0` and `rear = -1` initially. `rear` is incremented before insertion. isEmpty checks `front > rear`.

```
isFull(rear)
    if (rear + 1) == MAX_SIZE:
        return True
    else:
        return False
    endif
```

```
isEmpty(front, rear)
    if front > rear:
        return True
    else:
        return False
    endif
```

```
enqueue(queue, rear, data)
    if isFull(rear):
        print("Full")
    else:
        rear = rear + 1
        queue[rear] = data
    endif
    return rear
```

```
dequeue(queue, rear, front)
    if isEmpty(front, rear):
        print("Empty")
        dequeuedItem = Null
    else:
        dequeuedItem = queue[front]
        front = front + 1
    endif
    return (dequeuedItem, front)
```

#### Linear Queue Worked Example

Starting queue:

| A[0] | A[1] | A[2] | A[3] | A[4] | A[5] | A[6] | A[7] |
|---|---|---|---|---|---|---|---|
| Alex | Rajiv | Sam | Jayden | Charlie | | | |

Front = 0, Back = 5 (PMT convention).

| Step | Operation | Action | Front | Back | Output |
|---|---|---|---|---|---|
| 1 | `dequeue()` | Remove Alex | 1 | 5 | Alex |
| 2 | `enqueue("Julia")` | Add Julia at A[5] | 1 | 6 | -- |
| 3 | `size()` | 6 - 1 = 5 | 1 | 6 | 5 |
| 4 | `peek()` | View front | 1 | 6 | Rajiv |
| 5 | `size()` | Unchanged | 1 | 6 | 5 |
| 6 | `dequeue()` | Remove Rajiv | 2 | 6 | Rajiv |
| 7 | `isEmpty()` | 2 != 6 | 2 | 6 | False |

**Final output:** `Alex, 5, Rajiv, 5, Rajiv, False`

**Key limitation of linear queues:** once elements are dequeued, the spaces at the front of the array are wasted and cannot be reused, even if the back of the array is full. This is solved by circular queues.

### Circular Queues

A **circular queue** reuses freed spaces by wrapping the pointers around to the start of the array using the **modulo operator**:

$$\text{new position} = (\text{pointer} + 1) \bmod \text{MAX\_SIZE}$$

For example, in an array of size 7, when the pointer is at index 6: $(6 + 1) \bmod 7 = 0$, so the pointer wraps back to index 0.

| Position | (Position + 1) MOD 7 | Result |
|---|---|---|
| 0 | 1 | 1 |
| 5 | 6 | 6 |
| 6 | 0 | 0 (wraps around) |

#### Circular Queue Initialisation

Both `front` and `rear` are initialised to **-1**. When both are -1, the queue is known to be empty. After the first enqueue, both `front` and `rear` correctly reference the first item.

```
MAX_SIZE = 4
ARRAY cQueue[MAX_SIZE]
front = -1
rear = -1
```

#### Circular Queue isFull and Enqueue

The queue is **full** when the next position after `rear` would equal `front`, meaning the rear has wrapped around and caught up with the front:

```
is_full(front, rear)
    if (rear + 1) MOD MAX_SIZE == front:
        return True
    else:
        return False
    endif
```

When enqueuing, if this is the first item (`front == -1`), set `front = 0` so it points to the newly inserted element:

```
enqueue(queue, front, rear, data)
    if is_full(front, rear):
        print("Queue is full")
    else:
        rear = (rear + 1) MOD MAX_SIZE
        queue[rear] = data
        if front == -1:
            front = 0
        endif
    endif
    return (front, rear)
```

#### Circular Queue isEmpty and Dequeue

The queue is **empty** when `front == -1`:

```
is_empty(front)
    if front == -1:
        return True
    else:
        return False
    endif
```

When dequeuing, if the dequeued item was the only item (i.e. `front == rear`), reset both pointers to -1. Otherwise, advance `front` using the MOD formula:

```
dequeue(queue, front, rear)
    if is_empty(front):
        print("Queue is empty")
        dequeued_item = Null
    else:
        dequeued_item = queue[front]
        if front == rear:
            front = -1
            rear = -1
        else:
            front = (front + 1) MOD MAX_SIZE
        endif
    endif
    return (dequeued_item, front, rear)
```

### Priority Queues

A **priority queue** assigns each item a **priority value**. When a new item is enqueued, it is inserted **ahead of items with lower priority** and **behind items of equal priority** (maintaining FIFO order among items of the same priority). Dequeuing always removes the highest-priority item from the front.

Priority queues are best implemented using **OOP**, encapsulating data and methods within class definitions for reuse.

```
enqueue(queue, element, priority)
    if queue is empty OR priority > first element's priority:
        Insert element at the front
    else if priority <= last element's priority:
        Insert element at the end
    else:
        Find the correct position based on priority
        Insert element at that position
    endif
```

```
dequeue(queue)
    if queue is empty:
        return error
    else:
        Remove and return the front element
    endif
```

```
peek(queue)
    if queue is empty:
        return error
    else:
        return the front element
    endif
```

### Queue Type Comparison

| Feature | Linear Queue | Circular Queue | Priority Queue |
|---|---|---|---|
| Ordering | FIFO | FIFO with wrap-around | By priority, then FIFO |
| Pointer wrap | No, wasted space at front | Yes, via MOD | N/A (usually list-based) |
| Full condition | rear + 1 == MAX_SIZE | (rear + 1) MOD MAX_SIZE == front | Depends on implementation |
| Empty condition | front == back or front > rear | front == -1 | Queue length == 0 |
| Best for | Simple sequential processing | Fixed-size buffer with reuse | Task scheduling, OS processes |

---

## Linked Lists

A **linked list** is a dynamic data structure composed of **nodes**. Each node contains a **data field** and a **pointer** (`next`) to the next node in the list. The first node is called the **head** and the last is the **tail** (whose `next` pointer is `Null`).

If a node is referred to as `N`, the next node is accessed using `N.next`.

### Linked List Operations

**Creating a linked list** involves defining a `Node` class with a data field and a `next` pointer, then instantiating nodes and setting pointers:

```
class Node:
    field data
    field next

node1 = Node()
node1.data = "apple"
node2 = Node()
node2.data = "banana"

node1.next = node2
node2.next = None
```

**Traversing** a linked list starts at the head and follows `next` pointers until `Null` is reached:

```
current = head
while current is not None:
    print(current.data)
    current = current.next
```

**Searching** is performed as a linear search through sequential `next` operations until the desired element is found or the end of the list is reached.

**Adding to the end** creates a new node, traverses to the tail, and sets the tail's `next` pointer to the new node:

```
new_node = Node()
new_node.data = value
new_node.next = None

if head is None:
    head = new_node
else:
    current = head
    while current.next is not None:
        current = current.next
    current.next = new_node
```

**Removing a node** traverses the list tracking the previous node. If the target is the head, update the head pointer. Otherwise, set `previous.next = current.next` to bypass the removed node:

```
previous = None
current = head
while current is not None:
    if current.data == target:
        if previous is None:
            head = current.next
        else:
            previous.next = current.next
        break
    previous = current
    current = current.next
```

### Linked List Implementation (Python)

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create and connect nodes
node1 = Node("apple")
node2 = Node("banana")
node3 = Node("orange")
node1.next = node2
node2.next = node3

# Traverse
current = node1
while current is not None:
    print(current.data)
    current = current.next
```

---

## Trees

A **tree** is a data structure formed from **nodes** connected by **edges**. Trees are **acyclic** (contain no cycles) and **undirected**. They are useful because they can be **traversed** in different orders to produce different outputs.

In a **binary tree**, each node has at most two children: a **left** child and a **right** child. A node object typically has three attributes: `node.data`, `node.left`, and `node.right`.

### Creating a Tree

A tree can be represented using a `TreeNode` class with a `value` field and a `children` collection (or `left`/`right` for binary trees). A `createTreeNode` function initialises the node, and an `addChild` function appends a new child node to a parent:

```
struct TreeNode:
    value
    children []

function createTreeNode(value):
    node = new TreeNode()
    node.value = value
    node.children = []
    return node

function addChild(parentNode, childValue):
    childNode = createTreeNode(childValue)
    parentNode.children.append(childNode)
```

### Adding Data to a Binary Tree

For a binary search tree, new values are placed left if smaller than the current node, right if larger:

```
function add_node(tree, value):
    new_node = NODE()
    new_node.data = value

    if tree is Null:
        tree = new_node
    else:
        current = tree
        while True:
            if value < current.data:
                if current.left is Null:
                    current.left = new_node
                    break
                else:
                    current = current.left
            else:
                if current.right is Null:
                    current.right = new_node
                    break
                else:
                    current = current.right
    return tree
```

### Removing Data from a Binary Tree

Removing a node requires handling three cases:

**Case 1: Leaf node (no children).** Simply remove the node by setting it to Null.

**Case 2: One child.** Replace the node with its only child. Copy the child's data and pointers into the node being removed.

**Case 3: Two children.** Find the **in-order successor** (the minimum value node in the right subtree) using a `find_minimum` function. Copy the successor's data into the node being removed, then recursively remove the successor:

```
function find_minimum(node):
    while node.left is not Null:
        node = node.left
    return node

function remove_node(tree, item):
    node = find_node(tree, item)
    if node is Null:
        print("Item not found")
    else:
        if node.left is Null and node.right is Null:
            // Case 1: no children
            delete node
        else if node.left is Null or node.right is Null:
            // Case 2: one child
            if node.left is not Null:
                child = node.left
            else:
                child = node.right
            node.data = child.data
            node.left = child.left
            node.right = child.right
        else:
            // Case 3: two children
            replacement = find_minimum(node.right)
            node.data = replacement.data
            remove_node(node.right, replacement.data)
        endif
    endif
```

---

## Tree Traversal

There are two required traversal methods: **depth-first (post-order)** and **breadth-first**. Both can be implemented recursively. They differ in the order nodes are visited.

### Depth-First (Post-Order) Traversal

**Depth-first search** goes as far down into the tree as possible before backtracking. It uses a **stack** (either explicitly or via the call stack in recursion). The algorithm goes to the **left child** first. If there is no left child, it goes to the **right child**. If there are no children, it **visits** the current node (outputs its value) before backtracking.

**Post-order** means the node is visited **after** both its subtrees have been fully processed. The order is: **Left subtree, Right subtree, Root node**.

```
procedure post_order_traversal(node)
    if node.left != Null:
        post_order_traversal(node.left)
    endif
    if node.right != Null:
        post_order_traversal(node.right)
    endif
    print(node.data)
endprocedure
```

*(Beyond source: Pre-order visits in the order Root, Left, Right. In-order visits Left, Root, Right. These are not required by the OCR specification but use the same recursive structure, differing only in where the print statement appears.)*

#### Line-Drawing Method

A useful shortcut for determining traversal order is to draw a continuous line around the outside of the tree starting from the left of the root. For **post-order**, output each node's value as the line passes it **on the right side**.

For pre-order, output when the line passes on the **left**. For in-order, output when the line passes **directly underneath**. Only post-order is required for OCR.

#### Depth-First Worked Example

Tree structure:

```
        5
       / \
      3    8
     / \
    2    4
```

Trace:
1. Start at 5, go left to 3
2. At 3, go left to 2
3. At 2, no children, **visit 2** (output: 2)
4. Backtrack to 3, go right to 4
5. At 4, no children, **visit 4** (output: 4)
6. Backtrack to 3, both children visited, **visit 3** (output: 3)
7. Backtrack to 5, go right to 8
8. At 8, no children, **visit 8** (output: 8)
9. Backtrack to 5, both children visited, **visit 5** (output: 5)

**Post-order output: 2, 4, 3, 8, 5**

### Breadth-First Traversal

**Breadth-first search** visits all nodes at the current depth level before moving to the next level. Starting from the root, it visits all children from **left to right**, then all grandchildren left to right, and so on. It uses a **queue** (not a stack).

#### Breadth-First Worked Example

Same tree:

```
        5
       / \
      3    8
     / \
    2    4
```

Trace:
1. Visit root: **5** (output: 5)
2. Visit children of 5 left to right: **3**, **8** (output: 3, 8)
3. Visit children of 3 left to right: **2**, **4** (output: 2, 4)
4. 8 has no children. 2 and 4 have no children. Terminate.

**Breadth-first output: 5, 3, 8, 2, 4**

### Traversal Comparison

| Feature | Depth-First (Post-Order) | Breadth-First |
|---|---|---|
| Data structure used | Stack | Queue |
| Visit order | Left, Right, Root (deepest nodes first) | Level by level, left to right |
| Implementation | Recursive (uses call stack) | Iterative (uses explicit queue) |
| Example output (tree above) | 2, 4, 3, 8, 5 | 5, 3, 8, 2, 4 |
| When root is output | Last | First |

---

## Key Terms Summary

| Term | Definition |
|---|---|
| **Stack** | FILO data structure using a single top pointer |
| **Queue** | FIFO data structure using front and back/rear pointers |
| **Circular queue** | Queue that wraps pointers using MOD to reuse freed array spaces |
| **Priority queue** | Queue where items are ordered by priority value, not just arrival time |
| **Linked list** | Dynamic structure of nodes, each containing data and a pointer to the next node |
| **Head** | The first node in a linked list |
| **Tail** | The last node in a linked list (next = Null) |
| **Tree** | Acyclic, undirected structure of nodes connected by edges |
| **Binary tree** | Tree where each node has at most two children (left and right) |
| **Depth-first (post-order)** | Traversal visiting left subtree, right subtree, then root (uses stack) |
| **Breadth-first** | Traversal visiting nodes level by level, left to right (uses queue) |
| **push / pop** | Stack add / remove operations |
| **enqueue / dequeue** | Queue add / remove operations |
| **peek** | View the top (stack) or front (queue) element without removing it |
| **In-order successor** | The smallest-value node in the right subtree, used when removing a binary tree node with two children |
