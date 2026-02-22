"""Default Arguments — default values, keyword args, and mutable defaults.

Exercises:
  1. Write a function with default parameters
  2. Demonstrate keyword argument ordering
  3. Show the mutable default argument trap
  4. Fix the trap with None default
"""


def main():
    # TODO: Write a power(base, exp=2) function
    # Hint: def power(base, exp=2): return base ** exp

    # TODO: Call with positional, keyword, and mixed arguments
    # Hint: power(3), power(3, 3), power(base=2, exp=10)

    # TODO: Show the mutable default trap
    # Hint: def bad_append(item, lst=[]):
    #           lst.append(item); return lst
    # Call it twice and show the list grows unexpectedly

    # TODO: Fix it with None
    # Hint: def good_append(item, lst=None):
    #           if lst is None: lst = []
    #           lst.append(item); return lst

    pass  # Remove when done


if __name__ == "__main__":
    main()
