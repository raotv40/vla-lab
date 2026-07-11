# Forward Kinematics

**Forward Kinematics (FK)** is the mathematical process of calculating the Cartesian coordinates (position and orientation) of a robot's end-effector in world space, given its joint angles and link lengths.

---

## 2D Two-Link Arm Kinematics

Consider the planar 2-link robotic arm with link lengths $l_1$ and $l_2$, shoulder joint angle $\theta_1$, and elbow joint angle $\theta_2$ (relative to link 1):

```text
               Link 2 (l2)
             o===========x (x_tip, y_tip) End-Effector
            /  \
           /    \ Elbow Joint (\theta_2)
          /
         / Link 1 (l1)
        /
       / \
      o   \ Shoulder Joint (\theta_1)
    (0,0) Base Base Frame
```

The position of the elbow joint $(x_{\text{elbow}}, y_{\text{elbow}})$ is:
$$x_{\text{elbow}} = l_1 \cos(\theta_1)$$
$$y_{\text{elbow}} = l_1 \sin(\theta_1)$$

Since the elbow angle $\theta_2$ is relative to link 1, the absolute orientation of link 2 relative to the base frame is $(\theta_1 + \theta_2)$. The fingertip coordinates $(x_{\text{tip}}, y_{\text{tip}})$ are:
$$x_{\text{tip}} = l_1 \cos(\theta_1) + l_2 \cos(\theta_1 + \theta_2)$$
$$y_{\text{tip}} = l_1 \sin(\theta_1) + l_2 \sin(\theta_1 + \theta_2)$$

---

## Trigonometric Expansion

Using trigonometric identities, we can compute coordinates directly from sines/cosines (like those provided by Reacher observations):
$$\cos(\theta_1 + \theta_2) = \cos(\theta_1)\cos(\theta_2) - \sin(\theta_1)\sin(\theta_2)$$
$$\sin(\theta_1 + \theta_2) = \sin(\theta_1)\cos(\theta_2) + \cos(\theta_1)\sin(\theta_2)$$

So:
$$x_{\text{tip}} = l_1 \cos(\theta_1) + l_2 (\cos(\theta_1)\cos(\theta_2) - \sin(\theta_1)\sin(\theta_2))$$
$$y_{\text{tip}} = l_1 \sin(\theta_1) + l_2 (\sin(\theta_1)\cos(\theta_2) + \cos(\theta_1)\sin(\theta_2))$$
This allows us to perform forward kinematics directly on observation features without using inverse trigonometric functions (`arccos` or `arcsin`).

---

## Forward Kinematics vs. Inverse Kinematics

- **Forward Kinematics (FK)**: Takes joint angles ($\theta$) and maps them to Cartesian coordinates $(x, y)$. This mapping is unique, continuous, and straightforward to calculate.
- **Inverse Kinematics (IK)**: Takes Cartesian coordinates $(x, y)$ and maps them to joint angles ($\theta$). This mapping is non-linear, multi-valued (e.g. elbow-up vs elbow-down), and can be computationally expensive.

---

## Role of Forward Kinematics in Control Systems

### 1. Classical Robotics Control
In classical pipelines, FK is computed continuously at high frequencies (e.g. $1000\,\text{Hz}$) to:
- **State Estimation**: Read joint encoder values and calculate where the end-effector tip is located in world space.
- **Feedback Loop**: Compute the error vector ($\mathbf{e} = \mathbf{x}_{\text{target}} - \mathbf{x}_{\text{tip}}$) which is fed into Cartesian feedback controllers (such as PD or Jacobian transpose controllers).

### 2. Modern Vision-Language-Action (VLA) Systems
In deep learning and imitation learning VLA pipelines (such as OpenVLA):
- **Relative Commands**: VLA models often command delta Cartesian positions ($\Delta x, \Delta y$) directly from camera frames.
- **FK Validation**: FK is used as a safety layer to verify that the generated VLA actions do not push the joint limits or workspace boundaries of the physical manipulator.
- **Self-Supervised Labeling**: FK provides ground-truth Cartesian trajectories for automatically labeling visual demonstrations during imitation learning dataset curation.

