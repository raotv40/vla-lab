# Feedback Control

**Feedback Control** (also known as Closed-Loop Control) is a control strategy where the control action depends directly on measurements of the system's output (feedback) to regulate state variables toward a desired setpoint.

---

## Open-Loop vs. Closed-Loop Control

| Characteristic | Open-Loop Control | Closed-Loop (Feedback) Control |
| :--- | :--- | :--- |
| **Feedback Path** | None (no sensor input) | Continuous feedback loop from sensors |
| **Error Correction**| Cannot correct for errors or disturbances | Actively calculates and minimizes error |
| **Disturbance Rejection**| Poor (disturbances skew output) | High (can reject external noise/gravity) |
| **System Stability** | Inherently stable (no feedback oscillations)| Can become unstable if gains are tuned poorly |
| **Examples** | Washing machine timer, toaster | Cruise control, drone autopilot, joint motor PID |

---

## Block Diagram

```text
               ┌────────────┐   Control   ┌─────────┐
 Setpoint ───> │ Controller │ ── Command ─>│  Plant  │ ───> Output (y)
               └────────────┘             └─────────┘
                      ▲                        │
                      └────── sensor feedback ─┘
```

---

## The Role of Feedback in Robotics

Robotic joints use feedback control to achieve precise trajectories:
- **Sensors**: Encoders measure joint position ($\theta$) and joint velocity ($\dot{\theta}$).
- **Disturbance**: Friction, payload mass changes, and gravity apply variable torques that cannot be predicted in advance.
- **Control action**: Feedback controllers dynamically adjust motor current (joint torque) to match target trajectories regardless of these disturbances.
