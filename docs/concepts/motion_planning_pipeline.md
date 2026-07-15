# Motion Planning Pipeline

In modern AI-integrated robotic systems, the **Motion Planning Pipeline** connects high-level cognitive understanding (such as vision-language perception) with low-level joint torque actuation.

---

## The Complete Pipeline Flow

```text
  1. Vision (Cameras, RGB-D sensors)
        │
        ▼ (Raw pixels, depth maps, point clouds)
  2. Language Understanding (Text prompts, e.g., "pick up red mug")
        │
        ▼ (Task prompt tokens)
  3. Task Planning (High-level sequences, e.g. Open Gripper -> Move -> Close Gripper)
        │
        ▼ (Target coordinates, setpoints)
  4. Motion Planning (Solves collision-free path waypoints, e.g. A*, RRT)
        │
        ▼ (Geometric Path waypoints)
  5. Trajectory Generation (Profiles path over time, e.g., Trapezoidal profiles)
        │
        ▼ (Time-stamped joint positions, velocities, accelerations)
  6. Inverse Kinematics (IK) (Translates Cartesian points to joint variables)
        │
        ▼ (Joint angle trajectories)
  7. PID Controller (Regulates motor current to track setpoints)
        │
        ▼ (Torque commands)
  8. Motor Drivers (Converts commands to currents and voltages)
        │
        ▼ (Electrical signals)
  9. Robot Motion
```

---

## Responsibility of Each Stage

| Stage | Input | Output | Primary Responsibility |
| :--- | :--- | :--- | :--- |
| **1. Vision** | Photons | Point Clouds / RGB-D | Captures the physical state of the environment. |
| **2. Language** | User Text Prompt | Command Tokens | Interprets human intent (e.g. *"place block"*). |
| **3. Task Planning** | Command Tokens | End-effector Target Pose | Breaks the task down into sequential coordinate targets. |
| **4. Motion Planning**| Target Pose + Obstacles| Collision-free Path | Solves a geometric path connecting start to goal around obstacles. |
| **5. Trajectory Gen** | Geometric Path | Time-parameterized Path| Maps the path to smooth speed profiles to respect motor limits. |
| **6. Inverse Kinematics**| Cartesian Trajectory | Joint Angle Trajectory | Translates task coordinates into joint coordinates. |
| **7. PID Controller** | Joint Setpoints | Torque Commands | Drives error to zero and provides high-frequency disturbance rejection. |
| **8. Motor Drivers** | Torque Commands | Voltage / Current | Drives the physical joint electric motors. |
