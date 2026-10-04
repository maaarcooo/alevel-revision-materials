# 8.1 Algorithms

## Suitability of Algorithms

Algorithms must be compared to check their suitability for a specific set of data. Comparison considers two properties: how long an algorithm takes to solve a problem (**time complexity**) and how much memory it requires (**space complexity**). Generally, algorithms that finish quicker and use less memory are preferred, but which property matters more depends on the situation.

### Time Complexity

Time complexity measures execution time in terms of **operations or steps performed**, not numerical time in seconds. An algorithm's time complexity is **independent of the hardware and CPU** used to run it: a faster processor completes the same number of steps more quickly, but the step count itself does not change.

Consider two algorithms that both calculate the sum of the first n integers:

```
function sumNumbers1(n)
    sum = 0
    for i = 1 to n
        sum = sum + n
    next i
    return sum
endfunction
```

This executes n + 1 instructions (1 for the assignment, n for the loop). As n grows, the constant (1) becomes insignificant and the algorithm's time is dominated by n.

```
function sumNumbers2(n)
    sum = n * (n+1)/2
    return sum
endfunction
```

This executes exactly 1 instruction regardless of n. Its time complexity is **constant**.

Both algorithms share the same goal but complete it in fundamentally different ways, illustrating why complexity analysis matters.

### Space Complexity

**Space complexity** is how much memory an algorithm requires to complete. If additional space is needed to duplicate data (e.g. creating copies of lists), this contributes to overall space complexity. Space complexity is also expressed using Big-O notation.

### Trade-offs Between Time and Space

Time and space complexity have no fixed priority. The choice depends on the situation:

- If you have a lot of data but need fast processing (e.g. for a time-critical update), prioritise **time complexity** over space.
- If you have ample processing power but limited storage, prioritise **space complexity**.

To reduce space complexity, perform all changes on the original data (in-place operations). To reduce time complexity, minimise nested loops and reduce the number of items the algorithm must process (e.g. divide and conquer approaches achieve logarithmic time).

---

## Big-O Notation

**Big-O notation** expresses the complexity of an algorithm. It describes the **scalability** of an algorithm as its order (O), showing an upper limit for the amount of time or space taken relative to the number of data elements (n) given as input. It is named after the German mathematician **Edmund Landau**.

### Rules for Determining Big-O

1. **Remove all terms except the one with the largest factor or exponent** (the dominant term).
2. **Remove any coefficients** (constant multipliers).

For example, an algorithm with total instructions $3n^2 + 4n + 5$ (three nested loops, four standard loops, five statements) is described as $O(n^2)$ because $n^2$ dominates as n grows, and the coefficient 3 is removed.

### Complexity Classes

| Big-O | Name | Description |
|---|---|---|
| $O(1)$ | Constant | Time is independent of input size. Same number of instructions regardless of n. |
| $O(\log n)$ | Logarithmic | Time increases at a diminishing rate as input grows. Typical of divide-and-conquer algorithms that halve the problem each step. |
| $O(n)$ | Linear | Time is directly proportional to input size. One loop iterating over all n items. |
| $O(n \log n)$ | Linear-logarithmic | Between linear and polynomial. Typical of efficient sorting algorithms like merge sort. |
| $O(n^2)$ | Polynomial (quadratic) | Time is proportional to the square of the input. Typical of two nested loops each running n times. |
| $O(n^k)$ | Polynomial (general) | Time proportional to $n^k$ where k is the number of nested loops. All are still called polynomial time. |
| $O(2^n)$ | Exponential | Time doubles with every additional input item. Very inefficient; few practical algorithms use this. |
| $O(n!)$ | Factorial | Worse than exponential. Grows faster than all other common classes. |

Efficiency ranking (best to worst): $O(1) < O(\log n) < O(n) < O(n \log n) < O(n^2) < O(2^n) < O(n!)$

> ⚠ Check: PMT source text states "the best time complexity for an algorithm as the number of inputted items increases is the linear time complexity." This contradicts its own diagram which correctly shows $O(1)$ (constant) as the best. The ranking above is correct.

