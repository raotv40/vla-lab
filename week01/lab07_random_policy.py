"""
Week 1 - Lab 7: Random Policy Exploration in Gymnasium
======================================================

Objectives:
-----------
1. Initialize the Gymnasium Reacher-v5 environment.
2. Implement a pure Random Policy by sampling actions uniformly.
3. Study the concept of Exploration in Reinforcement Learning.
4. Measure the cumulative return (episode return) of a random agent.

Theory:
-------
A Policy (pi) is a mapping from observations to actions: a = pi(s).
A Random Policy samples actions uniformly at random from the environment's action space:
- action ~ Uniform(Action Space)
In Gymnasium, this is done using `env.action_space.sample()`.

Exploration is the process of trying novel actions to discover their effects and find states with high rewards.
A random policy represents the maximum exploration baseline. However, without exploitation, the policy is
unable to purposefully drive the arm to the target.

Expected Output:
----------------
Console output logging each step, the selected torque actions, step reward, and running cumulative return.
At the end, the total return of the episode is displayed.

Exercises:
----------
1. Increase the MAX_STEPS constant to 150 steps. Does the average return increase or decrease? Explain.
2. Calculate and print the standard deviation of the step rewards under the random policy to analyze variance.
"""

import gymnasium as gym
import time

# Constants
ENV_NAME = "Reacher-v5"
RENDER_MODE = "human"  # Change to None to run in headless mode
MAX_STEPS = 50
SLEEP_TIME = 0.02


def main():
    print("=" * 60)
    print(f"Starting Lab 07: Random Policy on {ENV_NAME}")
    print("=" * 60)

    # Create environment with fallback for headless servers
    try:
        env = gym.make(ENV_NAME, render_mode=RENDER_MODE)
        print(f"Environment initialized with render_mode='{RENDER_MODE}'")
    except Exception as e:
        print(f"Warning: Failed to initialize in human render mode: {e}")
        print("Falling back to headless mode (render_mode=None)")
        env = gym.make(ENV_NAME, render_mode=None)

    obs, info = env.reset(seed=42)
    total_reward = 0.0

    for step in range(MAX_STEPS):
        # Sample action uniformly at random from action space
        action = env.action_space.sample()

        # Step environment dynamics
        obs, reward, terminated, truncated, info = env.step(action)
        total_reward += reward

        # Slow down loop for visualization if rendering
        if env.render_mode == "human":
            time.sleep(SLEEP_TIME)

        # Log status
        print(
            f"Step {step:3d} | "
            f"Action: [{action[0]:+5.2f}, {action[1]:+5.2f}] | "
            f"Reward: {reward:7.3f} | "
            f"Cumulative Return: {total_reward:8.3f}"
        )

        if terminated or truncated:
            print("\nEpisode finished.")
            break

    print("-" * 60)
    print(f"Episode Completed in {step + 1} steps.")
    print(f"Final Episode Return: {total_reward:.3f}")
    print("=" * 60)

    # Cleanup environment resources
    env.close()


if __name__ == "__main__":
    main()