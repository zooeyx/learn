# 02 — Conditionals

## Concepts

Conditional statements let your program make decisions. Python uses `if`, `elif`, and `else` to branch execution based on boolean expressions. Unlike many languages, Python uses indentation to define blocks — no braces needed.

Boolean expressions evaluate to `True` or `False`. Python's comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`) and logical operators (`and`, `or`, `not`) combine to form complex conditions. Python also has "truthy" and "falsy" values: empty strings, zero, None, and empty collections are falsy.

## Key Points

- `elif` is Python's else-if — chain as many as needed
- No switch/case in Python < 3.10; use `match`/`case` in 3.10+
- Ternary: `value = a if condition else b`
- Falsy values: `0`, `0.0`, `""`, `None`, `[]`, `{}`, `()`
- Use `in` operator to check membership: `if x in [1, 2, 3]`

## Resources

**Helsinki MOOC**
- [Part 1: Conditional Statements](https://programming-24.mooc.fi/part-1/5-conditional-statements)
- [Part 2: More Conditionals](https://programming-24.mooc.fi/part-2/1-programming-terminology)

**Real Python**
- [Conditional Statements](https://realpython.com/python-conditional-statements/)
- [Ternary Operator](https://realpython.com/python-conditional-statements/#conditional-expressions-pythons-ternary-operator)

**Python Docs**
- [if Statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
- [Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)

## Exercises

- [x] `if_else.py` — Study this: if/elif/else, ternary, match/case
- [ ] `boolean_logic.py` — Implement: truthiness, logical operators, short-circuit
- [ ] `combining.py` — Implement: nested conditions, compound expressions
- [ ] `fizzbuzz.py` — Implement: classic fizzbuzz with conditionals
- [ ] `calculator.py` — Implement: simple calculator using if/elif
