# Feature Vectors in Robotics and RL

A **Feature Vector** is an n-dimensional vector of numerical features that represents the state of a system. It abstracts raw measurements (e.g. joint encoder values or image pixels) into structured inputs suitable for control policies or machine learning models.

---

## Importance of Feature Engineering

- **Dimensionality Reduction**: Abstracting complex environments (like 3D rendering) into a compact, low-dimensional vector of joint coordinates, target angles, and errors.
- **Normalization**: Scaling inputs (e.g. keeping sines and cosines within $[-1.0, 1.0]$) to stabilize optimization gradients.
- **Continuous Representation**: Ensuring physical quantities behave continuously to prevent learning disruption (e.g. using unit circle coordinates instead of raw angles).
