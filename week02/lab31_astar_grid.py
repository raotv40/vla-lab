"""
Week 2 - Lab 31: Complete Grid-Based A* Path Planner
===================================================

Objectives:
-----------
1. Implement a complete grid-based A* (A-Star) shortest path solver in Python.
2. Maintain Open Set (priority queue), Closed Set (visited nodes), g-scores, and f-scores.
3. Track parent node transitions using a came_from dictionary for path reconstruction.
4. Visualize the occupancy grid, obstacles, visited frontier, start/goal markers, and shortest path.

Theory:
-------
- f(n) = g(n) + h(n): Total priority score where g(n) is actual cost from start, h(n) is heuristic.
- Manhattan Heuristic: h(a, b) = |a_x - b_x| + |a_y - b_y| (admissible for 4-connected grid).
- Path Reconstruction: Traverses came_from mapping backwards from goal to start.
"""

import os
import heapq
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# 5x5 Occupancy Grid (0 = Free Space, 1 = Obstacle)
DEFAULT_GRID = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
]

DEFAULT_START = (0, 0)
DEFAULT_GOAL = (4, 4)

# Output Paths
SAVE_DIR = os.path.join("assets", "day14")
SAVE_PATH = os.path.join(SAVE_DIR, "astar_grid.png")


def manhattan_heuristic(a: tuple[int, int], b: tuple[int, int]) -> int:
    """Computes Manhattan distance heuristic between two grid coordinates."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def run_astar_grid(grid: list[list[int]], start: tuple[int, int], goal: tuple[int, int]):
    """Executes complete A* path planning on a 2D occupancy grid."""
    rows = len(grid)
    cols = len(grid[0])

    # Priority queue stores tuples of (f_score, node)
    open_set = []
    heapq.heappush(open_set, (manhattan_heuristic(start, goal), start))

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

            if not (0 <= nr < rows and 0 <= nc < cols):
                continue
            if grid[nr][nc] == 1:
                continue

            neighbor = (nr, nc)
            tentative_g = g_score[current] + 1

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + manhattan_heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))

    # Path reconstruction
    path = []
    if goal in visited or goal in came_from:
        node = goal
        while node in came_from:
            path.append(node)
            node = came_from[node]
        path.append(start)
        path.reverse()

    return path, visited, g_score, came_from


def plot_astar_results(grid: list[list[int]], path: list[tuple[int, int]],
                       start: tuple[int, int], goal: tuple[int, int], save_path: str) -> None:
    """Visualizes the grid map, obstacles, start/goal markers, and reconstructed shortest path."""
    rows = len(grid)
    cols = len(grid[0])
    image = np.array(grid, dtype=float)

    fig, ax = plt.subplots(figsize=(6, 6))

    # Display grid map (0 = White/Free, 1 = Dark Gray/Obstacle)
    ax.imshow(image, origin="lower", cmap="binary", alpha=0.3)

    # Fill obstacles cleanly
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                ax.fill_between([c - 0.5, c + 0.5], r - 0.5, r + 0.5, color="dimgray")

    # Plot path line and waypoints
    if path:
        path_r, path_c = zip(*path)
        ax.plot(path_c, path_r, color="dodgerblue", linewidth=3.5, zorder=3, label="Shortest Path")
        ax.scatter(path_c, path_r, color="dodgerblue", s=60, zorder=4)

    # Draw Start and Goal markers
    ax.scatter(start[1], start[0], color="crimson", s=200, marker="o", zorder=5, label=f"Start {start}")
    ax.scatter(goal[1], goal[0], color="gold", edgecolor="black", s=250, marker="*", zorder=5, label=f"Goal {goal}")

    ax.set_title("Complete A* Grid Path Planner", fontsize=11, fontweight="bold")
    ax.set_xlabel("Column Index (X)", fontsize=10)
    ax.set_ylabel("Row Index (Y)", fontsize=10)

    ax.set_xticks(np.arange(cols))
    ax.set_yticks(np.arange(rows))
    ax.set_xticks(np.arange(-0.5, cols, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, rows, 1), minor=True)
    ax.grid(which="minor", color="gray", linestyle="-", linewidth=0.5)

    ax.legend(loc="upper left", fontsize=9)

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path, dpi=150, bbox_inches="tight")
    plt.close()


def main() -> None:
    path, visited, g_score, came_from = run_astar_grid(DEFAULT_GRID, DEFAULT_START, DEFAULT_GOAL)

    plot_astar_results(DEFAULT_GRID, path, DEFAULT_START, DEFAULT_GOAL, SAVE_PATH)

    print("Shortest Path")
    for p in path:
        print(p)

    print("=" * 40)
    print("A* Search Complete")
    print("=" * 40)
    print(f"Start : {DEFAULT_START}")
    print(f"Goal  : {DEFAULT_GOAL}")
    print(f"Goal Reached : {DEFAULT_GOAL in visited}")
    print(f"Visited Nodes: {len(visited)}")
    print(f"Discovered Nodes: {len(g_score)}")
    print(f"\nSaved A* grid visualization to: {SAVE_PATH}")


if __name__ == "__main__":
    main()
