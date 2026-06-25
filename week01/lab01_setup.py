"""
Week 1 - Lab 1: MuJoCo Installation and Setup Verification
==========================================================

Objectives:
-----------
1. Verify that MuJoCo is correctly installed and accessible via Python.
2. Understand the relationship between MuJoCo's model (mjModel) and dynamic state (mjData).
3. Load a simple XML model from a string and inspect its properties.
4. Run a basic simulation loop using mj_step() and extract state information.

Theory:
-------
MuJoCo (Multi-Joint dynamics with Contact) is a physics engine designed for robotics and biomechanics.
Its core architecture separates static structure from dynamic state:
- MjModel (C struct: mjModel): Contains the static description of the model (geometries, masses, joints, limits). This does not change during simulation.
- MjData (C struct: mjData): Contains the dynamic state (joint positions, velocities, forces, solver diagnostics). This is updated at every physics step.

To step the simulation:
- mujoco.mj_step(model, data): Computes the next state of the system based on physical forces (gravity, joints, external forces) and updates `data`.

Expected Output:
----------------
You should see output printing the simulation time, height, and velocity of the ball as it falls due to gravity.
Example:
Time: 0.00s | Ball Height:  5.000m | Velocity:   0.000m/s
Time: 0.10s | Ball Height:  4.951m | Velocity:  -0.981m/s
...
Time: 1.00s | Ball Height:  0.095m | Velocity:  -9.810m/s
Ball has reached the ground!

Exercises:
----------
1. Change the gravity vector in the XML structure (e.g., set it to [0, 0, -1.62] to simulate Lunar gravity).
2. Modify the initial position of the ball from z = 5.0 to z = 10.0 and see how it affects terminal velocity.
3. Conceptual: Does changing the mass of the sphere in the XML change its acceleration under pure gravity? Verify by changing the mass and running the script.
"""

import mujoco
import time

# 1. Define the physical world in XML (MJCF format)
# We create a simple box (ground plane) and a free-falling sphere.
xml_string = """
<mujoco model="falling_ball">
    <option gravity="0 0 -9.81" timestep="0.002"/>
    
    <worldbody>
        <!-- Ground plane -->
        <geom name="floor" type="plane" size="0 0 .1" rgba=".9 .9 .9 1"/>
        
        <!-- Light source for rendering -->
        <light directional="true" diffuse=".8 .8 .8" specular=".2 .2 .2" pos="0 0 5" dir="0 0 -1"/>
        
        <!-- Falling sphere body -->
        <body name="ball" pos="0 0 5">
            <freejoint name="ball_joint"/>
            <geom name="ball_geom" type="sphere" size="0.1" rgba="0.8 0.2 0.2 1" mass="1.0"/>
        </body>
    </worldbody>
</mujoco>
"""

def main():
    print("--- Lab 01: Starting MuJoCo Setup Verification ---")
    
    # 2. Load the model from the XML string
    model = mujoco.MjModel.from_xml_string(xml_string)
    
    # 3. Create the data object representing dynamic state
    data = mujoco.MjData(model)
    
    print("Model successfully loaded!")
    print(f"Number of degrees of freedom (nv): {model.nv}")
    print(f"Number of generalized coordinates (nq): {model.nq}")
    print(f"Sphere mass: {model.body('ball').mass[0]} kg")
    
    # Let's run the simulation for 1.0 second of simulation time
    sim_duration = 1.0
    print(f"\nRunning simulation for {sim_duration} seconds...")
    
    # We will log the state every 0.1 seconds of simulation time
    log_interval = 0.1
    next_log_time = 0.0
    
    # Retrieve joint indexes
    # The ball has a free joint, which has 7 generalized coordinates (pos, quaternion) and 6 velocities.
    # The z-position is at index 2 (x=0, y=1, z=2) of qpos.
    # The z-velocity is at index 2 of qvel.
    
    while data.time < sim_duration:
        # Get current state of the ball
        ball_z = data.qpos[2]
        ball_vz = data.qvel[2]
        
        # Log status
        if data.time >= next_log_time:
            print(f"Time: {data.time:4.2f}s | Ball Height: {ball_z:6.3f}m | Velocity: {ball_vz:7.3f}m/s")
            next_log_time += log_interval
            
        # Step physics solver forward in time
        mujoco.mj_step(model, data)
        
        # Check for collision with the floor (height near ball radius = 0.1)
        if data.qpos[2] <= 0.1001 and abs(data.qvel[2]) < 0.01:
            print(f"Time: {data.time:4.2f}s | Ball Height: {data.qpos[2]:6.3f}m | Velocity: {data.qvel[2]:7.3f}m/s")
            print("Ball has reached the ground and settled!")
            break
            
    print("\n--- Lab 01: Verification Completed Successfully ---")

if __name__ == "__main__":
    main()