### Logarithms

A **logarithm** is the inverse of an exponential. It determines how many times a base number must be multiplied by itself to reach another number. In computer science, logarithms are usually measured in **base 2**.

$$2^3 = 8 \implies \log_2(8) = 3$$

| x | $\log_2(x)$ |
|---|---|
| 1 ($2^0$) | 0 |
| 8 ($2^3$) | 3 |
| 1,024 ($2^{10}$) | 10 |
| 1,048,576 ($2^{20}$) | 20 |
| 1,073,741,824 ($2^{30}$) | 30 |

Doubling the input has minimal effect on the number of instructions for logarithmic algorithms.

### Deriving Big-O from Code

The simplest method is to **count the number of loops and nested loops**.

**No loops (only statements):** Each statement is $O(1)$. If there are no loops, the algorithm is $O(1)$.

**Single loop:** A single `for` or `while` loop iterating n times gives $O(n)$. Multiple non-nested loops (e.g. three loops each running n times) give $3 \times O(n)$, but after removing the coefficient, this is still $O(n)$.

Detailed example: an algorithm with three sequential loops and five statements has total instructions $3n + 5$.

| n | 3n | 5 | 3n + 5 |
|---|---|---|---|
| 1 | 3 | 5 | 8 |
| 100 | 300 | 5 | 305 |
| 1,000,000 | 3,000,000 | 5 | 3,000,005 |

The constant (5) contributes less and less as n increases. 3n is the significant term. After removing the coefficient, the result is $O(n)$.

**Nested loops:** Two nested loops each running n times give $n \times n = O(n^2)$. The number of nesting levels determines the exponent:

| Nested loops | Big-O |
|---|---|
| 2 | $O(n^2)$ |
| 3 | $O(n^3)$ |
| 4 | $O(n^4)$ |
| 5 | $O(n^5)$ |
| 6 | $O(n^6)$ |

If an algorithm contains both nested loops and non-nested loops/statements, the dominant term is used. For example, one nesting of two loops $O(n^2)$, one separate loop $O(n)$, and one statement $O(1)$ gives overall $O(n^2)$ because polynomial dominates linear and constant.

**Recursive halving:** A divide-and-conquer algorithm that halves the search space each iteration gives $O(\log n)$.

### Best, Average, and Worst Case

All algorithms have three complexity scenarios:

**Best case:** The algorithm performs most efficiently. For example, a linear or binary search finding the item on the first comparison gives $O(1)$. A bubble sort receiving an already-sorted list gives $O(n)$ (one pass to confirm order).

**Average case:** The algorithm performs neither at its best nor worst. For example, a linear search finding the item in the middle gives $O(n/2)$, which after removing the coefficient is still $O(n)$.

**Worst case:** The algorithm is at its least efficient. For example, a linear search checking every element gives $O(n)$. A bubble sort on a reverse-sorted list gives $O(n^2)$.

**Big-O is almost always measured by the worst case.** This gives programmers a guaranteed minimum performance level for selecting appropriate algorithms.

### Worked Example: Comparing Solutions

Two solutions to the same problem have these complexities:

| | Solution A | Solution B |
|---|---|---|
| Time | $O(n)$ | $O(n)$ |
| Space | $O(k^n)$ where $k > 1$ | $O(\log n)$ |

**Recommendation:** Solution B. Both share the same time complexity, so space complexity is the deciding factor. Solution A's space grows exponentially with input size (very poorly), while Solution B's space grows logarithmically (very well).

---

## Searching Algorithms

A **searching algorithm** is a method to find a specific value or element within a data structure. The two most common are **linear search** and **binary search**.

### Linear Search

The linear search finds elements in an **unordered list**. It checks **sequentially and systematically** from start to end, one element at a time, comparing each element to the target value. If found, it outputs the index. If not found, it returns -1 (or a "not found" message).

