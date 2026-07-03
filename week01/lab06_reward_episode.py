"""
Week 1 - Lab 6: Reward and Episode Dynamics in Gymnasium
========================================================

Objectives:
-----------
1. Explore the concepts of step transitions, reward signals, and episodes in Gymnasium.
2. Analyze the reward formulation of the Reacher environment.
3. Understand the difference between episode termination (reaching terminal state) and truncation (time limits).
4. Run a passive control step loop to track cumulative reward accumulation.

Theory:
-------
Reinforcement learning operates on an agent-environment feedback loop:
1. The environment is reset to an initial observation using `reset()`.
2. The agent executes an action.
3. The environment steps forward in time using `step(action)`, returning:
   - observation: The new state of the world.
   - reward: A scalar value indicating the quality of the action.
   - terminated: A boolean showing if the agent reached a goal or a terminal state.
   - truncated: A boolean showing if the episode was ended by a time limit or budget.
   - info: Additional diagnostic logs.

Reacher Reward Function:
The reward is calculated as:
- reward = -distance - control_effort
Where:
- distance: The Euclidean distance from the fingertip to the target.
- control_effort: The sum of squared torques applied.

Since actions in this lab are [0, 0] (passive dynamics), the control effort is 0, and the reward is simply the negative distance.

Expected Output:
----------------
Console logs showing the step index, step reward, and running total reward (cumulative return).
Example:
Step   0 | Reward:  -0.125 | Total Reward:   -0.125
Step   1 | Reward:  -0.125 | Total Reward:   -0.250
...
Episode Truncated

Exercises:
----------
1. Change the action to a constant positive value, e.g. [0.5, 0.5], and observe how the reward changes due to control effort penalties.
2. Run a loop that prints the difference between the reward at step `t` and step `t-1` to observe if the arm is moving closer or further away from the target due to gravity.
"""

import gymnasium as gym

def main():
    # 1. Initialize environment
    # We use Reacher-v5 (the latest version of the Reacher task)
    env = gym.make("Reacher-v5")
    
    # 2. Reset environment to obtain initial state
    obs, info = env.reset(seed=42)
    
    print("=" * 50)
    print("Reward and Episode Demo - Passive Control [0.0, 0.0]")
    print("=" * 50)
    
    total_reward = 0.0
    
    # 3. Simulate step transition loop
    for step in range(100):
        # Apply zero torque action (passive arm behavior)
        action = [0.0, 0.0]
        
        # Step environment dynamics
        obs, reward, terminated, truncated, info = env.step(action)
        
        # Accumulate cumulative reward (return)
        total_reward += reward
        
        print(
            f"Step {step:3d} | "
            f"Reward: {reward:7.3f} | "
            f"Total Reward: {total_reward:8.3f}"
        )
        
        # Check termination or truncation flags
        if terminated:
            print("\nEpisode Terminated (Goal reached or invalid state)")
            break
            
        if truncated:
            print("\nEpisode Truncated (Time limit reached)")
            break
            
    # 4. Close environment resources
    env.close()
    print("=" * 50)

if __name__ == "__main__":
    main()