# Breadth-First Search (BFS)

**Breadth-First Search (BFS)** is a fundamental graph search algorithm that explores nodes level-by-level, expanding uniformly outward from a start node.

---

## 1. FIFO Queue Logic

BFS uses a **First-In, First-Out (FIFO)** queue to manage node expansion:
1. Initialize a `queue` and append the `start` node.
2. Mark the `start` node as `visited`.
3. While the `queue` is not empty:
   - Dequeue the front node $u$.
   - For each unvisited neighbor $v$ of $u$:
     - Mark $v$ as `visited`.
     - Record $u$ as the parent of $v$ (`parent[v] = u`).
     - Enqueue $v$.

---

## 2. Completed Path Verification

If the goal node is reached, the shortest path is reconstructed by backtracking through parent nodes:
```text
  Goal (3,3) ──> Parent (2,3) ──> Parent (2,2) ──> ... ──> Start (0,0)
```
Reversing this sequence yields the shortest path.

---

## 3. Completeness and Shortest Path Guarantees

- **Completeness**: BFS is complete. If a path exists on a finite graph, BFS is guaranteed to find it.
- **Shortest Path**: On unweighted graphs (where all edges have a uniform cost of 1), BFS guarantees finding the path with the minimum number of edges (shortest path).
- **Complexity**: Time complexity is $O(V + E)$, and space complexity is $O(V)$, where $V$ is vertices and $E$ is edges.
