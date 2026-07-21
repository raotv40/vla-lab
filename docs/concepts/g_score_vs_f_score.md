# g-score vs. f-score

In A* path planning, nodes are evaluated using two distinct cost metrics:

---

## 1. g-score ($g(n)$)
- **Definition**: The exact accumulated path cost from the start node to node $n$.
- **Formula**: $g(n) = g(\text{parent}) + \text{cost}(\text{parent}, n)$.
- **Role**: Tracks physical movement cost incurred so far.

---

## 2. f-score ($f(n)$)
- **Definition**: The total estimated cost of the path passing through node $n$ to the goal.
- **Formula**: $f(n) = g(n) + h(n)$.
- **Role**: Priority queue ordering key determining node expansion sequence.
