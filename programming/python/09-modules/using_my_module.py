"""Using My Module — importing from a local package.

Exercises:
  1. Import and use functions from my_module
  2. Import specific items
  3. Explore the package with dir()
  4. Add a new function to my_module and use it
"""

import sys
from pathlib import Path

# Add parent directory to path so we can import my_module
sys.path.insert(0, str(Path(__file__).parent))


def main():
    # TODO: Import my_module and use greet()
    # Hint: from my_module import greet, add, PI, APP_NAME

    # TODO: Call greet("World") and print the result

    # TODO: Call add(3, 4) and print the result

    # TODO: Print PI and APP_NAME constants

    # TODO: Use dir() to see what's in my_module
    # Hint: import my_module; print(dir(my_module))

    pass  # Remove when done


if __name__ == "__main__":
    main()
