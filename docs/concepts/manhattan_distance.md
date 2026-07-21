# Manhattan Distance

**Manhattan Distance** (also known as $L_1$ norm, City Block distance, or Taxicab distance) measures the distance between two points along axis-aligned grid lines.

---

## Mathematical Definition

For two points $\mathbf{a} = (x_1, y_1)$ and $\mathbf{b} = (x_2, y_2)$ in a 2D Cartesian plane:

$$d_{\text{Manhattan}}(\mathbf{a}, \mathbf{b}) = |x_1 - x_2| + |y_1 - y_2|$$

In $N$-dimensional space:

$$d_{\text{Manhattan}}(\mathbf{a}, \mathbf{b}) = \sum_{i=1}^{N} |a_i - b_i|$$

---

## Application in Grid Path Planning

- **4-Connected Grid**: On a grid where movement is strictly restricted to 4 orthogonal directions (Up, Down, Left, Right) with step cost 1:
  - Manhattan distance equals the **exact shortest path distance** in an obstacle-free grid.
  - It is an **admissible** and **consistent** heuristic for A* search on 4-connected grids.

```text
 (2,3) ──► ──► ──► ──► ──► (7,3)
                           │
                           ▼
                           ▼
                           ▼
                         (7,8)   Total Steps = |7-2| + |8-3| = 5 + 5 = 10
```
