"""
Week 2 - Lab 23: Proportional-Integral (PI) Control of a Robotic Joint
=====================================================================

Objectives:
-----------
1. Implement a Proportional-Integral (PI) control feedback loop.
2. Demonstrate how integral gain (Ki) eliminates steady-state error under gravity.
3. Observe the compromise of PI control: overshoot and integral windup.

Theory:
-------
- Control law: u(t) = Kp * e(t) + Ki * integral(e(t)dt)
- Integral Action: Sums the error over time. Even a tiny error will accumulate
  and force the actuator output to increase, driving the steady-state error to zero.
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
SAVE_PATH = os.path.join(SAVE_DIR, "pi_controller.png")


def simulate_pi_control(kp, ki):
    """Simulates joint response under Proportional-Integral feedback control."""
    time_history = np.zeros(STEPS)
    pos_history = np.zeros(STEPS)
    torque_history = np.zeros(STEPS)

    pos = 0.0  # Initial position
    vel = 0.0  # Initial velocity
    integral = 0.0  # Integral accumulator

    for i in range(STEPS):
        # Calculate tracking error
        error = SETPOINT - pos

        # Update integral accumulator
        integral += error * DT

        # Anti-windup clamping to prevent torque saturation overshoot
        integral = np.clip(integral, -5.0, 5.0)

        # PI-Control Law
        torque = kp * error + ki * integral

        # Dynamic physics integration
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
    print("Starting Lab 23: PI-Controller Simulation")
    print("=" * 60)

    # Base Proportional Gain
    KP = 3.0

    # Simulate for different integral gains (Exercise 2)
    integral_gains = [0.0, 1.0, 3.0]
    colors = ["red", "orange", "blue"]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.axhline(SETPOINT, color="black", linestyle="--", alpha=0.7, label="Setpoint")

    for ki, color in zip(integral_gains, colors):
        t, pos, torques = simulate_pi_control(KP, ki)
        ax.plot(t, pos, color=color, linewidth=2, label=f"Kp = {KP:.1f}, Ki = {ki:.2f}")

        # Compute peak overshoot
        peak = np.max(pos)
        overshoot_pct = max(0.0, (peak - SETPOINT) / SETPOINT * 100.0)
        ss_error = SETPOINT - pos[-1]
        print(f"Ki = {ki:.2f} | SS Error: {ss_error:+.4f} rad | Overshoot: {overshoot_pct:.1f}%")

    ax.set_title("Robot Joint Step Response under Proportional-Integral (PI) Control", fontsize=11, fontweight="bold")
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
