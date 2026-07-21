# Priority Queue (Min-Heap)

A **Priority Queue** is an abstract data structure where every element has an associated priority value, and elements are popped in order of priority (lowest priority value first in a Min-Heap).

---

## Binary Heap Mechanics

In Python, the `heapq` module implements a **Min-Heap** using an in-place binary tree array:
- **Root**: Element at index `0` is always the minimum item.
- **Push ($O(\log N)$)**: `heapq.heappush(pq, item)` inserts an item and bubbles it up to preserve heap order.
- **Pop ($O(\log N)$)**: `heapq.heappop(pq)` extracts the minimum element and restructures the tree.

---

## Role in A* Search

In A* search, the priority queue acts as the **Open Set**:
- Elements are pushed as tuples: `(f_score, g_score, node)`.
- Python compares tuples lexicographically starting with index `0` (`f_score`).
- `heapq.heappop` automatically retrieves the unvisited node with the lowest total cost estimate $f(n)$, ensuring that A* always expands the most promising node next.
