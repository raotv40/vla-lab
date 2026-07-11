"""
Week 1 - Lab 18: Forward Kinematics (FK) of a 2-Link Planar Robot Arm
=====================================================================

Objectives:
-----------
1. Understand links and joints in a serial kinematic manipulator.
2. Implement the mathematical equations for 2D Planar Forward Kinematics.
3. Compute the end-effector fingertip position from joint angles and link lengths.

Theory:
-------
For a 2-link planar robot arm with link lengths L1 and L2, and joint angles
theta1 (shoulder joint, relative to ground) and theta2 (elbow joint, relative to Link 1):
  x_elbow = L1 * cos(theta1)
  y_elbow = L1 * sin(theta1)
  x_tip   = x_elbow + L2 * cos(theta1 + theta2)
  y_tip   = y_elbow + L2 * sin(theta1 + theta2)
"""

import numpy as np

# Constants
LINK_LENGTH_1 = 1.0  # Length of Link 1 (meters)
LINK_LENGTH_2 = 0.8  # Length of Link 2 (meters)

# Default Joint angles (degrees)
DEFAULT_THETA1_DEG = 45.0
DEFAULT_THETA2_DEG = 90.0


def compute_forward_kinematics(l1, l2, theta1_deg, theta2_deg):
    """Calculates the elbow and end-effector positions.

    Args:
        l1 (float): Length of the first link (meters)
        l2 (float): Length of the second link (meters)
        theta1_deg (float): Shoulder joint angle (degrees)
        theta2_deg (float): Elbow joint angle (degrees, relative to Link 1)

    Returns:
        tuple: (elbow_x, elbow_y, tip_x, tip_y)
    """
    # Convert joint angles to radians
    t1 = np.deg2rad(theta1_deg)
    t2 = np.deg2rad(theta2_deg)

    # Compute joint positions
    elbow_x = l1 * np.cos(t1)
    elbow_y = l1 * np.sin(t1)

    # Absolute orientation of Link 2 is (theta1 + theta2)
    tip_x = elbow_x + l2 * np.cos(t1 + t2)
    tip_y = elbow_y + l2 * np.sin(t1 + t2)

    return elbow_x, elbow_y, tip_x, tip_y


def main():
    print("=" * 60)
    print("Forward Kinematics calculation for 2-Link Robot Arm")
    print("=" * 60)

    # Calculate default configuration
    elbow_x, elbow_y, tip_x, tip_y = compute_forward_kinematics(
        LINK_LENGTH_1, LINK_LENGTH_2, DEFAULT_THETA1_DEG, DEFAULT_THETA2_DEG
    )

    print(f"Link 1 Length : {LINK_LENGTH_1:.1f} m")
    print(f"Link 2 Length : {LINK_LENGTH_2:.1f} m")
    print(f"Theta1        : {DEFAULT_THETA1_DEG:.1f}°")
    print(f"Theta2        : {DEFAULT_THETA2_DEG:.1f}°")
    print("-" * 60)
    print(f"Elbow Joint Coordinate : ({elbow_x:+.4f}, {elbow_y:+.4f})")
    print(f"End-Effector (X, Y)    : ({tip_x:+.4f}, {tip_y:+.4f})")
    print("=" * 60)


if __name__ == "__main__":
    main()