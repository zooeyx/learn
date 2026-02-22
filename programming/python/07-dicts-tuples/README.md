# 07 — Dicts & Tuples

## Concepts

Dictionaries map keys to values — they're Python's hash table. Keys must be hashable (immutable): strings, numbers, tuples. Dicts are ordered by insertion (Python 3.7+) and provide O(1) average lookup.

Tuples are immutable sequences, often used for fixed collections like coordinates or database rows. Sets are unordered collections of unique elements, useful for membership testing and removing duplicates.

## Key Points

- Dict access: `d[key]` (raises KeyError) vs `d.get(key, default)`
- Dict comprehension: `{k: v for k, v in pairs}`
- Tuples are immutable — use for data that shouldn't change
- Tuple unpacking: `x, y = (1, 2)`
- Sets: `{1, 2, 3}`, set operations: `|`, `&`, `-`, `^`

## Resources

**Helsinki MOOC**
- [Part 5: Dictionary](https://programming-24.mooc.fi/part-5/4-dictionary)

**Real Python**
- [Dictionaries](https://realpython.com/python-dicts/)
- [Tuples](https://realpython.com/python-lists-tuples/#python-tuples)
- [Sets](https://realpython.com/python-sets/)

**Python Docs**
- [Mapping Types — dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
- [Set Types](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)

## Exercises

- [x] `dictionaries.py` — Study this: creation, access, methods, comprehensions
- [ ] `tuples.py` — Implement: creation, unpacking, named tuples
- [ ] `sets.py` — Implement: creation, operations, use cases
- [ ] `phone_book.py` — Implement: phone book with dict operations
- [ ] `student_db.py` — Implement: student database with nested dicts
