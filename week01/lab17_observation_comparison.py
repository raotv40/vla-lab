"""
Week 1 - Lab 17: Sequential Observation Comparison Under Control
================================================================

Objectives:
-----------
1. Run a closed-loop control simulation applying joint torques.
2. Compare observations step-by-step to identify state changes.
3. Classify parameters into fast-changing, slowly-changing, and static (Exercise 2).

Theory:
-------
When a controller applies torque command actions to joint motors:
- Joint Velocities (dq1, dq2 at indices 6-7) respond immediately due to acceleration dynamics (Newton's second law: torque = I * alpha).
- Joint Positions (sines and cosines at indices 0-3) change slowly because they are the integral of velocities (position changes gradually).
- Target Positions (indices 4-5) remain static as the target reference does not move.
- Target Errors (indices 8-9) change continuously as the end-effector fingertip moves.
"""

import gymnasium as gym
import numpy as np
import time

# Constants
ENV_NAME = "Reacher-v5"
RENDER_MODE = "human"  # Change to None to run in headless mode
MAX_STEPS = 5
FPS = 30


def main():
    print("=" * 70)
    print("Starting Lab 17: Observation Comparison")
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

    print("\nInitial State (Step 0):")
    print(f"  Angles (cos/sin) : [{obs[0]:.4f}, {obs[1]:.4f}, {obs[2]:.4f}, {obs[3]:.4f}]")
    print(f"  Target Position  : [{obs[4]:.4f}, {obs[5]:.4f}]")
    print(f"  Joint Velocities : [{obs[6]:.4f}, {obs[7]:.4f}]")
    print(f"  Target Error     : [{obs[8]:.4f}, {obs[9]:.4f}]")
    print("-" * 70)

    for step in range(1, MAX_STEPS + 1):
        # Apply a non-zero action to accelerate joints
        action = np.array([0.1, -0.1], dtype=np.float32)
        obs_new, reward, terminated, truncated, info = env.step(action)

        if env.render_mode == "human":
            env.render()
            time.sleep(1.0 / FPS)

        print(f"\nStep {step:d} State and Deltas:")
        print(f"  Angles (cos/sin) : [{obs_new[0]:.4f}, {obs_new[1]:.4f}, {obs_new[2]:.4f}, {obs_new[3]:.4f}]")
        print(f"  Joint Velocities : [{obs_new[6]:.4f}, {obs_new[7]:.4f}]")
        print(f"  Target Error     : [{obs_new[8]:.4f}, {obs_new[9]:.4f}]")

        # Calculate deltas from previous step to identify velocity acceleration vs position integration
        vel_delta_0 = obs_new[6] - obs[6]
        vel_delta_1 = obs_new[7] - obs[7]
        pos_delta_0 = obs_new[0] - obs[0]
        pos_delta_1 = obs_new[2] - obs[2]

        print(f"  [Deltas] Pos (Shoulder Cos/Sin): [{pos_delta_0:+.6f}, {pos_delta_1:+.6f}] (Slow positioning)")
        print(f"  [Deltas] Vel (Shoulder/Elbow)  : [{vel_delta_0:+.6f}, {vel_delta_1:+.6f}] (Fast acceleration)")

        obs = obs_new.copy()

        if terminated or truncated:
            break

    if env.render_mode == "human":
        input("\nPress Enter to close simulation...")

    env.close()


if __name__ == "__main__":
    main()