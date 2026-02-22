# 03 — Loops

## Concepts

Loops repeat a block of code. Python has two loop types: `while` loops repeat while a condition is true, and `for` loops iterate over sequences (lists, strings, ranges). The `range()` function generates number sequences for counting loops.

`break` exits a loop early, `continue` skips to the next iteration, and `else` on a loop runs only if the loop completed without `break`. Python's `for` loop is really a "for-each" — it iterates directly over items, not indices.

## Key Points

- `for x in range(n)` — loop n times (0 to n-1)
- `for i, val in enumerate(seq)` — loop with index
- `while True` + `break` — common pattern for input validation
- `range(start, stop, step)` — flexible number sequences
- Avoid modifying a list while iterating over it

## Resources

**Helsinki MOOC**
- [Part 2: Loops](https://programming-24.mooc.fi/part-2/2-repeating-functionality)
- [Part 3: More Loops](https://programming-24.mooc.fi/part-3/1-loops-with-conditions)

**Real Python**
- [Python for Loops](https://realpython.com/python-for-loop/)
- [Python while Loops](https://realpython.com/python-while-loop/)

**Python Docs**
- [for Statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [range()](https://docs.python.org/3/library/stdtypes.html#range)

## Exercises

- [x] `while_loops.py` — Study this: while, break, continue, input validation
- [ ] `for_loops.py` — Implement: for, range, enumerate, iteration patterns
- [ ] `nested_loops.py` — Implement: nested loops, multiplication table, patterns
- [ ] `loop_patterns.py` — Implement: accumulator, search, filter patterns
- [ ] `number_guessing.py` — Implement: number guessing game with while loop