**How it works:**
1. Start at the first element (index 0).
2. Compare the current element to the target.
3. If they match, record the index and stop.
4. If not, move to the next element.
5. Repeat until found or the end of the list is reached.

**Pseudocode:**

```
function linearSearch(list, item)
    index = -1
    i = 0
    found = False
    while i < len(list) and found = False
        if list[i] = item then
            index = i
            found = True
        endif
        i = i + 1
    endwhile
    return index
endfunction
```

Variables: `index = -1` is a default "not found" value. `i = 0` starts the counter at the beginning. `found = False` is a flag to stop the search when the item is located.

**Trace table** (searching for 8 in [5, 4, 7, 1, 3, 8, 9, 2]):

| item | index | i | list[i] | found |
|---|---|---|---|---|
| 8 | -1 | 0 | 5 | False |
| | | 1 | 4 | |
| | | 2 | 7 | |  
| | | 3 | 1 | |
| | | 4 | 3 | |
| 8 | 5 | 5 | 8 | True |

**Time complexity:**
The loop runs n times with two instructions inside (the if-check and the assignment), giving $O(2n)$. Three initial statements add $O(1)$. Total: $2n + 3$. After removing coefficients and dominated terms: **$O(n)$ worst case**. Best case $O(1)$ (item at first position). Average case $O(n/2) \rightarrow O(n)$.

**Space complexity:** $O(1)$. Only a constant number of extra variables (loop counter, target, index) regardless of input size.

### Binary Search

The binary search is a **divide-and-conquer** algorithm that is more efficient than linear search. It requires the list to be **sorted**. It compares the **middle item** to the target. If they match, the index is returned. If the target is less than the middle value, the **upper half is ignored**. If the target is greater, the **lower half is ignored**. The search continues on the remaining half until the item is found or the search space is exhausted.

The binary search does **not** discard, delete, or remove parts of the list. It only adjusts the **start, end, and mid pointers**, giving the appearance that items have been discarded.

**How it works (example: searching for 21 in [3, 5, 9, 10, 14, 16, 17, 21, 24, 26, 28, 30, 42, 44, 50, 51]):**

1. Start = 0, End = 15, Mid = (0+15)/2 = 7. list[7] = 21. Target is 21. Compare: 21 < 24? Yes. Adjust End = Mid - 1 = 7.

*(Beyond source: the walkthrough above is simplified. The SME source shows a detailed diagram where mid is initially index 8 (value 24), then adjusts to index 4 (value 14), then index 6 (value 17), then finally index 7 (value 21). Both sources round the midpoint differently. Either rounding up or down is valid provided consistent use throughout.)*

**Pseudocode:**

```
function binarySearch(list, item)
    found = False
    index = -1
    start = 0
    end = len(list) - 1
    while start <= end and found = False
        mid = int((start + end) / 2)
        if list[mid] = item then
            found = True
            index = mid
        else
            if list[mid] < item then
                start = mid + 1
            else
                end = mid - 1
            endif
        endif
    endwhile
    return index
endfunction
```

> ⚠ Check: The SME pseudocode uses both `end` and `last` as variable names for the same pointer in different lines (initialises `end`, but the while loop and else branch reference `last`). This is an inconsistency in the source. The corrected version above uses `end` consistently.

**Trace table** (searching for 21 in [3, 5, 9, 10, 14, 16, 17, 21, 24, 26, 28, 30, 42, 44, 50, 51]):

| item | index | found | start | end | mid | list[mid] |
|---|---|---|---|---|---|---|
| 21 | -1 | False | 0 | 15 | 8 | 24 |
| | | | 0 | 7 | 4 | 14 |
| | | | 5 | 7 | 6 | 17 |
| 21 | 7 | True | 7 | 7 | 7 | 21 |

