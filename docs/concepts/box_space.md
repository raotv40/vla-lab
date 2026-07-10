# Box Space in Gymnasium

In Gymnasium, **`gym.spaces.Box`** represents a continuous multidimensional space bounded by lower and upper limits. It is the most commonly used space class for physical simulations and robotic joints.

---

## Properties of Box Space

A `Box` space is initialized with:
- **`low`**: The minimum boundary values (can be a scalar or an array matching the space shape).
- **`high`**: The maximum boundary values.
- **`shape`**: A tuple defining the dimensions of the space.
- **`dtype`**: The precision format (e.g. `np.float32` or `np.float64`).

---

## Example breakdown (Exercise 1)

### 1. `Box(-inf, inf, (10,), float64)`
- Represents a 10-dimensional continuous vector.
- Bounded theoretically between negative and positive infinity.
- Uses 64-bit double-precision floating-point format (`float64`), providing high accuracy.
- Used in `Reacher-v5` for observations.

### 2. `Box(-1.0, 1.0, (2,), float32)`
- Represents a 2-dimensional continuous vector.
- Strictly bounded between -1.0 and 1.0.
- Uses 32-bit single-precision floating-point format (`float32`), which matches neural network model parameters and requires less memory/compute.
- Used in `Reacher-v5` for joint torque actions.
