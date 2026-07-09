# Robotics & Embodied AI Interview Questions

This document contains a structured study guide of interview questions and answers based on Day 1 and Day 2 concepts.

---

## Question 1: What is the fundamental difference between `mjModel` and `mjData` in MuJoCo?

### Answer:
MuJoCo separates state representations to maximize cache efficiency and maintain a clean separation between the static environment layout and its dynamic state:
- **`mjModel`**: Defines the physical, static configuration of the robot and world. This includes geometries, body masses, inertial parameters, joints, actuators, bounds, and gravity directions. It is loaded once from the XML and does not change during simulation steps.
- **`mjData`**: Represents the dynamic, time-varying state of the simulation. This contains the current time, joint angles (`qpos`), joint velocities (`qvel`), actuator forces, contact forces, and the output variables computed by the solver. It is modified at every call of `mj_step`.

---

## Question 2: Detail the contents of the 10-dimensional observation vector returned by Gymnasium's `Reacher-v4`.

### Answer:
The observation space of `Reacher-v4` is represented as a 10D vector:
1. **`obs[0]`**: $\cos(\theta_1)$ - Cosine of the shoulder joint angle.
2. **`obs[1]`**: $\cos(\theta_2)$ - Cosine of the elbow joint angle (relative to the shoulder link).
3. **`obs[2]`**: $\sin(\theta_1)$ - Sine of the shoulder joint angle.
4. **`obs[3]`**: $\sin(\theta_2)$ - Sine of the elbow joint angle.
5. **`obs[4]`**: Target X coordinate in world space.
6. **`obs[5]`**: Target Y coordinate in world space.
7. **`obs[6]`**: $\dot{\theta}_1$ - Angular velocity of the shoulder joint (rad/s).
8. **`obs[7]`**: $\dot{\theta}_2$ - Angular velocity of the elbow joint (rad/s).
9. **`obs[8]`**: $err_x$ - X-distance from fingertip to target ($x_{\text{target}} - x_{\text{fingertip}}$).
10. **`obs[9]`**: $err_y$ - Y-distance from fingertip to target ($y_{\text{target}} - y_{\text{fingertip}}$).

---

## Question 3: Why are actions in the Reacher environment represented as torque commands instead of direct joint angles?

