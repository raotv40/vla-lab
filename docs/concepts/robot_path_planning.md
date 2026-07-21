# Robot Path Planning

**Robot Path Planning** is the algorithmic module responsible for generating a spatial, collision-free sequence of waypoints for a robot to navigate through an environment toward a designated goal.

---

## Roles in the Navigation Stack

In mobile robots and manipulators:
- **Global Planner**: Computes a complete, coarse path from start to goal over a global map (using A* or Dijkstra).
- **Local Planner**: Executes real-time obstacle avoidance around dynamic obstacles using local sensor feedback (e.g., Dynamic Window Approach, TEB Local Planner).

```text
 Global Map ──► Global Planner (A*) ──► Waypoints ──► Local Planner (DWA) ──► Velocity Commands
```