**Time complexity derivation:**
The algorithm starts with n items. After each iteration the search space halves: n/2, n/4, n/8, ..., $n/2^i$ after i iterations. The worst case (maximum iterations) occurs when $n/2^i = 1$. Multiplying both sides by $2^i$ gives $n = 2^i$. Taking the logarithm: $\log_2 n = i$. Therefore the binary search is **$O(\log n)$ worst case**. Best case is $O(1)$ (item found on first comparison). Average case is $O(\log n / 2)$, which after removing coefficients is still $O(\log n)$.

**Space complexity:**
- **Iterative** implementation: $O(1)$ (uses only a fixed number of variables: start, end, mid).
- **Recursive** implementation: $O(\log n)$ (each recursive call adds a frame to the call stack, with maximum recursion depth proportional to $\log n$).

**Worked example:** Searching for 607 in the list of positive even numbers [2, 4, 6, ..., 998, 1000] (500 items):
1. Compare 607 with 500 (mid). 607 > 500, so discard the lower half.
2. Compare 607 with 750 (mid). 607 < 750, so discard the upper half.
3. Compare 607 with 624 (mid). 607 < 624, so discard the upper half. The search continues narrowing until the algorithm determines 607 is not in the list (it contains only even numbers).

---

## Sorting Algorithms

### Bubble Sort

The bubble sort compares **pairs of adjacent elements** and swaps them if they are out of order (placing the smaller value before the larger). Each complete traversal of the list is called a **pass**. After each pass, the largest unsorted value "bubbles" to the top (end) of the unsorted portion. The sort is complete when a final pass produces **no swaps**.

> ⚠ Check: The PMT source provides a bubble sort pseudocode that only contains a single while loop (no outer loop for multiple passes), making it an incomplete single-pass implementation. The correct bubble sort requires nested iteration (an outer loop for passes and an inner loop for comparisons), as shown in the SME source below.

**How it works (example: [9, 2, 4, 7, 10, 3, 1]):**

Pass 1: Compare adjacent pairs from left to right. Swap 9 & 2, swap 9 & 4, swap 9 & 7, 9 < 10 no swap, swap 10 & 3, swap 10 & 1. After pass 1: [2, 4, 7, 9, 3, 1, 10]. The largest value (10) is now in the correct position.

Pass 2: Repeat comparisons on the unsorted portion (excluding the last element). Continue until no swaps occur in a complete pass.

**Efficient pseudocode (with reducing comparisons):**

```
list = [5, 9, 4, 2, 6, 7, 1, 2, 4, 3]
last = len(list)
swap = True
i = 0
while i < (last - 1) and (swap = True)
    swap = False
    for j = 0 to last - i - 2
        if list[j] > list[j+1]
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp
            swap = True
        endif
    next j
    i = i + 1
endwhile
print(list)
```

Key implementation details:
- The inner `for` loop reduces its range by 1 each pass (`last - i - 2`) because the last i elements are already sorted.
- Using a `while` loop (not `for`) for the outer loop allows **early termination** if no swaps occur (the list is already sorted).
- A `for` loop would continue comparing even if items are already in order.

**Time complexity:** The outer while loop runs up to n times, the inner for loop also runs up to n times. Expression: $2n^2 + 4$. After removing coefficients and lower-order terms: **$O(n^2)$ worst case** (reverse-sorted list). Best case $O(n)$ (already sorted, one pass confirms order). Average case $O(n^2)$.

**Space complexity:** $O(1)$. Operates **in-place** with only a fixed number of extra variables (loop counters, temp for swapping).

### Insertion Sort

The insertion sort builds a sorted portion of the list one item at a time by **placing each item in its correct position** within the already-sorted portion. Starting from the second element, each **current item** is compared backwards against previous elements. If a previous element is larger, it is **shifted right** to make room. When a smaller-or-equal element is found (or the start of the list is reached), the current item is inserted.

**How it works (example: [5, 9, 4, 2, 7, 1, 2, 4, 3]):**

