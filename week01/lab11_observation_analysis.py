"""
Week 1 - Lab 11: Trigonometric Observation Analysis
====================================================

Objectives:
-----------
1. Perform mathematical verification of Reacher-v5 observations.
2. Confirm the trigonometric identity: cos^2(theta) + sin^2(theta) = 1.
3. Compute the angular state vector.

Theory:
-------
Joint angles in MuJoCo's Reacher environment are not represented directly in radians to avoid wrapping discontinuities
at the boundaries. Instead, they are encoded as cosine/sine coordinate pairs on a unit circle.
For any valid angle theta:
- cos^2(theta) + sin^2(theta) = 1.0 (with a small numerical margin due to floating-point representation).
"""

import gymnasium as gym
import numpy as np

# Constants
ENV_NAME = "Reacher-v5"


def main():
    print("=" * 60)
    print(f"Starting Lab 11: Observation Analysis on {ENV_NAME}")
    print("=" * 60)

    env = gym.make(ENV_NAME, render_mode=None)
    obs, info = env.reset(seed=42)

    # Decode sines and cosines
    cos_theta1, cos_theta2 = obs[0], obs[1]
    sin_theta1, sin_theta2 = obs[2], obs[3]

    # Verify cos^2 + sin^2 = 1.0
    sum_sq1 = cos_theta1**2 + sin_theta1**2
    sum_sq2 = cos_theta2**2 + sin_theta2**2

    print("Trigonometric Identity Validation:")
    print("-" * 60)
    print(f"Shoulder Joint: cos^2 + sin^2 = {cos_theta1:.4f}^2 + {sin_theta1:.4f}^2 = {sum_sq1:.6f}")
    print(f"Elbow Joint:    cos^2 + sin^2 = {cos_theta2:.4f}^2 + {sin_theta2:.4f}^2 = {sum_sq2:.6f}")
    print("-" * 60)

    # Validate with a threshold
    threshold = 1e-5
    if abs(sum_sq1 - 1.0) < threshold and abs(sum_sq2 - 1.0) < threshold:
        print("Success: Both joint observations correctly represent unit circle points!")
    else:
        print("Warning: Trigonometric validation failed to meet strict floating-point margins.")

    env.close()


if __name__ == "__main__":
    main()