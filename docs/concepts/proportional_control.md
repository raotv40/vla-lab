# Proportional Control (P Control)

**Proportional Control** is a feedback control scheme where the control action is directly proportional to the current tracking error:
$$u(t) = K_p e(t)$$

---

## Physical Analogy: The Virtual Spring

Proportional control acts exactly like a physical spring attached between the robot joint's actual position and the target setpoint:
- **Hooke's Law**: $F = -k \cdot x$
- In P-control, $u = K_p \cdot (r - y)$.
- The proportional gain $K_p$ represents the **spring stiffness** ($k$).
- A higher $K_p$ behaves like a stiffer spring, pulling the system toward the target with greater force as the distance increases.

---

## Effects of Proportional Gain ($Kp$)

1. **Rise Time**: Increasing $K_p$ increases initial torque, resulting in faster acceleration and a shorter rise time.
2. **Overshoot & Oscillation**: Because a high $K_p$ behaves like a stiff, undamped spring, the inertia of the system causes it to shoot past the target (overshoot) and oscillate back and forth.
3. **Steady-State Offset**: If the system is subject to a constant disturbance force (such as gravity or friction), P-control cannot drive the error to zero. An offset remains:
   $$e_{\text{ss}} = \frac{F_{\text{disturbance}}}{K_p}$$
   Because the spring force ($K_p \cdot e$) must exactly balance the disturbance force ($F_{\text{disturbance}}$) at equilibrium, the error $e$ cannot be zero.
