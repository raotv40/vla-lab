"""
Week 2 - Lab 24: Proportional-Integral-Derivative (PID) Control of a Robotic Joint
================================================================================

Objectives:
-----------
1. Implement a full Proportional-Integral-Derivative (PID) control feedback loop.
2. Demonstrate how derivative gain (Kd) acts as predictive damping to suppress overshoot.
3. Analyze transient metrics including settling time and overshoot reduction (Exercise 3).

Theory:
-------
- Control law: u(t) = Kp * e(t) + Ki * integral(e(t)dt) + Kd * de(t)/dt
- Derivative Action: Evaluates error slope. If the error is closing rapidly,
  derivative feedback acts as a predictive brake, damping oscillation and overshoot.
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
SAVE_PATH = os.path.join(SAVE_DIR, "pid_controller.png")


def simulate_pid_control(kp, ki, kd):
    """Simulates joint response under PID feedback control."""
    time_history = np.zeros(STEPS)
    pos_history = np.zeros(STEPS)
    torque_history = np.zeros(STEPS)

    pos = 0.0  # Initial position
    vel = 0.0  # Initial velocity
    integral = 0.0  # Integral accumulator
    prev_error = SETPOINT - pos  # Initial error

    for i in range(STEPS):
        # Calculate tracking error
        error = SETPOINT - pos

        # Update integral accumulator
        integral += error * DT
        integral = np.clip(integral, -5.0, 5.0)

        # Derivative error rate of change (delta error / dt)
        deriv = (error - prev_error) / DT

        # PID-Control Law
        torque = kp * error + ki * integral + kd * deriv

        # Dynamic physics integration
        accel = (torque - DAMPING * vel - GRAVITY) / INERTIA

        # Euler-Cromer Integration
        vel += accel * DT
        pos += vel * DT

        # Log history
        time_history[i] = i * DT
        pos_history[i] = pos
        torque_history[i] = torque

        # Save error for next step
        prev_error = error

    return time_history, pos_history, torque_history


def main():
    print("=" * 60)
    print("Starting Lab 24: PID-Controller Simulation")
    print("=" * 60)

    # Base Proportional and Integral Gains
    KP = 3.0
    KI = 1.0

    # Simulate for different derivative gains (Exercise 3)
    derivative_gains = [0.0, 0.2, 0.5]
    colors = ["red", "orange", "blue"]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.axhline(SETPOINT, color="black", linestyle="--", alpha=0.7, label="Setpoint")

    for kd, color in zip(derivative_gains, colors):
        t, pos, torques = simulate_pid_control(KP, KI, kd)
        ax.plot(t, pos, color=color, linewidth=2, label=f"Kp=0.8, Ki=0.1, Kd={kd:.1f}")

        # Compute overshoot and settling time (time taken to remain within 2% band of setpoint)
        peak = np.max(pos)
        overshoot_pct = max(0.0, (peak - SETPOINT) / SETPOINT * 100.0)
        ss_error = SETPOINT - pos[-1]

        # Find settling time
        settled_idx = np.where(np.abs(pos - SETPOINT) > 0.02)[0]
        settling_time = (settled_idx[-1] + 1) * DT if len(settled_idx) > 0 else 0.0

        print(f"Kd = {kd:.1f} | Overshoot: {overshoot_pct:.1f}% | Settling Time: {settling_time:.2f}s | SS Error: {ss_error:+.4f} rad")

    ax.set_title("Robot Joint Step Response under PID Control", fontsize=11, fontweight="bold")
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
