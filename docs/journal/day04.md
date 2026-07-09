# Day 4 Journal: Random Policy, Exploration and Policy Comparison

- **Date**: 2026-07-09
- **Author**: Vishrao
- **Milestone**: Day 4 of VLA Learning Lab

---

## Objectives
1. Implement and evaluate a Random Policy on the `Reacher-v5` environment.
2. Implement and evaluate a Fixed Action Policy on the `Reacher-v5` environment.
3. Compare the episode returns, average step rewards, and final target distances of both policies.
4. Analyze the fundamental trade-off between Exploration and Exploitation.

---

## Theory Learned
- **Policy ($\pi$)**: A decision-making function mapping states (or observations) to actions.
- **Random Policy**: A policy that samples actions uniformly at random from the action space. This represents maximum exploration (gathering new environment information) but fails to utilize observations (exploitation) to reach the goal.
- **Fixed Policy**: An open-loop control scheme that applies a constant action (e.g. constant torque profile $\mathbf{a} = [0.1, 0.0]$) at every step, completely ignoring state feedback.
- **Exploration vs Exploitation**: The classic reinforcement learning trade-off. Agents must explore to discover high-reward state-action pairs, but must exploit what they have learned to maximize cumulative rewards.

---

## Experiments

### Experiment 4.1: Random Policy Evaluation
- **Setup**: Evaluated an agent sampling actions uniformly from the Reacher-v5 action space for 50 steps.
- **Goal**: Establish a baseline return and observe joint movements.

### Experiment 4.2: Fixed Policy Evaluation
- **Setup**: Evaluated an agent applying a constant joint torque action $\mathbf{a} = [0.1, 0.0]$ (slight positive torque to joint 1, zero torque to joint 2) for 50 steps.
- **Goal**: Compare performance metrics against the random baseline.

---

## Results

### Random Policy Results
- **Final Episode Return**: $-36.620$
- **Average Step Reward**: $-0.732$
- **Final Target Distance**: $0.1874\text{m}$
- **Behavior**: The robotic arm wiggled aimlessly near its starting position, showing high kinetic jitter and failing to reach the target coordinates.

### Fixed Policy Results
- **Final Episode Return**: $-11.365$
- **Average Step Reward**: $-0.227$
- **Final Target Distance**: $0.2078\text{m}$
- **Behavior**: The arm swung smoothly in a circular arc due to the constant torque applied to the shoulder joint, but because it was open-loop, it did not adjust its path to reach the randomized target.

---

## Observations
1. **Return Comparison**: The Fixed Policy achieved a significantly higher episode return ($-11.365$) than the Random Policy ($-36.620$) because the random policy applied opposing forces at every step, wiggling aimlessly, whereas the fixed policy swept a larger area and stayed closer to the origin (where the target was located) on average.
2. **Target Distance**: Despite the fixed policy having a higher cumulative reward, its final distance to target ($0.2078\text{m}$) was worse than the random policy's final distance ($0.1874\text{m}$) in this particular rollout. This highlights that open-loop fixed policies cannot guarantee task success under randomized target initializations.
3. **Exploration vs. Exploitation**: A random policy represents pure exploration, while a fixed policy represents static open-loop behavior. To solve the Reacher task, the agent must be closed-loop: exploiting observations of target error to apply directed joint torques (as seen in Lab 5's Transpose Jacobian policy).

---

## Screenshots Placeholder

![Day 4 Policy Comparison Summary](../../assets/day04_policy_comparison.png)

---

## Commands Used
```powershell
# Run the random policy evaluation lab
python week01/lab07_random_policy.py

# Run the comparative policy evaluation lab
python week01/lab08_compare_policies.py
```

---

## Issues Encountered
- **Issue**: Visual window rendering failed on headless servers due to lacking display libraries (`GLFW`).

---

## Solutions
- Implemented try-except exception handling in `lab07_random_policy.py` and `lab08_compare_policies.py` to catch rendering errors and automatically fall back to headless simulation (`render_mode=None`).

---

## Glossary Updates
Day 4 glossary terms added to [docs/glossary.md](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/glossary.md):
- **Agent**
- **Episode Return**
- **Exploitation**
- **Exploration**
- **Fixed Policy**
- **Random Policy**

---

## Interview Questions
Day 4 interview questions added to [docs/interview_questions.md](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/interview_questions.md):
- **Beginner**: Policy definition and Random vs Fixed policies.
- **Intermediate**: Exploration/Exploitation definitions and Reacher-v5 failure modes.
- **Advanced**: Infinite-horizon returns and the role of the discount factor ($\gamma$).

---

## Lessons Learned
- Baseline policies (random/fixed) are essential to establish upper bounds of error and lower bounds of performance.
- Open-loop controllers are highly sensitive to initial conditions and target variations.

---

## Reflection
Robotics experiments require thorough baselining. Comparing a random agent with a fixed agent makes the value of closed-loop controllers (and later, learned neural network policies) immediately clear.

---

## Next Steps
Wrap up Week 1 of the VLA Lab and prepare for Week 2: Robotic Control Frameworks (PID, joint tracking, Operational Space Control).
