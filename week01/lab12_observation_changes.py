"""
Week 1 - Lab 12: Observation Changes During Robot Motion
========================================================

Objectives:
-----------
1. Run a passive physics simulation of Reacher-v5 (joint torques = 0.0).
2. Compare initial observations against subsequent steps.
3. Identify which observations change dynamically and which remain static.
4. Answer Exercise 2 regarding state changes.

Theory:
-------
In physical simulations:
- Dynamic quantities (velocities, coordinates, error vectors) evolve over time according to equations of motion.
- Static task context variables (target position coordinates) remain constant once initialized, providing
  a fixed reference setpoint for the control feedback loops.
"""

import gymnasium as gym
import numpy as np
import time

# Constants
ENV_NAME = "Reacher-v5"
RENDER_MODE = "human"  # Change to None to run in headless mode
MAX_STEPS = 10
FPS = 30


def main():
    print("=" * 70)
    print(f"Starting Lab 12: Observation Changes on {ENV_NAME}")
    print("=" * 70)

    try:
        env = gym.make(ENV_NAME, render_mode=RENDER_MODE)
        print(f"Environment initialized with render_mode='{RENDER_MODE}'")
    except Exception as e:
        print(f"Warning: Failed to load human render mode: {e}")
        print("Falling back to headless simulation (render_mode=None)")
        env = gym.make(ENV_NAME, render_mode=None)

    obs, info = env.reset(seed=42)
    initial_obs = obs.copy()

    print("\nInitial Observation Vector:")
    print("-" * 70)
    for i, val in enumerate(initial_obs):
        print(f"  obs[{i}] = {val:+.4f}")
    print("-" * 70)

    for step in range(MAX_STEPS):
        # Apply passive zero-torque control action
        action = np.array([0.0, 0.0], dtype=np.float32)

        obs, reward, terminated, truncated, info = env.step(action)

        if env.render_mode == "human":
            env.render()
            time.sleep(1.0 / FPS)

        print(f"\nStep {step + 1:2d} changes relative to Initial state:")
        print("-" * 70)
        print(f"  Index | Description         | Initial   | Current   | Delta")
        print("-" * 70)
        # We check change deltas
        labels = [
            "cos(theta1)", "cos(theta2)", "sin(theta1)", "sin(theta2)",
            "Target X", "Target Y", "Shoulder Vel", "Elbow Vel",
            "Error X", "Error Y"
        ]
        for i in range(10):
            delta = obs[i] - initial_obs[i]
            print(f"  obs[{i}] | {labels[i]:19s} | {initial_obs[i]:+.4f} | {obs[i]:+.4f} | {delta:+.6f}")
        print("-" * 70)

        if terminated or truncated:
            print("\nEpisode finished.")
            break

    if env.render_mode == "human":
        input("\nPress Enter to close simulation...")

    env.close()


if __name__ == "__main__":
    main()