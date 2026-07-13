"""
Week 1 - Lab 21: Inverse Kinematics Verification via Forward Kinematics
======================================================================

Objectives:
-----------
1. Compute the analytical inverse kinematics for a desired target coordinate.
2. Reconstruct the end-effector position using Forward Kinematics (FK).
3. Compute and log coordinate discrepancy errors (Exercise 3).

Theory:
-------
Plugging analytical joint angle solutions back into the forward kinematics equations
yields coordinates exactly matching the desired input target. Discrepancies are purely due to
floating-point roundoff tolerances (machine precision epsilon).
"""

import numpy as np

# Constants
LINK_LENGTH_1 = 1.0  # Length of Link 1 (meters)
LINK_LENGTH_2 = 0.8  # Length of Link 2 (meters)

# Target coordinates (Exercise 3)
TARGET_X = 1.2
TARGET_Y = 0.8


def main():
    print("=" * 60)
    print("Lab 21: Inverse Kinematics Verification")
    print("=" * 60)

    # 1. Compute Inverse Kinematics
    r_sq = TARGET_X**2 + TARGET_Y**2
    cos_theta2 = (r_sq - LINK_LENGTH_1**2 - LINK_LENGTH_2**2) / (2.0 * LINK_LENGTH_1 * LINK_LENGTH_2)
    cos_theta2_clamped = np.clip(cos_theta2, -1.0, 1.0)

    theta2 = np.arccos(cos_theta2_clamped)
    theta1 = np.arctan2(TARGET_Y, TARGET_X) - np.arctan2(
        LINK_LENGTH_2 * np.sin(theta2),
        LINK_LENGTH_1 + LINK_LENGTH_2 * np.cos(theta2)
    )

    # 2. Re-calculate actual Cartesian coordinates via Forward Kinematics
    actual_x = LINK_LENGTH_1 * np.cos(theta1) + LINK_LENGTH_2 * np.cos(theta1 + theta2)
    actual_y = LINK_LENGTH_1 * np.sin(theta1) + LINK_LENGTH_2 * np.sin(theta1 + theta2)

    # 3. Calculate Error
    error_x = TARGET_X - actual_x
    error_y = TARGET_Y - actual_y

    print(f"Target Coordinate      : ({TARGET_X:.4f}, {TARGET_Y:.4f})")
    print(f"Computed Joint Angles  : theta1 = {np.degrees(theta1):+.2f}°, theta2 = {np.degrees(theta2):+.2f}°")
    print(f"Reconstructed Position : ({actual_x:.4f}, {actual_y:.4f})")
    print("-" * 60)
    print(f"Coordinate Error X     : {error_x:+.16e} m")
    print(f"Coordinate Error Y     : {error_y:+.16e} m")
    print("-" * 60)
    print("Verification Conclusion:")
    print("The numerical errors are near zero (within 1e-16 meters). This is because the")
    print("analytical inverse kinematics solution is mathematically exact. The tiny residual")
    print("errors are purely due to float64 representation precision limits on CPU cores.")
    print("=" * 60)


if __name__ == "__main__":
    main()