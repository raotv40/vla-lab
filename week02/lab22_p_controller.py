"""
Week 2 - Lab 22: Proportional (P) Control of a Robotic Joint
============================================================

Objectives:
-----------
1. Simulate a second-order mechanical robot joint (with inertia, damping, and gravity).
2. Implement a Proportional (P) control feedback loop.
3. Observe how proportional gain (Kp) affects rise time, steady-state offset, and stability.

Theory:
-------
- Control law: u(t) = Kp * e(t)
- Plant dynamics: joint acceleration = u - damping * velocity - gravity_disturbance
- Steady-state error: A pure P-controller requires a non-zero error to output any command force.
  Under gravity, the arm sag error is e_ss = gravity / Kp.
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Simulation Constants
DT = 0.01          # Time step (seconds)
SIM_TIME = 8.0     # Total simulation time (seconds)
STEPS = int(SIM_TIME / DT)

SETPOINT = 1.0     # Desired joint position (radians)
INERTIA = 1.0      # Rotational inertia (kg * m^2)
DAMPING = 1.0      # Friction coefficient (N * m * s / rad)
GRAVITY = 0.5      # Gravity disturbance torque (N * m)

# Output Paths
SAVE_DIR = os.path.join("assets", "day10")
SAVE_PATH = os.path.join(SAVE_DIR, "p_controller.png")


def simulate_p_control(kp):
    """Simulates joint response under Proportional feedback control."""
    time_history = np.zeros(STEPS)
    pos_history = np.zeros(STEPS)
    torque_history = np.zeros(STEPS)

    pos = 0.0  # Initial position
    vel = 0.0  # Initial velocity

    for i in range(STEPS):
        # Calculate tracking error
        error = SETPOINT - pos

        # P-Control Law
        torque = kp * error

        # Dynamic physics integration (acceleration)
        accel = (torque - DAMPING * vel - GRAVITY) / INERTIA

        # Euler-Cromer Integration
        vel += accel * DT
        pos += vel * DT

        # Log history
        time_history[i] = i * DT
        pos_history[i] = pos
        torque_history[i] = torque

    return time_history, pos_history, torque_history


def main():
    print("=" * 60)
    print("Starting Lab 22: P-Controller Simulation")
    print("=" * 60)

    # Simulate for different proportional gains (Exercise 1)
    gains = [0.5, 0.8, 2.5]
    colors = ["red", "orange", "blue"]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.axhline(SETPOINT, color="black", linestyle="--", alpha=0.7, label="Setpoint")

    for kp, color in zip(gains, colors):
        t, pos, torques = simulate_p_control(kp)
        ax.plot(t, pos, color=color, linewidth=2, label=f"Kp = {kp:.1f}")

        # Print final steady-state error
        ss_error = SETPOINT - pos[-1]
        print(f"Kp = {kp:.1f} | Final Position: {pos[-1]:.4f} rad | Steady-State Error: {ss_error:+.4f} rad")

    ax.set_title("Robot Joint Step Response under Proportional (P) Control", fontsize=11, fontweight="bold")
    ax.set_xlabel("Time (seconds)", fontsize=10)
    ax.set_ylabel("Joint Position (radians)", fontsize=10)
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend(loc="lower right")

    os.makedirs(SAVE_DIR, exist_ok=True)
    plt.savefig(SAVE_PATH, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"\nSaved step response plot to: {SAVE_PATH}")
    print("=" * 60)


if __name__ == "__main__":
    main()
