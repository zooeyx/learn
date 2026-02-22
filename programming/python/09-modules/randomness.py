"""Randomness — the random module for games and simulations.

Exercises:
  1. Generate random integers, floats, and choices
  2. Shuffle a list and sample from it
  3. Simulate dice rolls and coin flips
  4. Simple Monte Carlo estimation of pi
"""

import random


def main():
    random.seed(42)  # Reproducible results

    # TODO: Random int in range, random float
    # Hint: random.randint(1, 6), random.random(), random.uniform(1.0, 10.0)

    # TODO: Random choice and sample from a list
    # Hint: random.choice(["a", "b", "c"])
    # Hint: random.sample(range(100), 5)

    # TODO: Shuffle a list
    # Hint: deck = list(range(1, 53)); random.shuffle(deck)

    # TODO: Simulate 1000 dice rolls, count distribution
    # Hint: rolls = [random.randint(1, 6) for _ in range(1000)]

    # TODO: Monte Carlo pi estimation
    # Hint: Generate random (x,y) in [0,1], count points inside unit circle
    # Hint: pi ≈ 4 * inside_count / total_count

    pass  # Remove when done


if __name__ == "__main__":
    main()
