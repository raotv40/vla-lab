"""
Week 1 - Lab 20: Inverse Kinematics (IK) of a 2-Link Planar Robot Arm
====================================================================

Objectives:
-----------
1. Implement the algebraic analytical inverse kinematics solution for a 2-link planar arm.
2. Incorporate boundary clamping using np.clip to prevent out-of-bounds math errors.
3. Compute and display both solutions: Elbow-Up (theta2 < 0) and Elbow-Down (theta2 > 0).

Theory:
-------
Given desired Cartesian coordinate (x, y) and link lengths L1, L2:
  cos_theta2 = (x^2 + y^2 - L1^2 - L2^2) / (2 * L1 * L2)
  theta2_down = +arccos(cos_theta2)
  theta2_up   = -arccos(cos_theta2)
  theta1_down = arctan2(y, x) - arctan2(L2 * sin(theta2_down), L1 + L2 * cos(theta2_down))
  theta1_up   = arctan2(y, x) - arctan2(L2 * sin(theta2_up), L1 + L2 * cos(theta2_up))
"""

import numpy as np

# Constants
LINK_LENGTH_1 = 1.0  # Length of Link 1 (meters)
LINK_LENGTH_2 = 0.8  # Length of Link 2 (meters)


def solve_inverse_kinematics(x, y, l1, l2):
    """Calculates both analytical inverse kinematics solutions for a 2-link arm.

    Args:
        x (float): Target X coordinate (meters)
        y (float): Target Y coordinate (meters)
        l1 (float): Length of the first link (meters)
        l2 (float): Length of the second link (meters)

    Returns:
        dict: Containing theta1, theta2 angles for elbow-up/down solutions, and reachability flag.
    """
    # Radial distance squared
    r_sq = x**2 + y**2
    r = np.sqrt(r_sq)

    max_reach = l1 + l2
    min_reach = abs(l1 - l2)

    reachable = (r >= min_reach) and (r <= max_reach)

    # Compute cosine of the elbow angle
    cos_t2 = (r_sq - l1**2 - l2**2) / (2.0 * l1 * l2)

    # Clamp value inside [-1.0, 1.0] to prevent mathematical domain errors (NaN)
    cos_t2_clamped = np.clip(cos_t2, -1.0, 1.0)

    # Solve elbow angles (radians)
    t2_down = np.arccos(cos_t2_clamped)
    t2_up = -t2_down

    # Solve shoulder angles (radians)
    t1_down = np.arctan2(y, x) - np.arctan2(l2 * np.sin(t2_down), l1 + l2 * np.cos(t2_down))
    t1_up = np.arctan2(y, x) - np.arctan2(l2 * np.sin(t2_up), l1 + l2 * np.cos(t2_up))

    return {
        "reachable": reachable,
        "clamped": not np.isclose(cos_t2, cos_t2_clamped),
        "elbow_down": (np.degrees(t1_down), np.degrees(t2_down)),
        "elbow_up": (np.degrees(t1_up), np.degrees(t2_up))
    }


def print_ik_result(x, y):
    """Runs IK solver and prints formatted console output."""
    result = solve_inverse_kinematics(x, y, LINK_LENGTH_1, LINK_LENGTH_2)
    status = "REACHABLE" if result["reachable"] else "UNREACHABLE (Clamped to boundary)"

    print(f"Target Coordinate : ({x:+.2f}, {y:+.2f})")
    print(f"Status            : {status}")

    t1_d, t2_d = result["elbow_down"]
    t1_u, t2_u = result["elbow_up"]

    print(f"  - Elbow-Down Solution: theta1 = {t1_d:+.2f}°, theta2 = {t2_d:+.2f}°")
    print(f"  - Elbow-Up Solution  : theta1 = {t1_u:+.2f}°, theta2 = {t2_u:+.2f}°")
    print("-" * 75)


def main():
    print("=" * 75)
    print("Lab 20: Inverse Kinematics Analysis")
    print("=" * 75)
    print(f"Link 1 Length: {LINK_LENGTH_1:.1f} m, Link 2 Length: {LINK_LENGTH_2:.1f} m")
    print("-" * 75)

    # Sweeping targets requested in Exercises 1 and 2
    targets = [
        (1.2, 0.8),  # Exercise 1 original
        (1.4, 0.2),  # Exercise 1 new
        (1.5, 0.2),  # Exercise 2 target 1
        (0.5, 1.2),  # Exercise 2 target 2
        (0.2, 1.5),  # Exercise 2 target 3
        (2.0, 2.0)   # Unreachable case to demonstrate clamping
    ]

    for tx, ty in targets:
        print_ik_result(tx, ty)


if __name__ == "__main__":
    main()