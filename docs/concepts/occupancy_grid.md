# Occupancy Grid

An **Occupancy Grid** is a discrete representation of a robot's workspace or configuration space where the environment is divided into a regular grid of cells, and each cell stores the occupancy state of that region.

---

## 1. Binary Occupancy Grids

In a binary occupancy grid, each cell has a discrete state:
- **0 (Free)**: No obstacles are present. The robot can cross this cell.
- **1 (Occupied)**: An obstacle is present. The cell is impassable.

---

## 2. Probabilistic Occupancy Grids

In real robots equipped with range sensors (LiDAR, ultrasonic), sensor readings are noisy and subject to uncertainty. Instead of binary values, each cell stores a probability of occupancy:
$$P(\mathbf{m}_i = 1)$$
where $\mathbf{m}_i$ represents grid cell $i$.
- **0.0**: Completely free.
- **0.5**: Unknown/Unexplored.
- **1.0**: Occupied.
- The probability is updated recursively using **Log-Odds** mapping as the robot sweeps the environment.

---

## 3. Discretization Trade-off

- **Resolution (Cell size)**:
  - Small cells (e.g. $1\,\text{cm}$) represent obstacles accurately but require large memory and slow down graph search planners.
  - Large cells (e.g. $1\,\text{m}$) require minimal memory and plan paths quickly but approximate boundaries coarsely, potentially blocking narrow doorways.
