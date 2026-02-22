"""Special Methods — dunder methods for Pythonic classes.

Exercises:
  1. Implement __repr__ and __str__
  2. Implement comparison: __eq__, __lt__ (+ @functools.total_ordering)
  3. Implement __len__ and __getitem__ for container behavior
  4. Implement __add__ for combining objects
"""

from functools import total_ordering


@total_ordering
class Vector:
    """A 2D vector with special methods."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # TODO: Implement __repr__ returning "Vector(x, y)"

    # TODO: Implement __str__ returning "(x, y)"

    # TODO: Implement __eq__ comparing x and y

    # TODO: Implement __lt__ comparing magnitude (length)
    # Hint: magnitude = (self.x**2 + self.y**2) ** 0.5

    # TODO: Implement __add__ returning new Vector(self.x + other.x, ...)

    # TODO: Implement __len__ returning integer magnitude

    # TODO: Implement __abs__ returning float magnitude

    pass  # Remove when done


def main():
    # TODO: Create vectors and test all special methods
    # Hint: v1 = Vector(3, 4); v2 = Vector(1, 2)
    # Hint: print(f"repr: {v1!r}")
    # Hint: print(f"str: {v1}")
    # Hint: print(f"v1 == v2: {v1 == v2}")
    # Hint: print(f"v1 + v2 = {v1 + v2}")
    pass  # Remove when done


if __name__ == "__main__":
    main()
