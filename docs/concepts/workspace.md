# Workspace

In robotics, the **Workspace** (or work envelope) is the volume of physical space that can be reached by the robot's end-effector.

---

## Reachable vs. Dexterous Workspace

1. **Reachable Workspace**:
   - The set of all Cartesian points $(x, y, z)$ that the robot's end-effector can reach in at least one orientation.
2. **Dexterous Workspace**:
   - The subset of the reachable workspace where the end-effector can reach points in *any* arbitrary orientation.

---

## Workspace of a 2-Link Planar Robot Arm

For a planar 2-link manipulator with link lengths $L_1$ and $L_2$, the workspace is determined by:
- **Maximum Reach ($R_{\max}$)**:
  $$R_{\max} = L_1 + L_2$$
  Occurs when the arm is fully extended ($\theta_2 = 0^\circ$).
- **Minimum Reach ($R_{\min}$)**:
  $$R_{\min} = |L_1 - L_2|$$
  Occurs when the arm is fully folded back ($\theta_2 = 180^\circ$).

If $L_1 = 1.0\,\text{m}$ and $L_2 = 0.8\,\text{m}$:
- Max reach = $1.8\,\text{m}$
- Min reach = $0.2\,\text{m}$
- The workspace is an **annulus** (ring shape) centered at the base joint, with outer radius $1.8\,\text{m}$ and inner radius $0.2\,\text{m}$.

If the target setpoint falls outside this annulus, the target is **unreachable**, and no mathematical inverse kinematics solution exists.
