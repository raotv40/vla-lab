# Observation Space

The **Observation Space** defines the set of all possible values that the environment can return as observations. It establishes the mathematical bounds, shape, and data types of the state descriptors.

---

## Purpose in Robotics and RL

- **API Standardization**: Dictates the shape of the neural network's input layers.
- **Out-of-Bounds Detection**: Ensures observations remain within physical limits.
- **Policy Tuning**: Allows algorithms to normalize observations (e.g. scaling feature variables between $0$ and $1$).

---

## Space Types in Gymnasium

Gymnasium environments support several space types:
1. **`gym.spaces.Box`**: Represents continuous multidimensional spaces (e.g. Reacher joint angles, coordinates, velocities).
2. **`gym.spaces.Discrete`**: Represents discrete choices (e.g. actions like moving left/right/up/down in grid worlds).
3. **`gym.spaces.Dict`**: Combines multiple named spaces (e.g. RGB camera images and joint encoder readings together).
4. **`gym.spaces.Tuple`**: Combines spaces sequentially.
