"""
Week 1 - Lab 19: Visualizing 2-Link Planar Robot Arm Configuration
==================================================================

Objectives:
-----------
1. Plot the physical link and joint segments of a planar manipulator.
2. Save the configuration coordinate plot to disk for reference.
3. Observe end-effector movements and analyze link rotation sensitivity (Exercise 3).

Theory:
-------
Visualizing the robot configuration enables immediate validation of kinematics calculations.
Plotting link segments as lines and joint nodes as circles creates a schematic of the workspace.
"""

import os
import numpy as np

# Choose Agg backend dynamically to prevent rendering GUI exceptions in headless systems
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Constants
LINK_LENGTH_1 = 1.0  # Length of Link 1 (meters)
LINK_LENGTH_2 = 0.8  # Length of Link 2 (meters)

# File save paths
SAVE_DIR = os.path.join("assets", "day08")
SAVE_PATH = os.path.join(SAVE_DIR, "robot_arm.png")


def compute_forward_kinematics(l1, l2, theta1_deg, theta2_deg):
    """Calculates elbow and end-effector coordinates."""
    t1 = np.deg2rad(theta1_deg)
    t2 = np.deg2rad(theta2_deg)

    elbow_x = l1 * np.cos(t1)
    elbow_y = l1 * np.sin(t1)

    tip_x = elbow_x + l2 * np.cos(t1 + t2)
    tip_y = elbow_y + l2 * np.sin(t1 + t2)

    return elbow_x, elbow_y, tip_x, tip_y


def plot_configuration(theta1_deg, theta2_deg, filename):
    """Generates and saves the 2D plot of the arm configuration."""
    elbow_x, elbow_y, tip_x, tip_y = compute_forward_kinematics(
        LINK_LENGTH_1, LINK_LENGTH_2, theta1_deg, theta2_deg
    )

    # Coordinates for lines
    x_coords = [0.0, elbow_x, tip_x]
    y_coords = [0.0, elbow_y, tip_y]

    fig, ax = plt.subplots(figsize=(6, 6))

    # Plot workspace limit boundary
    max_reach = LINK_LENGTH_1 + LINK_LENGTH_2
    workspace_circle = plt.Circle(
        (0, 0), max_reach, facecolor="whitesmoke", edgecolor="lightgray", fill=True, linestyle="--", label="Workspace Limit"
    )
    ax.add_patch(workspace_circle)

    # Plot links
    ax.plot(x_coords, y_coords, "-", color="navy", linewidth=4, zorder=2, label="Links")

    # Plot joints
    ax.scatter([0.0], [0.0], color="red", s=120, zorder=3, label="Base Joint")
    ax.scatter([elbow_x], [elbow_y], color="darkorange", s=100, zorder=3, label="Elbow Joint")
    ax.scatter([tip_x], [tip_y], color="forestgreen", s=120, marker="*", zorder=4, label="End-Effector Tip")

    # Set plot bounds and styling
    limit = max_reach + 0.2
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)
    ax.set_aspect("equal")
    ax.grid(True, linestyle=":", alpha=0.6)

    ax.set_title(f"2-Link Planar Robot Arm Configuration\n(theta1={theta1_deg}°, theta2={theta2_deg}°)", fontsize=11, fontweight="bold")
    ax.set_xlabel("X coordinate (meters)", fontsize=10)
    ax.set_ylabel("Y coordinate (meters)", fontsize=10)
    ax.legend(loc="upper right", framealpha=0.9)

    # Save figure
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    plt.savefig(filename, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved robot arm plot to: {filename}")


def main():
    print("=" * 60)
    print("Starting Lab 19: Plot Robot Arm")
    print("=" * 60)

    # Run for theta1 = 45° and theta2 = 90°
    plot_configuration(45.0, 90.0, SAVE_PATH)
    print("=" * 60)


if __name__ == "__main__":
    main()