- 5 is the first item, already "sorted".
- 9: compare with 5. 9 > 5, no move. Sorted so far: [5, 9].
- 4: compare with 9 (shift right), compare with 5 (shift right), insert at position 0. Sorted so far: [4, 5, 9].
- 2: compare with 9 (shift), 5 (shift), 4 (shift), insert at position 0. Sorted so far: [2, 4, 5, 9].
- The process continues until all items are in place. Final: [1, 2, 2, 3, 4, 4, 5, 7, 9].

**Pseudocode:**

```
procedure insertionSort(list)
    n = len(list)
    for i = 1 to n - 1
        item = list[i]
        position = i
        while position > 0 and list[position - 1] > item
            list[position] = list[position - 1]
            position = position - 1
        endwhile
        list[position] = item
    next i
endprocedure
```

The for loop iterates from element 1 (not 0, as the first element is trivially sorted). For each element, the while loop shifts larger elements right until the correct insertion point is found.

> ⚠ Check: The SME worked example pseudocode (line 07) uses `if dataArray[tempPos] < temp then` to trigger shifting, which would sort in descending order. The standard ascending insertion sort (as shown in the main pseudocode) shifts when `list[position - 1] > item`. The worked example's comparison direction appears reversed.

**Time complexity:** A for loop with a nested while loop. Expression: $6n^2 + 1$. After simplification: **$O(n^2)$ worst case** (reverse-sorted list). Best case $O(n)$ (already sorted, each item compared once). Average case $O(n^2)$.

**Space complexity:** $O(1)$. Operates in-place with no additional data structures.

### Merge Sort

Merge sort is a **divide-and-conquer** algorithm with two phases:

**Phase 1 (Divide):** Repeatedly split the list in half until each sub-list contains a single element (the **base case**).

**Phase 2 (Merge):** Repeatedly merge pairs of sub-lists in sorted order, building progressively larger sorted sub-lists until one fully sorted list remains.

**How it works (example: [15, 5, 2, 7, 4, 9, 10, 1, 8, 3]):**

Divide: [15, 5, 2, 7, 4] and [9, 10, 1, 8, 3] → further splits → eventually 10 single-element sub-lists.

Merge: [15] and [5] → [5, 15]. [2] and [7, 4] → [2] and [7] and [4] → [4, 7] → [2, 4, 7]. Then [5, 15] and [2, 4, 7] → [2, 4, 5, 7, 15]. The right half follows the same process. Final merge produces [1, 2, 3, 4, 5, 7, 8, 9, 10, 15].

Key details:
- Halving sometimes produces sub-lists of unequal size (odd number of elements).
- Only **two sub-lists can be merged at a time**. Any leftover sub-list waits for the next merging round.
- Merging uses **two pointers** (one per sub-list) to track which elements are being compared. When one sub-list is exhausted, the remaining elements of the other are appended directly.
- Merge sort relies on **recursion**. Each recursive call creates a stack frame. Stack frames are popped when the base case is reached, and merging occurs as the recursion unwinds.

**Pseudocode:**

```
procedure mergesort(list)
    if len(list) > 1 then
        mid = len(list) div 2
        left = list[:mid]
        right = list[mid:]

        mergesort(left)
        mergesort(right)

        leftPointer = 0
        rightPointer = 0
        newListPointer = 0

        while leftPointer < len(left) and rightPointer < len(right)
            if left[leftPointer] < right[rightPointer] then
                list[newListPointer] = left[leftPointer]
                leftPointer = leftPointer + 1
            else
                list[newListPointer] = right[rightPointer]
                rightPointer = rightPointer + 1
            endif
            newListPointer = newListPointer + 1
        endwhile

        while leftPointer < len(left)
            list[newListPointer] = left[leftPointer]
            leftPointer = leftPointer + 1
            newListPointer = newListPointer + 1
        endwhile

        while rightPointer < len(right)
            list[newListPointer] = right[rightPointer]
            rightPointer = rightPointer + 1
            newListPointer = newListPointer + 1
        endwhile
    endif
endprocedure
```

**Slicing notation:** `[:mid]` means all elements up to (but not including) the mid index. `[mid:]` means all elements from mid to the end.

