# Week 2: Robotic Control Frameworks

This directory covers **Robotic Controllers**, focusing on classical feedback loops, Proportional-Integral-Derivative (PID) algorithms, and physical step-response characteristics.

---

## 📂 Lab Directory

| Lab Script | Controller Type | Description |
| :--- | :--- | :--- |
| [lab22_p_controller.py](file:///C:/Users/Vishrao/vla-lab/vla-lab/week02/lab22_p_controller.py) | Proportional (P) | Simulates a single joint under P feedback. Demonstrates rise time, overshoot, and steady-state error under gravity. |
| [lab23_pi_controller.py](file:///C:/Users/Vishrao/vla-lab/vla-lab/week02/lab23_pi_controller.py) | Proportional-Integral (PI) | Introduces integral accumulation to cancel steady-state gravity offset. Demonstrates integral windup and phase lag. |
| [lab24_pid_controller.py](file:///C:/Users/Vishrao/vla-lab/vla-lab/week02/lab24_pid_controller.py) | Proportional-Integral-Derivative (PID) | Implements full PID feedback control. Demonstrates how derivative braking dampens oscillations and speeds up settling. |
| [lab25_linear_trajectory.py](file:///C:/Users/Vishrao/vla-lab/vla-lab/week02/lab25_linear_trajectory.py) | Linear Interpolation | Generates linear path trajectories (LERP) and demonstrates boundary discontinuities. |
| [lab26_velocity_profile.py](file:///C:/Users/Vishrao/vla-lab/vla-lab/week02/lab26_velocity_profile.py) | Trapezoidal Velocity Profile | Generates smooth trapezoidal velocity profiles to parameterize paths over time. |
| [lab27_grid_planner.py](file:///C:/Users/Vishrao/vla-lab/vla-lab/week02/lab27_grid_planner.py) | Grid Initialization | Discretizes space into a binary occupancy grid mapping obstacles. |
| [lab28_bfs_planner.py](file:///C:/Users/Vishrao/vla-lab/vla-lab/week02/lab28_bfs_planner.py) | Breadth-First Search | Performs discrete grid path planning using a FIFO queue to find shortest paths. |
| [lab29_manhattan_distance.py](file:///C:/Users/Vishrao/vla-lab/vla-lab/week02/lab29_manhattan_distance.py) | Manhattan Heuristic | Computes grid L1 norm distance heuristic and plots orthogonal steps. |
| [lab30_astar_planner.py](file:///C:/Users/Vishrao/vla-lab/vla-lab/week02/lab30_astar_planner.py) | A* Search | Demonstrates informed graph search using priority queue f(n) = g(n) + h(n). |
| [lab31_astar_grid.py](file:///C:/Users/Vishrao/vla-lab/vla-lab/week02/lab31_astar_grid.py) | Complete A* Grid | Solves 2D occupancy grid shortest path with Open/Closed sets and f-scores. |
| [lab32_astar_reconstruction.py](file:///C:/Users/Vishrao/vla-lab/vla-lab/week02/lab32_astar_reconstruction.py) | Path Reconstruction | Demonstrates parent node tracking via came_from and iterative backtracking. |
| [lab33_astar_visualization.py](file:///C:/Users/Vishrao/vla-lab/vla-lab/week02/lab33_astar_visualization.py) | Search Visualizer | Renders open/closed sets, obstacles, start/goal markers, and shortest paths. |

---

## Running the Labs

Ensure you have activated your virtual environment:
```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Run each lab script from the repository root:
```bash
python week02/lab22_p_controller.py
python week02/lab23_pi_controller.py
python week02/lab24_pid_controller.py
python week02/lab25_linear_trajectory.py
python week02/lab26_velocity_profile.py
python week02/lab27_grid_planner.py
python week02/lab28_bfs_planner.py
python week02/lab29_manhattan_distance.py
python week02/lab30_astar_planner.py
python week02/lab31_astar_grid.py
python week02/lab32_astar_reconstruction.py
python week02/lab33_astar_visualization.py
```
Each script will output text results to the console and save step-response/waveform/grid plots to the respective assets directories (`assets/day10/`, `assets/day11/`, `assets/day12/`, `assets/day13/`, and `assets/day14/`).
