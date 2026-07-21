# A* Search Algorithm

The **A\* (A-Star)** search algorithm is an informed graph search algorithm that finds the shortest path from a start node to a goal node by combining path costs and heuristic estimates.

---

## The Cost Evaluation Function

At every node $n$, A* evaluates the total estimated path cost using:

$$f(n) = g(n) + h(n)$$

Where:
- $g(n)$ is the **exact accumulated path cost** from the start node to node $n$.
- $h(n)$ is the **heuristic estimated cost** from node $n$ to the goal node.
- $f(n)$ is the **total estimated cost** of the cheapest path constrained to pass through node $n$.

```text
       Start Node ───────[ g(n) ]───────> Node n ───────[ h(n) (Estimated) ]───────> Goal Node
```

---

## Open Set vs. Closed Set

A* maintains two primary node structures during search:

1. **Open Set (Priority Queue)**:
   - Stores candidate nodes discovered but not yet expanded.
   - Implemented using a min-heap priority queue ordered by $f(n)$.
   - Always pops the node with the minimum $f(n)$ value.

2. **Closed Set (Visited Set)**:
   - Stores nodes already evaluated and expanded.
   - Prevents cycles and redundant re-evaluations ($O(1)$ lookup).

---

## Algorithm Steps

1. Initialize `open_set` priority queue with `(f(start), g(start), start)`.
2. Initialize `closed_set` as an empty set.
3. While `open_set` is not empty:
   - Pop node $u$ with lowest $f(u)$.
   - If $u$ is in `closed_set`, continue.
   - Add $u$ to `closed_set`.
   - If $u$ is the goal, reconstruct the path and terminate.
   - For each neighbor $v$ of $u$ with edge weight $w$:
     - If $v \notin \text{closed\_set}$:
       - Compute $g(v) = g(u) + w$.
       - Compute $f(v) = g(v) + h(v)$.
       - Push $(f(v), g(v), v)$ into `open_set`.
