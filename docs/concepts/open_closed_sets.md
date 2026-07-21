# Open Set vs. Closed Set

A* path search manages search expansion frontiers using two complementary data structures:

---

## 1. Open Set (Search Frontier)
- **Data Structure**: Min-Heap Priority Queue (`heapq` in Python).
- **Purpose**: Holds candidate nodes that have been discovered but not yet evaluated.
- **Priority**: Sorted by $f(n) = g(n) + h(n)$.
- **Operation**: Always pops the unvisited node with the lowest total estimated path cost in $O(\log N)$ time.

---

## 2. Closed Set (Evaluated Set)
- **Data Structure**: Hash Set (`set()` in Python).
- **Purpose**: Holds nodes that have already been popped from the Open Set and fully evaluated.
- **Operation**: Provides $O(1)$ lookup to prevent duplicate node re-expansions and infinite loops.
