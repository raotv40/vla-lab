# Integral Control (I Control)

**Integral Control** is a feedback control scheme where the control action is proportional to the accumulated sum (integral) of past tracking errors over time:
$$u(t) = K_i \int_{0}^{t} e(\tau) d\tau$$

---

## Eliminating Steady-State Error

While a Proportional controller experiences a steady-state offset ($e_{\text{ss}}$) when fighting constant disturbance forces like gravity, the Integral term eliminates this error:
- If a steady-state offset remains, the integral term continuously accumulates this offset:
  $$\text{Integral Accumulator} \leftarrow \text{Integral Accumulator} + e \cdot \Delta t$$
- The accumulated command torque grows larger and larger until it overcomes the disturbance force.
- The control command will only stop changing when the error is driven to exactly **zero**.

---

## The Cost: Phase Lag and Overshoot

Because the integral term relies on the *accumulation of past errors*, it introduces a **phase lag** in the controller's response:
- Even after the system crosses the desired setpoint (where error changes sign), the accumulated integral history remains large and positive.
- This positive history continues to push the system forward past the setpoint, leading to increased **overshoot** and **oscillations**.

---

## Integral Windup & Clamping Protection

If a robot joint is physically blocked or the actuators saturate, the error will remain non-zero for a long time. The integral term will build up to an extremely large value (windup). Once the block is removed, the controller will output a dangerously large torque, resulting in massive overshoot or hardware damage.

### Solution: Clamping (Anti-Windup)
To prevent this, the integral accumulator must be restricted to a maximum threshold:
```python
# Discretized accumulation with anti-windup clamping
integral_accumulator += error * dt
integral_accumulator = np.clip(integral_accumulator, -INTEGRAL_MAX, INTEGRAL_MAX)
```
This forces the integrator to deactivate once the controller output reaches physical actuator saturation limits.
