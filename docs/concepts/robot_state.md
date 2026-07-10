# Robot State

In robotics, the **Robot State** is the complete set of physical quantities required to uniquely describe the robot's physical configuration and dynamics at any specific point in time.

---

## State Space Components

For a robotic manipulator, the state is typically composed of:

1. **Generalized Coordinates ($\mathbf{q}$)**: The positions of all joints (e.g. angles for revolute joints, extensions for prismatic joints).
2. **Generalized Velocities ($\dot{\mathbf{q}}$)**: The rates of change of all joints (angular velocities, linear velocities).
3. **Generalized Accelerations ($\ddot{\mathbf{q}}$)**: The rates of change of velocities.

Mathematically, the dynamic state vector $\mathbf{x}$ is defined as:
$$\mathbf{x} = \begin{bmatrix} \mathbf{q} \\ \dot{\mathbf{q}} \end{bmatrix}$$

---

## State Representation in Reacher-v5

For the 2-joint Reacher arm, the physical state is represented by:
- **Joint Angles ($\mathbf{q}$)**: $\theta_1$ (shoulder angle) and $\theta_2$ (elbow angle).
- **Joint Velocities ($\dot{\mathbf{q}}$)**: $\dot{\theta}_1$ and $\dot{\theta}_2$.

Thus, the core physical state of the Reacher arm is a 4D vector:
$$\mathbf{x} = \begin{bmatrix} \theta_1 \\ \theta_2 \\ \dot{\theta}_1 \\ \dot{\theta}_2 \end{bmatrix}$$
Knowing these four values is sufficient to describe the entire configuration and momentum of the arm links.
