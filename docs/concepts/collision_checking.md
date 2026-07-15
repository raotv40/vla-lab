# Collision Checking

**Collision Checking** is the algorithmic process of determining whether a robot's configuration $\mathbf{q}$ results in a mechanical intersection with obstacles in the environment or with the robot's own body.

---

## 1. Geometric Collision Checking

In geometric collision checking, both the robot links and environmental obstacles are modeled as geometric shapes. The planner performs mathematical intersection tests:

- **Bounding Volumes**: To speed up checking, complex meshes are enclosed in simple shapes like **Bounding Spheres** or **Axis-Aligned Bounding Boxes (AABB)**.
  - Two spheres collide if the distance between their centers is less than the sum of their radii:
    $$d(\mathbf{c}_1, \mathbf{c}_2) < r_1 + r_2$$
- **Separating Axis Theorem (SAT)**: Used to check if two convex polygons overlap. If there exists a line along which the projections of the two shapes do not overlap, they do not collide.

---

## 2. Occupancy Grid Collision Checking

In discretized grids (like occupancy grids):
- The environment is represented by a multi-dimensional array of binary values:
  - `0`: Free space.
  - `1`: Obstacle space.
- Collision checking is reduced to a simple array lookup at index `(row, col)`:
  ```python
  def is_collision(grid, row, col):
      return grid[row][col] == 1
  ```
- This lookup is exceptionally fast ($O(1)$ complexity) but suffers from discretization errors (large grid cell sizes approximate obstacle boundaries poorly).
