# Rapidly-exploring Random Tree (RRT)

A **Rapidly-exploring Random Tree (RRT)** is a sampling-based path planning algorithm designed to solve high-dimensional path planning problems quickly without requiring explicit representation of the obstacle space boundaries.

---

## 1. Algorithm Logic

RRT builds a tree structure rooted at the start configuration:
1. Sample a random configuration $\mathbf{q}_{\text{rand}}$ from the C-space.
2. Find the nearest node $\mathbf{q}_{\text{near}}$ in the existing tree to $\mathbf{q}_{\text{rand}}$.
3. Extend a new node $\mathbf{q}_{\text{new}}$ from $\mathbf{q}_{\text{near}}$ in the direction of $\mathbf{q}_{\text{rand}}$ by a small step size $\Delta q$.
4. Check if the segment connecting $\mathbf{q}_{\text{near}}$ to $\mathbf{q}_{\text{new}}$ is collision-free.
5. If free, add $\mathbf{q}_{\text{new}}$ to the tree and record $\mathbf{q}_{\text{near}}$ as its parent.
6. Repeat until a node is added within a threshold distance of the goal.

```text
                     q_rand (Sampled Point)
                       .
                       .
        q_near         .
          o───────────>o q_new
         /  (Step size)
        o
       /
      o Root (q_start)
```

---

## 2. Advantages in High Dimensions

- **Dimension Scalability**: Algorithms like BFS and A* require grid discretization, which suffers from the *curse of dimensionality* (a 6-joint arm discretized into 100 bins per joint requires a grid of $100^6 = 10^{12}$ states). RRT scales very well to high dimensions.
- **Lazy Collision Checking**: RRT does not compute obstacle shapes in C-space in advance. It only runs local collision-checking on line segments.
