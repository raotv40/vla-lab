# Day 2 Notes: Observation, Action and Policy Fundamentals

Notes covering the kinematics, dynamics, and control aspects of the Reacher environment.

## Key Concepts
1. **State vs. Observation**: State is the complete underlying physical configuration, whereas observation is what the robot's sensors measure.
2. **Action Space**: Rotational torques sent to shoulder and elbow actuators.
3. **Transpose Jacobian Control**: Virtual force method mapping Cartesian forces to joint space.
   $$\tau = J^T F$$

## Lab Tasks
*   Initialized Reacher-v4 in Gymnasium.
*   Deconstructed the observation vector.
*   Validated Forward Kinematics manually.
*   Implemented feedback control using transpose Jacobians.
