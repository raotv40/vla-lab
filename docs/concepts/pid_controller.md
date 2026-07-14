# PID Controller

A **Proportional-Integral-Derivative (PID)** controller is the most widely used feedback control algorithm in industrial and robotic applications. It calculates an error value as the difference between a desired setpoint and a measured process variable and applies a correction based on proportional, integral, and derivative terms.

---

## Continuous Formulation

The continuous control law of a PID controller is:
$$u(t) = K_p e(t) + K_i \int_{0}^{t} e(\tau) d\tau + K_d \frac{de(t)}{dt}$$

Where:
- $u(t)$ is the control output (e.g., motor command, torque, or voltage).
- $e(t) = r(t) - y(t)$ is the tracking error (Setpoint $r$ minus actual state $y$).
- $K_p$ is the Proportional gain.
- $K_i$ is the Integral gain.
- $K_d$ is the Derivative gain.

---

## Discrete Formulation (Code Implementation)

Because microcontrollers and computer loops operate on discrete time intervals $\Delta t$, the continuous equations must be discretized:

1. **Error**:
   $$e_k = r_k - y_k$$
2. **Proportional Term**:
   $$P_k = K_p \cdot e_k$$
3. **Integral Term** (rectangular approximation):
   $$I_k = I_{k-1} + K_i \cdot e_k \cdot \Delta t$$
   *(Note: The integral accumulator is often clamped to prevent integral windup).*
4. **Derivative Term** (finite difference):
   $$D_k = K_d \cdot \frac{e_k - e_{k-1}}{\Delta t}$$
5. **Control Output**:
   $$u_k = P_k + I_k + D_k$$

---

## PID Term Tradeoffs

- **Proportional (P)**: Dictates responsiveness. High $K_p$ speeds up rise time but increases overshoot and oscillation. Cannot eliminate steady-state error under constant disturbances.
- **Integral (I)**: Eliminates steady-state error by accumulating past offsets. High $K_i$ introduces phase lag, leading to larger overshoot and slow settling.
- **Derivative (D)**: Acts as a brake. Predicts future error by looking at the slope, adding damping to suppress overshoot and oscillations. High $K_d$ amplifies high-frequency sensor noise.
