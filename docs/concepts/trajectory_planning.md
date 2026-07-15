# Trajectory Planning

**Trajectory Planning** is the robotic task planner's step of synthesizing smooth, collision-free joints or Cartesian trajectories that drive the physical hardware safely between configuration states.

---

## The Motion Planning Pipeline

A standard robotic control architecture uses a hierarchical pipeline:

```text
 ┌───────────────────────────────────────┐
 │ Vision-Language-Action Model (VLA)    │  Processes pixel frames + prompt: "pick apple"
 └───────────────────────────────────────┘
                     │
                     ▼ (Goal Task target coordinates)
 ┌───────────────────────────────────────┐
 │ Task & Path Planner                   │  Solves collision-free spatial waypoints (e.g. A*, RRT)
 └───────────────────────────────────────┘
                     │
                     ▼ (Geometric Waypoints Path)
 ┌───────────────────────────────────────┐
 │ Trajectory Generator (Time Profile)   │  Parameterizes the path with time (e.g., Trapezoidal profile)
 └───────────────────────────────────────┘
                     │
                     ▼ (Positions, Velocities, Accelerations over Time)
 ┌───────────────────────────────────────┐
 │ Inverse Kinematics (IK)               │  Converts Cartesian coordinates to joint setpoints (theta_d)
 └───────────────────────────────────────┘
                     │
                     ▼ (Joint Setpoint trajectories)
 ┌───────────────────────────────────────┐
 │ Low-Level Feedback Controller (PID)   │  Regulates motor currents/torques to track trajectories
 └───────────────────────────────────────┘
```

---

## Constraints in Trajectory Planning

When planning trajectories, planners must respect multiple constraints:
- **Kinematic Constraints**: Avoiding singularity configurations and violating joint travel limits.
- **Dynamic Constraints**: Actuator saturation (voltage, torque limits).
- **Environmental Constraints**: Collision avoidance with obstacles and self-collisions.
- **Task Constraints**: Keep the end-effector at specific orientations (e.g. not spilling a cup of water).
