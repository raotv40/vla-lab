# Joint Velocity

**Joint Velocity** is the time rate of change of joint positions. It represents how fast a robot joint is rotating (revolute joints) or translating (prismatic joints).

---

## Representation in Reacher-v5

Joint velocities are represented in radians per second ($\text{rad/s}$):
- **`obs[6]`**: $\dot{\theta}_1$ (angular velocity of shoulder joint).
- **`obs[7]`**: $\dot{\theta}_2$ (angular velocity of elbow joint).

---

## Importance in Robotics

- **Dynamics Calculations**: Joint velocities determine the Coriolis and centrifugal forces acting on the robotic links during motion.
- **Damping Control**: Closed-loop control algorithms use velocity feedback to apply dampening forces (damping term $K_d \cdot \dot{\theta}$), preventing the robot from oscillating wildly or overshooting target coordinates.
- **Safety Boundaries**: Real-world robot controllers enforce maximum velocity limits to prevent joint damage.
