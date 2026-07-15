# Trajectory Generation

**Trajectory Generation** is the process of computing a continuous, time-parameterized sequence of robotic state coordinates (positions, velocities, and accelerations) to move a robot manipulator from an initial configuration to a target setpoint.

---

## Spatial Domains in Trajectory Generation

Trajectory planning can occur in two primary spaces:

1. **Joint-Space Trajectory Generation**:
   - Trajectory is planned directly in terms of joint angles: $\theta(t)$.
   - Simple to calculate since it does not require running Inverse Kinematics at every intermediate time step.
   - The end-effector path in Cartesian space is generally a curved, non-linear arc that is difficult to predict.
2. **Cartesian-Space (Task-Space) Trajectory Generation**:
   - Trajectory is planned in terms of end-effector positions: $\mathbf{x}(t) = (x(t), y(t))$.
   - Straightforward for task planning (e.g. drawing a straight line or cutting with a laser).
   - Requires running Inverse Kinematics at every control step ($\theta(t) = \text{IK}(\mathbf{x}(t))$), which has a higher computational cost.

---

## Continuity and Trajectory Smoothness

To prevent mechanical wear and joint vibrations, trajectories must satisfy boundary continuity conditions:
- **\(C^0\) Continuity**: Position is continuous (no gaps, but velocity can jump).
- **\(C^1\) Continuity**: Position and Velocity are continuous (no velocity jumps, but acceleration can jump, as in trapezoidal profiles).
- **\(C^2\) Continuity**: Position, Velocity, and Acceleration are continuous (no acceleration jumps, resulting in bounded jerk, typical of S-curves and cubic/quintic splines).
