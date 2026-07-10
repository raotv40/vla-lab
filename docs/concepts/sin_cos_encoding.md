# Sine/Cosine Angle Encoding

In reinforcement learning and neural network design, angles are rarely passed directly as raw scalars (in degrees or radians). Instead, they are encoded as coordinate pairs on a unit circle using the **sine** and **cosine** trigonometric functions.

---

## The Angle Wrap-Around Discontinuity

Representing a joint angle $\theta$ as a raw scalar value in $[0, 360^\circ]$ or $[-\pi, \pi]$ introduces a mathematical **discontinuity** at the wrap-around boundary:

- A joint moving slightly from $359.9^\circ$ to $0.1^\circ$ changes physically by only $0.2^\circ$.
- Numerically, the scalar jump is $-359.8^\circ$.

When neural networks calculate gradients based on this scalar input, this large numerical jump causes extreme gradient spikes, causing learning instability.

---

## The Trigonometric Solution

By representing the angle as a coordinate point on a unit circle $(\cos(\theta), \sin(\theta))$, the representation becomes completely **smooth and continuous** across the boundary:

- $\cos(359.9^\circ) \approx 1.0$, $\cos(0.1^\circ) \approx 1.0$ (continuous)
- $\sin(359.9^\circ) \approx 0.0$, $\sin(0.1^\circ) \approx 0.0$ (continuous)

```text
               Y (sin)
                |  State B (0.1°)
                | / 
         -------+------- X (cos)
                | \
                |  State A (359.9°)
```

This is why Gymnasium's Reacher-v5 environment encodes joint angles as `cos(theta1), cos(theta2), sin(theta1), sin(theta2)` inside the observation vector.