The merge has two stages: Stage 1 compares elements from both halves and places the smaller one into the merged list (first while loop). Stage 2 appends any remaining elements from whichever half is not yet exhausted (the two trailing while loops; only one will execute).

**Time complexity:** The divide phase halves the list $O(\log n)$ times. At each level, n elements must be merged. Overall: **$O(n \log n)$ for all cases** (best, average, and worst). The structure of the data does not change the number of splits or merges required.

**Space complexity:** $O(n)$ original space plus an additional $O(n)$ for copies of the left and right halves. Merge sort requires **twice the space** of in-place sorts due to holding copies of sub-lists.

### Quick Sort

Quick sort is a **divide-and-conquer** algorithm that uses a **pivot** value to partition the list.

**How it works:**

1. Set the **pivot** to the first element. Set a **left pointer** to pivot + 1 and a **right pointer** to the end of the list.
2. **Increment the left pointer** until it finds a value greater than the pivot (or passes the right pointer).
3. **Decrement the right pointer** until it finds a value less than the pivot (or passes the left pointer).
4. If the left and right pointers have **not crossed**, swap the values at the two pointers. Continue steps 2-3.
5. If the pointers have **crossed**, swap the pivot with the value at the right pointer. The pivot is now in its **correct sorted position**.
6. **Recursively** call quick sort on both sub-lists: elements to the left of the pivot and elements to the right.
7. Repeat until all sub-lists are sorted.

**Example: [8, 2, 6, 1, 7, 9, 1, 4]**

Pivot = 8, Left starts at index 1, Right starts at index 7. Left moves right, finds 9 (> 8) at index 5. Right moves left, finds 4 (< 8) at index 7. Swap 9 and 4 → [8, 2, 6, 1, 7, 4, 1, 9]. Continue: Left finds 9 at index 7, Right finds 1 at index 6. Pointers cross. Swap pivot (8) with right pointer value (1) → [1, 2, 6, 1, 7, 4, 8, 9]. 8 is now sorted. Recursively sort [1, 2, 6, 1, 7, 4] and [9].

**Pseudocode:**

```
function quicksort(list, start, end)
    if start >= end then
        return
    else
        pivot = list[start]
        left = start + 1
        right = end
        done = False
        while done == False
            while left <= right and list[left] <= pivot
                left = left + 1
            endwhile
            while right >= left and list[right] >= pivot
                right = right - 1
            endwhile
            if left < right then
                temp = list[left]
                list[left] = list[right]
                list[right] = temp
            else
                done = True
            endif
        endwhile
        temp = list[start]
        list[start] = list[right]
        list[right] = temp
        quicksort(list, start, right - 1)
        quicksort(list, right + 1, end)
    endif
    return list
endfunction
```

**Time complexity:**

- **Best and average case: $O(n \log n)$.** If the pivot divides the list roughly in the middle, each level of recursion performs n operations across approximately $\log n$ levels.
- **Worst case: $O(n^2)$.** If the pivot is consistently the smallest or largest value (e.g. already sorted input), one partition is always empty. The recursion degenerates into n calls each processing n - 1 elements.

Poor pivot selection or already-sorted input causes worst-case behaviour. In practice, **randomised** or **median-of-three** pivot selection avoids this. If recursion depth becomes too large, a **stack overflow** can occur.

**Space complexity:** $O(n)$ with $O(n)$ additional space required, as copies of sub-lists are placed on the call stack.

### Sorting Algorithms Comparison

| Algorithm | Best Case | Average Case | Worst Case | Space | In-Place? | Stable? |
|---|---|---|---|---|---|---|
| Bubble sort | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Yes | Yes |
| Insertion sort | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Yes | Yes |
| Merge sort | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | No | Yes |
| Quick sort | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(n)$ | Depends | No |

*(Beyond source: The "Stable?" column is included for completeness. A stable sort preserves the relative order of equal elements. This is occasionally relevant at A-Level but is not discussed in either source.)*

---

