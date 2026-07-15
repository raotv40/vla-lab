"""
Week 2 - Lab 25: Linear Trajectory Generation
=============================================

Objectives:
-----------
1. Generate a basic linear interpolation (LERP) trajectory between a start and goal.
2. Analyze why constant velocity profiles require infinite acceleration at boundaries.
3. Observe the behavior of position and velocity waveforms under linear planning.

Theory:
-------
- Position equation: x(t) = start + (goal - start) * (t / total_time)
- Velocity equation: v(t) = (goal - start) / total_time (constant)
- Acceleration: a(t) = 0 everywhere, except at t = 0 and t = total_time where
  acceleration is infinite (impulse functions delta(t)).
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Trajectory Constants
START = 0.0        # Start position (radians/meters)
GOAL = 10.0        # Goal position (radians/meters)
TOTAL_TIME = 5.0   # Total trajectory time (seconds)
STEPS = 50         # Number of intermediate waypoints

# Output Paths
SAVE_DIR = os.path.join("assets", "day11")
SAVE_PATH = os.path.join(SAVE_DIR, "linear_trajectory.png")


def generate_linear_trajectory(start, goal, total_time, steps):
    """Computes a linear interpolation trajectory over time."""
    t = np.linspace(0, total_time, steps)
    dt = total_time / (steps - 1)

    # Compute constant velocity
    velocity_val = (goal - start) / total_time

    # Position is a linear ramp
    positions = start + (goal - start) * (t / total_time)

    # Velocity is constant (except at boundaries, but we represent the continuous segment)
    velocities = np.full(steps, velocity_val)
    velocities[0] = 0.0
    velocities[-1] = 0.0

    # Acceleration is zero inside the trajectory
    accelerations = np.zeros(steps)

    return t, positions, velocities, accelerations


def main():
    print("=" * 60)
    print("Starting Lab 25: Linear Trajectory Generator")
    print("=" * 60)

    # Generate default trajectory
    t, pos, vel, accel = generate_linear_trajectory(START, GOAL, TOTAL_TIME, STEPS)

    print(f"Start Position : {START:.2f}")
    print(f"Goal Position  : {GOAL:.2f}")
    print(f"Total Time     : {TOTAL_TIME:.2f} seconds")
    print(f"Number of Steps: {STEPS}")
    print(f"Calculated Constant Velocity: {vel[1]:.4f} units/sec")

    # Plot position and velocity
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

    # Position plot
    ax1.plot(t, pos, color="blue", linewidth=2, label="Position")
    ax1.axhline(GOAL, color="black", linestyle="--", alpha=0.5, label="Setpoint Goal")
    ax1.set_ylabel("Position (units)", fontsize=10)
    ax1.set_title("Linear Trajectory (LERP) Waveforms", fontsize=11, fontweight="bold")
    ax1.grid(True, linestyle=":", alpha=0.6)
    ax1.legend(loc="upper left")

    # Velocity plot
    ax2.plot(t, vel, color="red", linewidth=2, label="Velocity")
    # Annotate boundary velocity jumps to show infinite acceleration
    ax2.annotate("Infinite Acceleration", xy=(0, 0), xytext=(0.5, vel[1]*0.4),
                 arrowprops=dict(facecolor='black', shrink=0.08, width=1, headwidth=6))
    ax2.annotate("Infinite Deceleration", xy=(TOTAL_TIME, 0), xytext=(TOTAL_TIME-2.0, vel[1]*0.4),
                 arrowprops=dict(facecolor='black', shrink=0.08, width=1, headwidth=6))

    ax2.set_xlabel("Time (seconds)", fontsize=10)
    ax2.set_ylabel("Velocity (units/s)", fontsize=10)
    ax2.grid(True, linestyle=":", alpha=0.6)
    ax2.legend(loc="upper left")

    os.makedirs(SAVE_DIR, exist_ok=True)
    plt.savefig(SAVE_PATH, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"\nSaved linear trajectory plot to: {SAVE_PATH}")
    print("=" * 60)


if __name__ == "__main__":
    main()
