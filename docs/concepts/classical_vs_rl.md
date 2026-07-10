# Classical Robotics vs. Reinforcement Learning vs. VLA Pipelines

There are three primary paradigms for designing robotic control loops: **Classical Control**, **Reinforcement Learning (RL)**, and **Vision-Language-Action (VLA)**.

---

## 1. Classical Control Pipeline
The classical robotics pipeline relies on rigorous physical modeling, kinematics, and control theory.

```text
  [ Target Position ]
          │
          ▼
  [ Inverse Kinematics (IK) ] ──> [ Joint Setpoints ] ──> [ PID Controller ] ──> [ Joint Torques ]
```

- **Pros**: Highly explainable, mathematically provable stability, no training required.
- **Cons**: Vulnerable to modeling errors, struggles to generalize to unstructured environments or complex visual inputs.

---

## 2. Reinforcement Learning (RL) Pipeline
The RL pipeline replaces the analytical controller with a learned policy optimized via reward signals.

```text
  [ Observation Vector ] ──> [ Neural Policy Network ] ──> [ Joint Actions / Torques ]
```

- **Pros**: Can learn complex dynamics without analytical models, robust to environmental variation.
- **Cons**: Requires millions of trial-and-error simulation steps, lacks explainability, no mathematical safety guarantees.

---

## 3. Vision-Language-Action (VLA) Pipeline
VLA pipelines combine visual perception, language instruction parsing, and low-level action output into a unified multi-modal foundation model.

```text
  [ Camera Image + Text Prompt ] ──> [ Pre-trained VLA Model ] ──> [ Low-Level Control Actions ]
```

- **Pros**: Generalized instructions (e.g. "pick up the red mug"), open-vocabulary semantic parsing.
- **Cons**: Computationally heavy, slower control frequencies, requires fine-tuning.

---

## Summary Comparison

| Feature | Classical Control | Reinforcement Learning | Vision-Language-Action |
| :--- | :--- | :--- | :--- |
| **Model dependency** | High (Requires physical parameters) | Low (Data-driven) | None (Pre-trained foundation model) |
| **Primary Input** | Target Cartesian / joint states | Numerical state observation vector | RGB-D camera frames + Language instruction |
| **Primary Output** | Torques / joint commands | Joint commands | Normalized actions |
| **Compute Cost** | Low | Medium (During training only) | High (Continuous VLM inference) |
