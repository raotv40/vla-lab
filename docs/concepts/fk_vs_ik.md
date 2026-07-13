# Forward Kinematics vs. Inverse Kinematics

In robotics, **Forward Kinematics (FK)** and **Inverse Kinematics (IK)** represent inverse mathematical mappings between joint space configurations and Cartesian space coordinates.

---

## Kinematics Mappings

1. **Forward Kinematics (FK)**:
   - **Direction**: Joint Space $\to$ Cartesian Space.
   - **Inputs**: Joint Angles ($\theta_1, \theta_2, \dots, \theta_n$).
   - **Outputs**: End-Effector position and orientation $(x, y, z, \text{roll}, \text{pitch}, \text{yaw})$.
   - **Properties**: Always yields a single unique solution. Mathematically straightforward, continuous, and computationally fast.
2. **Inverse Kinematics (IK)**:
   - **Direction**: Cartesian Space $\to$ Joint Space.
   - **Inputs**: Desired End-Effector position and orientation (Target Pose).
   - **Outputs**: Joint Angles ($\theta_1, \theta_2, \dots, \theta_n$).
   - **Properties**: Can have multiple solutions (elbow-up/down), infinite solutions (for redundant robots with $>6$ DoFs), or zero solutions (if the target is out of reach). Non-linear, complex, and computationally expensive.

---

## Comparison Table

| Metric | Forward Kinematics (FK) | Inverse Kinematics (IK) |
| :--- | :--- | :--- |
| **Mathematical Nature** | Unique algebraic mapping | Non-linear, multi-valued system |
| **Computational Complexity**| Low (simple matrix products) | High (requires analytical or iterative solvers) |
| **Workspace Boundaries** | Naturally maps to workspace boundary | Requires bounds checking and clamping |
| **Primary Use Case** | State feedback and error calculations | Trajectory planning and task space command execution |
