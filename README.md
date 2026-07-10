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
├── docs/                    # Architectural documents and study notes
│   ├── concepts/            # Core control theory and robotics concepts
│   │   ├── action_space.md  # Action space specifications
│   │   ├── box_space.md     # Gymnasium Box spaces
│   │   ├── controller.md    # Robot controller definition
│   │   ├── end_effector.md  # End-effector kinematics
│   │   ├── error.md         # Tracking error mathematical derivation
│   │   ├── feature_vector.md # Feature vector representation
│   │   ├── feedback.md      # Open-loop vs closed-loop feedback systems
│   │   ├── joint_position.md # Joint positions and angles
│   │   ├── joint_velocity.md # Joint velocities
│   │   ├── observation_space.md # Observation space specifications
│   │   ├── observation_vector.md # Observation vector structure
│   │   ├── proportional_controller.md # Proportional control laws
│   │   ├── sin_cos_encoding.md # Trigonometric angle encoding
│   │   └── target_position.md # Target position reference
│   ├── journal/             # Daily progress journals
│   │   ├── day01.md         # Setup and passive simulation
│   │   ├── day02.md         # Observations, actions, and Jacobian control
│   │   ├── day03.md         # Reward dynamics and step transitions
│   │   ├── day04.md         # Random policy and exploration
│   │   ├── day05.md         # Proportional control loops
│   │   ├── day06.md         # Deciphering observation vectors
│   │   └── day06_5.md       # Angle representations and continuous spaces
│   ├── architecture.md      # System layout (Python -> Gym -> MuJoCo)
│   ├── glossary.md          # Key terminology and confidence scores
│   ├── interview_questions.md # Study guide Q&As for robotics and VLA
│   └── roadmap.md           # 8-week curriculum breakdown
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
│   └── lab15_angles.py      # arctan2 decoding & discontinuity demo
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
6. **Week 6: OpenVLA Foundations**: Load pre-trained foundation models, tokenize actions, and evaluate zero-shot performance.
7. **Week 7: Fine-Tuning**: Implement Parameter-Efficient Fine-Tuning (PEFT/LoRA) on custom manipulation datasets.
8. **Week 8: Capstone Project**: Deploy a full VLA control loop in simulation to solve a multi-stage manipulation task.

---

## 📖 Progress Tracker

- [x] **Day 1**: Setup environment and run passive MuJoCo simulation.
- [x] **Day 2**: Interface with MuJoCo models using Gymnasium.
- [x] **Day 3**: Decipher step transitions, rewards, and episodes.
- [x] **Day 4**: Implement random and fixed action policy comparisons.
- [x] **Day 5**: Structuring proportional control loops.
- [x] **Day 6**: Deciphering Reacher-v5 observation vectors.
- [x] **Day 6.5**: Angle representation and Box spaces.
- [ ] **Day 7**: Implementing observation-driven P-controllers (Next).

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
