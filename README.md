# VLA Learning Lab

> **Vision - Language - Action (VLA)**: A hands-on educational repository for modern robotics and embodied Artificial Intelligence.

This repository tracks the core concepts, labs, and projects completed during the VLA Learning Lab curriculum. We focus on building robotics systems from the ground up - starting with raw physics engines and classical controllers, and scaling up to vision-language-action models (VLMs) and deep imitation learning policies.

---

## 🛠️ Quickstart Guide

### 1. Prerequisites
Ensure you have Python 3.10+ installed on your system.

### 2. Setup Virtual Environment
Clone this repository and create a Python virtual environment to isolate project dependencies:

```powershell
# Clone the repository
git clone https://github.com/raotv40/vla-lab.git
cd vla-lab

# Create virtual environment
python -m venv .venv

# Activate virtual environment (Windows)
.venv\Scripts\Activate.ps1

# Activate virtual environment (Linux/macOS)
source .venv/bin/activate
```

### 3. Install Dependencies
Install all required packages (including MuJoCo physics solver, Gymnasium environment wrapper, Torch, Transformers, and Accelerate):

```bash
pip install -r requirements.txt
```

---

## 📂 Repository Structure

The workspace is organized as follows:

```text
vla-lab/
├── .github/                 # GitHub Action workflows and CI configs
├── assets/                  # Simulation visual plots and media assets
│   ├── day08/               # Day 8 robot configurations and plots
│   │   └── robot_arm.png    # Matplotlib schematic plot of the manipulator
│   ├── day09/               # Day 9 kinematics flowcharts
│   │   └── kinematics_flowchart.png # Technical flowchart of the control pipeline
│   ├── day10/               # Day 10 PID step response plots
│   │   ├── p_controller.png   # Proportional step response plot
│   │   ├── pi_controller.png  # Proportional-Integral step response plot
│   │   └── pid_controller.png # Proportional-Integral-Derivative step response plot
│   ├── day11/               # Day 11 Trajectory generation plots
│   │   ├── linear_trajectory.png # LERP trajectory position & velocity plot
│   │   └── velocity_profile.png  # Trapezoidal velocity profile comparison plot
│   └── day12/               # Day 12 Motion planning plots
│       ├── occupancy_grid.png # Discrete 2D occupancy grid map
│       └── bfs_traversal.png  # Breadth-First Search node traversal shortest path plot
├── docs/                    # Architectural documents and study notes
│   ├── concepts/            # Core control theory and robotics concepts
│   │   ├── action_space.md  # Action space specifications
│   │   ├── box_space.md     # Gymnasium Box spaces
│   │   ├── classical_vs_rl.md # Classical control vs RL vs VLA pipelines
│   │   ├── collision_checking.md # Geometric intersection & grid checks
│   │   ├── configuration_space.md # Workspace parameters vs C-Space variables
│   │   ├── control_loop.md  # Feedback loop control blocks
│   │   ├── controller.md    # Robot controller definition
│   │   ├── degrees_of_freedom.md # Mechanical DoFs
│   │   ├── derivative_control.md # Derivative feedback D term
│   │   ├── end_effector.md  # End-effector kinematics
│   │   ├── error.md         # Tracking error mathematical derivation
│   │   ├── feature_vector.md # Feature vector representation
│   │   ├── feedback.md      # Open-loop vs closed-loop feedback systems
│   │   ├── feedback_control.md # Closed-loop dynamics and disturbance rejection
│   │   ├── fk_vs_ik.md      # Forward vs Inverse Kinematics mapping
│   │   ├── forward_kinematics.md # Coordinate computation (FK)
│   │   ├── ik_verification.md # Verification loop procedures
│   │   ├── integral_control.md # Integral accumulation I term
│   │   ├── inverse_kinematics.md # Joint setpoints computation (IK)
│   │   ├── joint_position.md # Joint positions and angles
│   │   ├── joint_velocity.md # Joint velocities
│   │   ├── kinematic_chain.md # Joint-link topologies
│   │   ├── motion_planning.md # Collision-free path generation
│   │   ├── motion_planning_pipeline.md # Complete vision-understanding-motion pipelines
│   │   ├── motion_profiles.md # S-curves, trapezoids, and cubic splines
│   │   ├── multiple_ik_solutions.md # Elbow-up vs Elbow-down postures
│   │   ├── observation_space.md # Observation space specifications
│   │   ├── observation_vs_state.md # Physical state vs sensor observation
│   │   ├── observation_vector.md # Observation vector structure
│   │   ├── occupancy_grid.md # Binary cell grids
│   │   ├── oscillation.md   # Dynamic stability and damping ratios
│   │   ├── overshoot.md     # Transient peak overshoot metrics
│   │   ├── path_vs_trajectory.md # Geometric paths vs time trajectories
│   │   ├── pid_controller.md # Discrete PID algorithms
│   │   ├── pid_tuning.md    # Manual and Ziegler-Nichols tuning strategies
│   │   ├── pid_vs_rl.md     # Classical PID loops vs RL neural nets
│   │   ├── proportional_control.md # Proportional feedback P term
│   │   ├── reachable_workspace.md # Physical limits and bounds
│   │   ├── robot_joints.md  # Joint boundaries and limits
│   │   ├── robot_links.md   # Link dynamics and mass properties
│   │   ├── robot_state.md   # Mathematical state vectors
│   │   ├── sin_cos_encoding.md # Trigonometric angle encoding
│   │   ├── steady_state_error.md # Steady state offsets under load
│   │   ├── target_pose.md   # Cartesian target descriptors
│   │   ├── target_position.md # Target position reference
│   │   ├── trajectory_generation.md # Interpolation and continuity
│   │   ├── trajectory_planning.md # The hierarchical motion planning pipeline
│   │   ├── trapezoidal_velocity_profile.md # Acceleration-cruise-deceleration equations
│   │   ├── two_link_robot.md # Planar serial kinematics
│   │   ├── velocity_profile.md # Speed constraints over time
│   │   └── workspace.md     # Reachable work envelopes
│   ├── journal/             # Daily progress journals
│   │   ├── day01.md         # Setup and passive simulation
│   │   ├── day02.md         # Observations, actions, and Jacobian control
│   │   ├── day03.md         # Reward dynamics and step transitions
│   │   ├── day04.md         # Random policy and exploration
│   │   ├── day05.md         # Proportional control loops
│   │   ├── day06.md         # Deciphering observation vectors
│   │   ├── day06_5.md       # Angle representations and continuous spaces
│   │   ├── day07.md         # Robot state, decoding & kinematics
│   │   ├── day08.md         # Forward kinematics and 2-link robot arm
│   │   ├── day09.md         # Inverse kinematics and verification
│   │   ├── day10.md         # PID feedback control loops
│   │   ├── day11.md         # Trajectory generation and velocity profiling
│   │   └── day12.md         # Motion planning and Configuration Space
│   ├── architecture.md      # System layout (Python -> Gym -> MuJoCo)
│   ├── glossary.md          # Key terminology and confidence scores
│   ├── interview_questions.md # Study guide Q&As for robotics and VLA
│   └── roadmap.md           # 8-week curriculum breakdown
├── notes/                   # User notes directory
│   ├── day01.md             # Initial Day 1 notes
│   ├── day02.md             # Initial Day 2 notes
│   ├── day09.md             # Copy of Day 9 progress log
│   ├── day10.md             # Copy of Day 10 progress log
│   ├── day11.md             # Copy of Day 11 progress log
│   └── day12.md             # Copy of Day 12 progress log
├── week01/                  # Week 1: MuJoCo and Gymnasium Fundamentals
│   ├── README.md            # Week 1 instructions & theory
│   ├── lab01_setup.py       # Basic MuJoCo physics test
│   ├── lab02_reacher.py     # Gymnasium Reacher-v4 random policy
│   ├── lab03_observation.py # Deconstructing observation space
│   ├── lab04_actions.py     # Understanding joint torque dynamics
│   ├── lab05_policy.py      # Transpose Jacobian feedback policy
│   ├── lab06_reward_episode.py # Reward and episode mechanics
│   ├── lab07_random_policy.py  # Random policy exploration
│   ├── lab08_compare_policies.py # Policy comparison metrics
│   ├── lab09_simple_controller.py # Proportional control loop demo
│   ├── lab10_observation_decoder.py # Decode observation elements
│   ├── lab11_observation_analysis.py # Validate trig identities
│   ├── lab12_observation_changes.py # Track dynamic vs static states
│   ├── lab13_environment_info.py # Space bounds and precision
│   ├── lab14_pretty_observation.py # Dynamic tabular logs
│   ├── lab15_angles.py      # arctan2 decoding & discontinuity demo
│   ├── lab16_decode_observation.py # Reset changes comparison
│   ├── lab17_observation_comparison.py # Velocity vs position dynamics
│   ├── lab18_forward_kinematics.py # Analytical 2D forward kinematics
│   ├── lab19_plot_robot_arm.py # Matplotlib workspace plotter
│   ├── lab20_inverse_kinematics.py # Planar joint angle solver
│   └── lab21_verify_ik.py   # Closed-loop kinematics validator
├── week02/                  # Week 2: Robotic Control Frameworks
│   ├── README.md            # Week 2 instructions & theory
│   ├── lab22_p_controller.py   # Proportional feedback joint simulation
│   ├── lab23_pi_controller.py  # Proportional-Integral feedback joint simulation
│   ├── lab24_pid_controller.py # Proportional-Integral-Derivative feedback joint simulation
│   ├── lab25_linear_trajectory.py # Linear LERP trajectory generator
│   ├── lab26_velocity_profile.py  # Trapezoidal velocity profile generator
│   ├── lab27_grid_planner.py   # Occupancy grid generation and plotting
│   └── lab28_bfs_planner.py    # Breadth-First Search (BFS) grid path planner
├── requirements.txt         # Core dependencies listing
└── LICENSE                  # License terms
```

