"""
Week 1 - Lab 13: Environment Observation and Action Space Specifications
========================================================================

Objectives:
-----------
1. Query and print the action space and observation space configurations.
2. Deconstruct the shape, type, bounds, and precision (float32 vs float64) of continuous spaces.
3. Understand the Gymnasium Box Space structure (Exercise 1).

Theory:
-------
Gymnasium defines observation and action spaces using structured space classes:
- `gym.spaces.Box` represents a continuous multi-dimensional space bounded by minimum and maximum values.
- Action Space: Box(-1.0, 1.0, (2,), float32)
  - Continual space bounded between -1.0 and 1.0, with a shape of (2,) and float32 precision.
- Observation Space: Box(-inf, inf, (10,), float64)
  - Continual space with shape (10,) and float64 precision. The bounds are infinite since values can mathematically
    scale infinitely (though physical bounds are limited).
"""

import gymnasium as gym

# Constants
ENV_NAME = "Reacher-v5"


def main():
    print("=" * 60)
    print(f"Starting Lab 13: Environment Info on {ENV_NAME}")
    print("=" * 60)

    env = gym.make(ENV_NAME)

    # Print Observation Space details
    print("Observation Space Details:")
    print("-" * 60)
    print(f"  Space representation : {env.observation_space}")
    print(f"  Space Shape          : {env.observation_space.shape}")
    print(f"  Space Dtype          : {env.observation_space.dtype}")
    print(f"  Space Lower Bounds   : {env.observation_space.low}")
    print(f"  Space Upper Bounds   : {env.observation_space.high}")
    print("-" * 60)

    # Print Action Space details
    print("\nAction Space Details:")
    print("-" * 60)
    print(f"  Space representation : {env.action_space}")
    print(f"  Space Shape          : {env.action_space.shape}")
    print(f"  Space Dtype          : {env.action_space.dtype}")
    print(f"  Space Lower Bounds   : {env.action_space.low}")
    print(f"  Space Upper Bounds   : {env.action_space.high}")
    print("-" * 60)

    # Explanations
    print("\nKey Explanations:")
    print("1. Box(-inf, inf, (10,), float64): A continuous observation space containing 10 elements with 64-bit float")
    print("   precision, bounded theoretically between negative and positive infinity.")
    print("2. Box(-1.0, 1.0, (2,), float32): A continuous action space containing 2 elements representing shoulder/elbow")
    print("   torque commands, strictly limited between -1.0 and 1.0, using 32-bit float precision.")

    env.close()


if __name__ == "__main__":
    main()