# Path Reconstruction & Parent Tracking

In graph search algorithms, **Path Reconstruction** is the procedure used to build the final sequence of waypoints from the start node to the goal node after the search loop terminates.

---

## The `came_from` Dictionary

Instead of storing full path histories inside every priority queue item, A* maintains a single mapping dictionary:

$$\text{came\_from}[\text{neighbor}] = \text{current}$$

Whenever a cheaper path to `neighbor` is discovered, `came_from` is updated to point back to `current`.

---

## Backtracking Procedure

1. Initialize `node = goal` and `path = []`.
2. While `node` exists in `came_from`:
   - Append `node` to `path`.
   - Update `node = came_from[node]`.
3. Append `start` to `path`.
4. Reverse `path` to obtain order: `[start, waypoint_1, ..., goal]`.

```text
 Goal (4,4) ──► Parent (3,4) ──► Parent (2,4) ──► ... ──► Start (0,0)  ==Reversed==►  Full Path
```
