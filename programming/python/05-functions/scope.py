"""Scope — local/global scope, LEGB rule, and closures.

Exercises:
  1. Demonstrate local vs global variables
  2. Use the global keyword
  3. Show LEGB rule with nested functions
  4. Create a closure that maintains state
"""


def main():
    # TODO: Create a global variable and a function that tries to read it
    # Hint: x = 10; def show(): print(x)

    # TODO: Show that assignment creates a local variable
    # Hint: def modify(): x = 20; print(f"local x: {x}")

    # TODO: Demonstrate LEGB with nested functions
    # Hint: def outer():
    #           x = "outer"
    #           def inner():
    #               print(f"inner sees: {x}")
    #           inner()

    # TODO: Create a counter closure
    # Hint: def make_counter():
    #           count = 0
    #           def increment():
    #               nonlocal count
    #               count += 1
    #               return count
    #           return increment

    pass  # Remove when done


if __name__ == "__main__":
    main()
