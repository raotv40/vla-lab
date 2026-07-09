"""
Week 1 - Lab 8: Comparing Random and Fixed Policies in Gymnasium
================================================================

Objectives:
-----------
1. Implement both a Random Policy and a Fixed Action Policy.
2. Run back-to-back evaluations to compare policy performance.
3. Discuss the trade-off between Exploration and Exploitation.
4. Compare the final returns and fingertip-to-target distances.

Theory:
-------
- Random Policy: Samples actions uniformly. Good for exploration, poor for task completion.
- Fixed Policy: Applies a constant action (e.g. constant torque [0.1, 0.0] to joint 1). Represents a simple open-loop action profile.
- Exploration vs Exploitation:
  - Exploration gathers new information but might receive low immediate rewards.
  - Exploitation uses current knowledge to get rewards but fails to learn better actions in unknown environments.

Expected Output:
----------------
A console log for each step under both policies, followed by a final summary table comparing:
- Total Episode Return
- Average Reward per Step
- Final Distance to Target

Exercises:
----------
1. Change the FIXED_ACTION constant to [0.5, -0.5]. How does this torque profile affect the final return compared to [0.1, 0.0]?
2. Implement a simple "alternating policy" that applies positive torque for 10 steps, then negative torque for 10 steps. Compare its return.
"""

import gymnasium as gym
import numpy as np
import time

# Constants
ENV_NAME = "Reacher-v5"
RENDER_MODE = "human"  # Change to None to run in headless mode
MAX_STEPS = 50
FPS = 60
FIXED_ACTION = np.array([0.1, 0.0], dtype=np.float32)


def evaluate_policy(policy_type):
    print(f"\nEvaluating {policy_type.upper()} Policy...")

    try:
        env = gym.make(ENV_NAME, render_mode=RENDER_MODE)
    except Exception as e:
        env = gym.make(ENV_NAME, render_mode=None)

    obs, info = env.reset(seed=42)
    total_reward = 0.0
    step_count = 0
    final_dist = 0.0

    for step in range(MAX_STEPS):
        # Select action based on policy type
        if policy_type == "random":
            action = env.action_space.sample()
        elif policy_type == "fixed":
            action = FIXED_ACTION
        else:
            raise ValueError(f"Unknown policy type: {policy_type}")

        # Step physics
        obs, reward, terminated, truncated, info = env.step(action)
        total_reward += reward
        step_count += 1

        # Extract target error (last elements of observation depending on gym version)
        # In Reacher-v5, the last 2 elements represent the fingertip-to-target distance vector
        err_x, err_y = obs[-2], obs[-1]
        final_dist = np.sqrt(err_x**2 + err_y**2)

        if env.render_mode == "human":
            time.sleep(1.0 / FPS)

        print(
            f"Step {step:2d} | "
            f"Action: [{action[0]:+5.2f}, {action[1]:+5.2f}] | "
            f"Reward: {reward:6.3f} | "
            f"Target Dist: {final_dist:6.4f}m"
        )

        if terminated or truncated:
            break

    env.close()
    return total_reward, final_dist


def main():
    print("=" * 60)
    print("Starting Lab 08: Policy Comparison")
    print("=" * 60)

    # Evaluate Random Policy
    random_return, random_dist = evaluate_policy("random")

    # Evaluate Fixed Policy
    fixed_return, fixed_dist = evaluate_policy("fixed")

    # Summary table
    print("\n" + "=" * 60)
    print("POLICY COMPARISON SUMMARY")
    print("=" * 60)
    print(f"{'Metric':25s} | {'Random Policy':15s} | {'Fixed Policy':15s}")
    print("-" * 60)
    print(f"{'Episode Return':25s} | {random_return:15.3f} | {fixed_return:15.3f}")
    print(f"{'Average Step Reward':25s} | {random_return/MAX_STEPS:15.3f} | {fixed_return/MAX_STEPS:15.3f}")
    print(f"{'Final Target Distance':25s} | {random_dist:15.4f}m | {fixed_dist:15.4f}m")
    print("=" * 60)


if __name__ == "__main__":
    main()