# Day 11 Journal: Trajectory Generation and Motion Profiles

- **Date**: 2026-07-15
- **Author**: Vishrao
- **Milestone**: Day 11 of VLA Learning Lab

---

## Learning Objectives
1. Understand the core mechanical difference between a geometric path and a time-parameterized trajectory.
2. Implement linear interpolation (LERP) and analyze its boundary acceleration discontinuities.
3. Formulate and code a symmetric Trapezoidal Velocity Profile motion generator.
4. Characterize step response variations under path scale adjustments and intermediate waypoint densities.
5. Identify the roles of trajectory planners in modern Vision-Language-Action (VLA) pipelines.

---

## Why Robots Need Trajectories
If a robot controller is simply fed raw setpoint coordinates without a time profile:
- Intermediate speeds are undefined, forcing the low-level controller to command immediate shifts.
- At the boundaries (starting and stopping), the instantaneous jump in position commands infinite velocity and acceleration.
- In a physical robot, this generates massive torque spikes ($F = m \cdot a$) that trip safety switches, cause violent structural vibrations (jerk), and damage gearboxes.
Trajectories map geometric paths to smooth, continuous velocity and acceleration curves, keeping the motor demands within safe bounds.

---

## Path vs. Trajectory

- **Path**: A purely geometric description of the sequence of coordinates or joint configurations that the robot visits. It is completely independent of time.
- **Trajectory**: A time-parameterized path. It specifies the exact time at which each coordinate is reached, along with the required velocities and accelerations.

---

## Motion Profile
A **Motion Profile** defines the mathematical speed curve of the joint or end-effector over the course of a trajectory. The most common profiles are:
- **Linear (Constant Velocity)**: Position is a linear ramp; velocity is constant; acceleration jumps instantaneously at boundaries.
- **Trapezoidal**: Divides motion into three phases: linear acceleration, constant cruise velocity, and linear deceleration. Acceleration is bounded.
- **S-Curve**: Smooths acceleration using linear ramps, yielding zero acceleration jumps (finite jerk).

---

## Lab Results

### Lab 25: Linear Trajectory Generation
- **Setup**: Computed a LERP trajectory from $0.0 \to 10.0$ units over $5.0\,\text{s}$ with $50$ steps.
- **Command**: `python week02/lab25_linear_trajectory.py`
- **Output**:
  ```text
  Start Position : 0.00
  Goal Position  : 10.00
  Total Time     : 5.00 seconds
  Number of Steps: 50
  Calculated Constant Velocity: 2.0000 units/sec
  ```
- **Observations**: Position is a straight diagonal line. Velocity jumps immediately from $0 \to 2.0\,\text{units/s}$ at $t=0$, and drops from $2.0 \to 0$ at $t=5.0\,\text{s}$, representing infinite acceleration at boundaries.
- **Plot**: Saved to `assets/day11/linear_trajectory.png`

### Lab 26: Trapezoidal Velocity Profile Generator
- **Setup**: Parameterized a trapezoidal profile with $t_a = 1.5\,\text{s}$.
- **Command**: `python week02/lab26_velocity_profile.py`
- **Output**:
  ```text
  Case 1 (Goal=10, Steps=50)  | Peak Vel: 2.86 | Peak Accel: 1.90
  Case 2 (Goal=20, Steps=50)  | Peak Vel: 5.71 | Peak Accel: 3.81
  Case 3 (Goal=10, Steps=100) | Peak Vel: 2.86 | Peak Accel: 1.90
  Case 4 (Goal=10, Steps=10)  | Peak Vel: 2.86 | Peak Accel: 1.90
  ```
- **Observations**: Position rises quadratically, then linearly, then quadratically. Velocity increases and decreases linearly, eliminating infinite boundary accelerations.
- **Plot**: Saved to `assets/day11/velocity_profile.png`

---

## Exercise Answers

