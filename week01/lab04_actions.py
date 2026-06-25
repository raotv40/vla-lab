"""
Week 1 - Lab 4: Exploring Action Space and Torque Control Dynamics
==================================================================

Objectives:
-----------
1. Understand the action space of Reacher-v4 (2D continuous torque limits).
2. Apply constant and time-varying torques to specific joints.
3. Observe how torque inputs translate to changes in angular velocity and position.
4. Log and analyze physical reactions to torque inputs.

Theory:
-------
In physical robotics, we control motors by sending current, which produces torque (rotational force).
In Reacher-v4, the action space is Box(-1.0, 1.0, (2,), float32):
- action[0]: Torque applied to the shoulder joint.
- action[1]: Torque applied to the elbow joint.

Because the system operates on torque (and not directly on joint angles or velocities), it is a dynamic system.
Applying a constant torque causes a joint to accelerate (Newton's Second Law for rotation: tau = I * alpha, where I is inertia and alpha is angular acceleration).
Friction and joint damping will eventually cap the velocity if the torque is held constant.

Expected Output:
----------------
A series of step logs showing the applied torques, the resulting angular velocities, and how the joint angles change over time.

Exercises:
----------
1. Modify the loop to apply negative torques. Observe the change in velocity direction.
2. Implement a sinusoidal torque input to both joints (e.g. action[0] = sin(t), action[1] = cos(t)) and log the resulting angular velocity values.
"""

import gymnasium as gym
import numpy as np

def main():
    print("--- Lab 04: Exploring Torque Control Dynamics ---")
    
    env = gym.make("Reacher-v4")
    observation, info = env.reset(seed=42)
    
    print("\nPhase 1: Applying maximum shoulder torque [1.0, 0.0] (Shoulder accelerates)...")
    for step in range(10):
        # Action: Full positive torque to shoulder, zero to elbow
        action = np.array([1.0, 0.0], dtype=np.float32)
        observation, reward, terminated, truncated, info = env.step(action)
        
        shoulder_vel = observation[6]
        elbow_vel = observation[7]
        print(f"Step: {step:2d} | Torque: [1.0,  0.0] | Shoulder Vel: {shoulder_vel:+6.3f} rad/s | Elbow Vel: {elbow_vel:+6.3f} rad/s")
        
    print("\nPhase 2: Applying maximum elbow torque [0.0, 1.0] (Elbow accelerates)...")
    for step in range(10):
        # Action: Zero to shoulder, full positive torque to elbow
        action = np.array([0.0, 1.0], dtype=np.float32)
        observation, reward, terminated, truncated, info = env.step(action)
        
        shoulder_vel = observation[6]
        elbow_vel = observation[7]
        print(f"Step: {step:2d} | Torque: [0.0,  1.0] | Shoulder Vel: {shoulder_vel:+6.3f} rad/s | Elbow Vel: {elbow_vel:+6.3f} rad/s")

    print("\nPhase 3: Applying opposing torque [-1.0, -1.0] (Braking and reversing)...")
    for step in range(10):
        action = np.array([-1.0, -1.0], dtype=np.float32)
        observation, reward, terminated, truncated, info = env.step(action)
        
        shoulder_vel = observation[6]
        elbow_vel = observation[7]
        print(f"Step: {step:2d} | Torque: [-1.0, -1.0] | Shoulder Vel: {shoulder_vel:+6.3f} rad/s | Elbow Vel: {elbow_vel:+6.3f} rad/s")
        
    env.close()
    print("--- Lab 04: Completed Successfully ---")

if __name__ == "__main__":
    main()
