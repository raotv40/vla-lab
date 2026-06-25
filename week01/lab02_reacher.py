"""
Week 1 - Lab 2: Gymnasium Reacher-v4 Environment Integration
============================================================

Objectives:
-----------
1. Initialize the Gymnasium 'Reacher-v4' environment.
2. Inspect the structure, dimensions, and limits of the observation and action spaces.
3. Understand the Gymnasium loop (reset, step, terminated, truncated, reward, info).
4. Run a simulation episode with a random agent (applying random actions).

Theory:
-------
Gymnasium is the standard API for reinforcement learning in Python.
The Reacher-v4 environment simulates a two-jointed robotic arm on a 2D plane trying to touch a target.
Key concepts:
- Observation Space: What the agent sees. For Reacher-v4, this is a 10-dimensional continuous vector.
- Action Space: What the agent does. For Reacher-v4, this is a 2-dimensional continuous torque vector.
- Episode termination vs. truncation:
  - Terminated: The agent reached a terminal state (not applicable for Reacher unless specified, typically runs for a fixed step length).
  - Truncated: The environment reached its time limit (default is 50 steps for Reacher-v4).

Expected Output:
----------------
Console logs detailing the shape of observation and action spaces, followed by step logs showing action applied, reward received, and state status.
Example:
Observation space: Box(-inf, inf, (10,), float64)
Action space: Box(-1.0, 1.0, (2,), float32)
Step: 1 | Action: [-0.12,  0.45] | Reward: -0.082 | Terminated: False | Truncated: False
...

Exercises:
----------
1. Change the code to run the environment with visual rendering (render_mode="human") and observe the behavior (requires a display/GUI environment).
2. Write a loop to run 5 consecutive episodes and calculate the average cumulative reward obtained by a random policy.
"""

import gymnasium as gym
import numpy as np

def main():
    print("--- Lab 02: Initializing Gymnasium Reacher-v4 ---")
    
    # 1. Initialize environment
    # We use render_mode=None (headless) by default to ensure it runs anywhere.
    # To see the visualization, change render_mode to "human".
    try:
        env = gym.make("Reacher-v4", render_mode=None)
        print("Successfully created Reacher-v4 environment.")
    except Exception as e:
        print(f"Error creating Reacher-v4 environment: {e}")
        print("Make sure you have gymnasium[mujoco] and mujoco installed.")
        return
        
    # 2. Inspect Action and Observation Space
    obs_space = env.observation_space
    act_space = env.action_space
    
    print(f"Observation Space: {obs_space}")
    print(f"Observation Space Low: {obs_space.low}")
    print(f"Observation Space High: {obs_space.high}")
    print(f"Action Space: {act_space}")
    print(f"Action Space Low: {act_space.low}")
    print(f"Action Space High: {act_space.high}")
    
    # 3. Reset the environment to get initial observation
    # Reset returns a tuple: (observation, info)
    observation, info = env.reset(seed=42)
    print(f"\nInitial Observation: {observation}")
    print(f"Initial Info: {info}")
    
    # 4. Step through the environment using random actions
    print("\nRunning a single episode with a random policy...")
    total_reward = 0.0
    step_count = 0
    
    while True:
        # Sample a random action from the action space
        action = act_space.sample()
        
        # Step the environment forward
        # Step returns: (observation, reward, terminated, truncated, info)
        observation, reward, terminated, truncated, info = env.step(action)
        
        total_reward += reward
        step_count += 1
        
        print(f"Step: {step_count:2d} | Action: [{action[0]:5.2f}, {action[1]:5.2f}] | Reward: {reward:6.3f} | Terminated: {terminated} | Truncated: {truncated}")
        
        if terminated or truncated:
            break
            
    print(f"\nEpisode finished after {step_count} steps.")
    print(f"Total Cumulative Reward (Return): {total_reward:6.3f}")
    
    # 5. Clean up the environment resources
    env.close()
    print("--- Lab 02: Completed Successfully ---")

if __name__ == "__main__":
    main()
