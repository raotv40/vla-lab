"""
Week 1 - Lab 3: Deconstructing the Reacher-v4 Observation Space
===============================================================

Objectives:
-----------
1. Understand the 10-dimensional observation space of Gymnasium's Reacher-v4.
2. Manually parse each observation element and verify its physical meaning.
3. Validate trigonometric relationships (cos^2 + sin^2 = 1).
4. Compute the fingertip coordinates using forward kinematics and verify the target error vector.

Theory:
-------
In reinforcement learning, the observation is the numerical state description that the agent receives.
In Reacher-v4, the observation is a 10D vector:
- Index 0: cos(theta1) - Cosine of shoulder angle
- Index 1: cos(theta2) - Cosine of elbow angle (relative to shoulder link)
- Index 2: sin(theta1) - Sine of shoulder angle
- Index 3: sin(theta2) - Sine of elbow angle
- Index 4: target_x - Target X coordinate in world space
- Index 5: target_y - Target Y coordinate in world space
- Index 6: qvel0 - Angular velocity of the shoulder joint
- Index 7: qvel1 - Angular velocity of the elbow joint
- Index 8: err_x - X-distance from fingertip to target (target_x - fingertip_x)
- Index 9: err_y - Y-distance from fingertip to target (target_y - fingertip_y)

Forward Kinematics:
For a 2-link robotic arm with link lengths l1 = 0.1m and l2 = 0.1m, the fingertip coordinates (x, y) are:
- x_fingertip = l1 * cos(theta1) + l2 * cos(theta1 + theta2)
- y_fingertip = l1 * sin(theta1) + l2 * sin(theta1 + theta2)

Trigonometric Identities:
- cos(theta1 + theta2) = cos(theta1)*cos(theta2) - sin(theta1)*sin(theta2)
- sin(theta1 + theta2) = sin(theta1)*cos(theta2) + cos(theta1)*sin(theta2)

Expected Output:
----------------
A printed breakdown table of the 10 observation dimensions, along with the results of validation tests (Trigonometric check and Forward Kinematics match).

Exercises:
----------
1. Write a function that converts the joint angles theta1 and theta2 from radians to degrees, and print them at each step.
2. Verify if the target position (indices 4 and 5) stays constant throughout a single episode.
"""

import gymnasium as gym
import numpy as np

def main():
    print("--- Lab 03: Deconstructing the Observation Space ---")
    
    env = gym.make("Reacher-v4")
    observation, info = env.reset(seed=42)
    
    # 1. Print the raw observation vector
    print(f"Raw Observation Vector:\n{observation}\n")
    
    # 2. Deconstruct the observations
    cos_theta1 = observation[0]
    cos_theta2 = observation[1]
    sin_theta1 = observation[2]
    sin_theta2 = observation[3]
    target_x   = observation[4]
    target_y   = observation[5]
    qvel0      = observation[6]
    qvel1      = observation[7]
    err_x      = observation[8]
    err_y      = observation[9]
    
    print("Parsed Observations:")
    print(f"  [0] cos(theta1):      {cos_theta1:+8.4f} (Shoulder Cosine)")
    print(f"  [1] cos(theta2):      {cos_theta2:+8.4f} (Elbow Cosine - Relative)")
    print(f"  [2] sin(theta1):      {sin_theta1:+8.4f} (Shoulder Sine)")
    print(f"  [3] sin(theta2):      {sin_theta2:+8.4f} (Elbow Sine - Relative)")
    print(f"  [4] Target X:         {target_x:+8.4f} (Target X coordinate)")
    print(f"  [5] Target Y:         {target_y:+8.4f} (Target Y coordinate)")
    print(f"  [6] Shoulder Vel:     {qvel0:+8.4f} (rad/s)")
    print(f"  [7] Elbow Vel:        {qvel1:+8.4f} (rad/s)")
    print(f"  [8] Target Error X:   {err_x:+8.4f} (target_x - fingertip_x)")
    print(f"  [9] Target Error Y:   {err_y:+8.4f} (target_y - fingertip_y)")
    
    # 3. Trigonometric check
    # cos^2(theta) + sin^2(theta) must equal 1.0
    check1 = cos_theta1**2 + sin_theta1**2
    check2 = cos_theta2**2 + sin_theta2**2
    print(f"\nTrigonometric Verification:")
    print(f"  Shoulder: cos^2(t1) + sin^2(t1) = {check1:.6f} (Expected: 1.000000)")
    print(f"  Elbow:    cos^2(t2) + sin^2(t2) = {check2:.6f} (Expected: 1.000000)")
    
    # 4. Forward Kinematics Verification
    # Reacher link lengths are l1 = 0.1m, l2 = 0.11m (fingertip position is at 0.11 relative to body1)
    l1 = 0.1
    l2 = 0.11
    
    # Using trig identity to calculate fingertip relative position:
    # cos(theta1 + theta2) = cos(theta1)cos(theta2) - sin(theta1)sin(theta2)
    # sin(theta1 + theta2) = sin(theta1)cos(theta2) + cos(theta1)sin(theta2)
    cos_theta12 = cos_theta1 * cos_theta2 - sin_theta1 * sin_theta2
    sin_theta12 = sin_theta1 * cos_theta2 + cos_theta1 * sin_theta2
    
    # Compute fingertip position in world coordinates
    fingertip_x = l1 * cos_theta1 + l2 * cos_theta12
    fingertip_y = l1 * sin_theta1 + l2 * sin_theta12
    
    # Manually compute target error (fingertip - target) as defined in Gymnasium's Reacher-v4
    computed_err_x = fingertip_x - target_x
    computed_err_y = fingertip_y - target_y
    
    print(f"\nForward Kinematics Verification:")
    print(f"  Fingertip Position:  X = {fingertip_x:7.4f}m, Y = {fingertip_y:7.4f}m")
    print(f"  Observed Target Error:  X = {err_x:7.4f}m, Y = {err_y:7.4f}m")
    print(f"  Computed Target Error:  X = {computed_err_x:7.4f}m, Y = {computed_err_y:7.4f}m")
    
    # Check if they are equal within floating point precision
    diff_x = abs(err_x - computed_err_x)
    diff_y = abs(err_y - computed_err_y)
    print(f"  Absolute Error Difference: X = {diff_x:.6e}, Y = {diff_y:.6e}")
    
    assert diff_x < 1e-4 and diff_y < 1e-4, "Forward kinematics mismatch!"
    print("Kinematics check passed! Observation math is correct.")
    
    env.close()
    print("--- Lab 03: Completed Successfully ---")

if __name__ == "__main__":
    main()
