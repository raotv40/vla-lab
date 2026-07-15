# Day 12 Journal: Motion Planning and Configuration Space

- **Date**: 2026-07-15
- **Author**: Vishrao
- **Milestone**: Day 12 of VLA Learning Lab

---

## Learning Objectives
1. Define the fundamental differences between motion planning and trajectory planning.
2. Conceptualize the utility of Configuration Space (C-Space) and C-obstacles in simplifying path search.
3. Formulate and construct discrete 2D Occupancy Grid Maps in Python.
4. Execute and trace Breadth-First Search (BFS) graph planning to find shortest paths.
5. Review search-based A* heuristics and sampling-based RRT scalability constraints.
6. Outline the roles of each module inside modern hierarchical Vision-Language-Action (VLA) robot control pipelines.

---

## Motion Planning Overview
**Motion Planning** is the geometric problem of finding a continuous, collision-free path that connects a starting configuration $\mathbf{q}_{\text{start}}$ to a goal configuration $\mathbf{q}_{\text{goal}}$ in the presence of obstacles.

---

## Motion Planning vs. Trajectory Planning
- **Motion Planning**: Solves the *geometry* of the path. It outputs a spatial sequence of collision-free waypoints without timing parameters.
- **Trajectory Planning**: Solves the *physics* of the path. It takes geometric waypoints and maps them to smooth speed profiles over time (calculating target positions, velocities, and accelerations) to respect torque limits.

---

## Configuration Space (C-Space)
The **Configuration Space (C-Space)** represents the set of all possible mechanical postures of a robot:
- Coordinates are joint variables: $\mathbf{q} = (\theta_1, \theta_2, \dots, \theta_n)$.
- By mapping physical obstacles into joint space, the robot's complex geometry collapses into a **single point**.
- Planning is simplified from intersecting multi-link solids in the workspace to searching for a path of a single point moving through the free space ($\mathcal{C}_{\text{free}}$).

---

## Occupancy Grid
An **Occupancy Grid** discretizes continuous space into a regular matrix of cells, where each cell stores the occupancy state (e.g. `0` for free space, `1` for occupied space). This provides a computationally efficient lookup structure for collision checking.

---

## Collision Checking
Collision checking determines whether a robot's posture intersects obstacles or its own body:
- **Geometric checking**: Uses bounding spheres or boxes (AABB) and intersection math (e.g. Separating Axis Theorem).
- **Grid checking**: Reduced to an $O(1)$ array lookup: `if grid[row][col] == 1: collision`.

---

## Lab Results

### Lab 27: Occupancy Grid Generation
- **Setup**: Initialized a $10 \times 10$ binary occupancy grid map, designating a central $3 \times 3$ block as an obstacle.
- **Command**: `python week02/lab27_grid_planner.py`
- **Output**:
  ```text
  Occupancy Grid Initialized:
  [[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 1. 1. 1. 0. 0. 0.]
   [0. 0. 0. 0. 1. 1. 1. 0. 0. 0.]
   [0. 0. 0. 0. 1. 1. 1. 0. 0. 0.]
   [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
  ```
- **Plot**: Saved to `assets/day12/occupancy_grid.png`

### Lab 28: BFS Grid Planner
- **Setup**: Solved the shortest path on a $4 \times 4$ maze from `(0,0)` to `(3,3)`.
- **Command**: `python week02/lab28_bfs_planner.py`
- **Output**:
  ```text
  0 0
  0 1
  0 2
  1 2
  0 3
  2 2
  2 3
  2 1
  3 3

  Shortest Path found from (0, 0) to (3, 3):
  (0, 0) -> (0, 1) -> (0, 2) -> (1, 2) -> (2, 2) -> (2, 3) -> (3, 3)
  ```
- **Plot**: Saved to `assets/day12/bfs_traversal.png`

---

## BFS Algorithm
Breadth-First Search uses a FIFO queue to expand nodes uniformly level-by-level. It guarantees finding the shortest path on unweighted graphs with $O(V+E)$ time complexity, but suffers from high memory usage because it is an uninformed search.

---

## A* Overview
A* is an informed search algorithm that uses heuristics to guide node expansion, evaluating:
$$f(n) = g(n) + h(n)$$
This restricts the search space toward the goal, avoiding uniform exploration.

---

## RRT Overview
RRT is a sampling-based planning algorithm that builds a tree by randomly sampling configurations in the continuous C-Space. It scales very well to high dimensions because it avoids grid discretization.

---

## Exercise Answers

- **Why robots need motion planning**: Without motion planning, a robot would move blindly toward a target, resulting in collisions with obstacles, self-collisions, or mechanical damage.
- **Why trajectory generation alone is not sufficient**: Trajectory generators only compute speed profiles over time. They assume the path is already collision-free. They do not know about obstacles.
- **Why collision checking is essential**: It is the safety layer of the planner, verifying that candidate configurations do not intersect obstacles before commands are executed.
- **Why Configuration Space simplifies planning**: It reduces a complex multi-link robot collision check down to a single point moving through C-obstacles.

---

## Where Motion Planning Is Used
- **Industrial Software**: **ABB RobotStudio**, **FANUC**, **KUKA System Software**, and **Universal Robots** Polyscope use planners to design collision-free trajectories.
- **Open-source Stacks**: **ROS MoveIt** is the standard manipulation library using RRT and A* variants.
- **Autonomous & Mobile Robots**: Autonomous vehicles (e.g. Tesla, Waymo) use hybrid A* to plan lane changes, while warehouse AGVs (e.g. Amazon Kiva) use grid search.
- **Drones**: 3D obstacle avoidance planning.

---

## VLA Connection

```text
 1. Vision (RGB-D Cameras)
    │  (Captures depth images, point clouds, and object shapes)
    ▼
 2. Language Understanding (VLM)
    │  (Interprets natural text: "pick up the blue cup and stack it")
    ▼
 3. Task Planning
    │  (Sequences actions: Move to cup -> Close Gripper -> Lift -> Move to Box)
    ▼
 4. Motion Planning
    │  (Computes geometric waypoints around barriers, avoiding collisions)
    ▼
 5. Trajectory Generation
    │  (Maps geometric waypoints to smooth velocity profiles, respecting torque limits)
    ▼
 6. Inverse Kinematics (IK)
    │  (Converts Cartesian points (x, y) into target joint angles theta_d)
    ▼
 7. PID Controller
    │  (Runs at 1 kHz to track joint setpoints, outputting torque currents)
    ▼
 8. Motor Drivers -> Robot Motion
```

---

## Commands Used
```bash
# Run occupancy grid map plotter
python week02/lab27_grid_planner.py

# Run BFS shortest path grid planner
python week02/lab28_bfs_planner.py
```

---

## Issues Encountered & Solutions
- **Issue**: AttributeError on matplotlib `AxesImage.set() got an unexpected keyword argument 'edgecolors'` in `imshow`.
- **Solution**: Removed `edgecolors` and `linewidths` from `imshow` and added gridlines using minor tick grid configurations instead.

---

## Glossary & Interview Links
- Glossary terms added to [docs/glossary.md](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/glossary.md).
- Q&As added to [docs/interview_questions.md](file:///C:/Users/Vishrao/vla-lab/vla-lab/docs/interview_questions.md).

---

## Reflection
Configuration space collapses physical link collision complexities into a single point, allowing graph-search algorithms like BFS to solve geometric paths cleanly.

---

## Next Steps
Day 13: Implement a complete A* (A-Star) path planner with search heuristic variations, shortest-path reconstructions, and comparisons with BFS.
