"""
Week 2 - Lab 33: A* Search Visualization Module
==============================================

Objectives:
-----------
1. Provide a standalone visualization tool for grid-based A* path planning.
2. Render open set frontiers, closed set visited states, obstacles, start/goal markers, and shortest paths.
3. Save high-resolution visualization plots to disk for analysis.

Theory:
-------
- Color-coded grid layers visually distinguish search states:
  - White: Unvisited Free Space (0)
  - Gray: Obstacles (1)
  - Light Cyan: Visited Closed Set Nodes
  - Lime Green: Reconstructed Shortest Path
  - Red Circle: Start Coordinate
  - Gold Star: Target Goal Coordinate
"""

import os
import heapq
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

GRID = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
]

START = (0, 0)
GOAL = (4, 4)

SAVE_DIR = os.path.join("assets", "day14")
SAVE_PATH = os.path.join(SAVE_DIR, "lab33_visualization.png")


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def run_and_visualize(grid, start, goal, save_path):
    rows = len(grid)
    cols = len(grid[0])

    open_set = []
    heapq.heappush(open_set, (manhattan(start, goal), start))
    came_from = {}
    g_score = {start: 0}
    visited = set()

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while open_set:
        _, current = heapq.heappop(open_set)

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            break

        for dr, dc in directions:
            nr = current[0] + dr
            nc = current[1] + dc

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                neighbor = (nr, nc)
                tentative_g = g_score[current] + 1

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    heapq.heappush(open_set, (tentative_g + manhattan(neighbor, goal), neighbor))

    # Path reconstruction
    path = []
    if goal in visited or goal in came_from:
        node = goal
        while node in came_from:
            path.append(node)
            node = came_from[node]
        path.append(start)
        path.reverse()

    # Visualization
    fig, ax = plt.subplots(figsize=(6.5, 6.5))
    grid_arr = np.array(grid, dtype=float)
    ax.imshow(grid_arr, origin="lower", cmap="binary", alpha=0.3)

    # Plot Visited Closed Set Nodes
    if visited:
        vr, vc = zip(*visited)
        ax.scatter(vc, vr, color="cyan", s=120, alpha=0.6, label="Visited (Closed Set)", zorder=2)

    # Plot Shortest Path
    if path:
        pr, pc = zip(*path)
        ax.plot(pc, pr, color="limegreen", linewidth=4, zorder=4, label="Shortest Path")
        ax.scatter(pc, pr, color="darkgreen", s=50, zorder=5)

    # Start & Goal
    ax.scatter(start[1], start[0], color="crimson", s=200, marker="o", zorder=6, label=f"Start {start}")
    ax.scatter(goal[1], goal[0], color="gold", edgecolor="black", s=250, marker="*", zorder=6, label=f"Goal {goal}")

    ax.set_title("A* Search State & Path Visualization", fontsize=11, fontweight="bold")
    ax.set_xlabel("X (Cols)", fontsize=10)
    ax.set_ylabel("Y (Rows)", fontsize=10)

    ax.set_xticks(np.arange(cols))
    ax.set_yticks(np.arange(rows))
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend(loc="upper left", fontsize=8.5)

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path, dpi=150, bbox_inches="tight")
    plt.close()


def main():
    print("=" * 55)
    print("Starting Lab 33: A* Visualization Demo")
    print("=" * 55)
    run_and_visualize(GRID, START, GOAL, SAVE_PATH)
    print(f"Saved A* visualization plot to: {SAVE_PATH}")
    print("=" * 55)


if __name__ == "__main__":
    main()