"""
Week 1 - Lab 9: Introduction to Robot Controllers and P-Control Concepts
=======================================================================

Objectives:
-----------
1. Understand the concept of a robot controller in a closed-loop system.
2. Initialize and step through Gymnasium's Reacher-v5 environment.
3. Establish the structure of a controller loop with Proportional Gain (Kp).
4. Predict controller behaviors under different gain settings.

Theory:
-------
A Controller is a software algorithm that calculates motor commands (actions) based on a target state.
A Proportional (P) Controller scales the error between target and current state by a gain coefficient Kp:
- Action (torque) = Kp * Error

*Note: In today's lab, the action profile is hardcoded to np.array([0.1, 0.0]) to demonstrate the control loop structure.
The proportional gain (Kp) is defined as a parameter but not yet applied to the action. In upcoming labs, we will calculate
tracking errors from observations and scale actions dynamically.*

Expected Output:
----------------
Console output logging each step index and the immediate reward returned by the environment.
Example:
Step   0 | Reward:  -0.125
Step   1 | Reward:  -0.125
...

Exercises:
----------
1. Set the RENDER_MODE constant to "human" to run the GUI simulation (requires display).
2. Modify the MAX_STEPS constant to 100. How does this impact evaluation length?
"""

import gymnasium as gym
import numpy as np
import time

# Constants
ENV_NAME = "Reacher-v5"
RENDER_MODE = "human"  # Change to None to run in headless mode
MAX_STEPS = 50
FPS = 60


def main():
    print("=" * 60)
    print("Starting Lab 09: Simple Controller Demo")
    print("=" * 60)

    # Initialize environment with headless fallback
    try:
        env = gym.make(ENV_NAME, render_mode=RENDER_MODE)
        print(f"Environment '{ENV_NAME}' loaded with render_mode='{RENDER_MODE}'")
    except Exception as e:
        print(f"Warning: Failed to load human render mode: {e}")
        print("Falling back to headless simulation (render_mode=None)")
        env = gym.make(ENV_NAME, render_mode=None)

    obs, info = env.reset(seed=42)
    
    # Proportional Gain (Kp) parameter
    # Change Kp in exercises to predict behavior (not yet mapped to action)
    kp = 0.1
    print(f"Controller Proportional Gain (Kp) initialized to: {kp}")

    for step in range(MAX_STEPS):
        # Apply a constant action profile (torque) to joint 1
        # The true feedback controller will compute this from observation tracking error
        action = np.array([0.1, 0.0], dtype=np.float32)

        # Step the environment dynamics
        obs, reward, terminated, truncated, info = env.step(action)

        # Render step frames
        if env.render_mode == "human":
            env.render()
            time.sleep(1.0 / FPS)

        print(f"Step {step:3d} | Reward {reward:7.3f}")

        if terminated or truncated:
            print("\nEpisode finished.")
            break

    # Prompt before closing GUI window
    if env.render_mode == "human":
        input("\nPress Enter to close visual simulation...")

    env.close()
    print("=" * 60)


if __name__ == "__main__":
    main()