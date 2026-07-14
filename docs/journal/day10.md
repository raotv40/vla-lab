# Day 10 Journal: PID Control and Feedback Systems

- **Date**: 2026-07-14
- **Author**: Vishrao
- **Milestone**: Day 10 of VLA Learning Lab

---

## Objectives
1. Understand the core principles of open-loop vs. closed-loop (feedback) control systems.
2. Implement Proportional (P), Proportional-Integral (PI), and Proportional-Integral-Derivative (PID) feedback control loops in Python.
3. Simulate and analyze joint-space step responses for a robot joint subject to inertia, damping, and gravity.
4. Formulate responses to gain sweeps (tuning Kp, Ki, and Kd) to isolate transient behaviors like rise time, overshoot, oscillation, and steady-state tracking errors.
5. Detail how classical feedback control fits into modern Vision-Language-Action (VLA) architectures.

---

## Feedback Control Overview
A **Feedback Control System** (or Closed-Loop system) continuously monitors the difference between a desired target state (setpoint) and the actual physical output of the plant. It uses this tracking error to adjust the command signals sent to actuators, driving the error to zero and rejecting external disturbances.

---

## Control Loop Diagram

```text
                  ┌─────────────────┐   Control Torque   ┌─────────┐
 Setpoint (r) ──> │ Sum (Error = e) │ ──────────────────>│  Plant  │ ───> Position (y)
                  └─────────────────┘        u(t)        └─────────┘
                           ▲                                  │
                           │         Sensor Encoders          │
                           └────────── (Feedback) ────────────┘
```

---

## P, I, and D Explanation

1. **Proportional Term (P)**: 
   - Law: $u_p = K_p \cdot e$
   - Physical Meaning: Acts like a virtual spring pulling the joint toward the setpoint. It determines responsiveness but suffers from steady-state error under load.
2. **Integral Term (I)**: 
   - Law: $u_i = K_i \int e \cdot dt$
   - Physical Meaning: Acts as an accumulator of past tracking offsets, continuously ramping up motor torque until steady-state error is eliminated.
3. **Derivative Term (D)**: 
   - Law: $u_d = K_d \frac{de}{dt}$
   - Physical Meaning: Acts like a virtual shock absorber. It opposes velocity, applying a predictive brake to suppress overshoot and oscillations.

---

## Lab Results

### Lab 22: Proportional (P) Controller
- **Setup**: Simulated a joint with gravity ($0.5\,\text{N}\cdot\text{m}$) and damping ($1.0\,\text{N}\cdot\text{m}\cdot\text{s}/\text{rad}$) under P-only control.
- **Command**: `python week02/lab22_p_controller.py`
- **Output**:
  ```text
  Kp = 0.5 | Final Position: 0.0000 rad | Steady-State Error: +1.0000 rad
  Kp = 0.8 | Final Position: 0.3702 rad | Steady-State Error: +0.6298 rad
  Kp = 2.5 | Final Position: 0.7901 rad | Steady-State Error: +0.2099 rad
  ```
- **Plot**: Saved to `assets/day10/p_controller.png`

### Lab 23: Proportional-Integral (PI) Controller
- **Setup**: Added an integral accumulator to eliminate steady-state error.
- **Command**: `python week02/lab23_pi_controller.py`
- **Output**:
  ```text
  Ki = 0.00 | SS Error: +0.1807 rad | Overshoot: 15.6%
  Ki = 1.00 | SS Error: +0.0717 rad | Overshoot: 43.5%
  Ki = 3.00 | SS Error: +0.2543 rad | Overshoot: 86.1%
  ```
- **Plot**: Saved to `assets/day10/pi_controller.png`

### Lab 24: Proportional-Integral-Derivative (PID) Controller
- **Setup**: Simulated the full PID controller loop, sweeping $K_d$ to damp out oscillations.
- **Command**: `python week02/lab24_pid_controller.py`
- **Output**:
  ```text
  Kd = 0.0 | Overshoot: 43.5% | Settling Time: 8.00s | SS Error: +0.0717 rad
  Kd = 0.2 | Overshoot: 36.9% | Settling Time: 8.00s | SS Error: +0.0375 rad
  Kd = 0.5 | Overshoot: 28.9% | Settling Time: 6.72s | SS Error: +0.0090 rad
  ```
- **Plot**: Saved to `assets/day10/pid_controller.png`

---

## Exercise Results

### Exercise 1: Tuning Proportional Gain ($Kp$)
- **Action**: Increased $K_p$ from $0.5 \to 0.8 \to 2.5$.
- **Was the response faster?** Yes, because a larger $K_p$ commands higher initial motor torque, accelerating the mass faster and reducing rise time.
- **Did overshoot occur?** Yes, at $K_p = 2.5$, the joint overshot the target setpoint.
- **Was oscillation observed?** Yes, the joint exhibited oscillatory decay around its final equilibrium position.
- **Reasoning**: A P-controller acts like a spring. Higher stiffness ($K_p$) accelerates the system faster, but without damping, the mass's kinetic energy carries it past the target, resulting in overshoot and oscillations. Steady-state offset is reduced but never completely eliminated ($e_{\text{ss}} = T_{\text{gravity}} / K_p$).

---

