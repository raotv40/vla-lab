# Motion Planning

**Motion Planning** is the task of finding a collision-free path for a robot from a starting configuration to a goal configuration in the presence of obstacles.

---

## The Motion Planning Problem

Let:
- $\mathcal{C}$ be the **Configuration Space** of all possible postures of the robot.
- $\mathcal{C}_{\text{free}} \subset \mathcal{C}$ be the **Free Space** where the robot is not in collision with any obstacle or itself.
- $\mathcal{C}_{\text{obs}} \subset \mathcal{C}$ be the **Obstacle Space** where collisions occur.
- $\mathbf{q}_{\text{start}} \in \mathcal{C}_{\text{free}}$ be the starting configuration.
- $\mathbf{q}_{\text{goal}} \in \mathcal{C}_{\text{free}}$ be the target configuration.

The objective of a motion planner is to compute a continuous path:
$$\tau: [0, 1] \to \mathcal{C}_{\text{free}}$$
such that $\tau(0) = \mathbf{q}_{\text{start}}$ and $\tau(1) = \mathbf{q}_{\text{goal}}$.

---

## Path Planning vs. Trajectory Planning

- **Path Planning**: A purely geometric problem of finding a collision-free sequence of points ($\mathbf{q}$) connecting the start to the goal. It does not parameterize velocity or time.
- **Trajectory Planning**: Takes the geometric path and parameterizes it with time, velocities, and accelerations, ensuring that actuator torque limits and boundary speeds are respected.
