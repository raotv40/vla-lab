# Configuration Space (C-Space)

The **Configuration Space (C-Space)**, denoted by $\mathcal{C}$, is the set of all possible mechanical postures of a robot. A single point in C-Space completely specifies the position and orientation of every link of the robot.

---

## Workspace vs. Configuration Space

- **Workspace**: The physical 2D or 3D space where the robot operates (usually Cartesian coordinates, e.g., $x, y, z$). In the workspace, the robot has shape, volume, and complex linkages.
- **Configuration Space (C-Space)**: The parameter space of the robot's joint variables. For an $n$-joint serial manipulator, C-Space is an $n$-dimensional space where coordinates are joint angles:
  $$\mathbf{q} = (\theta_1, \theta_2, \dots, \theta_n)$$

---

## Why C-Space Simplifies Planning

Planning in physical Workspace is extremely complex because the planner must check if any point on the robot's multi-link body intersects with any point on an obstacle.

In **C-Space**:
- The robot's multi-link body is collapsed into a **single point** $\mathbf{q}$.
- The physical obstacles in the workspace are inflated to represent all joint configurations that would cause a collision. These inflated structures form the **Obstacle Space** ($\mathcal{C}_{\text{obs}}$).
- The path planning problem is simplified to finding a path for a **point robot** moving through $\mathcal{C}_{\text{free}}$, which makes collision-checking and search algorithms mathematically straightforward.

```text
 Physical Workspace:                     C-Space Representation:
 
    Obstacle                                C-Obstacle (Inflated)
     ┌──┐                                    ┌──────┐
     └──┘         / Elbow Link               │      │     ● Point Robot (q)
                 o                           └──────┘
                / \ Link 2
       Base    o   x Tip
```
