"""
Week 2 - Lab 30: A* Search Algorithm Demonstration
=================================================

Objectives:
-----------
1. Implement the A* (A-Star) search algorithm on a weighted directed graph.
2. Evaluate priority queue node selection using total cost f(n) = g(n) + h(n).
3. Demonstrate how heuristic functions guide node expansion toward the goal.
4. Visualize graph nodes and search execution.

Theory:
-------
- g(n): The exact path cost accumulated from the start node to node n.
- h(n): The heuristic estimated cost from node n to the goal node.
- f(n): The total estimated cost of the path passing through node n.
- Priority Queue (Min-Heap): Always pops the node with the lowest f(n) value.
"""

import os
import heapq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Graph Structure (Directed Adjacency List: Node -> List of (Neighbor, EdgeWeight))
GRAPH = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("C", 1)],
    "C": [("G", 3)],
    "G": []
}

# Default Heuristic Values (h(n) = 0 for all nodes represents Dijkstra's algorithm baseline)
DEFAULT_HEURISTIC = {
    "S": 0,
    "A": 0,
    "B": 0,
    "C": 0,
    "G": 0
}

# Node Layout Positions for Visualization
NODE_POSITIONS = {
    "S": (0, 1),
    "A": (1, 2),
    "B": (1, 0),
    "C": (2, 1),
    "G": (3, 1)
}

# Output Paths
SAVE_DIR = os.path.join("assets", "day13")
SAVE_PATH = os.path.join(SAVE_DIR, "astar_expansion.png")


def run_astar(graph: dict, heuristic: dict, start: str = "S", goal: str = "G") -> list[str]:
    """Runs A* search on a graph given a heuristic dictionary and returns visited nodes in order."""
    # Priority Queue stores tuples of (f_score, g_score, node)
    pq = []
    heapq.heappush(pq, (0 + heuristic[start], 0, start))

    visited = set()
    visitation_order = []

    while pq:
        f, g, node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        visitation_order.append(node)
        print(f"Visiting {node}")

        if node == goal:
            break

        for nxt, weight in graph[node]:
            if nxt not in visited:
                g_nxt = g + weight
                f_nxt = g_nxt + heuristic[nxt]
                heapq.heappush(pq, (f_nxt, g_nxt, nxt))

    return visitation_order


def plot_astar_graph(graph: dict, visited_nodes: list[str]) -> None:
    """Plots the directed graph nodes, edge weights, and visitation order."""
    fig, ax = plt.subplots(figsize=(7, 5))

    # Draw directed edges
    for node, neighbors in graph.items():
        x1, y1 = NODE_POSITIONS[node]
        for nxt, weight in neighbors:
            x2, y2 = NODE_POSITIONS[nxt]
            ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                        arrowprops=dict(arrowstyle="->", color="gray", lw=1.5, mutation_scale=15))
            # Edge weight text
            mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
            ax.text(mid_x, mid_y + 0.08, f"w={weight}", fontsize=9, color="blue",
                    ha="center", fontweight="bold")

    # Draw nodes
    for node, (x, y) in NODE_POSITIONS.items():
        color = "limegreen" if node in visited_nodes else "lightgray"
        edgecolor = "darkgreen" if node in visited_nodes else "black"
        ax.scatter(x, y, s=800, color=color, edgecolors=edgecolor, linewidth=2, zorder=3)
        ax.text(x, y, node, fontsize=12, fontweight="bold", ha="center", va="center", zorder=4)

    ax.set_title("A* Graph Expansion Visualization", fontsize=11, fontweight="bold")
    ax.axis("off")

    os.makedirs(SAVE_DIR, exist_ok=True)
    plt.savefig(SAVE_PATH, dpi=150, bbox_inches="tight")
    plt.close()


def main() -> None:
    print("=" * 50)
    print("Starting Lab 30: Simple A* Demonstration")
    print("=" * 50)

    visited_nodes = run_astar(GRAPH, DEFAULT_HEURISTIC, "S", "G")
    plot_astar_graph(GRAPH, visited_nodes)

    print(f"\nSaved A* expansion plot to: {SAVE_PATH}")
    print("=" * 50)


if __name__ == "__main__":
    main()