### Answer:
In physical robots, motors cannot instantly teleport joints to a specific angle because of mass, inertia, and joint limits. Instead, motors apply electrical current, which creates a rotational force (**torque**).
Commanding torques rather than angles forces the simulator to resolve the true equations of motion (Newton's laws):
- Acceleration is determined by torque, inertia, gravity, and contact forces.
- Velocities and angles are computed by numerically integrating this acceleration.
This is called **torque control** (or force control) and is crucial for learning policies that transfer robustly to physical robotic systems (reducing the sim-to-real gap).

---

## Question 4: How does Transpose Jacobian Control work, and why does it avoid solving Inverse Kinematics (IK)?

### Answer:
Inverse Kinematics (IK) calculates target joint angles $(\theta_1, \theta_2)$ from a target Cartesian position $(x, y)$, which can be computationally expensive and non-unique.
**Transpose Jacobian Control** avoids IK by simulating a virtual spring pulling the robot's fingertip directly to the target.
1. We define a virtual force vector $F = [F_x, F_y]^T$ pulling the fingertip to the target:
   $$F = K_p(x_{\text{target}} - x_{\text{tip}}) - K_d v_{\text{tip}}$$
2. We project this Cartesian force directly to joint torques $\tau$ using the transpose of the Jacobian matrix $J$:
   $$\tau = J^T F$$
Since $J$ is easy to calculate analytically from the forward kinematics, this method is computationally cheap, handles singularities gracefully, and drives the arm directly toward the target without ever needing to solve the joint angles.

---

## Question 5: Compare "Passive Simulation" and "Active Simulation" in MuJoCo.

### Answer:
- **Passive Simulation**: The system moves solely due to external forces (such as gravity, contact, damping, or initial momentum). No control signals or actuator forces are actively applied. For example, simulating a ball falling or a pendulum swinging freely.
- **Active Simulation**: Actuators actively apply joint forces or torques computed by an external controller or policy at each timestep. This allows the system to perform goal-directed behaviors, like a robotic arm reaching toward a point.

---

## Question 6: What is the math behind the reward function of Gymnasium's Reacher environment, and how does it balance path efficiency and power usage?

### Answer:
The reward $R_t$ at step $t$ in the Reacher environment is designed to guide the agent to the target while minimizing excessive control effort:
$$R_t = -d_{\text{fingertip, target}} - \|\mathbf{a}_t\|^2$$
Where:
1. **Distance Penalty** ($-d_{\text{fingertip, target}}$): The negative Euclidean distance between the fingertip and the target. This term dominates the signal, encouraging the policy to drive the error to zero.
2. **Control Effort Penalty** ($-\|\mathbf{a}_t\|^2$): The negative sum of squared actuator torques applied at the current step. This penalizes rapid, jerky joint commands, encouraging smooth, energy-efficient trajectories and protecting physical motor gears from high-frequency wear.

---

## Question 7: Explain the difference between `terminated` and `truncated` in the Gymnasium step function returns, and why it is important to distinguish them in Reinforcement Learning.

### Answer:
Gymnasium separates episode ending conditions into two flags:
- **`terminated`**: Indicates that the episode ended naturally due to reaching a terminal state defined by the MDP task design (e.g. falling over, reaching the target goal, or failing irreversibly). In these cases, no further rewards are possible.
- **`truncated`**: Indicates that the episode was cut short due to an external agent-independent constraint (e.g. reaching a step limit like 50/100 steps, or manual operator override).

In Reinforcement Learning, distinguishing these is crucial for bootstrapping and value estimation. If an episode is truncated, the agent's value function should bootstrap (predict future returns from the final state) because the task wasn't finished. If terminated, the target value is simply the immediate reward since no future states exist.

---

## Question 8: What is a "Transition" in Markov Decision Processes (MDPs), and what are its components?

### Answer:
A transition is the fundamental unit of interaction between an RL agent and its environment. It represents a single step of experience and is defined by the tuple:
$$\left(s_t, a_t, r_t, s_{t+1}, d_t\right)$$
Where:
- $s_t$: The state (or observation) at time step $t$.
- $a_t$: The action chosen by the policy at time step $t$.
- $r_t$: The scalar reward received from the environment.
- $s_{t+1}$: The resulting state (or observation) at time step $t+1$.
- $d_t$: The done/termination flag indicating if the transition led to an absorbing state.

---

# Day 4: Policy Dynamics, Exploration, and Exploitation

## Beginner: Explain the concept of a Policy ($\pi$) in Reinforcement Learning, and contrast a Random Policy with a Fixed Policy.

### Answer:
- **Policy ($\pi$)**: A policy is the "brain" or decision-making rule of an agent. It defines how the agent behaves at any given time by mapping observations (or states) to actions. Mathematically, it is either deterministic ($a = \pi(s)$) or stochastic ($\pi(a \mid s)$).
- **Random Policy**: A policy where actions are sampled uniformly at random from the action space, independent of observations (i.e., $\pi(a \mid s) = \frac{1}{|A|}$). It represents the maximum exploration baseline.
- **Fixed Policy**: A policy where the agent executes a constant, pre-determined action profile (e.g. constant torque $\mathbf{a} = [0.1, 0.0]$) at every step, ignoring environmental observations. It is an open-loop controller.

---

## Intermediate: Define "Exploration" and "Exploitation" in RL, and explain why both a pure random policy and a pure fixed policy struggle to solve environments like Reacher.

### Answer:
- **Exploration**: Gathering new information about the environment by taking novel actions. This helps the agent discover new state-action pairs and locate high-reward regions.
- **Exploitation**: Maximizing immediate rewards by choosing the best-known actions based on the agent's current knowledge.
- **Why they fail on Reacher**:
  - **Pure Random Policy**: Over-explores. It continuously switches joint torques at random, causing the arm to wiggle aimlessly near the origin. It never exploits its observations to steer toward and settle on the target.
  - **Pure Fixed Policy**: Over-exploits a static assumption. Because it ignores observations (open-loop), it cannot adapt to different randomized target coordinates. If the target spawns in a different quadrant, a constant torque profile will completely miss it.
  - **Solution**: A closed-loop feedback policy (like Transpose Jacobian or RL network) is required to dynamically exploit observations while exploring paths toward the target.

---

## Advanced: How does the concept of "Episode Return" (Cumulative Reward) change when transitioning from finite-horizon tasks to infinite-horizon tasks? Explain the role of the discount factor ($\gamma$) and why it is mathematically necessary.

### Answer:
- **Finite Horizon**: The episode has a fixed or bounded length $T$. The return $G_t$ is a simple sum of rewards:
  $$G_t = \sum_{k=0}^{T-1} R_{t+k+1}$$
- **Infinite Horizon**: The interaction continues indefinitely ($T = \infty$). The undiscounted sum of rewards could diverge to infinity:
  $$G_t = \sum_{k=0}^{\infty} R_{t+k+1} = \pm \infty$$
- **Role of Discount Factor ($\gamma \in [0, 1)$)**: To keep the return mathematically bounded (finite), we discount future rewards:
  $$G_t = \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}$$
  If the rewards are bounded by a constant $R_{\max}$, the discounted return is guaranteed to converge:
  $$G_t \leq \frac{R_{\max}}{1 - \gamma}$$
- **Physical Interpretation**: $\gamma$ balances the agent's preference for immediate gratification ($\gamma \to 0$) vs. long-term planning ($\gamma \to 1$).


