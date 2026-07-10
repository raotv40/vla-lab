"""
Week 1 - Lab 15: Angle Representation and wrap-around discontinuity
==================================================================

Objectives:
-----------
1. Calculate Reacher-v5 joint angles from sine and cosine observations.
2. Demonstrate how to decode angles in radians and degrees using arctan2.
3. Discuss the 360 to 0 degrees wrap-around discontinuity (Exercise 3).
4. Explain why sines and cosines are preferred for neural network inputs.

Theory:
-------
Joint angles are calculated as:
- theta = arctan2(sin_theta, cos_theta)

Angle wrap-around discontinuity:
Representing angles directly as a scalar theta in [-pi, pi] or [0, 360] creates a discontinuity at the boundary.
For example, a tiny joint movement from 359.9 degrees to 0.1 degrees results in a numerical step change
of ~360 degrees. This massive jump in numerical value creates extreme gradients during neural network training,
degrading learning stability.

Using sine and cosine features resolves this because both are continuous functions:
- cos(359.9) = 1.0, cos(0.1) = 1.0 (continuous transition)
- sin(359.9) = 0.0, sin(0.1) = 0.0 (continuous transition)
"""

import gymnasium as gym
import numpy as np

# Constants
ENV_NAME = "Reacher-v5"


def main():
    print("=" * 60)
    print(f"Starting Lab 15: Angle Wrap-around on {ENV_NAME}")
    print("=" * 60)

    env = gym.make(ENV_NAME)
    obs, info = env.reset(seed=42)

    # Decode sines and cosines
    cos_theta1, cos_theta2 = obs[0], obs[1]
    sin_theta1, sin_theta2 = obs[2], obs[3]

    # Calculate angles using arctan2
    theta1_rad = np.arctan2(sin_theta1, cos_theta1)
    theta2_rad = np.arctan2(sin_theta2, cos_theta2)

    # Convert to degrees
    theta1_deg = np.degrees(theta1_rad)
    theta2_deg = np.degrees(theta2_rad)

    # Adjust elbow to [0, 360] range for demonstration
    theta1_deg_360 = theta1_deg if theta1_deg >= 0 else 360 + theta1_deg
    theta2_deg_360 = theta2_deg if theta2_deg >= 0 else 360 + theta2_deg

    print("Decoded Joint State Angles:")
    print("-" * 60)
    print(f"Shoulder Joint Angle (theta1) : {theta1_rad:+.4f} rad | {theta1_deg:+.2f}° ({theta1_deg_360:.2f}°)")
    print(f"Elbow Joint Angle (theta2)    : {theta2_rad:+.4f} rad | {theta2_deg:+.2f}° ({theta2_deg_360:.2f}°)")
    print("-" * 60)

    # Wrap-around Demonstration
    print("\nDemonstrating Angle Discontinuity:")
    print("-" * 70)
    angle_a = 359.9
    angle_b = 0.1
    raw_delta = angle_b - angle_a
    print(f"1. Raw Degrees: Angle A = {angle_a}°, Angle B = {angle_b}°")
    print(f"   Physical Difference : 0.2°")
    print(f"   Numerical Difference: {raw_delta}° (Severe Discontinuity!)")

    # Sine/Cosine check
    cos_a, sin_a = np.cos(np.radians(angle_a)), np.sin(np.radians(angle_a))
    cos_b, sin_b = np.cos(np.radians(angle_b)), np.sin(np.radians(angle_b))
    cos_delta = cos_b - cos_a
    sin_delta = sin_b - sin_a
    print(f"\n2. Sine/Cosine Encoding:")
    print(f"   State A: [cos={cos_a:.4f}, sin={sin_a:.4f}]")
    print(f"   State B: [cos={cos_b:.4f}, sin={sin_b:.4f}]")
    print(f"   Deltas : [cos_delta={cos_delta:+.4f}, sin_delta={sin_delta:+.4f}] (Smooth transition!)")
    print("-" * 70)

    env.close()


if __name__ == "__main__":
    main()
