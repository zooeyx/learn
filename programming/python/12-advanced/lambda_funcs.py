"""Lambda Functions — anonymous functions and functional patterns.

Exercises:
  1. Basic lambda syntax
  2. Use lambda with sorted() for custom keys
  3. Use lambda with map() and filter()
  4. Combine with functools for partial application
"""

from functools import partial


def main():
    # TODO: Basic lambda — square, add
    # Hint: square = lambda x: x**2
    # Hint: add = lambda a, b: a + b

    # TODO: Sort a list of tuples by second element
    # Hint: pairs = [(1, "b"), (3, "a"), (2, "c")]
    # Hint: sorted(pairs, key=lambda p: p[1])

    # TODO: Sort strings by length
    # Hint: words = ["banana", "pie", "Washington", "a"]
    # Hint: sorted(words, key=lambda w: len(w))

    # TODO: map with lambda — convert strings to ints
    # Hint: list(map(lambda s: int(s), ["1", "2", "3"]))

    # TODO: filter with lambda — keep positive numbers
    # Hint: list(filter(lambda x: x > 0, [-1, 2, -3, 4]))

    # TODO: partial application
    # Hint: double = partial(lambda a, b: a * b, 2)
    # Hint: print(double(5))  # 10

    pass  # Remove when done


if __name__ == "__main__":
    main()
