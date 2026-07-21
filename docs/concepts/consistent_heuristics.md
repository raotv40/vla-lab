# Consistent (Monotonic) Heuristics

A heuristic $h(n)$ is **consistent** (or monotonic) if for every node $n$ and every neighbor $p$ of $n$ reached by step cost $c(n, p)$:

$$h(n) \le c(n, p) + h(p)$$

---

## Significance in Graph Search

Consistency ensures that $f(n)$ values along any path are non-decreasing. When a node is expanded in A*, its $g(n)$ score is guaranteed to be optimal. Consequently, nodes in the closed set never need to be re-opened or re-expanded, maximizing execution efficiency.
