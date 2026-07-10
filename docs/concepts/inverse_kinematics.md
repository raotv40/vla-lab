# Inverse Kinematics

**Inverse Kinematics (IK)** is the mathematical process of calculating the joint angles ($\theta_1, \theta_2$) required to place a robot's end-effector at a desired Cartesian coordinate $(x_{\text{target}}, y_{\text{target}})$ in world space.

---

## The Inverse Kinematics Problem

Unlike Forward Kinematics (which always yields a single unique position), Inverse Kinematics is:
- **Non-linear**: Involves trigonometric terms.
- **Multiple Solutions**: A robot arm can often reach the same target coordinate using different postures (e.g., elbow-up vs. elbow-down).
- **No Solution**: If the target position is outside the robot's physical reach (workspace boundary).

```text
       Elbow-Up Solution            Elbow-Down Solution
             o                            x Target
            / \                          / \
           /   \                        /   \
          /     x Target               /     \
         o Base                       o Base  o Elbow
```

---

## Algebraic Derivation for 2-Link Planar Arm

Using the law of cosines, we can solve for elbow angle $\theta_2$ given target coordinate $(x, y)$ and link lengths $l_1, l_2$:
$$\cos(\theta_2) = \frac{x^2 + y^2 - l_1^2 - l_2^2}{2 l_1 l_2}$$
$$\theta_2 = \pm \arccos\left(\cos(\theta_2)\right)$$

Once $\theta_2$ is solved, we calculate the shoulder joint angle $\theta_1$:
$$\theta_1 = \arctan2(y, x) - \arctan2(l_2 \sin(\theta_2), l_1 + l_2 \cos(\theta_2))$$

In classical control pipelines, IK is computed at each step to convert high-level Cartesian commands (such as "move tool right 1cm") into low-level joint motor angle instructions.
