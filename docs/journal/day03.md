# Day 3 Journal: Reward, Episodes, Actions and Learning Fundamentals

- **Date**: 2026-07-03
- **Author**: Vishrao
- **Milestone**: Day 3 of VLA Learning Lab

---

## Objectives
1. Explore reward design and joint dynamics under passive action vectors.
2. Analyze the components of MDP transition steps (observations, rewards, termination/truncation flags).
3. Investigate the differences between episode termination and truncation.
4. Set up and run Gymnasium's `Reacher-v5` environment with a passive controller.

---

## Theory
Gymnasium transitions are represented as:
$$\left(s_t, a_t, r_t, s_{t+1}, \text{terminated}, \text{truncated}\right)$$

In the Reacher environment, the reward is configured to penalize both distance to target and excessive joint torques:
$$\text{reward} = -d_{\text{fingertip, target}} - \|\mathbf{a}_t\|^2$$

By applying passive control ($\mathbf{a}_t = [0.0, 0.0]$), we isolate the gravity-driven displacement and measure the raw distance-based reward signal.

---

## Commands Used
```powershell
# Run the reward and episode simulation lab
python week01/lab06_reward_episode.py
```

---

## Experiments

### Experiment 3.1: Passive Joint Movement and Reward Accumulation
- **Setup**: Initialized `Reacher-v5`, applied constant `[0.0, 0.0]` actions for 100 steps.
- **Goal**: Observe joint displacement under gravity and verify the negative distance reward accumulation.

---

## Observations
1. **Passive Return**: Applying zero torque led to a cumulative return of $-7.421$ over 50 steps.
2. **Episode Length**: The episode was truncated exactly at Step 49 (totaling 50 steps) because Reacher-v5 caps time horizons at 50 steps by default.
3. **Gravity Acceleration**: The step reward decreased slightly from $-0.148$ to $-0.149$ over the episode, indicating that the arm sagged slightly away from the target center due to gravity.

---

## Screenshots Placeholder

![Day 3 Passive Reacher-v5 Reward Curve](../../assets/day03_reward_plot.png)

---

## Issues Encountered
- **Issue**: Attempting to use `Reacher-v4` threw deprecation warnings encouraging the use of `Reacher-v5`.

---

## Solutions
- Used `gym.make("Reacher-v5")` to utilize the latest codebase which removes redundant zero-value dimensions in the observation space, ensuring cleaner training.

---

## Interview Questions
- **Q**: Explain the difference between `terminated` and `truncated` in Gymnasium.
  - **A**: `terminated` indicates the agent reached an absorbing goal or failure state defined by the task MDP. `truncated` means the episode was forced to end due to an external budget/time limit.

---

## Glossary Updates
- **Reward**: Scalar feedback indicating immediate action utility.
- **Episode**: Complete interaction sequence from reset to end.
- **Return**: Sum of cumulative rewards obtained over an episode.
- **Transition**: Step tuple $(s_t, a_t, r_t, s_{t+1}, \text{done})$.
- **Termination**: End of episode due to natural MDP task completion.
- **Truncation**: End of episode due to time limits.

---

## Lessons Learned
- Always distinguish between termination and truncation in RL setups to ensure correct target value calculation during bootstrap updates.
- Keep reward functions simple and computationally efficient.

---

## Reflection
Investigating passive dynamics and reward functions provides a deep, intuitive understanding of the environment's state space before introducing complex training loops.

---

## Next Steps
Prepare for Week 2 controllers (joint tracking, PID controllers, and gravity compensation).
