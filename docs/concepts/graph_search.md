# Graph Search

**Graph Search** is the process of exploring a graph composed of discrete **nodes** (states) connected by **edges** (transitions) to find a path from a start node to a goal node.

---

## Core Components

- **Node ($u, v \in V$)**: Represents a discrete configuration or position in state space.
- **Edge ($(u, v) \in E$)**: Represents a valid transition or action between two nodes.
- **Edge Weight ($w(u, v)$)**: The cost associated with moving from node $u$ to node $v$ (e.g., distance, time, energy).

---

## Graph Representations in Python

### Adjacency List (Used in Lab 30)
```python
graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("C", 1)],
    "C": [("G", 3)],
    "G": []
}
```
Adjacency lists are memory-efficient for sparse graphs ($O(V + E)$ space complexity) and allow fast neighbor lookups.
