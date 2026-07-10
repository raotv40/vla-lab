# Kinematic Chain

A **Kinematic Chain** is an assembly of rigid bodies called **links** connected by movable connections called **joints** to form a structured mechanism.

---

## Kinematic Chain Topologies

Kinematic chains are classified into two main topologies:
1. **Open Kinematic Chain**: A chain with only one path connecting any two links (no closed loops). The endpoint is free to move.
   - *Example*: Serial robotic manipulators (such as the Reacher arm, human arm).
2. **Closed Kinematic Chain**: A chain that contains closed loops of links.
   - *Example*: Delta parallel robots, scissor lifts.

---

## Components of a Kinematic Chain

- **Base Link**: The fixed foundation of the manipulator, typically anchored to the origin frame $(0,0)$.
- **Intermediate Links**: Connect joints together. In Reacher, Link 1 connects the shoulder and elbow joints.
- **End-Effector Link**: The final link that interacts with the target.

### Reacher kinematic chain:
`Base Base` $\to$ `Shoulder Joint` $\to$ `Link 1` $\to$ `Elbow Joint` $\to$ `Link 2` $\to$ `Fingertip`
