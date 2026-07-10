# Action Space

The **Action Space** defines the set of all valid actions that the agent is allowed to execute in the environment. It specifies the mathematical format, shape, limits, and type of control commands.

---

## Action Space of Reacher-v5

In `Reacher-v5`, the action space is continuous and is represented as:
$$\text{Action Space} = \text{Box}(-1.0, 1.0, (2,), \text{float32})$$

Where:
- **Shape `(2,)`**: Represents two joint torque commands (shoulder joint and elbow joint).
- **Bounds `[-1.0, 1.0]`**: Defines the maximum normalized joint torque limits.
- **Dtype `float32`**: Corresponds to single-precision floating-point format (typical for deep learning framework parameters).

---

## Continuous vs. Discrete Actions

- **Continuous Space**: Actions can take any real value within a range (e.g. applying a specific torque command like $+0.427\,\text{N}\cdot\text{m}$). Standard for robotic arms, quadcopters, and autonomous driving.
- **Discrete Space**: Actions represent discrete index commands (e.g. `0` for left, `1` for right). Standard for Atari games or grid-world paths.
