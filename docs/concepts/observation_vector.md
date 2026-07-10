# Observation Vector

An **Observation Vector** (or state observation) is a one-dimensional array of numerical features returned by the environment at each step representing what the agent currently perceives about its own state and its surrounding workspace.

---

## Reacher-v5 Observation Vector Breakdown

In Gymnasium's `Reacher-v5` environment, the observation space is represented as a 10D vector:

| Index | Name | Description | Physical Unit | Bounds |
| :--- | :--- | :--- | :--- | :--- |
| **`obs[0]`** | `cos(theta1)` | Cosine of shoulder joint angle | Dimensionless | $[-1, 1]$ |
| **`obs[1]`** | `cos(theta2)` | Cosine of elbow joint angle (relative to shoulder link) | Dimensionless | $[-1, 1]$ |
| **`obs[2]`** | `sin(theta1)` | Sine of shoulder joint angle | Dimensionless | $[-1, 1]$ |
| **`obs[3]`** | `sin(theta2)` | Sine of elbow joint angle (relative to shoulder link) | Dimensionless | $[-1, 1]$ |
| **`obs[4]`** | `target_x` | Target coordinate along X-axis | Meters | $[-0.27, 0.27]$ |
| **`obs[5]`** | `target_y` | Target coordinate along Y-axis | Meters | $[-0.27, 0.27]$ |
| **`obs[6]`** | `qvel_shoulder`| Angular velocity of shoulder joint | Radians per second ($\text{rad/s}$) | $[-\infty, \infty]$ |
| **`obs[7]`** | `qvel_elbow` | Angular velocity of elbow joint | Radians per second ($\text{rad/s}$) | $[-\infty, \infty]$ |
| **`obs[8]`** | `error_x` | X-axis distance from fingertip to target ($x_{\text{target}} - x_{\text{fingertip}}$) | Meters | $[-0.27, 0.27]$ |
| **`obs[9]`** | `error_y` | Y-axis distance from fingertip to target ($y_{\text{target}} - y_{\text{fingertip}}$) | Meters | $[-0.27, 0.27]$ |

---

## Role in Reinforcement Learning

The observation vector is the input to the agent's policy:
$$\mathbf{a}_t = \pi(\mathbf{o}_t)$$

The agent uses this vector to compute the correct action. For example:
- In closed-loop classical feedback (Transpose Jacobian), target errors (`obs[8:10]`) are used to project Cartesian forces to joint torques.
- In neural network reinforcement learning, the entire 10D vector is passed to the input layer of the policy network.
