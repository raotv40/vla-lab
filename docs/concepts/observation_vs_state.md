# Observation vs. Robot State

In robotics and reinforcement learning, the terms **State** and **Observation** are related but represent different concepts regarding how system state information is accessed.

---

## Definitions

- **Robot State ($\mathbf{s}$)**: The complete, true physical configuration of the system. It contains all variables required to reconstruct the physical world (e.g. raw joint angles $\theta_1, \theta_2$, velocities $\dot{\theta}_1, \dot{\theta}_2$, target coordinates, and joint forces). The state is often unmeasurable in the real world due to sensor noise or occlusions.
- **Observation ($\mathbf{o}$)**: The subset of processed sensor measurements actually available to the controller or agent at a specific time step. It represents a transformed or partially observed feature vector.

---

## Comparison Table

| Property | Robot State ($\mathbf{s}$) | Observation ($\mathbf{o}$) |
| :--- | :--- | :--- |
| **Completeness** | Full physical completeness | Often partial or noisy |
| **Coordinate Space**| Raw physical units (e.g. radians) | Engineered features (e.g. sines, cosines) |
| **Sensor Dependency**| Independent of sensors | Dependent on sensor configuration |
| **Availability** | Simulator internal (MuJoCo `mjData`) | API outputs (Gymnasium observation vector) |

### Reacher-v5 Example
- **State**: Raw joint angles in radians: `[theta1, theta2, dtheta1, dtheta2]`.
- **Observation**: 10D feature vector containing sines/cosines of joint angles, target positions, velocities, and Cartesian error vectors.
