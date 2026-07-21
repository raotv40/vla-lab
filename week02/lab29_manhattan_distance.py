"""
Week 2 - Lab 29: Manhattan Distance Heuristic
==============================================

Objectives:
-----------
1. Compute the Manhattan ($L_1$ norm) distance between grid coordinates.
2. Demonstrate how grid-constrained movement (4-connected orthogonal steps)
   relates to distance heuristics in path planning.
3. Visualize the Manhattan grid path and bounding box in Matplotlib.

Theory:
-------
- Manhattan Distance is the sum of absolute differences of Cartesian coordinates:
  d(a, b) = |a_x - b_x| + |a_y - b_y|
- It represents the shortest distance between two points on a 4-connected grid
  where diagonal movements are not permitted.
- In A* grid search, Manhattan distance provides an admissible and consistent
  heuristic when orthogonal step movement cost is 1.
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Default Start and Goal Coordinates
START_COORD = (2, 3)
GOAL_COORD = (7, 8)

# Output Paths
SAVE_DIR = os.path.join("assets", "day13")
SAVE_PATH = os.path.join(SAVE_DIR, "manhattan_distance.png")


def manhattan(a: tuple[int, int], b: tuple[int, int]) -> int:
    """Computes the Manhattan distance between two 2D grid coordinates."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def plot_manhattan_path(start: tuple[int, int], goal: tuple[int, int], distance: int) -> None:
    """Plots the start/goal coordinates and a representative Manhattan path on a grid."""
    fig, ax = plt.subplots(figsize=(6, 6))

    # Generate step-by-step orthogonal grid path coordinates
    x_path = [start[0]]
    y_path = [start[1]]

    # Step horizontally first, then vertically
    curr_x, curr_y = start
    step_x = 1 if goal[0] >= start[0] else -1
    step_y = 1 if goal[1] >= start[1] else -1

    while curr_x != goal[0]:
        curr_x += step_x
        x_path.append(curr_x)
        y_path.append(curr_y)

    while curr_y != goal[1]:
        curr_y += step_y
        x_path.append(curr_x)
        y_path.append(curr_y)

    # Plot grid boundaries
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_xticks(range(11))
    ax.set_yticks(range(11))
    ax.grid(True, linestyle="--", alpha=0.6)

    # Plot Manhattan path steps
    ax.plot(x_path, y_path, color="crimson", linestyle="-", linewidth=2.5,
            marker="o", markersize=6, label=f"Manhattan Path (Cost = {distance})")

    # Plot Euclidean straight line for visual comparison
    ax.plot([start[0], goal[0]], [start[1], goal[1]], color="gray", linestyle=":",
            linewidth=1.5, label="Euclidean Line")

    # Highlight Start and Goal
    ax.plot(start[0], start[1], marker="s", color="green", markersize=12, label=f"Start {start}")
    ax.plot(goal[0], goal[1], marker="X", color="blue", markersize=12, label=f"Goal {goal}")

    ax.set_title(f"Manhattan Distance Grid Calculation (Distance = {distance})",
                 fontsize=11, fontweight="bold")
    ax.set_xlabel("X Grid Coordinate", fontsize=10)
    ax.set_ylabel("Y Grid Coordinate", fontsize=10)
    ax.legend(loc="upper left", fontsize=9)

    os.makedirs(SAVE_DIR, exist_ok=True)
    plt.savefig(SAVE_PATH, dpi=150, bbox_inches="tight")
    plt.close()


def main() -> None:
    distance = manhattan(START_COORD, GOAL_COORD)

    print("=" * 50)
    print("Manhattan Distance")
    print("=" * 50)
    print(f"Start : {START_COORD}")
    print(f"Goal  : {GOAL_COORD}")
    print(f"Distance = {distance}")

    plot_manhattan_path(START_COORD, GOAL_COORD, distance)
    print(f"\nSaved Manhattan distance plot to: {SAVE_PATH}")


if __name__ == "__main__":
    main()