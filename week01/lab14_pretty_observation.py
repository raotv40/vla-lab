"""
Week 1 - Lab 14: Pretty-Printing Observation Tables
===================================================

Objectives:
-----------
1. Initialize the Reacher-v5 environment.
2. Step through the environment and decode the observations.
3. Print observations in a beautifully formatted text table.
"""

import gymnasium as gym
import numpy as np
import time

# Constants
ENV_NAME = "Reacher-v5"
RENDER_MODE = "human"  # Change to None to run in headless mode
MAX_STEPS = 5
FPS = 30


def print_pretty_table(step, obs):
    """Parses and prints the observation vector in a neat table format."""
    labels = [
        "Shoulder Cosine (cos_q1)", "Elbow Cosine (cos_q2)",
        "Shoulder Sine (sin_q1)", "Elbow Sine (sin_q2)",
        "Target X Position", "Target Y Position",
        "Shoulder Velocity (dq1)", "Elbow Velocity (dq2)",
        "Target Error X", "Target Error Y"
    ]
    units = ["[-1, 1]", "[-1, 1]", "[-1, 1]", "[-1, 1]", "meters", "meters", "rad/s", "rad/s", "meters", "meters"]

    print(f"\n================ STEP {step:02d} OBSERVATION TABLE ================")
    print(f"{'Index':5s} | {'Observation Name':30s} | {'Value':10s} | {'Units':10s}")
    print("-" * 65)
    for i in range(10):
        print(f"obs[{i}] | {labels[i]:30s} | {obs[i]:+10.4f} | {units[i]}")
    print("=================================================================\n")


def main():
    print("=" * 60)
    print(f"Starting Lab 14: Pretty Observation on {ENV_NAME}")
    print("=" * 60)

    try:
        env = gym.make(ENV_NAME, render_mode=RENDER_MODE)
        print(f"Environment initialized with render_mode='{RENDER_MODE}'")
    except Exception as e:
        print(f"Warning: Failed to load human render mode: {e}")
        print("Falling back to headless simulation (render_mode=None)")
        env = gym.make(ENV_NAME, render_mode=None)

    obs, info = env.reset(seed=42)

    # Print initial state
    print_pretty_table(0, obs)

    for step in range(1, MAX_STEPS + 1):
        # Apply slight constant action torque
        action = np.array([0.05, 0.05], dtype=np.float32)
        obs, reward, terminated, truncated, info = env.step(action)

        if env.render_mode == "human":
            env.render()
            time.sleep(1.0 / FPS)

        print_pretty_table(step, obs)

        if terminated or truncated:
            break

    if env.render_mode == "human":
        input("\nPress Enter to close simulation...")

    env.close()


if __name__ == "__main__":
    main()
