# Admissible Heuristics

An **Admissible Heuristic** $h(n)$ is a heuristic function that never overestimates the actual minimum cost to reach the goal state from node $n$:

$$h(n) \le h^*(n) \quad \forall n$$

where $h^*(n)$ is the true optimal cost to reach the goal.

---

## Guarantee of Optimality

If $h(n)$ is admissible, A* search is **guaranteed to return an optimal (shortest) path**. Overestimation ($h(n) > h^*(n)$) can penalize optimal paths in the priority queue, causing A* to pop suboptimal nodes first.
