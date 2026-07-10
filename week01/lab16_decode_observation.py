"""
Week 1 - Lab 16: Deconstructing Observations and Reset Dynamics
===============================================================

Objectives:
-----------
1. Query and decode the 10-dimensional observation vector of Reacher-v5.
2. Formulate and parse observations with clear human-readable descriptions.
3. Compare states before and after reset to analyze randomized variables (Exercise 1).

Theory:
-------
- Observation Vector: A 10D continuous float64 vector.
- On Reset: Joint angles ($\theta_1, \theta_2$) are re-initialized, and target coordinates ($x_{\text{target}}, y_{\text{target}}$)
  are randomized to a new point on the table.
- This results in a completely different target position and target error vector on reset, while velocity fields are reset to zero.
"""

import gymnasium as gym

# Constants
ENV_NAME = "Reacher-v5"


def print_decoded_observation(label, obs):
    """Logs the index-by-index breakdown of the Reacher observation vector."""
    labels = [
        "cos(theta1) - Shoulder Cos", "cos(theta2) - Elbow Cos",
        "sin(theta1) - Shoulder Sin", "sin(theta2) - Elbow Sin",
        "target_x - Target X coordinate", "target_y - Target Y coordinate",
        "qvel_shoulder - Shoulder Velocity", "qvel_elbow - Elbow Velocity",
        "err_x - Target Error X (target_x - fingertip_x)",
        "err_y - Target Error Y (target_y - fingertip_y)"
    ]

    print(f"\n--- Decoded Observation: {label} ---")
    print(f"Observation Shape: {obs.shape}")
    print("-" * 70)
    for i in range(10):
        print(f"  obs[{i:2d}] | {labels[i]:48s} | Value: {obs[i]:+.5f}")
    print("-" * 70)


def main():
    print("=" * 70)
    print("Starting Lab 16: Decode Observation")
    print("=" * 70)

    env = gym.make(ENV_NAME)

    # 1. Reset environment to get initial observation
    obs_1, info_1 = env.reset(seed=42)
    print_decoded_observation("First Reset (Seed 42)", obs_1)

    # 2. Reset again with a different seed to see what changes
    obs_2, info_2 = env.reset(seed=100)
    print_decoded_observation("Second Reset (Seed 100)", obs_2)

    # 3. Compare changes
    print("\nReset Parameter Variations:")
    print("-" * 70)
    print(f"  Index | Description         | Seed 42   | Seed 100  | Delta")
    print("-" * 70)
    for i in range(10):
        delta = obs_2[i] - obs_1[i]
        print(f"  obs[{i}] | Feature {i:2d}           | {obs_1[i]:+.4f} | {obs_2[i]:+.4f} | {delta:+.6f}")
    print("-" * 70)

    env.close()


if __name__ == "__main__":
    main()