---

## 🎓 Learning Curriculum

1. **[Week 1: MuJoCo & Gymnasium Fundamentals](file:///C:/Users/Vishrao/vla-lab/vla-lab/week01/README.md)**: Explore simulator engines, step functions, observations, actions, and custom closed-loop feedback policies.
2. **Week 2: Robotic Controllers**: Study PID control, Operational Space Control (OSC), inverse kinematics, and dynamics.
3. **Week 3: Computer Vision**: Integrate cameras in simulation, camera projection matrices, depth maps, and point clouds.
4. **Week 4: Vision-Language Models**: Prompt VLMs for spatial tasks, parse target coordinates from text, and visual grounding.
5. **Week 5: Imitation Learning**: Collect expert demonstrations and train Behavioral Cloning (BC) policies.
6. **Week 7: Fine-Tuning**: Implement Parameter-Efficient Fine-Tuning (PEFT/LoRA) on custom manipulation datasets.
7. **Week 8: Capstone Project**: Deploy a VLA control loop in simulation to solve a multi-stage manipulation task.

---

## 📖 Progress Tracker

- [x] **Day 1**: Setup environment and run passive MuJoCo simulation.
- [x] **Day 2**: Interface with MuJoCo models using Gymnasium.
- [x] **Day 3**: Decipher step transitions, rewards, and episodes.
- [x] **Day 4**: Implement random and fixed action policy comparisons.
- [x] **Day 5**: Structuring proportional control loops.
- [x] **Day 6**: Deciphering Reacher-v5 observation vectors.
- [x] **Day 6.5**: Angle representation and Box spaces.
- [x] **Day 7**: Robot state, observation decoding, and kinematics fundamentals.
- [x] **Day 8**: Forward kinematics, planar arm geometry, and workspace analysis.
- [x] **Day 9**: Inverse kinematics algebraic solvers and verification loops.
- [x] **Day 10A**: Proportional (P) Control Loops.
- [x] **Day 10B**: Proportional-Integral (PI) Control Loops.
- [x] **Day 10C**: Proportional-Integral-Derivative (PID) Control Loops.
- [x] **Day 11**: Trajectory generation and smooth velocity profiling.
- [x] **Day 12**: Motion planning algorithms and Configuration Space (C-space) representation.
- [ ] **Day 13**: Implementing search-based A* (A-Star) path planners with heuristics (Next).

---

## 📖 Documentation Index

- **[System Architecture](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/architecture.md)**: Learn how MuJoCo, Gymnasium, and Python interact.
- **[Curriculum Roadmap](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/roadmap.md)**: A detailed week-by-week curriculum overview.
- **[Terminology Glossary](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/glossary.md)**: Standard concepts and definitions in robotics.
- **[Interview Questions](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/interview_questions.md)**: Study Q&As for robotics and VLA concepts.
- **Progress Journals**:
  - **[Day 1 Journal: Setup & Passive Sim](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/journal/day01.md)**
  - **[Day 2 Journal: Observations, Actions & Jacobian Control](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/journal/day02.md)**
  - **[Day 3 Journal: Reward & Episode Dynamics](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/journal/day03.md)**
  - **[Day 4 Journal: Random Policy & Exploration Baseline](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/journal/day04.md)**
  - **[Day 5 Journal: Proportional Control Loops](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/journal/day05.md)**
  - **[Day 6 Journal: Observation Vectors](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/journal/day06.md)**
  - **[Day 6.5 Journal: Continuous Spaces and Angles](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/journal/day06_5.md)**
  - **[Day 7 Journal: Robot State and Kinematics](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/journal/day07.md)**
  - **[Day 8 Journal: Forward Kinematics and 2-Link Robot Arm](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/journal/day08.md)**
  - **[Day 9 Journal: Inverse Kinematics and Verification](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/journal/day09.md)**
  - **[Day 10 Journal: PID Control & Feedback Systems](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/journal/day10.md)**
  - **[Day 11 Journal: Trajectory Generation & Motion Profiles](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/journal/day11.md)**
  - **[Day 12 Journal: Motion Planning & Configuration Space](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/journal/day12.md)**
