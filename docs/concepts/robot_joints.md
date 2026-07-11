# Robot Joints

A **Joint** is a movable connection in a robot kinematic chain that constrains the relative motion between two adjacent links. Joints define the degrees of freedom of the robotic system.

---

## Types of Joints

Most robot manipulators are composed of two main joint types:

1. **Revolute Joint (Rotational)**:
   - Permits rotational motion around a single axis.
   - The joint variable is an angle ($\theta$), measured in radians or degrees.
   - *Example*: Shoulder and elbow joints in `Reacher-v5`.
2. **Prismatic Joint (Linear/Translational)**:
   - Permits sliding or translational motion along a single axis.
   - The joint variable is a linear displacement ($d$), measured in meters.
   - *Example*: A gantry rail system.

---

## Joint Limits and Constraints

Joints are typically constrained by physical or software limits:
- **Angle Limits**: A joint might only rotate between a minimum ($\theta_{\min}$) and maximum ($\theta_{\max}$) angle to prevent self-collision or cable twisting.
- **Velocity Limits**: The maximum angular rate of change ($\dot{\theta}_{\max}$) determined by motor capabilities.
- **Torque/Force Limits**: The maximum effort ($\tau_{\max}$) the joint motor can exert.

---

## Joints in Reacher-v5

Reacher-v5 has **2 revolute joints** rotating about the vertical Z-axis (orthogonal to the 2D plane of motion):
- **Shoulder Joint**: Connects the base link to Link 1.
- **Elbow Joint**: Connects Link 1 to Link 2.
- Both joints are continuous (no mechanical limits in standard Reacher), meaning their angles $\theta_1, \theta_2 \in [-\infty, \infty]$.
