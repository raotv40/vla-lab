# Reachable Workspace

The **Reachable Workspace** represents the complete volume (or planar area) of space that a robot's end-effector tip can physically access.

---

## Workspace Limits of 2-Link Planar Robot

For a serial 2-link planar arm with link lengths $L_1$ and $L_2$:
- **Outer Bound ($R_{\max}$)**:
  $$R_{\max} = L_1 + L_2$$
  Occurs when the elbow is fully straight ($\theta_2 = 0^\circ$).
- **Inner Bound ($R_{\min}$)**:
  $$R_{\min} = |L_1 - L_2|$$
  Occurs when the elbow is fully folded back ($\theta_2 = 180^\circ$).

The reachable workspace area forms a ring or **annulus**:
$$\mathcal{W} = \{ (x,y) \in \mathbb{R}^2 \mid R_{\min} \leq \sqrt{x^2 + y^2} \leq R_{\max} \}$$

---

## Kinematic Singularities

A **singular configuration** occurs when the robot loses one or more degrees of freedom, meaning it cannot move in specific directions:
- **Boundary Singularity**: Occurs at the outer boundary ($r = R_{\max}$) or inner boundary ($r = R_{\min}$). The arm is fully extended or folded, making it impossible to move radially outwards/inwards.
- **Internal Singularity**: Occurs when joint axes align, collapsing the Jacobian matrix rank.

---

## Numerical Clamping and Guarding

When a target pose falls outside the reachable workspace:
- The argument to the inverse kinematics cosine calculation exceeds the domain $[-1, 1]$:
  $$\cos(\theta_2) = \frac{x^2 + y^2 - L_1^2 - L_2^2}{2 L_1 L_2} \notin [-1, 1]$$
- Passing this out-of-domain value directly into `arccos()` will cause a **domain error**, returning `NaN` (Not a Number).
- To prevent solver crashes, robust solvers apply clamping using `np.clip(cos_theta2, -1.0, 1.0)`. This forces the robot to extend fully towards unreachable targets rather than crashing.
