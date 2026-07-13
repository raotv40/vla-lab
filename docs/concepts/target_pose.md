# Target Pose

In robotics, a **Pose** specifies both the spatial position (coordinates) and rotational orientation of a rigid body relative to a reference coordinate frame.

---

## Planar vs. Spatial Pose Representation

1. **Planar Pose (2D)**:
   - Operation is restricted to a flat surface.
   - Described by **3 parameters**: $(x, y, \theta)$, where $x, y$ are Cartesian coordinates and $\theta$ is the rotation angle about the Z-axis.
2. **Spatial Pose (3D)**:
   - Operation occurs in three-dimensional space.
   - Described by **6 parameters**: $(x, y, z, \phi, \theta, \psi)$, where $x, y, z$ represent the translation vector, and $\phi, \theta, \psi$ represent rotational orientation angles (roll, pitch, yaw).

---

## Target Pose in Reacher-v5

For `Reacher-v5`:
- The target pose is represented solely by a **2D position** $(x_{\text{target}}, y_{\text{target}})$, because the end-effector has no rotation constraints.
- In reinforcement learning observations, this target is represented by indices 4 and 5:
  - `obs[4]`: Target X coordinate.
  - `obs[5]`: Target Y coordinate.
- The controller's objective is to command joint torques to minimize the Cartesian distance error vector between the fingertip pose and the target pose.
