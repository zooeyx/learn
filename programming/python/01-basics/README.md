# 01 — Basics

## Concepts

Python is a high-level, interpreted language. Every Python program is a sequence of statements executed top-to-bottom. The `print()` function outputs text, and variables store values without explicit type declarations — Python infers types dynamically.

Python uses indentation (4 spaces) to define code blocks, not braces. This enforces readable code structure from the start. Every value has a type: `int`, `float`, `str`, `bool` — use `type()` to inspect.

## Key Points

- Python is dynamically typed — variables don't need type annotations
- Use `f-strings` for string formatting: `f"Hello, {name}"`
- `input()` always returns a string — cast with `int()`, `float()` as needed
- Integer division: `//`, modulo: `%`, exponent: `**`
- Python has no semicolons or braces — indentation is syntax

## Resources

**Helsinki MOOC**
- [Part 1: Getting Started](https://programming-24.mooc.fi/part-1)

**Real Python**
- [Your First Python Program](https://realpython.com/python-first-steps/)
- [Variables in Python](https://realpython.com/python-variables/)
- [Basic Data Types](https://realpython.com/python-data-types/)

**Python Docs**
- [Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [Built-in Functions](https://docs.python.org/3/library/functions.html)

## Exercises

- [x] `hello.py` — Study this: print, f-strings, escape characters
- [x] `types.py` — Study this: Python's basic data types and type()
- [ ] `variables.py` — Implement: variable declaration, types, assignment
- [ ] `operators.py` — Implement: arithmetic, comparison, logical operators
- [ ] `input_output.py` — Implement: input(), type conversion, formatted output
