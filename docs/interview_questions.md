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
