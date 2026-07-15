"""
Week 2 - Lab 26: Trapezoidal Velocity Profile Generator
=======================================================

Objectives:
-----------
1. Generate a trapezoidal velocity profile dividing motion into acceleration, cruise, and deceleration.
2. Formulate step response evaluations across goal sweeps and step density variations.
3. Contrast trapezoidal smooth profile acceleration with linear profile jump boundaries.

Theory:
-------
- Accel phase: t in [0, ta] | Position rises quadratically, velocity rises linearly.
- Cruise phase: t in [ta, tf - ta] | Position rises linearly, velocity remains constant (v_max).
- Decel phase: t in [tf - ta, tf] | Position rises quadratically to goal, velocity falls linearly.
- Equations:
  D = goal - start
  v_max = D / (total_time - ta)
  acceleration_rate = v_max / ta
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Default Trajectory Constants
START = 0.0
GOAL = 10.0
TOTAL_TIME = 5.0
STEPS = 50
ACCEL_TIME = 1.5   # Time spent accelerating/decelerating (seconds)

# Output Paths
SAVE_DIR = os.path.join("assets", "day11")
SAVE_PATH = os.path.join(SAVE_DIR, "velocity_profile.png")


def generate_trapezoidal_profile(start, goal, total_time, steps, ta):
    """Generates time-stamped position, velocity, and acceleration values for a trapezoidal profile."""
    t = np.linspace(0, total_time, steps)
    dt = total_time / (steps - 1)

    # Total distance
    D = goal - start

    # Prevent acceleration time from exceeding half of total duration
    if ta > total_time / 2.0:
        ta = total_time / 2.0

    # Max cruising velocity
    v_max = D / (total_time - ta)
    accel_val = v_max / ta

    positions = np.zeros(steps)
    velocities = np.zeros(steps)
    accelerations = np.zeros(steps)

    for i, ti in enumerate(t):
        if ti < ta:
            # 1. Acceleration Phase
            velocities[i] = accel_val * ti
            positions[i] = start + 0.5 * accel_val * (ti ** 2)
            accelerations[i] = accel_val
        elif ti < total_time - ta:
            # 2. Cruising Phase (Constant Velocity)
            velocities[i] = v_max
            positions[i] = start + 0.5 * accel_val * (ta ** 2) + v_max * (ti - ta)
            accelerations[i] = 0.0
        else:
            # 3. Deceleration Phase
            t_dec = ti - (total_time - ta)
            velocities[i] = v_max - accel_val * t_dec
            positions[i] = (start + 0.5 * accel_val * (ta ** 2) +
                            v_max * (total_time - 2 * ta) +
                            v_max * t_dec - 0.5 * accel_val * (t_dec ** 2))
            accelerations[i] = -accel_val

    return t, positions, velocities, accelerations


def main():
    print("=" * 60)
    print("Starting Lab 26: Trapezoidal Velocity Profile Generator")
    print("=" * 60)

    # 1. Standard Case: Goal = 10, Steps = 50
    t1, pos1, vel1, accel1 = generate_trapezoidal_profile(START, 10.0, TOTAL_TIME, 50, ACCEL_TIME)
    print(f"Case 1 (Goal=10, Steps=50)  | Peak Vel: {np.max(vel1):.2f} | Peak Accel: {np.max(accel1):.2f}")

    # 2. Exercise 1: Goal = 20, Steps = 50
    t2, pos2, vel2, accel2 = generate_trapezoidal_profile(START, 20.0, TOTAL_TIME, 50, ACCEL_TIME)
    print(f"Case 2 (Goal=20, Steps=50)  | Peak Vel: {np.max(vel2):.2f} | Peak Accel: {np.max(accel2):.2f}")

    # 3. Exercise 2: Goal = 10, Steps = 100
    t3, pos3, vel3, accel3 = generate_trapezoidal_profile(START, 10.0, TOTAL_TIME, 100, ACCEL_TIME)
    print(f"Case 3 (Goal=10, Steps=100) | Peak Vel: {np.max(vel3):.2f} | Peak Accel: {np.max(accel3):.2f}")

    # 4. Exercise 3: Goal = 10, Steps = 10
    t4, pos4, vel4, accel4 = generate_trapezoidal_profile(START, 10.0, TOTAL_TIME, 10, ACCEL_TIME)
    print(f"Case 4 (Goal=10, Steps=10)  | Peak Vel: {np.max(vel4):.2f} | Peak Accel: {np.max(accel4):.2f}")

    # Plot comparisons
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(8, 8))

    # Position Plot
    ax1.plot(t1, pos1, color="blue", linewidth=2, label="Goal = 10 (Steps = 50)")
    ax1.plot(t2, pos2, color="orange", linewidth=2, linestyle="--", label="Goal = 20 (Steps = 50)")
    ax1.plot(t4, pos4, color="purple", marker="o", markersize=4, linestyle=":", label="Goal = 10 (Steps = 10)")
    ax1.set_ylabel("Position (units)", fontsize=10)
    ax1.set_title("Trapezoidal Velocity Profile Comparison", fontsize=11, fontweight="bold")
    ax1.grid(True, linestyle=":", alpha=0.6)
    ax1.legend(loc="upper left")

    # Velocity Plot
    ax2.plot(t1, vel1, color="blue", linewidth=2, label="Goal = 10 (Steps = 50)")
    ax2.plot(t2, vel2, color="orange", linewidth=2, linestyle="--", label="Goal = 20 (Steps = 50)")
    ax2.plot(t4, vel4, color="purple", marker="o", markersize=4, linestyle=":", label="Goal = 10 (Steps = 10)")
    ax2.set_ylabel("Velocity (units/s)", fontsize=10)
    ax2.grid(True, linestyle=":", alpha=0.6)
    ax2.legend(loc="upper left")

    # Acceleration Plot
    ax3.plot(t1, accel1, color="blue", linewidth=2, label="Goal = 10 (Steps = 50)")
    ax3.plot(t2, accel2, color="orange", linewidth=2, linestyle="--", label="Goal = 20 (Steps = 50)")
    ax3.plot(t4, accel4, color="purple", marker="o", markersize=4, linestyle=":", label="Goal = 10 (Steps = 10)")
    ax3.set_xlabel("Time (seconds)", fontsize=10)
    ax3.set_ylabel("Acceleration (units/s²)", fontsize=10)
    ax3.grid(True, linestyle=":", alpha=0.6)
    ax3.legend(loc="upper left")

    os.makedirs(SAVE_DIR, exist_ok=True)
    plt.savefig(SAVE_PATH, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"\nSaved velocity profile comparisons to: {SAVE_PATH}")
    print("=" * 60)


if __name__ == "__main__":
    main()
