"""Error Handling — try/except for file and general operations.

Exercises:
  1. Handle FileNotFoundError
  2. Handle ValueError for type conversion
  3. Use try/except/else/finally
  4. Raise custom exceptions
"""


def safe_read(filepath):
    """Read a file, return content or error message."""
    # TODO: Implement with try/except for FileNotFoundError
    # Hint: try: ... except FileNotFoundError: return "File not found"
    pass


def safe_int(value):
    """Convert to int, return None on failure."""
    # TODO: Implement with try/except for ValueError
    pass


def main():
    # TODO: Test safe_read with existing and non-existing files
    # Hint: print(safe_read("data/names.txt"))
    # Hint: print(safe_read("nonexistent.txt"))

    # TODO: Test safe_int with valid and invalid inputs
    # Hint: print(safe_int("42"), safe_int("abc"))

    # TODO: Demonstrate try/except/else/finally
    # Hint: try: ... except: ... else: (runs if no error) finally: (always runs)

    # TODO: Raise and catch a custom exception
    # Hint: class AppError(Exception): pass
    # Hint: raise AppError("something went wrong")

    pass  # Remove when done


if __name__ == "__main__":
    main()
