# Day 6 Journal: Deciphering the Reacher-v5 Observation Vector

- **Date**: 2026-07-10
- **Author**: Vishrao
- **Milestone**: Day 6 of VLA Learning Lab

---

## Objectives
1. Interface with Gymnasium's `Reacher-v5` environment observations.
2. Decode the 10-dimensional observation vector into joints, velocities, target positions, and fingertip errors.
3. Perform mathematical verification of observations.
4. Analyze how states evolve dynamically over a trajectory.

---

## Theory
The observation vector contains 10 components in a single `Box` space:
- `obs[0:2]`: Cosine of joint angles ($\cos(\theta_1), \cos(\theta_2)$).
- `obs[2:4]`: Sine of joint angles ($\sin(\theta_1), \sin(\theta_2)$).
- `obs[4:6]`: Target Cartesian coordinates ($x_{\text{target}}, y_{\text{target}}$).
- `obs[6:8]`: Joint angular velocities ($\dot{\theta}_1, \dot{\theta}_2$).
- `obs[8:10]`: Fingertip-to-target distance vector ($x_{\text{target}} - x_{\text{fingertip}}, y_{\text{target}} - y_{\text{fingertip}}$).

Trigonometric identities verify that the angles represent valid unit circle coordinates:
$$\cos^2(\theta) + \sin^2(\theta) = 1.0$$

---

## Experiments

### Experiment 6.1: Parsing and Decoded Printing
- **Setup**: Reset `Reacher-v5` and printed the index-by-index observation breakdown.
- **Commands**: `python week01/lab10_observation_decoder.py`
- **Output**:
  ```text
  Parsed Reacher-v5 Observation Vector:
    obs[0] | cos(theta1)     :  +0.9852 (Shoulder joint angle cosine)
    obs[1] | cos(theta2)     :  +0.9998 (Elbow joint angle cosine)
    obs[2] | sin(theta1)     :  -0.1711 (Shoulder joint angle sine)
    ...
  ```

### Experiment 6.2: Trigonometric Identity Verification
- **Setup**: Verified $\cos^2(\theta) + \sin^2(\theta) = 1.0$ for both revolute joints.
- **Commands**: `python week01/lab11_observation_analysis.py`
- **Output**:
  ```text
  Shoulder Joint: cos^2 + sin^2 = 0.9852^2 + -0.1711^2 = 1.000000
  Elbow Joint:    cos^2 + sin^2 = 0.9998^2 + -0.0175^2 = 1.000000
  ```

---

## Observations
- **Trigonometric Success**: Both joint positions mathematically verified to represent points exactly on the unit circle (error margin $< 10^{-6}$).
- **Joint Separation**: MuJoCo represents the elbow joint relative to the first link, whereas the shoulder joint is represented relative to the origin base frame.

---

## Exercises

### Exercise 2: State Changes under Zero-Torque Control
We ran `lab12_observation_changes.py` with zero torques to observe state evolution:
- **Observations that change most**: Velocities (`obs[6:8]`), cosines/sines of angles (`obs[0:4]`), and target errors (`obs[8:10]`). The arm swings freely under gravity, changing its joint states and fingertip distance continuously.
- **Observations that remain nearly constant**: The target positions (`obs[4:5]`) are completely static during the episode.
- **Reason**: The target coordinate is a fixed task goal initialized on reset. The joint angles and velocities are physical degrees of freedom that change dynamically due to gravity and physics solver integration.

---

## Issues Encountered
- **Issue**: Rending in GUI mode failed on headless test terminals.
- **Solution**: Handled GLFW display errors using try-except fallback to `render_mode=None`.

---

## Glossary & Interview Links
- Glossary terms added to [docs/glossary.md](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/glossary.md): Observation Vector, Observation Space, Feature Vector, Joint Position, Joint Velocity, Target Position.
- Q&As added to [docs/interview_questions.md](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/interview_questions.md).

---

## Lessons Learned
- Verifying the mathematical structure of observation vectors prevents bugs when building feedback equations.
- Target setpoints are static throughout an episode in standard reacher tasks.

---

## Next Steps
Day 6.5: Deepen understanding of continuous Box spaces and trigonometric angle wrap-around representations.
