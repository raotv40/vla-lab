# Inverse Kinematics Verification

**Inverse Kinematics Verification** is the process of confirming that calculated joint angles correctly place the robot's end-effector at the desired target coordinate.

---

## The Verification Loop

Verification is performed by closing the kinematics loop. Joint angles solved via Inverse Kinematics are plugged back into the Forward Kinematics equations:

```text
  Target Coordinate (x_target, y_target)
            │
            ▼
   [ Inverse Kinematics ]
            │
            ▼
    Joint Angles (\theta_1, \theta_2)
            │
            ▼
    [ Forward Kinematics ]
            │
            ▼
  Actual Position (x_actual, y_actual)
            │
            ▼
      [ Subtraction ] ──> Error = Target - Actual ≈ 0
```

For a planar 2-link arm:
1. Solve joint angles $(\theta_1, \theta_2)$ for target coordinate $(x_t, y_t)$.
2. Calculate reconstructed position:
   - $x_a = L_1 \cos(\theta_1) + L_2 \cos(\theta_1 + \theta_2)$
   - $y_a = L_1 \sin(\theta_1) + L_2 \sin(\theta_1 + \theta_2)$
3. Calculate errors:
   - $e_x = x_t - x_a$
   - $e_y = y_t - y_a$

---

## Numerical Roundoff Error

Because analytical IK equations are exact closed-form solutions, the mathematical error is zero:
$$e_x = 0, \quad e_y = 0$$
In code, calculations run on CPU registers using standard double-precision floating-point formats (`float64`). Small roundoff tolerances on the order of:
$$\epsilon \approx 10^{-16}\,\text{meters}$$
occur due to machine precision limitations (machine epsilon). Any error larger than this indicates a math logic bug in the solver implementation.
