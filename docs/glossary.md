# Glossary of Robotics & Embodied AI Terms

This table defines key terminology learned during Day 1 and Day 2 of the VLA Learning Lab.

| Term | Definition | First Learned | Last Reviewed | Confidence |
| :--- | :--- | :--- | :--- | :--- |
| **MuJoCo** | Multi-Joint dynamics with Contact. A fast, accurate C-based physics engine optimized for robotic simulations. | Day 1 | Day 2 | High |
| **Gymnasium** | An open-source Python library providing a standardized API for Reinforcement Learning (formerly OpenAI Gym). | Day 1 | Day 2 | High |
| **mjModel** | A static C structure in MuJoCo containing physical properties (geoms, masses, joint types) that remain unchanged. | Day 1 | Day 2 | High |
| **mjData** | A dynamic C structure in MuJoCo representing current physical states (positions, velocities, forces, simulation time). | Day 1 | Day 2 | High |
| **Observation Space** | The set of inputs (visual or numerical vectors) that an agent receives from the environment at each time step. | Day 2 | Day 2 | High |
| **Action Space** | The set of allowed control inputs (e.g. joint torques, velocity targets, discrete commands) the policy can apply. | Day 2 | Day 2 | High |
| **Forward Kinematics** | Calculating the Cartesian position $(x, y)$ of the end-effector (fingertip) given the joint angles $(\theta_1, \theta_2)$. | Day 2 | Day 2 | Medium |
| **Torque Control** | Commanding rotational force (torque) to joints, requiring the solver to calculate acceleration and velocity. | Day 2 | Day 2 | High |
| **Jacobian Matrix** | A matrix of first-order partial derivatives relating joint velocities to linear/angular velocities of the end-effector. | Day 2 | Day 2 | Medium |
| **Transpose Jacobian Control** | Mapping Cartesian forces to joint torques using the transpose of the Jacobian ($\tau = J^T F$) for target reaching. | Day 2 | Day 2 | Medium |
| **Closed-Loop Control** | A feedback control system where the controller reads state observations to compute and adjust control actions. | Day 2 | Day 2 | High |
| **Passive Simulation** | Simulating a physics model without active actuators (e.g., a ball falling under gravity or a free swinging arm). | Day 1 | Day 2 | High |
| **Active Simulation** | Simulating a model where actuators actively apply forces or torques computed by a control policy. | Day 2 | Day 2 | High |
