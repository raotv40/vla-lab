# Day 7 Journal: Robot State, Observation Decoding and Kinematics Fundamentals

- **Date**: 2026-07-10
- **Author**: Vishrao
- **Milestone**: Day 7 of VLA Learning Lab

---

## Objectives
1. Understand the difference between true physical Robot State and observable environmental features.
2. Decode Reacher-v5 observations dynamically and examine reset characteristics.
3. Compare sequential observations over a controlled trajectory to isolate joint position dynamics.
4. Establish the basics of Degrees of Freedom, Kinematic Chains, and Forward/Inverse Kinematics.

---

## Theory Learned
- **Robot State**: The exact coordinates ($\mathbf{q}$) and velocities ($\dot{\mathbf{q}}$) representing physical mechanical dimensions. For Reacher, this is a 4D vector: $[\theta_1, \theta_2, \dot{\theta}_1, \dot{\theta}_2]^T$.
- **Observation vs. State**: True state represents full physical truth (internal MuJoCo values), whereas observations are feature engineered outputs designed for optimization (sine/cosine coordinates, Cartesian errors).
- **Degrees of Freedom**: The number of independent joints (variables) specifying joint state. Reacher has 2 revolute joints, so $2\,\text{DoFs}$.
- **Kinematic Chain**: Series of rigid link linkages connected by joints.
- **Forward Kinematics**: Calculating Cartesian tip $(x, y)$ from joint angles:
  - $x_{\text{tip}} = l_1 \cos(\theta_1) + l_2 \cos(\theta_1 + \theta_2)$
  - $y_{\text{tip}} = l_1 \sin(\theta_1) + l_2 \sin(\theta_1 + \theta_2)$
- **Inverse Kinematics**: Working backward to find joint angles from desired Cartesian coordinates.

---

## Experiments

### Experiment 7.1: Decode Observation on Reset (Exercise 1)
- **Setup**: Evaluated initial observations from reset across seeds.
- **Commands**: `python week01/lab16_decode_observation.py`
- **Results**:
  - **Observation Shape**: `(10,)` Box space.
  - **Values**: Cosine and sine projections of shoulder/elbow joints, target coordinate position, joint velocities, and fingertip error vector.
  - **What changes after reset**: The target coordinates ($x_{\text{target}}, y_{\text{target}}$ at indices 4-5) and the target error vectors (indices 8-9) change completely, because the target sphere is randomized to a new setpoint. The velocities are reset to zero.

### Experiment 7.2: Sequential State Comparison (Exercise 2)
- **Setup**: Executed a 5-step loop under a torque command sequence `[0.1, -0.1]`.
- **Commands**: `python week01/lab17_observation_comparison.py`
- **Results**:
  - **Values that change immediately**: Velocities (indices 6-7) respond instantly to input torque forces (showing large deltas like $+0.194$).
  - **Values that change slowly**: Joint angles (indices 0-3) change slowly and incrementally, as position is the integral of velocity over time.
  - **Values representing joint motion**: Joint sines/cosines (indices 0-3) and joint velocities (indices 6-7).

---

## Exercise 3: Closed-Loop Control Signal Flow

The control pipeline sequence behaves as follows:

```text
  Joint Angles (q1, q2)
          │
          ▼
  Forward Kinematics (FK)
          │
          ▼
  End-Effector Position (x_tip, y_tip) <──> Target Position (x_target, y_target)
          │
          ▼
     Error Vector (e = target - tip)
          │
          ▼
      Controller (Feedback) ────> Actuator Joint Torques (u) ────> Robot Motors
```

### Why a controller requires accurate robot state information:
If state information is noisy, incorrect, or lagged:
1. The calculated fingertip coordinates from FK will be wrong.
2. The calculated error vector will be incorrect.
3. The feedback controller will apply restorative torque inputs at the wrong time (e.g. accelerating after the target is passed).
4. This turns restorative forces into destabilizing forces, resulting in target overshoot, severe oscillations, and system instability.

---

## Open Loop vs Closed Loop Comparison

| Metric | Classical Control Pipeline | Reinforcement Learning Pipeline | VLA Pipeline |
| :--- | :--- | :--- | :--- |
| **Primary Input** | Target Cartesian reference / joint states | Continuous state observation vector | Camera frames + Language prompt |
| **Output** | Joint torques | Action commands | Low-level action trajectory |
| **Safety** | Provable stability (Lyapunov/Nyquist) | Empirical validation only | Complex, no safety guarantees |

---

## Commands Used
```powershell
# Decode observation vector
python week01/lab16_decode_observation.py

# Compare sequential observations
python week01/lab17_observation_comparison.py
```

---

## Issues Encountered
- None. Exception handlers gracefully handle terminal displays.

---

## Glossary & Interview Links
- Day 7 glossary additions documented in [docs/glossary.md](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/glossary.md).
- Day 7 interview guide additions documented in [docs/interview_questions.md](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/interview_questions.md).

---

## Lessons Learned
- Joint velocities are direct representations of force acceleration, whereas positions change incrementally as the integral of velocity.
- Accurate state feedback is the bedrock of system stability.

---

## Next Steps
Day 8: Implement the first real feedback controller (PD/spring controller) utilizing state feedback and forward kinematics to drive the end-effector fingertip directly to randomized target coordinates.
