# Oscillation

**Oscillation** is the repetitive, periodic fluctuation of a system's output variable back and forth around its target setpoint or equilibrium state.

---

## Types of Oscillations in Control Systems

1. **Undamped Oscillation**: The system oscillates back and forth at a constant amplitude forever (typical of an undamped mass-spring system, $\zeta = 0$).
2. **Underdamped Oscillation**: The system oscillates around the setpoint, but the amplitude decay is exponential over time ($0 < \zeta < 1$).
3. **Critically Damped / Overdamped**: The system returns to the setpoint smoothly without any oscillation ($\zeta \geq 1$).

---

## Causes of Oscillations in Robotics

- **Stiffness vs. Damping Imbalance**: High proportional gain $K_p$ (stiffness) relative to derivative gain $K_d$ (damping).
- **Integral Windup**: Oversaturated integral accumulators continuously over-correcting back and forth.
- **Sensor Latency**: Delay between joint position measurement and actuator torque updates. If a motor receives feedback commands late, it applies correction torques in the wrong direction, feeding energy into the oscillation and causing instability.

---

## Control Solutions

Oscillations are minimized by tuning for a target **damping ratio** ($\zeta \approx 0.707$ for fast settling with minimal overshoot, or $\zeta = 1.0$ for critical damping). In software, this is achieved by increasing derivative gain $K_d$ or implementing low-pass filters to reduce sensor noise delays.