## Path-Finding Algorithms

### Dijkstra's Shortest Path Algorithm

**Dijkstra's algorithm** is an **optimisation algorithm** that calculates the shortest path from a starting node to **all other nodes** in a **weighted graph**. It operates similarly to a breadth-first search, exhaustively exploring routes to find the optimal path.

**Optimisation problems** involve maximising the efficiency of a solution. Examples include: finding the shortest route between two points, minimising resource usage, timetabling, and scheduling.

**How the algorithm works:**

1. Set the distance to the starting node to 0 and all other nodes to **infinity** (∞).
2. Add all nodes to a **priority queue** sorted by current distance.
3. While the queue is not empty:
   a. Remove the node with the **smallest distance** from the queue. Mark it as **visited**.
   b. For each **unvisited neighbour** of the current node, calculate `newDistance = distanceAtCurrentNode + edgeWeight`.
   c. If `newDistance < currentDistanceAtNeighbour`, update the neighbour's distance and record the current node as the **previous node** on the shortest path.
4. Once all nodes are visited, **backtrack** through the previous-node records from the goal to the start to reconstruct the shortest path.

**Worked walkthrough (A to G):**

Given a weighted graph with nodes A-G (A is the start, G is the goal):

| Step | Visit | Updates | Notes |
|---|---|---|---|
| 1 | A (distance 0) | B=3, C=5, D=1 | Set A's neighbours |
| 2 | D (distance 1, lowest) | C updated 5→3 (A→D→C), E=2, F=7 | C shortened via D |
| 3 | E (distance 2) | F updated 7→5 (A→D→E→F), G=5 | F shortened via E |
| 4 | B (distance 3) | C not updated (A→B→C = 4 > 3) | No improvement |
| 5 | C (distance 3) | G not updated (A→D→C→G = 7 > 5) | No improvement |
| 6 | F (distance 5) | No unvisited neighbours | |
| 7 | G (distance 5) | No unvisited neighbours | |

Shortest path A→G: **A → D → E → G**, total distance = **5**. Reconstructed by backtracking: G's previous is E, E's previous is D, D's previous is A.

**Key properties:**
- The algorithm is **exhaustive**: it checks every available node and path, calculating the shortest distance from the start to every other node.
- A **dictionary** storing nodes and their neighbours (adjacency list) is passed to the algorithm.
- A corresponding dictionary of shortest distances is maintained during execution.
- The algorithm can use either a priority queue or a simple loop to find the next shortest node.

**Structured English:**

```
assign distance 0 to the initial node and infinity to every other node
add all nodes to a priority queue sorted by current distance
while the queue is not empty
    remove node x from the front of the queue and add to visited list
    for each unvisited neighbour y of node x
        newDistance = distanceAtX + distanceFromXtoY
        if newDistance < distanceAtY then
            distanceAtY = newDistance
            reorder priority queue based on new distance
        endif
    next y
endwhile
```

### A* Search Algorithm

The **A* algorithm** builds on Dijkstra's by adding a **heuristic** function that estimates the distance from the current node to the **goal node**, making it more efficient by focusing the search toward the goal rather than exploring all nodes equally.

