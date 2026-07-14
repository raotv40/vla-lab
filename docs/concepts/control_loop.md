# Control Loop

A **Control Loop** is a continuous feedback cycle that reads system sensors, computes control commands, updates actuators, and allows a physical system to maintain state variables at a desired setpoint.

---

## Block Diagram and Signal Flow

```text
                  ┌─────────┐   Control   ┌─────────┐
 Setpoint (r) ──> │ Sum (e) │ ── Command ─>│  Plant  │ ───> Output (y)
                  └─────────┘    u(t)     └─────────┘
                       ▲                       │
                       │     Sensor Reading    │
                       └─────── (Feedback) ────┘
```

1. **Reference Input ($r$)**: The target setpoint (e.g. joint position $\theta_d = 1.0\,\text{rad}$).
2. **Measured Output ($y$)**: The current state variable read by sensors (e.g. encoder reading $\theta = 0.8\,\text{rad}$).
3. **Tracking Error ($e$)**: Calculated as the algebraic difference:
   $$e = r - y$$
4. **Controller**: Uses the error signal to compute command outputs (e.g. PID: $u = P + I + D$).
5. **Actuator**: Translates command signals into physical forces/torques (e.g., motor driver converting command voltage to torque).
6. **Plant**: The physical robot arm and environment obeying Newtonian physics (accelerating under motor torque, friction, and gravity).

---

## Loop Execution Frequency

The execution speed (sampling frequency) of the control loop is critical:
- In industrial robot arms, joint control loops run at high frequencies (e.g. **500 Hz to 2 kHz**).
- If the loop frequency is too slow, the latency between reading a sensor and updating the motor torque will cause phase lag, rendering the system unstable and causing violent oscillations.
