"""Tuples — creation, unpacking, and named tuples.

Exercises:
  1. Create tuples, demonstrate immutability
  2. Tuple unpacking with * operator
  3. Use tuples as dict keys
  4. Use namedtuple for structured data
"""

from collections import namedtuple


def main():
    # TODO: Create a tuple and try to modify it (catch TypeError)
    # Hint: t = (1, 2, 3)
    # Hint: try: t[0] = 10 except TypeError as e: print(e)

    # TODO: Tuple unpacking
    # Hint: first, *middle, last = (1, 2, 3, 4, 5)

    # TODO: Use tuples as dictionary keys (coordinates)
    # Hint: grid = {(0,0): "origin", (1,0): "right"}

    # TODO: Create a namedtuple Point and use it
    # Hint: Point = namedtuple("Point", ["x", "y"])
    # Hint: p = Point(3, 4); print(f"x={p.x}, y={p.y}")

    # TODO: Swap variables using tuple unpacking
    # Hint: a, b = b, a

    pass  # Remove when done


if __name__ == "__main__":
    main()
