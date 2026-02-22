# 06 — Lists

## Concepts

Lists are Python's most versatile data structure — ordered, mutable sequences that can hold any type. Lists support indexing, slicing, and a rich set of methods for adding, removing, and reordering elements.

List comprehensions (`[expr for x in iterable if cond]`) are a concise way to create lists. Understanding references vs copies is crucial: assigning a list to a new variable creates an alias, not a copy.

## Key Points

- Lists are mutable — elements can be changed in place
- `.append()`, `.extend()`, `.insert()`, `.pop()`, `.remove()`
- Slicing creates a shallow copy: `new = old[:]`
- List comprehensions replace many map/filter patterns
- `sorted()` returns new list; `.sort()` modifies in place

## Resources

**Helsinki MOOC**
- [Part 4: Lists](https://programming-24.mooc.fi/part-4/3-lists)
- [Part 5: More Lists](https://programming-24.mooc.fi/part-5/1-more-lists)

**Real Python**
- [Python Lists](https://realpython.com/python-lists-tuples/)
- [List Comprehensions](https://realpython.com/list-comprehension-python/)

**Python Docs**
- [Sequence Types](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)
- [Sorting HOW TO](https://docs.python.org/3/howto/sorting.html)

## Exercises

- [x] `list_basics.py` — Study this: creation, indexing, slicing, methods
- [ ] `list_methods.py` — Implement: append, extend, insert, pop, remove, sort
- [ ] `iteration.py` — Implement: loops, comprehensions, enumerate, zip
- [ ] `references.py` — Implement: aliasing, copying, deep copy
- [ ] `list_exercises.py` — Implement: practical list problems
