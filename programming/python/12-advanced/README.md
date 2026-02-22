# 12 — Advanced

## Concepts

Python's advanced features enable concise, expressive code. List/dict/set comprehensions create collections in a single expression. Generators produce values lazily, saving memory for large datasets. Lambda functions are anonymous one-liners, and decorators wrap functions to add behavior.

Regular expressions (regex) provide powerful text pattern matching via the `re` module. These tools together form the backbone of idiomatic, professional Python.

## Key Points

- Comprehensions: `[expr for x in iter if cond]` — also works with `{}` and `{k:v}`
- Generators: `(expr for x in iter)` or `yield` in a function — lazy evaluation
- Lambda: `lambda x: x * 2` — anonymous functions for simple operations
- Decorators: `@decorator` syntax wraps functions — logging, timing, caching
- Regex: `re.search(pattern, string)`, `re.findall()`, `re.sub()`

## Resources

**Helsinki MOOC**
- [Part 11: Comprehensions](https://programming-24.mooc.fi/part-11/1-list-comprehensions)
- [Part 12: Generators](https://programming-24.mooc.fi/part-12/1-generators)

**Real Python**
- [List Comprehensions](https://realpython.com/list-comprehension-python/)
- [Generators](https://realpython.com/introduction-to-python-generators/)
- [Decorators](https://realpython.com/primer-on-python-decorators/)
- [Regular Expressions](https://realpython.com/regex-python/)

**Python Docs**
- [Generator Expressions](https://docs.python.org/3/reference/expressions.html#generator-expressions)
- [Decorators](https://docs.python.org/3/glossary.html#term-decorator)
- [re Module](https://docs.python.org/3/library/re.html)

## Exercises

- [x] `comprehensions.py` — Study this: list/dict/set comprehensions, nested
- [ ] `generators.py` — Implement: generator functions, yield, expressions
- [ ] `lambda_funcs.py` — Implement: lambda, sorting, map/filter with lambda
- [ ] `decorators.py` — Implement: function decorators, with arguments
- [ ] `regex.py` — Implement: pattern matching, groups, substitution
