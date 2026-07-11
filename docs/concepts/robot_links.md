# Robot Links

In robotics, a **Link** is a rigid body that forms part of the structure of a robotic manipulator. Links are connected to one another by joints, forming a kinematic chain.

---

## Rigid Body Assumption

In classical kinematics, links are modeled as **rigid bodies**, meaning they do not bend, stretch, or compress under forces or torques. While real-world robot links experience microscopic deflections (elastic deformation), the rigid-body assumption makes kinematic and dynamic calculations mathematically tractable.

---

## Properties of Links

Every link in a simulator like MuJoCo is defined by several physical properties:

1. **Geometric Shape**: The visual and collision geometry (e.g., cylinder, box, mesh).
2. **Mass ($m$)**: The quantity of matter in the link, which determines the gravitational force ($F = mg$) acting on it.
3. **Center of Mass (CoM)**: The point at which the entire mass of the link is assumed to be concentrated for force calculations.
4. **Inertia Tensor ($I$)**: A $3 \times 3$ matrix representing the link's resistance to angular acceleration about its axes.

---

## Links in Reacher-v5

The planar Reacher-v5 arm consists of:
- **Base Link**: The fixed cylinder located at the origin $(0,0)$.
- **Link 1**: The first moving link (shoulder link) connecting the shoulder joint to the elbow joint.
- **Link 2**: The second moving link (elbow link) connecting the elbow joint to the end-effector fingertip.
