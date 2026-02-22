"""Recursion — recursive functions.

Exercises:
  1. Implement factorial(n)
  2. Implement fibonacci(n)
  3. Implement sum_nested(lst) for nested lists
  4. Implement binary_search(lst, target)
"""


def factorial(n):
    """Return n! using recursion."""
    # TODO: Base case: n <= 1 returns 1
    # TODO: Recursive case: n * factorial(n-1)
    pass


def fibonacci(n):
    """Return the nth Fibonacci number."""
    # TODO: Base cases: fib(0)=0, fib(1)=1
    # TODO: Recursive case: fib(n-1) + fib(n-2)
    pass


def sum_nested(lst):
    """Sum all numbers in a potentially nested list."""
    # TODO: For each item: if it's a list, recurse; else add it
    # Hint: isinstance(item, list)
    pass


def binary_search(lst, target, lo=0, hi=None):
    """Search sorted list for target, return index or -1."""
    # TODO: Implement recursive binary search
    # Hint: if hi is None: hi = len(lst) - 1
    # Hint: mid = (lo + hi) // 2
    pass


def main():
    # TODO: Test each function
    # Hint: print(f"5! = {factorial(5)}")
    # Hint: print(f"fib(10) = {fibonacci(10)}")
    # Hint: print(f"sum_nested([1,[2,[3,4],5]]) = {sum_nested([1,[2,[3,4],5]])}")
    # Hint: print(f"binary_search: {binary_search([1,3,5,7,9], 5)}")
    pass  # Remove when done


if __name__ == "__main__":
    main()
