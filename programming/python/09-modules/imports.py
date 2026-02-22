"""Imports — different import forms and module basics."""

import math
from os import path
from pathlib import Path
import sys


def main():
    # Import forms
    print(f"math.sqrt(16) = {math.sqrt(16)}")
    print(f"path.exists('.') = {path.exists('.')}")
    print(f"Path.cwd() = {Path.cwd()}")

    # __name__ guard
    print(f"\n__name__ = {__name__!r}")
    print(f"This runs only when executed directly")

    # sys.path — where Python looks for modules
    print(f"\nsys.path (first 3):")
    for p in sys.path[:3]:
        print(f"  {p}")

    # Module attributes
    print(f"\nmath.pi = {math.pi}")
    print(f"math.__name__ = {math.__name__!r}")
    print(f"math.__file__ = {getattr(math, '__file__', 'built-in')}")

    # dir() to explore a module
    public = [x for x in dir(math) if not x.startswith("_")]
    print(f"\nmath public attrs ({len(public)}): {public[:5]}...")


if __name__ == "__main__":
    main()
