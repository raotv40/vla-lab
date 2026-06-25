# Day 1 Journal: MuJoCo Setup and Passive Simulation

- **Date**: 2026-06-25
- **Author**: Vishrao
- **Milestone**: Day 1 of VLA Learning Lab

---

## Objectives
1. Set up a Python virtual environment and install standard robotics libraries.
2. Verify native Python bindings for MuJoCo.
3. Understand the separation between static physical models (`mjModel`) and dynamic simulation state (`mjData`).
4. Load an MJCF XML file and simulate a falling sphere under gravity (passive simulation).

---

## Theory
MuJoCo divides its execution into:
- **`mjModel`**: A C structure containing the static configuration of the model (masses, shapes, joints, sensors). It does not change.
- **`mjData`**: A C structure representing the dynamic state (time, positions `qpos`, velocities `qvel`, forces).
- **`mj_step`**: The core solver that reads control commands, computes accelerations, resolves constraints, and integrates state forward by `timestep` seconds.

---

## Commands Used
```powershell
# Create a virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\Activate.ps1

# Install project dependencies
pip install -r requirements.txt

# Run the setup verification script
python week01/lab01_setup.py
```

---

## Experiments

### Experiment 1.1: Passive Falling Sphere
- **Setup**: Loaded a sphere of mass $1.0\text{kg}$ at $z = 5.0\text{m}$ under Earth gravity ($g = -9.81\text{m/s}^2$).
- **Goal**: Measure velocity and height over time.

### Experiment 1.2: Gravity Modification (Lunar Gravity)
- **Setup**: Modified the `<option gravity="0 0 -1.62"/>` inside the MJCF XML string.
- **Goal**: Observe the slower descent rate on the Moon.

---

## Observations
1. **Experiment 1.1**: The ball fell from $5.0\text{m}$ and reached the ground (settling at $z = 0.1\text{m}$ due to its $0.1\text{m}$ radius) at exactly $1.00\text{s}$, with a velocity of $-9.81\text{m/s}$, matching analytic calculations ($v = -gt$).
2. **Experiment 1.2**: Under Lunar gravity, the sphere fell much slower, reaching a height of $4.19\text{m}$ at $1.00\text{s}$ with a velocity of $-1.62\text{m/s}$.
3. **Mass Invariance**: Changing the mass from $1.0\text{kg}$ to $10.0\text{kg}$ did not change the acceleration, verifying that MuJoCo correctly implements ideal gravitational acceleration without drag.

---

## Screenshots Placeholder

![Day 1 Simulation Output - Console logs and falling height plot](../../assets/day01_sim_height.png)

---

## Issues Encountered
- **Issue**: Importing `mujoco` raised `ModuleNotFoundError: No module named 'mujoco'`.
- **Cause**: The script was run in the global python context instead of the local virtual environment where dependencies were installed.

---

## Solutions
- Activated the virtual environment explicitly using `.venv\Scripts\Activate.ps1` (or `source .venv/bin/activate` on Linux/macOS) and confirmed the interpreter path with `Get-Command python` (or `which python`).

---

## Interview Questions
- **Q**: What is the difference between `mjModel` and `mjData`?
  - **A**: `mjModel` contains the static configuration of the physical world (loaded once, read-only during sim). `mjData` contains the mutable, dynamic state variables (updated every physics step).

---

## Glossary Updates
- **MuJoCo**: Multi-Joint dynamics with Contact.
- **mjModel**: Static physical model structure.
- **mjData**: Dynamic state variable structure.
- **Passive Simulation**: Motion resulting only from gravity, joints, and collisions, with no control torques.

---

## Lessons Learned
- Always run scripts inside activated virtual environments to isolate dependencies.
- Separating static description (`mjModel`) from dynamic state (`mjData`) makes MuJoCo highly thread-safe and efficient for parallel rollouts in reinforcement learning.

---

## Reflection
Setting up MuJoCo used to require license keys and complex system builds. With DeepMind's native `mujoco` Python bindings, getting a simulation running is fast and clean, lowering the barrier to entry for robotics engineering.

---

## Next Steps
Wrap the MuJoCo simulation environment in Gymnasium, load a 2-joint arm (Reacher-v4), and analyze observation and action spaces.
