# PID vs. Reinforcement Learning

Modern robot control systems often combine classical feedback controllers like **PID** with advanced machine learning paradigms like **Reinforcement Learning (RL)** and **Vision-Language-Action (VLA)** models.

---

## Comparison Table

| Attribute | PID Controller | Reinforcement Learning (RL) Policy |
| :--- | :--- | :--- |
| **Model-Free / Data Requirement** | High (needs no model or training data) | Requires millions of environment interaction steps |
| **Computations** | Minimal (few arithmetic multiplications) | High (deep neural network forward passes) |
| **State Scope** | 1D joint setpoints | High-dimensional (pixel images, observations) |
| **Adaptability** | Fixed gains; struggles with new tasks | Can learn complex policies for diverse scenarios |
| **Safety Guarantees**| High (bounded via linear systems theory) | Low (black-box neural networks, no safety bounds) |

---

## How They Combine in VLA Systems

Rather than replacing PID, modern robotics frameworks use both in a hierarchical pipeline:

1. **High-Level Policy (RL/VLA)**: Processes camera images and text prompts (e.g. *"pick up the red mug"*) at a low frequency (e.g., **5 Hz - 20 Hz**). It outputs Cartesian goal coordinates or joint setpoints.
2. **Low-Level Controller (PID)**: Receives these joint setpoints and runs at a very high frequency (e.g. **500 Hz - 2 kHz**), regulating motor current to achieve the desired joint targets safely, smoothly, and with zero steady-state error.
