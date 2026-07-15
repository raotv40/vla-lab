# A* Search Algorithm

**A\* (A-Star)** is an informed graph search algorithm that finds the shortest path between nodes by using heuristics to guide the search, significantly reducing the search space compared to uninformed algorithms like BFS.

---

## 1. The Cost Evaluation Function

A* evaluates nodes using a combined cost function:
$$f(n) = g(n) + h(n)$$

Where:
- $g(n)$ is the **exact cost** to reach node $n$ from the start node.
- $h(n)$ is the **heuristic estimate** of the cost to reach the goal from node $n$.
- $f(n)$ is the estimated total cost of the path passing through node $n$.

```text
       Start Node ───────[ g(n) ]───────> Current Node (n) ───────[ h(n) (Estimated) ]───────> Goal Node
```

---

## 2. Heuristics

A heuristic function $h(n)$ guides the search towards the goal:
- **Manhattan Distance**: Used when movements are restricted to 4 directions (up, down, left, right):
  $$h(n) = |x_n - x_g| + |y_n - y_g|$$
- **Euclidean Distance**: Used when movements can occur in any continuous direction:
  $$h(n) = \sqrt{(x_n - x_g)^2 + (y_n - y_g)^2}$$

*Note: For A\* to guarantee the shortest path, the heuristic must be **admissible** (it never overestimates the actual cost to reach the goal).*
