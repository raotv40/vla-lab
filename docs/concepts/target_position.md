# Target Position

In robotics control and reinforcement learning, the **Target Position** (or setpoint) is the reference coordinate in world space that the robot is commanded to reach.

---

## Target Position in Reacher-v5

In `Reacher-v5`, the target is represented as a small red sphere spawning in a randomized 2D coordinate on each environment reset:
- **`obs[4]`**: $x_{\text{target}}$ (X coordinate)
- **`obs[5]`**: $y_{\text{target}}$ (Y coordinate)

---

## Key Characteristics in Reacher
- **Step Invariance (Static per Episode)**: The target is randomized on `env.reset()`, but it **remains static** throughout the course of a single episode. This is why when running `lab12_observation_changes.py`, indices 4 and 5 do not change.
- **Reference Frame**: Target positions are represented in the Cartesian coordinate frame relative to the robot's base origin $(0, 0)$.
