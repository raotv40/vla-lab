# Proportional Controller (P Controller)

A **Proportional (P) Controller** is the simplest form of feedback control. It calculates a control output that is directly proportional to the current tracking error.

---

## Proportional Law

The control command $u(t)$ is computed as:
$$u(t) = K_p \cdot e(t)$$

Where:
- **$e(t)$**: The current tracking error ($r(t) - y(t)$).
- **$K_p$**: The **Proportional Gain**, a positive tuning coefficient.

---

## Effect of Proportional Gain ($K_p$)

The gain coefficient $K_p$ determines how aggressively the controller reacts to a given error signal:

- **High $K_p$ (Aggressive Control)**:
  - The robot reacts quickly and moves faster toward the target.
  - Higher likelihood of overshooting the target.
  - Can cause oscillations and instability if tuned too high.
  
- **Low $K_p$ (Gentle Control)**:
  - The robot reacts gently and moves smoothly.
  - It takes longer to reach the target.
  - Higher system stability, but sluggish response.

---

## Limitations: Steady-State Error

A pure proportional controller cannot eliminate steady-state error (offset) when the system experiences constant external disturbances, such as gravity or friction.

For example, when holding a robotic arm against gravity, a non-zero error is required to generate the torque $u(t) = K_p \cdot e(t)$ needed to balance gravity. If the error were zero, the control torque would also be zero, and the arm would sag. To eliminate this steady-state error, we must combine proportional control with an **Integral (I)** term, forming a PI or PID controller.
