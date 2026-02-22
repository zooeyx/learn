# 05 — Functions

## Concepts

Functions encapsulate reusable logic. In Python, `def` defines a function, and functions are first-class objects — they can be assigned to variables, passed as arguments, and returned from other functions.

Python supports default parameter values, keyword arguments, and `*args`/`**kwargs` for variable arguments. Scope rules follow LEGB: Local, Enclosing, Global, Built-in.

## Key Points

- `def func(param=default):` — default parameters
- Functions return `None` implicitly if no `return` statement
- `*args` collects positional args as tuple, `**kwargs` as dict
- Mutable default arguments are shared across calls — use `None` instead
- Type hints are optional: `def greet(name: str) -> str:`

## Resources

**Helsinki MOOC**
- [Part 3: Functions](https://programming-24.mooc.fi/part-3/3-defining-functions)
- [Part 4: More Functions](https://programming-24.mooc.fi/part-4/1-the-vscode-debugger)

**Real Python**
- [Defining Functions](https://realpython.com/defining-your-own-python-function/)
- [Python Scope](https://realpython.com/python-scope-legb-rule/)

**Python Docs**
- [Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [More on Functions](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)

## Exercises

- [x] `functions.py` — Study this: def, return, default args, *args/**kwargs
- [ ] `scope.py` — Implement: local/global scope, LEGB rule, closures
- [ ] `default_args.py` — Implement: default values, keyword args, mutable defaults
- [ ] `recursion.py` — Implement: factorial, fibonacci, recursive search
- [ ] `higher_order.py` — Implement: functions as arguments, map/filter/reduce
