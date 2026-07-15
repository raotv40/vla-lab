"""
Week 2 - Lab 28: Breadth-First Search (BFS) Grid Planner
========================================================

Objectives:
-----------
1. Perform a Breadth-First Search (BFS) graph traversal on an occupancy grid.
2. Track visited configurations to avoid infinite loops.
3. Trace and print the order of cell exploration.
4. Reconstruct the shortest path from start to goal coordinates.

Theory:
-------
- BFS is a graph search algorithm that explores nodes level-by-level (expanding uniformly outwards).
- It uses a FIFO (First-In, First-Out) queue.
- BFS guarantees finding the shortest path in graphs with uniform edge costs.
"""

import os
from collections import deque
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Occupancy Grid (0 = Free, 1 = Obstacle)
GRID = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0],
]

START = (0, 0)
GOAL = (3, 3)

# Output Paths
SAVE_DIR = os.path.join("assets", "day12")
SAVE_PATH = os.path.join(SAVE_DIR, "bfs_traversal.png")


def run_bfs(grid, start, goal):
    """Executes BFS path finding on a 2D binary grid."""
    rows = len(grid)
    cols = len(grid[0])

    queue = deque([start])
    visited = set()
    parent = {}
    traversal_order = []

    # Movement directions: Down, Up, Right, Left
    directions = [
        (1, 0),   # Down
        (-1, 0),  # Up
        (0, 1),   # Right
        (0, -1),  # Left
    ]

    while queue:
        r, c = queue.popleft()

        if (r, c) in visited:
            continue

        visited.add((r, c))
        traversal_order.append((r, c))

        # Print current visited cell (matches original script functionality)
        print(r, c)

        if (r, c) == goal:
            break

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if (0 <= nr < rows and 0 <= nc < cols and
                    grid[nr][nc] == 0 and (nr, nc) not in visited):
                queue.append((nr, nc))
                if (nr, nc) not in parent:
                    parent[(nr, nc)] = (r, c)

    # Path reconstruction
    path = []
    if goal in visited:
        curr = goal
        while curr != start:
            path.append(curr)
            curr = parent[curr]
        path.append(start)
        path.reverse()

    return traversal_order, path


def plot_traversal(grid, traversal, path):
    """Plots occupancy grid, node search expansion, and shortest path."""
    rows = len(grid)
    cols = len(grid[0])

    grid_array = np.array(grid)
    fig, ax = plt.subplots(figsize=(6, 6))

    # Display grid (obstacles in dark gray, free space in white)
    ax.imshow(grid_array, cmap="binary", origin="upper", alpha=0.3)

    # Plot obstacles clearly
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                ax.fill_between([c - 0.5, c + 0.5], r - 0.5, r + 0.5, color="dimgray")

    # Plot traversal order (visited nodes as circles with progressive colors)
    if traversal:
        t_rows, t_cols = zip(*traversal)
        ax.scatter(t_cols, t_rows, c=range(len(traversal)), cmap="cool", s=150, zorder=3,
                   label="Visited Order")

    # Plot start and goal
    ax.plot(START[1], START[0], marker="s", color="green", markersize=12, label="Start (0,0)")
    ax.plot(GOAL[1], GOAL[0], marker="X", color="red", markersize=12, label="Goal (3,3)")

    # Plot shortest path
    if path:
        p_rows, p_cols = zip(*path)
        ax.plot(p_cols, p_rows, color="lime", linewidth=4.0, zorder=4, label="Shortest Path")

    ax.set_title("Breadth-First Search (BFS) Grid Planner", fontsize=11, fontweight="bold")
    ax.set_xlabel("Column Index", fontsize=10)
    ax.set_ylabel("Row Index", fontsize=10)

    ax.set_xticks(np.arange(cols))
    ax.set_yticks(np.arange(rows))
    ax.grid(True, which="both", color="lightgray", linestyle="--", linewidth=0.5)
    ax.legend(loc="upper right", fontsize=8)

    os.makedirs(SAVE_DIR, exist_ok=True)
    plt.savefig(SAVE_PATH, dpi=150, bbox_inches="tight")
    plt.close()


def main():
    # Run the traversal and path finding
    traversal, path = run_bfs(GRID, START, GOAL)

    # Re-verify results
    print(f"\nShortest Path found from {START} to {GOAL}:")
    if path:
        print(" -> ".join([str(p) for p in path]))
    else:
        print("NO PATH FOUND")

    # Save visualization plot
    plot_traversal(GRID, traversal, path)
    print(f"\nSaved BFS traversal plot to: {SAVE_PATH}")


if __name__ == "__main__":
    main()