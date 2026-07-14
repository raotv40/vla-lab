# PID Tuning

**PID Tuning** is the process of selecting the gains ($K_p$, $K_i$, $K_d$) of a PID controller to achieve a desired step response while maintaining stability, minimizing overshoot, and reducing settling time.

---

## 1. Manual Tuning Strategy

Manual tuning is the most common approach for robotic system setup:

| Step | Action | Objective |
| :--- | :--- | :--- |
| **Step 1** | Set $K_i = 0$ and $K_d = 0$. | Clear integrator and derivative terms. |
| **Step 2** | Increase $K_p$ gradually. | Stop when the system responds quickly but exhibits constant oscillation. |
| **Step 3** | Increase $K_d$ gradually. | Damps the oscillations and eliminates overshoot. |
| **Step 4** | Increase $K_i$ gradually. | Eliminates any steady-state offsets caused by gravity or friction. |

---

## 2. Ziegler-Nichols Tuning Rule

Ziegler-Nichols is a classic heuristic tuning method based on the system's stability boundary:

1. Set $K_i = 0$ and $K_d = 0$.
2. Increase $K_p$ until the system exhibits sustained, constant oscillation. This gain is the **Ultimate Gain** ($K_u$), and the oscillation period is the **Ultimate Period** ($P_u$).
3. Apply the tuning formulas based on $K_u$ and $P_u$:

| Controller | $K_p$ | $K_i$ | $K_d$ |
| :--- | :--- | :--- | :--- |
| **P** | $0.5 K_u$ | — | — |
| **PI** | $0.45 K_u$ | $0.54 K_u / P_u$ | — |
| **PID** | $0.6 K_u$ | $1.2 K_u / P_u$ | $0.075 K_u \cdot P_u$ |

---

## 3. Industrial Tuning Considerations

Heuristic tuning methods like Ziegler-Nichols often yield highly oscillatory step responses. In real industrial arms, controllers are tuned for **critical damping** ($\zeta = 1.0$), ensuring zero overshoot to prevent the robot tool from colliding with components.
