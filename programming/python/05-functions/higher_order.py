"""Higher-Order Functions — functions as arguments, map/filter/reduce.

Exercises:
  1. Pass a function as an argument
  2. Use map() to transform a list
  3. Use filter() to select elements
  4. Use functools.reduce() to aggregate
"""

from functools import reduce


def main():
    # TODO: Write apply_twice(func, value) that applies func twice
    # Hint: def apply_twice(f, x): return f(f(x))
    # Hint: apply_twice(lambda x: x * 2, 3)  -> 12

    # TODO: Use map() to square a list of numbers
    # Hint: list(map(lambda x: x**2, [1,2,3,4,5]))

    # TODO: Use filter() to keep only even numbers
    # Hint: list(filter(lambda x: x % 2 == 0, range(1, 11)))

    # TODO: Use reduce() to compute product of a list
    # Hint: reduce(lambda a, b: a * b, [1, 2, 3, 4, 5])

    pass  # Remove when done


if __name__ == "__main__":
    main()
