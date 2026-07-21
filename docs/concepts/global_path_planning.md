# Global Path Planning

**Global Path Planning** is the high-level navigation module that computes a coarse, collision-free path from a robot's start position to a distant goal across a static global map.

---

## Global vs. Local Planners in ROS Nav2

- **Global Planner (A*, Dijkstra)**: Solves long-distance spatial paths over static occupancy grids.
- **Local Planner (TEB, DWA)**: Solves real-time obstacle avoidance around dynamic obstacles at high frequency ($10-50\,\text{Hz}$).

```text
 Static Map ──► Global Planner (A*) ──► Waypoints ──► Local Planner (DWA) ──► Motor Commands
```