**Key definitions:**
- **Heuristic** $h(x)$: a rule of thumb, best guess, or estimate that approximates the **straight-line (Euclidean) distance** from node x to the goal node. Every node has a heuristic value.
- **Cost function** $g(x)$: the actual distance from the start node to node x (same as Dijkstra's distance).
- **Total cost** $f(x) = g(x) + h(x)$: the estimated total cost of the path through node x to the goal.

**Key principles:**
- The heuristic must **never overestimate** the real cost from the current node to the goal. The real cost should always be greater than or equal to the heuristic value. *(Beyond source: this property is called **admissibility** of the heuristic.)*
- If $h(x)$ increases compared to the previous node, the algorithm is travelling **further from the goal**.
- A* **stops when the goal node is reached**, unlike Dijkstra's which calculates distances to all nodes. This makes A* more efficient when only one destination matters.
- If $h(x) = 0$ for all nodes, A* behaves identically to Dijkstra's.

**How it differs from Dijkstra's:**

| Property | Dijkstra's | A* |
|---|---|---|
| Cost function | $g(x)$ only | $f(x) = g(x) + h(x)$ |
| Uses heuristic | No | Yes |
| Goal-directed | No (finds shortest to all nodes) | Yes (stops at goal) |
| Efficiency | Explores broadly | Focused toward goal |

**How A* works:**

1. Set $g(\text{start}) = 0$ and $f(\text{start}) = h(\text{start})$. Set $g$ and $f$ to infinity for all other nodes.
2. Add all nodes to a priority queue sorted by $f(x)$.
3. While the queue is not empty:
   a. Remove the node with the **smallest $f(x)$** from the queue. Mark as visited.
   b. If this node is the **goal node**, stop.
   c. For each unvisited neighbour y: calculate $g_\text{new} = g(\text{current}) + \text{edgeWeight}$.
   d. If $g_\text{new} < g(y)$, update $g(y) = g_\text{new}$ and $f(y) = g(y) + h(y)$. Reorder the queue.
4. Backtrack through previous nodes to reconstruct the shortest path.

**Worked walkthrough (A to G, with heuristic values):**

Given heuristic values: A=5, B=5, C=3, D=4, E=2, F=3, G=0.

| Step | Visit | g(x) | h(x) | f(x) | Previous |
|---|---|---|---|---|---|
| 1 | A | 0 | 5 | 5 | - |
| 2 | D (lowest f) | 1 | 4 | 5 | A |
| 3 | E (lowest f=4) | 2 | 2 | 4 | D |
| 4 | G (f=5) | 5 | 0 | 5 | E |

Shortest path: **A → D → E → G**, total distance = **5**. A* found the same path as Dijkstra's but visited fewer nodes (it did not need to explore B, C, or F).

---

## Algorithm Comparison Summary

| Algorithm | Type | Time (Worst) | Time (Best) | Space | Key Requirement |
|---|---|---|---|---|---|
| Linear search | Search | $O(n)$ | $O(1)$ | $O(1)$ | None (works on unsorted data) |
| Binary search | Search | $O(\log n)$ | $O(1)$ | $O(1)$ iterative | List must be sorted |
| Bubble sort | Sort | $O(n^2)$ | $O(n)$ | $O(1)$ | None |
| Insertion sort | Sort | $O(n^2)$ | $O(n)$ | $O(1)$ | None |
| Merge sort | Sort | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | Additional memory for copies |
| Quick sort | Sort | $O(n^2)$ | $O(n \log n)$ | $O(n)$ | Good pivot selection avoids worst case |
| Dijkstra's | Path-finding | - | - | - | Weighted graph, no negative weights |
| A* | Path-finding | - | - | - | Weighted graph, admissible heuristic |

---

## Key Terms Summary

| Term | Definition |
|---|---|
| **Time complexity** | Number of operations/steps an algorithm requires, measured independently of hardware |
| **Space complexity** | Amount of memory an algorithm requires to complete |
| **Big-O notation** | Notation expressing an algorithm's scalability as its order O, showing worst-case upper bound |
| **Dominant term** | The term in a complexity expression that contributes most as input grows (others are dropped) |
| **Divide and conquer** | Strategy that splits a problem into smaller sub-problems, solves each, then combines results |
| **Heuristic** | A rule of thumb or estimate used to guide an algorithm toward a solution more efficiently |
| **Pivot** | Element chosen in quick sort to partition the list into values less than and greater than it |
| **Pass** | One complete traversal of a list during a sorting algorithm |
| **In-place** | An algorithm that sorts using only a constant amount of extra memory (no copies of the list) |
| **Optimisation problem** | A problem requiring the most efficient solution (e.g. shortest route, minimum cost) |
| **Priority queue** | A queue where elements are ordered by priority (e.g. shortest distance) rather than arrival |
