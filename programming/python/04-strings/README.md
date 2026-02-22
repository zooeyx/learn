# 04 — Strings

## Concepts

Strings in Python are immutable sequences of characters. They support indexing (`s[0]`), slicing (`s[1:4]`), and a rich set of methods. Python 3 strings are Unicode by default, so they handle international text naturally.

F-strings (`f"..."`) are the preferred way to embed expressions in strings. String methods like `.upper()`, `.split()`, `.strip()`, `.replace()` always return new strings — they never modify the original.

## Key Points

- Strings are immutable — methods return new strings
- Slicing: `s[start:stop:step]`, negative indices count from end
- `in` operator for substring check: `"hello" in "hello world"`
- `.split()` and `" ".join(list)` for splitting/joining
- Raw strings `r"..."` ignore escape characters (useful for regex, paths)

## Resources

**Helsinki MOOC**
- [Part 3: Strings](https://programming-24.mooc.fi/part-3/2-working-with-strings)

**Real Python**
- [Python Strings](https://realpython.com/python-strings/)
- [f-Strings](https://realpython.com/python-f-strings/)

**Python Docs**
- [String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Format Specification](https://docs.python.org/3/library/string.html#format-specification-mini-language)

## Exercises

- [x] `string_basics.py` — Study this: indexing, slicing, immutability
- [ ] `string_methods.py` — Implement: common string methods
- [ ] `formatting.py` — Implement: f-strings, format spec, alignment
- [ ] `string_exercises.py` — Implement: practical string problems
