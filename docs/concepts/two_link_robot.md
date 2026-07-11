# Two-Link Planar Robot

A **Two-Link Planar Robot** is the fundamental serial manipulator structure used in robotics research and education to demonstrate kinematics, dynamics, and control algorithms.

---

## Kinematic Schematic

The 2-link arm operates in a single 2D plane:

```text
                  Link 2 (L2)
                o===========* (x_tip, y_tip) End-Effector
               /  \
              /    \ Elbow Joint (\theta_2 relative to Link 1)
             /
            / Link 1 (L1)
           /
          / \
   Base  o   \ Shoulder Joint (\theta_1 relative to X-axis)
  (0,0)
```

- **L1**: Length of the proximal link (shoulder link).
- **L2**: Length of the distal link (elbow link).
- **$\theta_1$**: Angle between Link 1 and the positive X-axis.
- **$\theta_2$**: Angle between Link 2 and the extension of Link 1.

---

## Equations of Motion & Kinematics

1. **Forward Kinematics**:
   - $x = L_1 \cos(\theta_1) + L_2 \cos(\theta_1 + \theta_2)$
   - $y = L_1 \sin(\theta_1) + L_2 \sin(\theta_1 + \theta_2)$
2. **Degrees of Freedom**:
   - The arm has **2 Degrees of Freedom** ($2\,\text{DoFs}$), enabling control of coordinates $(x, y)$ within its planar workspace.
3. **Usage in Reacher-v5**:
   - `Reacher-v5` uses a two-link planar configuration where joint motor torques act as actions to drive the fingertip to target coordinates.
