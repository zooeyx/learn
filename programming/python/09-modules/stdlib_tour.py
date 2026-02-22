"""Standard Library Tour — exploring commonly used modules.

Exercises:
  1. math: sqrt, ceil, floor, log, factorial, gcd
  2. os / pathlib: file existence, directory listing
  3. sys: argv, platform, version
  4. collections: Counter, defaultdict, deque
"""

import math
from pathlib import Path


def main():
    # TODO: math module — demonstrate 5+ functions
    # Hint: print(f"sqrt(144) = {math.sqrt(144)}")
    # Hint: math.ceil, math.floor, math.log, math.factorial, math.gcd

    # TODO: pathlib — list files in current directory
    # Hint: for p in Path(".").iterdir(): print(p)

    # TODO: sys — print Python version and platform
    # Hint: import sys; print(f"Python {sys.version}")

    # TODO: collections.Counter — count characters in a string
    # Hint: from collections import Counter
    # Hint: Counter("mississippi")

    pass  # Remove when done


if __name__ == "__main__":
    main()
