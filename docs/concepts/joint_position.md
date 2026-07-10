# Joint Position

In robotics, **Joint Position** defines the angular displacement (for rotational/revolute joints) or linear displacement (for prismatic joints) of a robot link relative to its parent base or link.

---

## Joints in Reacher-v5

`Reacher-v5` is a planar 2-link robotic arm with two revolute joints:
1. **Shoulder Joint ($\theta_1$)**: Connects link 1 to the fixed base at the origin $(0, 0)$.
2. **Elbow Joint ($\theta_2$)**: Connects link 2 to the end of link 1. It is a relative joint angle (displacement relative to the orientation of link 1).

```text
               Link 2 (l2 = 0.1m)
             o=================x  Fingertip / End-Effector
            /  \
           /    \ Elbow Joint (\theta_2)
          /
         / Link 1 (l1 = 0.1m)
        /
       / \
      o   \ Shoulder Joint (\theta_1)
    (0,0) Base
```
---

## Physical Limits and Coordinates

Joint positions are measured in radians. In Gymnasium's Reacher environment, they are parsed through unit circle projection coordinates:
- $x$-coordinate projection: $\cos(\theta)$
- $y$-coordinate projection: $\sin(\theta)$
This provides a continuous representation for reinforcement learning algorithms.
