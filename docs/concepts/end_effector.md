# End-Effector

An **End-Effector** is the peripheral device or final link of a robotic manipulator designed to interact directly with the environment (e.g. grippers, suction cups, welding torches, or fingertips).

---

## End-Effector of Reacher-v5

In the 2D Reacher environment, the end-effector is the **fingertip** at the end of the second link. 

### Forward Kinematics Coordinates
Given the shoulder link length $l_1 = 0.1\,\text{m}$ and elbow link length $l_2 = 0.1\,\text{m}$, the Cartesian position $(x_{\text{tip}}, y_{\text{tip}})$ of the end-effector is calculated from joint angles:
- $x_{\text{tip}} = l_1 \cos(\theta_1) + l_2 \cos(\theta_1 + \theta_2)$
- $y_{\text{tip}} = l_1 \sin(\theta_1) + l_2 \sin(\theta_1 + \theta_2)$

---

## Target Error Vector
The primary goal of the controller is to drive the end-effector to match the target coordinates. The error vector is computed as:
- $\text{error\_x} = x_{\text{target}} - x_{\text{tip}}$
- $\text{error\_y} = y_{\text{target}} - y_{\text{tip}}$
These error components are passed to the controller to calculate joint torque corrections.
