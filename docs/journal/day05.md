# Day 5 Journal: Controllers, Feedback Control and Proportional Control

- **Date**: 2026-07-10
- **Author**: Vishrao
- **Milestone**: Day 5 of VLA Learning Lab

---

## Objectives
1. Introduce the fundamentals of robot control loops (Sense-Think-Act).
2. Distinguish between Open-Loop and Closed-Loop (Feedback) systems.
3. Understand the mathematical definition of Tracking Error.
4. Implement the structure of a Proportional (P) controller loop with gain ($K_p$).
5. Document prediction exercises on proportional gain tuning.

---

## Concepts Learned
- **Controller**: The computational block in a control loop that calculates correction inputs (torques).
- **Feedback**: Feeding back the system's output state to calculate real-time error corrections.
- **Error**: The signal driving the controller: $e(t) = r(t) - y(t)$.
- **Proportional Control**: An algorithm where corrective control is directly proportional to current error: $u(t) = K_p \cdot e(t)$.
- **Gain ($K_p$)**: The proportionality constant scaling the error signal.

---

## Theory
Robotic feedback controllers regulate actuator inputs in a continuous loop:

$$u(t) = K_p \cdot (r(t) - y(t))$$

In a physical joint space, the error is the difference between target angle and actual joint angle. The proportional control law behaves like a virtual torsion spring pulling the joint toward the setpoint.

---

## Experiments

### Experiment 5.1: Proportional Control Loop Structure
- **Setup**: Initialized `Reacher-v5` and ran a 50-step loop applying a constant torque action $\mathbf{a} = [0.1, 0.0]$, verifying the control loop and parameter structure.
- **Goal**: Establish the closed-loop control structure template.

---

## Exercise Predictions

Today we analyzed the theoretical impact of the proportional gain ($K_p$):

| Question | Prediction |
| :--- | :--- |
| **What happens if $K_p = 2.0$?** | The controller reacts aggressively, moving the arm joints faster. However, it is highly likely to overshoot the target and oscillate before settling (or become unstable). |
| **What happens if $K_p = 0.1$?** | The controller reacts gently, steering the joints smoothly toward the target. The system remains highly stable but converges slowly. |

> [!IMPORTANT]
> **Physical Caveat**: In today's lab code (`lab09_simple_controller.py`), the controller is structured with a parameter `Kp = 0.1` but the torque action is held constant at `[0.1, 0.0]`. Changing `Kp` in the script has **no visible effect** on the simulation yet. In tomorrow's lab, we will replace the static action with a feedback command derived from observations and scaled by $K_p$.

---

## Open Loop vs Closed Loop

We compared both control frameworks:

| Feature | Open-Loop | Closed-Loop (Feedback) |
| :--- | :--- | :--- |
| **Sensors** | Not required | Encoders / Cameras required |
| **Disturbance Rejection** | Fails (ignores offsets) | Succeeds (corrects errors) |
| **Adaptability** | None (Static assumed path) | Dynamic correction |

---

## Commands Used
```powershell
# Run the simple controller structure lab
python week01/lab09_simple_controller.py
```

---

## Issues Encountered
- **Issue**: Standard visual render commands (`render_mode="human"`) failed to run on headless development targets.

---

## Solutions
- Integrated try-except exception blocks inside `lab09_simple_controller.py` to automatically fall back to headless simulation (`render_mode=None`) when visual display drivers are absent.

---

## Glossary & Interview Q&A Links
- Day 5 glossary additions documented in [docs/glossary.md](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/glossary.md).
- Day 5 interview guide additions documented in [docs/interview_questions.md](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/interview_questions.md).

---

## Lessons Learned
- Proportional control acts as a basic linear spring model.
- Model-based calculations or integral actions are required to eliminate steady-state error under persistent gravity loads.

---

## Reflection
Structuring a control loop before connecting physical observation errors prevents debugging confusion. Understanding the scaling effect of $K_p$ is fundamental to tuning any robotics pipeline.

---

## Next Steps
In tomorrow's lab, map the Reacher-v5 observation vector to track joint target angles and execute a complete proportional feedback control loop.
