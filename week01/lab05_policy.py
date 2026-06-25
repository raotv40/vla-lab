"""
Week 1 - Lab 5: Designing a Closed-Loop Feedback Control Policy
==============================================================

Objectives:
-----------
1. Understand the difference between open-loop and closed-loop control.
2. Implement a classic robotic control policy using the Transpose Jacobian method.
3. Compute the Jacobian matrix of a 2-link robotic arm in real-time.
4. Tune proportional (Kp) and derivative (Kd) control gains to minimize target error.
5. Successfully drive the arm to reach the target within 50 steps.

Theory:
-------
In open-loop control, actions are planned in advance without looking at the state. In closed-loop (feedback) control, the policy uses current observations to calculate actions.

Transpose Jacobian Control (Virtual Force Method):
Instead of solving the complex inverse kinematics equations to find target joint angles, we can define a virtual spring and damper that pulls the fingertip directly toward the target with a virtual force F:
- F = Kp * (target_pos - fingertip_pos) - Kd * fingertip_velocity

Where:
- target_pos - fingertip_pos is given in observations as [err_x, err_y].
- fingertip_velocity can be computed using the Jacobian J: v_fingertip = J * qvel.

To convert the Cartesian force F (in x, y coordinates) to joint torques (tau_shoulder, tau_elbow), we use the Transpose of the Jacobian matrix:
- torque = J^T * F

The Jacobian J for a 2-link arm with links l1 and l2:
- J = [ [dx/dq0, dx/dq1], [dy/dq0, dy/dq1] ]
- dx/dq0 = -l1*sin(q0) - l2*sin(q0 + q1)
- dx/dq1 = -l2*sin(q0 + q1)
- dy/dq0 = l1*cos(q0) + l2*cos(q0 + q1)
- dy/dq1 = l2*cos(q0 + q1)

Where:
- q0 is shoulder angle (theta1), q1 is elbow angle (theta2).
- we compute sin(q0+q1) and cos(q0+q1) using trigonometric identities:
  - sin(q0+q1) = sin(q0)cos(q1) + cos(q0)sin(q1)
  - cos(q0+q1) = cos(q0)cos(q1) - sin(q0)sin(q1)

Expected Output:
----------------
Console logs showing the fingertip distance decreasing step by step and a message confirming the target has been reached.

Exercises:
----------
1. Tune Kp and Kd. What happens if Kp is too high (e.g. 100.0) without increasing Kd? What happens if Kd is too high?
2. Compare the final target distance of the Jacobian policy with the random policy from Lab 2.
"""

import gymnasium as gym
import numpy as np

def compute_jacobian_transpose_control(obs, Kp=20.0, Kd=2.0):
    # Link lengths
    l1 = 0.1
    l2 = 0.11
    
    # 1. Extract values from observation
    c1, c2 = obs[0], obs[1]
    s1, s2 = obs[2], obs[3]
    qvel0, qvel1 = obs[6], obs[7]
    err_x, err_y = obs[8], obs[9]
    
    # 2. Compute trig identities for joint angle sum (q0 + q1)
    s12 = s1 * c2 + c1 * s2
    c12 = c1 * c2 - s1 * s2
    
    # 3. Compute Jacobian partial derivatives
    dx_dq0 = -l1 * s1 - l2 * s12
    dx_dq1 = -l2 * s12
    dy_dq0 =  l1 * c1 + l2 * c12
    dy_dq1 =  l2 * c12
    
    # J = np.array([[dx_dq0, dx_dq1], [dy_dq0, dy_dq1]])
    # J.T = np.array([[dx_dq0, dy_dq0], [dx_dq1, dy_dq1]])
    
    # 4. Compute fingertip Cartesian velocity
    # vx = dx/dq0 * qvel0 + dx/dq1 * qvel1
    # vy = dy/dq0 * qvel0 + dy/dq1 * qvel1
    vx = dx_dq0 * qvel0 + dx_dq1 * qvel1
    vy = dy_dq0 * qvel0 + dy_dq1 * qvel1
    
    # 5. Define virtual force (PD control in Cartesian space)
    # Since err_x is defined as fingertip_x - target_x, the force pulling the fingertip
    # to the target must be proportional to target_x - fingertip_x (which is -err_x).
    Fx = Kp * (-err_x) - Kd * vx
    Fy = Kp * (-err_y) - Kd * vy
    
    # 6. Map virtual force to joint torques: torque = J.T * F
    torque_shoulder = dx_dq0 * Fx + dy_dq0 * Fy
    torque_elbow    = dx_dq1 * Fx + dy_dq1 * Fy
    
    action = np.array([torque_shoulder, torque_elbow], dtype=np.float32)
    
    # Clip to action limits [-1.0, 1.0]
    return np.clip(action, -1.0, 1.0)

def main():
    print("--- Lab 05: Closed-Loop Feedback Control Policy ---")
    
    env = gym.make("Reacher-v4")
    observation, info = env.reset(seed=42)
    
    # Define controller gains
    Kp = 20.0
    Kd = 1.0
    
    print(f"Controller configured with gains: Kp = {Kp}, Kd = {Kd}")
    print("\nRunning closed-loop control episode...")
    
    step_count = 0
    total_reward = 0.0
    
    while True:
        # Calculate feedback action using the Jacobian Transpose policy
        action = compute_jacobian_transpose_control(observation, Kp=Kp, Kd=Kd)
        
        observation, reward, terminated, truncated, info = env.step(action)
        
        # Calculate current distance to target
        err_x, err_y = observation[8], observation[9]
        distance = np.sqrt(err_x**2 + err_y**2)
        
        total_reward += reward
        step_count += 1
        
        print(f"Step: {step_count:2d} | Torque: [{action[0]:+5.2f}, {action[1]:+5.2f}] | Distance to Target: {distance:6.4f}m | Reward: {reward:6.3f}")
        
        if terminated or truncated:
            break
            
    print(f"\nEpisode finished after {step_count} steps.")
    print(f"Final Distance to Target: {distance:6.4f}m")
    print(f"Total Cumulative Reward (Return): {total_reward:6.3f}")
    
    if distance < 0.02:
        print("Success! The policy successfully drove the robotic arm to the target.")
    else:
        print("The controller did not reach the target. Consider tuning gains.")
        
    env.close()
    print("--- Lab 05: Completed Successfully ---")

if __name__ == "__main__":
    main()
