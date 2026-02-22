"""Generators — lazy evaluation with yield.

Exercises:
  1. Write a generator function that yields squares
  2. Write a fibonacci generator
  3. Use generator expressions
  4. Chain generators for a data pipeline
"""


def squares_up_to(n):
    """Yield squares from 1 to n."""
    # TODO: Use yield to produce squares one at a time
    # Hint: for i in range(1, n+1): yield i**2
    pass


def fibonacci():
    """Infinite fibonacci generator."""
    # TODO: Yield fibonacci numbers forever
    # Hint: a, b = 0, 1; while True: yield a; a, b = b, a + b
    pass


def main():
    # TODO: Use squares_up_to generator
    # Hint: for sq in squares_up_to(10): print(sq)

    # TODO: Take first 10 fibonacci numbers
    # Hint: fib = fibonacci()
    # Hint: fibs = [next(fib) for _ in range(10)]

    # TODO: Generator expression — sum of squares
    # Hint: total = sum(x**2 for x in range(1, 101))

    # TODO: Pipeline — chain generators
    # Hint: nums = range(1, 101)
    # Hint: evens = (x for x in nums if x % 2 == 0)
    # Hint: squared = (x**2 for x in evens)
    # Hint: result = sum(squared)

    pass  # Remove when done


if __name__ == "__main__":
    main()
