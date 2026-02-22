"""Decorators — wrapping functions to add behavior.

Exercises:
  1. Write a simple logging decorator
  2. Write a timing decorator
  3. Write a decorator that caches results (memoize)
  4. Use functools.wraps to preserve function metadata
"""

import functools
import time


def logged(func):
    """Decorator that logs function calls."""
    # TODO: Implement
    # Hint: @functools.wraps(func)
    # Hint: def wrapper(*args, **kwargs):
    #           print(f"Calling {func.__name__}")
    #           result = func(*args, **kwargs)
    #           print(f"{func.__name__} returned {result}")
    #           return result
    #       return wrapper
    pass


def timed(func):
    """Decorator that times function execution."""
    # TODO: Implement
    # Hint: start = time.perf_counter()
    # Hint: elapsed = time.perf_counter() - start
    pass


def memoize(func):
    """Decorator that caches results based on arguments."""
    # TODO: Implement
    # Hint: cache = {}
    # Hint: key = (args, tuple(sorted(kwargs.items())))
    # Hint: if key not in cache: cache[key] = func(...)
    pass


def main():
    # TODO: Apply decorators to functions and test
    # Hint: @logged
    #       def add(a, b): return a + b

    # Hint: @timed
    #       def slow(): time.sleep(0.1); return "done"

    # Hint: @memoize
    #       def fib(n): return n if n < 2 else fib(n-1) + fib(n-2)

    pass  # Remove when done


if __name__ == "__main__":
    main()
