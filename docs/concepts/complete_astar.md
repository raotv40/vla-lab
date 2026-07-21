# Complete Grid A* Search Algorithm

The **Grid-Based A\* Search Algorithm** solves for optimal shortest paths on continuous workspace maps discretized into regular 2D occupancy grids.

---

## Algorithm Architecture

```text
 1. Initialize Open Set Priority Queue (Min-Heap) with (h(start), start)
 2. Set g_score[start] = 0, all other nodes g_score = ∞
 3. Initialize Closed Set (visited) = ∅ and came_from = {}
 
 4. While Open Set is not empty:
      a. Pop node u with lowest f(u) = g(u) + h(u)
      b. If u ∈ Closed Set: continue
      c. Add u to Closed Set
      d. If u == goal: Break and Reconstruct Path
      e. For each orthogonal neighbor v of u:
           - Skip if v is out of bounds or an obstacle
           - Compute tentative_g = g_score[u] + cost(u, v)
           - If tentative_g < g_score[v]:
               - came_from[v] = u
               - g_score[v] = tentative_g
               - Push (tentative_g + h(v), v) to Open Set
```

---

## Discretized Grid Complexity

- **Time Complexity**: $O(E \log V)$ where $V$ is total grid cells ($N \times M$) and $E$ is valid 4-connected edges.
- **Space Complexity**: $O(V)$ to store `g_score`, `came_from`, `visited`, and `open_set` structures.
