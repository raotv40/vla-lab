"""
Week 2 - Lab 27: Occupancy Grid Generation
==========================================

Objectives:
-----------
1. Initialize a simple discrete grid representing a robotic workspace.
2. Mark regions of space as binary obstacles (obstacle space vs. free space).
3. Visualize the occupancy grid using Matplotlib.

Theory:
-------
- An Occupancy Grid discretizes space into a binary matrix where:
  - 0: Free space (passable by the robot).
  - 1: Obstacle space (collisions occur, impassable).
- Discretization simplifies continuous geometric environments into graphs
  suitable for search algorithms (BFS, A*).
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Grid Dimensions
GRID_ROWS = 10
GRID_COLS = 10

# Obstacle Slice Bounds (Rows 4-6, Columns 4-6)
OBS_ROW_START = 4
OBS_ROW_END = 7
OBS_COL_START = 4
OBS_COL_END = 7

# Output Paths
SAVE_DIR = os.path.join("assets", "day12")
SAVE_PATH = os.path.join(SAVE_DIR, "occupancy_grid.png")


def main():
    print("=" * 60)
    print("Starting Lab 27: Occupancy Grid Planner")
    print("=" * 60)

    # Initialize a 10x10 empty grid (all zeros represent free space)
    grid = np.zeros((GRID_ROWS, GRID_COLS))

    # Mark the central block as an obstacle (1)
    grid[OBS_ROW_START:OBS_ROW_END, OBS_COL_START:OBS_COL_END] = 1.0

    print("Occupancy Grid Initialized:")
    print(grid)

    # Plot the grid
    fig, ax = plt.subplots(figsize=(6, 6))
    im = ax.imshow(grid, origin="lower", cmap="binary", alpha=0.8)

    # Add grid lines between cells
    ax.set_xticks(np.arange(-0.5, GRID_COLS, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, GRID_ROWS, 1), minor=True)
    ax.grid(which="minor", color="gray", linestyle="-", linewidth=0.5)

    ax.set_title("Simple Occupancy Grid Map", fontsize=11, fontweight="bold")
    ax.set_xlabel("X Grid Cell Coordinate", fontsize=10)
    ax.set_ylabel("Y Grid Cell Coordinate", fontsize=10)

    # Add labels to ticks
    ax.set_xticks(np.arange(GRID_COLS))
    ax.set_yticks(np.arange(GRID_ROWS))

    # Colorbar to represent obstacle values
    fig.colorbar(im, ax=ax, label="Occupancy State (0=Free, 1=Obstacle)", ticks=[0, 1])

    os.makedirs(SAVE_DIR, exist_ok=True)
    plt.savefig(SAVE_PATH, dpi=150, bbox_inches="tight")
    plt.close()

    print(f"\nSaved occupancy grid plot to: {SAVE_PATH}")
    print("=" * 60)


if __name__ == "__main__":
    main()