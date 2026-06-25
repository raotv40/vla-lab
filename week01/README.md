# Week 1: MuJoCo and Gymnasium Fundamentals

Welcome to Week 1 of the **VLA Learning Lab**. This week focus on building a strong foundation in physics simulation (using **MuJoCo**) and reinforcement learning environment APIs (using **Gymnasium**).

---

## Overview

In robotics and Embodied AI, we rely heavily on simulation to train and test policies before deploying them to real hardware. We will use a standard 2D two-joint robotic arm (the **Reacher** environment) to study observations, actions, and classical closed-loop controllers.

---

## Learning Objectives

By the end of this week, you will be able to:
1. Load and step physical models inside the **MuJoCo** physics engine.
2. Interface with MuJoCo models using the **Gymnasium** API.
3. Decipher complex multi-dimensional observation spaces and map them to physical quantities.
4. Apply torque control commands to robotic joints and analyze the resulting dynamics.
5. Build and tune a **Transpose Jacobian** closed-loop feedback controller.

---

## Directory Structure

This folder contains the following labs:

| File | Title | Description |
| :--- | :--- | :--- |
| [lab01_setup.py](file:///C:/Users/Vishrao/vla-lab/vla-lab/week01/lab01_setup.py) | Setup & Verification | Loads a simple free-falling sphere MJCF model directly in MuJoCo. |
| [lab02_reacher.py](file:///C:/Users/Vishrao/vla-lab/vla-lab/week01/lab02_reacher.py) | Gymnasium Integration | Initializes the Reacher-v4 environment and executes a random policy. |
| [lab03_observation.py](file:///C:/Users/Vishrao/vla-lab/vla-lab/week01/lab03_observation.py) | Observation Space | Manually parses the 10D observation vector and checks kinematics. |
| [lab04_actions.py](file:///C:/Users/Vishrao/vla-lab/vla-lab/week01/lab04_actions.py) | Action Space | Applies continuous torque control values to analyze motor dynamics. |
| [lab05_policy.py](file:///C:/Users/Vishrao/vla-lab/vla-lab/week01/lab05_policy.py) | Feedback Controller | Implements a classic Transpose Jacobian virtual-spring controller. |

---

## Running the Labs

Ensure you have activated your virtual environment:
```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Run each lab script from the repository root:
```bash
python week01/lab01_setup.py
python week01/lab02_reacher.py
python week01/lab03_observation.py
python week01/lab04_actions.py
python week01/lab05_policy.py
```

*Note: The labs are configured to run in headless mode (no visual window) by default to prevent crashes on systems without a display server. To enable visual rendering for labs 2-5, change the `render_mode` argument in `gym.make()` from `None` to `"human"`.*

---

## Core Theory

### 1. MjModel vs MjData
MuJoCo divides its state representation into two main components:
- **`mjModel`**: Defines the static physical configuration of the world (e.g. geometry, body masses, joint types, coordinates).
- **`mjData`**: Represents the current dynamic state (e.g. simulation time, joint positions `qpos`, joint velocities `qvel`, contact forces).

### 2. Forward Kinematics
Forward Kinematics calculates the Cartesian coordinate $(x, y)$ of the end-effector (fingertip) given the joint angles $(\theta_1, \theta_2)$:
$$x = l_1 \cos(\theta_1) + l_2 \cos(\theta_1 + \theta_2)$$
$$y = l_1 \sin(\theta_1) + l_2 \sin(\theta_1 + \theta_2)$$
For Reacher-v4, $l_1 = 0.1\text{m}$ and $l_2 = 0.1\text{m}$.

### 3. Transpose Jacobian Control
The Jacobian matrix $J$ relates joint velocities to Cartesian tip velocities ($\dot{x} = J \dot{\theta}$). Using the principle of virtual work, we can project a desired Cartesian force vector $F$ directly to joint torques $\tau$ using the transpose of the Jacobian:
$$\tau = J^T F$$
Where $F$ acts as a spring-damper pulling the tip toward the target:
$$F = K_p(x_{\text{target}} - x_{\text{tip}}) - K_d v_{\text{tip}}$$
This classical feedback policy drives the arm to the target without any neural network training!