### Exercise 1: Goal Scaling (Goal = 20)
- **Why the trajectory becomes longer?** The geometric distance spans double the length (from $10 \to 20$), so the path covers a larger distance in space.
- **Why velocity increases when the number of steps remains constant?** Because the total duration $t_f = 5.0\,\text{s}$ remains constant. To cover double the distance in the exact same time window, the joint must move faster, doubling the peak cruising velocity from $2.86\,\text{units/s} \to 5.71\,\text{units/s}$ and doubling peak acceleration from $1.90 \to 3.81\,\text{units/s}^2$.

---

### Exercise 2: Waypoint Density Increase (Steps = 100)
- **Why motion becomes smoother?** The time interval $\Delta t$ between consecutive trajectory waypoints decreases from $0.1\,\text{s} \to 0.05\,\text{s}$. The joint setpoint changes in much smaller increments.
- **Why increasing intermediate points improves trajectory quality?** A dense waypoint list minimizes discretization error, avoids setpoint command steps, and allows low-level joint PID loops to track the reference path smoothly without tracking lag or torque spikes.

---

### Exercise 3: Waypoint Density Decrease (Steps = 10)
- **Why motion becomes abrupt?** The time interval between consecutive waypoints increases to $\Delta t = 0.55\,\text{s}$. The joint setpoints jump in large, coarse blocks.
- **Why fewer trajectory samples create jerky movement?** The coarse setpoint steps represent sharp velocity jumps. When fed to low-level controllers, the derivative term sees large changes in tracking error, commanding sudden torque surges (jerk) that make the robot shake.

---

## Trajectory Planning in Real Robots
Industrial and autonomous robot controllers incorporate trajectory generators:
- **Industrial robot software** (e.g. **ABB RobotStudio**, **FANUC**, **KUKA System Software**, **Universal Robots Polyscope**) uses S-curve trajectory profiling to prevent structural oscillation and protect gearboxes.
- **Autonomous Vehicles & Mobile Robots**: Local planners generate path trajectories that avoid obstacles while matching vehicle speed limits and passenger comfort constraints.
- **Drone Navigation**: Trajectory generators plan smooth splines (minimum snap trajectories) through 3D space.
- **CNC Machines & Warehouse Robots**: Command smooth speed profiles along cutter paths to maintain cutting accuracy.

---

## VLA Connection
In a modern Vision-Language-Action (VLA) robot pipeline, trajectory generation bridges high-level semantic AI reasoning with physical motor currents:

```text
 1. Vision-Language-Action Model (VLA)
    │  (Processes visual cameras + prompt "place block on box" to output target pose)
    ▼
 2. Task Planner
    │  (Determines state sequence: open gripper, move to block, close gripper)
    ▼
 3. Motion Planner
    │  (Computes a collision-free geometric path around obstacles, e.g. A*, RRT)
    ▼
 4. Trajectory Generator
    │  (Applies time parameterization and a trapezoidal profile to the path waypoints)
    ▼
 5. Inverse Kinematics (IK)
    │  (Translates Cartesian trajectory points (x, y) into joint-angle setpoints)
    ▼
 6. Low-Level Feedback Controller (PID)
    │  (Runs at 1 kHz to track joint setpoints, outputting torque currents)
    ▼
 7. Motor Drivers & Actuators
    │  (Drives joint currents to move the robot limbs smoothly)
    ▼
 8. Robot Motion
```

---

## Commands Used
```bash
# Run linear interpolation trajectory generator
python week02/lab25_linear_trajectory.py

# Run trapezoidal velocity profile comparison
python week02/lab26_velocity_profile.py
```

---

## Issues Encountered & Solutions
- **Issue**: Coarse step counts (steps=10) created steps in position plots, making the derivative jump.
- **Solution**: Evaluated waypoint density parameters to demonstrate the trade-off of discretization in control loops.

---

## Glossary & Interview Links
- Glossary terms added to [docs/glossary.md](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/glossary.md).
- Q&As added to [docs/interview_questions.md](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/interview_questions.md).

---

## Reflection
Time parameterization is the link between geometry and physics. Adding time profiles ensures that robotic motion remains safe, smooth, and kinematically feasible.

---

## Next Steps
Day 12: Introduction to Motion Planning in Configuration Space (C-space), Obstacle Avoidance, and search-based path planning algorithms (A* and RRT).
