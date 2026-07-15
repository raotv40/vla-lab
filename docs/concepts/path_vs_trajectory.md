# Path vs. Trajectory

In robotics, **Path** and **Trajectory** are distinct concepts that represent different aspects of motion planning.

---

## Definitions and Differences

### Path (Geometric)
A **Path** is a purely geometric description of the sequence of points or configurations that a robot visits to reach a goal. It has **no time parameterization**.
- **Representation**: A set of coordinates or a curve: $s(\alpha)$ where $\alpha \in [0, 1]$ parameterizes the curve geometry.
- **Example**: A straight line on a map connecting Point A to Point B.
- **Concern**: Collision avoidance, clearance, kinematics feasibility.

### Trajectory (Time-Parameterized)
A **Trajectory** is a time-parameterized path. It specifies not only where the robot should go, but also **when** it should arrive at each point, along with corresponding velocities and accelerations.
- **Representation**: Equations of motion: $\mathbf{x}(t)$, $\mathbf{v}(t)$, $\mathbf{a}(t)$ over time interval $t \in [0, t_f]$.
- **Example**: Moving from Point A to Point B such that the robot accelerates at $2.0\,\text{m/s}^2$, cruises at $5.0\,\text{m/s}$, and decelerates to a stop at the goal.
- **Concern**: Actuator torque limits, dynamic stability, joint velocities, settling time.

---

## Comparison Table

| Attribute | Path | Trajectory |
| :--- | :--- | :--- |
| **Time Dimension** | Absent (independent of time) | Present (explicitly time-dependent) |
| **Output Type** | Set of waypoints / curve | Positions, velocities, accelerations |
| **Physics Constraints**| Kinematic feasibility only | Dynamic actuator and acceleration limits |
| **Formulation** | Geometric curves (lines, arcs) | Interpolation functions (trapezoids, splines) |
