# Heuristics in Path Planning

A **Heuristic** $h(n)$ is a domain-specific estimation function used by informed search algorithms to predict the remaining distance or cost from a current state $n$ to the goal state.

---

## Properties of Heuristics

### 1. Admissibility
A heuristic $h(n)$ is **admissible** if it never overestimates the true minimum cost to reach the goal:

$$h(n) \le h^*(n) \quad \forall n$$

where $h^*(n)$ is the true optimal cost from node $n$ to the goal.
- **Consequence**: Admissibility guarantees that A* will always find the **optimal (shortest) path**.

### 2. Consistency (Monotonicity)
A heuristic $h(n)$ is **consistent** (or monotonic) if for every node $n$ and every neighbor $p$ of $n$ with step cost $c(n, p)$:

$$h(n) \le c(n, p) + h(p)$$

- **Consequence**: Consistency guarantees that the $f(n)$ values along any path are non-decreasing. When a node is expanded by A*, its $g(n)$ value is guaranteed to be optimal, meaning nodes never need to be re-opened.

---

## Impact of Heuristic Magnitude

- **$h(n) = 0$**: Reverts A* to **Dijkstra's Algorithm**. Search is optimal but expands nodes uniformly in all directions.
- **$0 < h(n) \le h^*(n)$**: A* finds the optimal path while expanding significantly fewer nodes than Dijkstra.
- **$h(n) = h^*(n)$ (Perfect Heuristic)**: A* explores only nodes on the optimal path, achieving ideal efficiency.
- **$h(n) > h^*(n)$ (Inadmissible)**: Search runs faster, but optimality is lost; A* may return a suboptimal path.
