# 09 — Modules

## Concepts

Modules organize Python code into reusable files. Any `.py` file is a module. Packages are directories containing an `__init__.py` file. The standard library provides hundreds of modules for common tasks.

The `import` statement has several forms: `import module`, `from module import name`, and `import module as alias`. Python searches for modules in `sys.path`, which includes the current directory and installed packages.

## Key Points

- `import math` vs `from math import sqrt` vs `import math as m`
- `if __name__ == "__main__":` — only runs when script is executed directly
- Standard library highlights: `os`, `sys`, `math`, `random`, `datetime`, `json`, `pathlib`
- `pip install package` for third-party packages
- Create packages with `__init__.py` in a directory

## Resources

**Helsinki MOOC**
- [Part 7: Modules](https://programming-24.mooc.fi/part-7/1-modules)

**Real Python**
- [Python Modules and Packages](https://realpython.com/python-modules-packages/)
- [Python import System](https://realpython.com/python-import/)

**Python Docs**
- [Modules Tutorial](https://docs.python.org/3/tutorial/modules.html)
- [Python Module Index](https://docs.python.org/3/py-modindex.html)

## Exercises

- [x] `imports.py` — Study this: import forms, __name__, sys.path
- [ ] `stdlib_tour.py` — Implement: explore math, os, sys, pathlib
- [ ] `randomness.py` — Implement: random module for games and simulations
- [ ] `dates.py` — Implement: datetime module for dates and times
- [ ] `using_my_module.py` — Implement: import from my_module package