### Exercise 2: Tuning Integral Gain ($Ki$)
- **Action**: Set $K_p = 3.0$ and increased $K_i$ from $0.0 \to 1.0 \to 3.0$.
- **Did steady-state error reduce?** Yes, under $K_i = 1.0$, the final offset at 8.0s fell from $+0.1807\,\text{rad}$ to $+0.0717\,\text{rad}$ and is heading to zero.
- **Did overshoot increase?** Yes, overshoot increased dramatically from $15.6\% \to 43.5\% \to 86.1\%$.
- **Reasoning**: The integral term integrates error over time, growing the torque command until it cancels gravity. However, this history accumulation introduces a phase lag, continuing to accelerate the system even after it crosses the setpoint, which amplifies overshoot and oscillation.

---

### Exercise 3: Tuning Derivative Gain ($Kd$)
- **Action**: Set $K_p = 3.0$, $K_i = 1.0$, and increased $K_d$ from $0.0 \to 0.2 \to 0.5$.
- **Was the motion smoother?** Yes, the joint approached the setpoint without violent fluctuations.
- **Was overshoot reduced?** Yes, overshoot dropped from $43.5\% \to 36.9\% \to 28.9\%$.
- **Did settling improve?** Yes, the settling time (remaining within 2% of the setpoint) improved from $8.00\,\text{s}$ (unsettled) to $6.72\,\text{s}$.
- **Reasoning**: The derivative term acts like a shock absorber ($u_d = -K_d \cdot v$). It applies a predictive braking force that opposes high velocities as the joint approaches the setpoint, dissipating kinetic energy and accelerating settling.

---

## Where PID Is Used
Classical PID control remains the workhorse of real-world industrial and autonomous robotics:
- **Industrial Robot Arms**: Systems from manufacturers like **ABB**, **FANUC**, **KUKA**, and **Universal Robots** run high-speed PID loops (often cascaded position-velocity-torque loops) on dedicated motor controller boards to achieve sub-millimeter precision.
- **DJI Drones**: Quadcopters use PID loops running at $400\,\text{Hz} - 1\,\text{kHz}$ to calculate rotor speeds based on IMU gyroscope/accelerometer feedback to stabilize flight and hover.
- **Cruise Control**: Automobiles adjust throttle position based on vehicle velocity feedback.
- **Aircraft Autopilot**: Flight control surfaces (ailerons, elevators) are actuated via PID to maintain pitch, roll, and heading setpoints.
- **CNC Machines & Factory Automation**: Servo motors driving gantry axes rely on PID to trace precise tool paths.

---

## PID vs. RL Comparison

| Feature | PID Control | Reinforcement Learning (RL) |
| :--- | :--- | :--- |
| **Model Requirements** | Model-Free (only requires parameter tuning) | Model-Free but requires millions of interactive training steps |
| **Stability Guarantees** | High (validated via linear systems theory) | Low (black-box neural networks; hard to guarantee bounds) |
| **Computational Cost** | Extremely low (few arithmetic operations) | High (requires deep neural network forward passes) |
| **Data Scope** | Single joint error inputs | High-dimensional inputs (pixels, camera images) |
| **Generalization** | Specific to a single setpoint | Learns arbitrary, complex task coordination |

---

## VLA Connection
Modern Vision-Language-Action (VLA) robot architectures do not replace classical controllers; they use them in a **hierarchical pipeline**:

```text
 1. Vision-Language-Action Model (VLA)  [Low Frequency: 5Hz - 20Hz]
    │  (Processes camera pixels and prompt "grab mug" to predict Cartesian target)
    ▼
 2. Motion Planner & Trajectory Generator
    │  (Generates a smooth path profile connecting current pose to target pose)
    ▼
 3. Inverse Kinematics (IK)
    │  (Calculates desired joint angles theta_d for the target path coordinates)
    ▼
 4. PID Controller  [High Frequency: 500Hz - 2kHz]
    │  (Computes joint torques based on encoder feedback to track joint angle setpoints)
    ▼
 5. Motor Drivers & Actuators
    │  (Converts torque commands to physical currents running through joint motors)
    ▼
 6. Robot Arm
```

Classical PID control acts as the safety-critical stabilization layer, handling fast disturbance rejection, while the high-level VLA model handles perception and semantic reasoning.

---

## Commands Used
```bash
# Run P-controller simulation
python week02/lab22_p_controller.py

# Run PI-controller simulation
python week02/lab23_pi_controller.py

# Run PID-controller simulation
python week02/lab24_pid_controller.py
```

---

## Issues Encountered & Solutions
- **Issue**: Proportional gain was too low relative to gravity, causing the joint position to drift into negative values.
- **Solution**: Reduced the gravity torque disturbance to $0.5\,\text{N}\cdot\text{m}$ to keep the step response positive and intuitive.
- **Issue**: Matplotlib display errors on headless environments.
- **Solution**: Explicitly set the non-interactive backend using `matplotlib.use('Agg')` before importing pyplot.

---

## Glossary & Interview Links
- Glossary terms added to [docs/glossary.md](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/glossary.md).
- Q&As added to [docs/interview_questions.md](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/interview_questions.md).

---

## Reflection
PID control bridges classical physics loops with high-level AI models. It demonstrates that precise control requires balancing responsiveness (P), history accumulation (I), and predictive braking (D).

---

## Next Steps
Day 11: Introduction to robot trajectories, velocity profiles, and motion planning.
