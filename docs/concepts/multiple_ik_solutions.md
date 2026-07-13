# Multiple Inverse Kinematics Solutions

robotic systems often have more than one set of joint angles that place the end-effector at the exact same target position. These configurations are called **multiple solutions**.

---

## Planar 2-Link Arm Solutions

For a planar 2-link serial manipulator, there are generally **two solutions** to reach a target coordinate $(x, y)$ inside the workspace:

```text
       Elbow-Up Solution            Elbow-Down Solution
             o                            x Target
            / \                          / \
           /   \                        /   \
          /     x Target               /     \
         o Base                       o Base  o Elbow
```

1. **Elbow-Up Configuration**:
   - In this course's standard counterclockwise-positive convention, the elbow angle $\theta_2$ is positive ($\theta_2 > 0$).
   - The elbow is positioned above the line from the base to the target.
2. **Elbow-Down Configuration**:
   - The elbow angle $\theta_2$ is negative ($\theta_2 < 0$).
   - The elbow is positioned below the line from the base to the target.

---

## Mathematical Derivation

When solving the elbow angle:
$$\theta_2 = \pm \arccos\left(\cos(\theta_2)\right)$$
- The positive sign ($+$) yields the **Elbow-Up** configuration (returned by `np.arccos()`).
- The negative sign ($-$) yields the **Elbow-Down** configuration.

Plugging each angle into the shoulder equation:
$$\theta_1 = \arctan 2(y, x) - \arctan 2(L_2 \sin(\theta_2), L_1 + L_2 \cos(\theta_2))$$
yields two distinct pairs of joint configurations $(\theta_1^d, \theta_2^d)$ and $(\theta_1^u, \theta_2^u)$ that both place the end-effector at $(x, y)$.

---

## Practical Selection in Control Systems

Robotic controllers select between these configurations using specific criteria:
- **Minimize Travel**: Choose the solution closest to the robot's current joint angles (minimizing motor movement).
- **Obstacle Avoidance**: Choose the configuration that avoids collisions with the environment or the robot's own body.
- **Joint Limits**: Exclude configurations that violate physical angle boundaries.
