"""Iteration — loops, comprehensions, enumerate, and zip.

Exercises:
  1. Iterate with for loop and index
  2. Use enumerate for index + value
  3. Use zip to combine lists
  4. Write list comprehensions with conditions
"""


def main():
    fruits = ["apple", "banana", "cherry", "date"]
    prices = [1.20, 0.50, 2.00, 3.50]

    # TODO: Print each fruit with its index using enumerate
    # Hint: for i, fruit in enumerate(fruits): print(f"{i}: {fruit}")

    # TODO: Use zip to print fruit-price pairs
    # Hint: for fruit, price in zip(fruits, prices):

    # TODO: List comprehension — uppercase fruits
    # Hint: upper = [f.upper() for f in fruits]

    # TODO: Filtered comprehension — fruits with price > 1.00
    # Hint: expensive = [f for f, p in zip(fruits, prices) if p > 1.00]

    # TODO: Nested comprehension — flatten [[1,2],[3,4],[5,6]]
    # Hint: [x for row in matrix for x in row]

    pass  # Remove when done


if __name__ == "__main__":
    main()
