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
│   │   ├── controller.md    # Robot controller definition
│   │   ├── error.md         # Tracking error mathematical derivation
│   │   ├── feedback.md      # Open-loop vs closed-loop feedback systems
│   │   └── proportional_controller.md # Proportional control laws
│   ├── journal/             # Daily progress journals
│   │   ├── day01.md         # Setup and passive simulation
│   │   ├── day02.md         # Observations, actions, and Jacobian control
│   │   ├── day03.md         # Reward dynamics and step transitions
│   │   ├── day04.md         # Random policy and exploration
│   │   └── day05.md         # Proportional control loops
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
│   └── lab09_simple_controller.py # Proportional control loop demo
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
