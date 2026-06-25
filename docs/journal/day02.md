# Day 2 Journal: Observation, Action and Policy Fundamentals

- **Date**: 2026-06-26
- **Author**: Vishrao
- **Milestone**: Day 2 of VLA Learning Lab

---

## Objectives
1. Interface with Gymnasium's `Reacher-v4` environment.
2. Analyze and verify the 10-dimensional observation space structure.
3. Understand the 2-dimensional torque action space.
4. Implement a closed-loop feedback policy using Transpose Jacobian control to reach target coordinates.

---

## Theory
Gymnasium provides a standard loop where agents read observations and apply continuous actions. In `Reacher-v4`:
- **Observation Space**: 10D vector representing joint cosines/sines, target coordinate, angular velocities, and relative tip-to-target distance.
- **Action Space**: 2D torque vector bounded between $[-1.0, 1.0]$.
- **Transpose Jacobian Control**: Uses forward kinematics to relate joint angles to end-effector coordinates. By applying a virtual force $F = K_p(e) - K_d(v)$ pulling the fingertip to the target, we map it to joint torques:
  $$\tau = J^T F$$
  This allows closed-loop feedback without complex inverse kinematics.

---

## Commands Used
```powershell
# Run Gymnasium Reacher integration with random actions
python week01/lab02_reacher.py

# Run observation deconstruction & kinematics checks
python week01/lab03_observation.py

# Run joint torque response test
python week01/lab04_actions.py

# Run Transpose Jacobian feedback policy
python week01/lab05_policy.py
```

---

## Experiments

### Experiment 2.1: Random Rollout Baseline
- **Setup**: Evaluated an agent applying random torques.
- **Goal**: Measure average cumulative reward and final distance.

### Experiment 2.2: Forward Kinematics Verification
- **Setup**: Reset the environment, extracted the 10D observations, calculated the fingertip position using forward kinematics, and compared it with the environment's internal error coordinates.

### Experiment 2.3: Closed-Loop Tuning
- **Setup**: Implemented the Transpose Jacobian controller and evaluated with different gain settings:
  1. $Kp = 20.0, Kd = 1.0$ (Proposed default)
  2. $Kp = 100.0, Kd = 0.1$ (High proportional, low derivative)

---

## Observations
1. **Experiment 2.1**: The random policy resulted in erratic arm movements, a low cumulative reward (approx. $-4.5$), and failed to reach the target, leaving a final target distance of $0.22\text{m}$.
2. **Experiment 2.2**: The forward kinematics calculation matched the observed target error vector exactly (absolute difference $<10^{-16}$), validating our trigonometric formulas.
3. **Experiment 2.3**: 
   - With $Kp = 20.0, Kd = 1.0$, the arm reached the target smoothly, reducing the distance from $0.21\text{m}$ to $0.009\text{m}$ in 40 steps, obtaining a high reward.
   - With $Kp = 100.0, Kd = 0.1$, the arm accelerated too fast, overshot the target, and oscillated wildly back and forth.

---

## Screenshots Placeholder

![Day 2 Simulation Response - Target distance decay over time](../../assets/day02_controller_response.png)

---

## Issues Encountered
- **Issue**: Initial forward kinematics equations yielded a mismatch with the target error coordinates.
- **Cause**: Assumed the elbow angle ($\theta_2$) was absolute in world space. In MuJoCo, the elbow joint is a child of the shoulder body, making its angle relative to the shoulder joint ($\theta_1$).

---

## Solutions
- Corrected the absolute angle of the second link to be $\theta_1 + \theta_2$, modifying the equations to:
  - $x_{\text{fingertip}} = l_1 \cos(\theta_1) + l_2 \cos(\theta_1 + \theta_2)$
  - $y_{\text{fingertip}} = l_1 \sin(\theta_1) + l_2 \sin(\theta_1 + \theta_2)$
  This resolved the mismatch.

---

## Interview Questions
- **Q**: Why command torques instead of joint angles?
  - **A**: Real motors apply torques. Command torque forces policies to respect physical inertia, mass, and dynamics, ensuring better sim-to-real transfer.

---

## Glossary Updates
- **Observation Space**: Description of environment state.
- **Action Space**: Limits and structure of control inputs.
- **Forward Kinematics**: Mapping joint space to Cartesian space.
- **Jacobian Matrix**: Relating joint velocities to Cartesian velocities.
- **Transpose Jacobian Control**: Projecting Cartesian force into joint torques.
- **Closed-Loop Control**: Adjusting actions based on state feedback.

---

## Lessons Learned
- Verify coordinate frames and joint hierarchies before writing kinematics code.
- Closed-loop control provides immediate stability; derivative gain is essential to damp oscillations.

---

## Reflection
Robotics problems that seem complex (like moving an arm to an arbitrary coordinate) can be solved elegantly using classical vector calculus (Jacobians) and physics analogies (virtual spring-dampers) rather than jumping straight to deep neural networks.

---

## Next Steps
Proceed to Week 2 of the VLA Lab and learn about PID control configurations, Operational Space Control (OSC), and dynamic gravity compensation.
