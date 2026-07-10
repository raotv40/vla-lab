"""
Week 1 - Lab 10: Observation Decoder for Reacher-v5
===================================================

Objectives:
-----------
1. Initialize the Reacher-v5 environment.
2. Decode the 10-dimensional observation vector into physical components.
3. Understand how joints, velocities, target positions, and fingertip errors are structured.

Theory:
-------
In reinforcement learning, the environment states are passed to the agent as observation vectors.
For Reacher-v5, this vector is a 10D Box space containing:
- Index 0: cos(theta1) - Cosine of shoulder angle
- Index 1: cos(theta2) - Cosine of elbow angle (relative link position)
- Index 2: sin(theta1) - Sine of shoulder angle
- Index 3: sin(theta2) - Sine of elbow angle (relative link position)
- Index 4: target_x - Target X coordinate in world coordinate frame
- Index 5: target_y - Target Y coordinate in world coordinate frame
- Index 6: qvel_shoulder - Angular velocity of shoulder joint (rad/s)
- Index 7: qvel_elbow - Angular velocity of elbow joint (rad/s)
- Index 8: error_x - Fingertip-to-target Cartesian distance along X axis
- Index 9: error_y - Fingertip-to-target Cartesian distance along Y axis
"""

import gymnasium as gym

# Constants
ENV_NAME = "Reacher-v5"


def main():
    print("=" * 60)
    print(f"Starting Lab 10: Observation Decoder on {ENV_NAME}")
    print("=" * 60)

    # Initialize environment
    env = gym.make(ENV_NAME, render_mode=None)
    obs, info = env.reset(seed=42)

    # Check shape
    print(f"Observation Length : {len(obs)}")
    print(f"Observation Dtype  : {obs.dtype}\n")

    # Deconstruct and print
    cos_theta1 = obs[0]
    cos_theta2 = obs[1]
    sin_theta1 = obs[2]
    sin_theta2 = obs[3]
    target_x = obs[4]
    target_y = obs[5]
    qvel_shoulder = obs[6]
    qvel_elbow = obs[7]
    error_x = obs[8]
    error_y = obs[9]

    print("Parsed Reacher-v5 Observation Vector:")
    print("-" * 60)
    print(f"  obs[0] | cos(theta1)     : {cos_theta1:+8.4f} (Shoulder joint angle cosine)")
    print(f"  obs[1] | cos(theta2)     : {cos_theta2:+8.4f} (Elbow joint angle cosine)")
    print(f"  obs[2] | sin(theta1)     : {sin_theta1:+8.4f} (Shoulder joint angle sine)")
    print(f"  obs[3] | sin(theta2)     : {sin_theta2:+8.4f} (Elbow joint angle sine)")
    print(f"  obs[4] | Target X        : {target_x:+8.4f} (Target x-coordinate in world space)")
    print(f"  obs[5] | Target Y        : {target_y:+8.4f} (Target y-coordinate in world space)")
    print(f"  obs[6] | Shoulder Vel    : {qvel_shoulder:+8.4f} (rad/s - angular velocity)")
    print(f"  obs[7] | Elbow Vel       : {qvel_elbow:+8.4f} (rad/s - angular velocity)")
    print(f"  obs[8] | Target Error X  : {error_x:+8.4f} (target_x - fingertip_x)")
    print(f"  obs[9] | Target Error Y  : {error_y:+8.4f} (target_y - fingertip_y)")
    print("-" * 60)

    env.close()


if __name__ == "__main__":
    main()