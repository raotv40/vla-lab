# Degrees of Freedom (DoF)

**Degrees of Freedom (DoF)** refers to the number of independent variables or joint inputs required to uniquely determine the physical position and orientation of a rigid body or kinematic system.

---

## 3D Rigid Body DoFs

A free rigid body in 3D Cartesian space has **6 Degrees of Freedom**:
- **3 Translational DoFs**: Movement along the $X, Y, Z$ axes (forward/backward, left/right, up/down).
- **3 Rotational DoFs**: Rotation around the $X, Y, Z$ axes (roll, pitch, yaw).

---

## Kinematic System DoFs

In robotics, DoFs are determined by the types and number of joints in the kinematic chain:
- Each revolute joint adds $1\,\text{DoF}$ (rotational motion).
- Each prismatic joint adds $1\,\text{DoF}$ (translational motion).

### Reacher-v5 DoFs
`Reacher-v5` is a planar robotic arm restricted to a 2D plane:
- It has **2 joints** (shoulder joint and elbow joint).
- Therefore, the system has **2 Degrees of Freedom** ($2\,\text{DoFs}$).
- A minimum of 2 variables ($\theta_1, \theta_2$) is needed to specify the arm's state.
- Since it operates in a 2D plane (where task coordinates have 2 dimensions: $x$ and $y$), the 2 DoFs are sufficient to reach any point within its circular workspace.
