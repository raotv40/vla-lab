"""
Week 2 - Lab 32: A* Parent Tracking and Path Reconstruction
==========================================================

Objectives:
-----------
1. Explicitly demonstrate parent node tracking using a `came_from` dictionary during search.
2. Implement iterative backtracking from goal coordinate to start coordinate.
3. Print parent node mappings and reconstructed path sequences.
4. Plot step-by-step backtracked vectors in Matplotlib.

Theory:
-------
- During graph exploration, whenever a shorter path to neighbor v is discovered via node u,
  the algorithm updates `came_from[v] = u`.
- Once the goal node is reached, the path is reconstructed by reversing parent links:
  Goal -> parent[Goal] -> parent[parent[Goal]] -> ... -> Start
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
SAVE_PATH = os.path.join(SAVE_DIR, "lab32_reconstruction.png")


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def reconstruct_path_explicit(came_from: dict, start: tuple[int, int], goal: tuple[int, int]):
    """Iteratively backtracks through came_from dictionary from goal to start."""
    path = []
    curr = goal

    print("\nParent Tracking (Backtracking Step-by-Step):")
    print("-" * 45)
    while curr in came_from:
        parent = came_from[curr]
        print(f"Node {curr} <-- came from Parent {parent}")
        path.append(curr)
        curr = parent

    path.append(start)
    path.reverse()
    print("-" * 45)
    return path


def main():
    print("=" * 55)
    print("Starting Lab 32: A* Path Reconstruction Demonstration")
    print("=" * 55)

    rows = len(GRID)
    cols = len(GRID[0])

    open_set = []
    heapq.heappush(open_set, (manhattan(START, GOAL), START))
    came_from = {}
    g_score = {START: 0}
    visited = set()

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while open_set:
        _, current = heapq.heappop(open_set)

        if current in visited:
            continue
        visited.add(current)

        if current == GOAL:
            break

        for dr, dc in directions:
            nr = current[0] + dr
            nc = current[1] + dc

            if 0 <= nr < rows and 0 <= nc < cols and GRID[nr][nc] == 0:
                neighbor = (nr, nc)
                tentative_g = g_score[current] + 1

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    heapq.heappush(open_set, (tentative_g + manhattan(neighbor, GOAL), neighbor))

    # Reconstruct Path
    path = reconstruct_path_explicit(came_from, START, GOAL)

    print(f"\nFinal Reconstructed Path ({len(path)} waypoints):")
    print(" -> ".join([str(p) for p in path]))

    # Visualization
    fig, ax = plt.subplots(figsize=(6, 6))
    grid_arr = np.array(GRID, dtype=float)
    ax.imshow(grid_arr, origin="lower", cmap="binary", alpha=0.3)

    # Plot Backtracking Arrows
    for child, parent in came_from.items():
        pr, pc = parent
        cr, cc = child
        ax.annotate("", xy=(pc, pr), xytext=(cc, cr),
                    arrowprops=dict(arrowstyle="->", color="purple", lw=1.5, alpha=0.7))

    # Highlight Final Path
    pr, pc = zip(*path)
    ax.plot(pc, pr, color="limegreen", linewidth=3.5, label="Reconstructed Path")

    ax.scatter(START[1], START[0], color="crimson", s=180, zorder=5, label="Start")
    ax.scatter(GOAL[1], GOAL[0], color="gold", edgecolor="black", s=200, marker="*", zorder=5, label="Goal")

    ax.set_title("A* Parent Links (came_from) and Reconstructed Path", fontsize=11, fontweight="bold")
    ax.set_xlabel("X (Cols)")
    ax.set_ylabel("Y (Rows)")
    ax.legend(loc="upper left")
    ax.grid(True, linestyle="--", alpha=0.5)

    os.makedirs(SAVE_DIR, exist_ok=True)
    plt.savefig(SAVE_PATH, dpi=150, bbox_inches="tight")
    plt.close()

    print(f"\nSaved path reconstruction plot to: {SAVE_PATH}")
    print("=" * 55)


if __name__ == "__main__":
    main()
