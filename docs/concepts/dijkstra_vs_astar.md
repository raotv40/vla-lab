# Dijkstra's Algorithm vs. A* Search

Both **Dijkstra's Algorithm** and **A\* Search** are graph traversal algorithms used to find shortest paths, but they differ in how they prioritize node expansion.

---

## Comparative Analysis

| Feature | Dijkstra's Algorithm | A* Search |
| :--- | :--- | :--- |
| **Search Type** | Uninformed (blind search) | Informed (heuristic-guided) |
| **Evaluation Function**| $f(n) = g(n)$ | $f(n) = g(n) + h(n)$ |
| **Goal Direction** | Ignored (expands uniformly in all directions) | Directed towards the goal using $h(n)$ |
| **Explored States** | Expands large numbers of unnecessary nodes | Expands significantly fewer nodes |
| **Special Case** | Equivalent to A* when $h(n) = 0$ | Generalization of Dijkstra |

---

## Expansion Pattern

```text
 Dijkstra (Uniform Circular Wavefront):         A* (Focused Ellipsoidal Expansion):
 
               ░ ░ ░                                            ░
             ░ ░ S ░ ░                                          S ──► ░ ░ ──► G
               ░ ░ ░                                            ░
```
