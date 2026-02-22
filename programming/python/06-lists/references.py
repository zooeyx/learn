"""References — aliasing, shallow copy, and deep copy.

Exercises:
  1. Show that assignment creates an alias (not a copy)
  2. Use slicing or list() for shallow copy
  3. Show shallow copy limitation with nested lists
  4. Use copy.deepcopy for true independence
"""

import copy


def main():
    # TODO: Create a list, assign to new variable, modify original
    # Show that both variables reflect the change
    # Hint: a = [1,2,3]; b = a; a.append(4); print(b)

    # TODO: Make a shallow copy and show it's independent
    # Hint: c = a[:] or c = list(a) or c = a.copy()

    # TODO: Show shallow copy fails with nested lists
    # Hint: nested = [[1,2], [3,4]]; shallow = nested[:]
    # Hint: nested[0].append(99); print(shallow)

    # TODO: Use deepcopy for true independence
    # Hint: deep = copy.deepcopy(nested)

    pass  # Remove when done


if __name__ == "__main__":
    main()
