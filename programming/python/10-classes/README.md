# 10 — Classes

## Concepts

Classes bundle data (attributes) and behavior (methods) into reusable objects. Python's OOP is flexible: no access modifiers, duck typing, and multiple inheritance. The `__init__` method initializes new instances.

Special (dunder) methods like `__str__`, `__repr__`, `__eq__`, and `__len__` let your objects work with built-in Python operations. Composition ("has-a") is often preferred over inheritance ("is-a").

## Key Points

- `self` is the first parameter of all instance methods
- `__init__` initializes attributes, `__str__` for printing
- `_name` convention for "private" (not enforced), `__name` for name mangling
- `@property` for computed attributes with getter/setter
- Composition: store objects as attributes of other objects

## Resources

**Helsinki MOOC**
- [Part 8: Objects and Methods](https://programming-24.mooc.fi/part-8/1-objects-and-methods)
- [Part 9: Objects and Classes](https://programming-24.mooc.fi/part-9/1-objects-and-references)

**Real Python**
- [OOP in Python](https://realpython.com/python3-object-oriented-programming/)
- [Python @property](https://realpython.com/python-property/)

**Python Docs**
- [Classes](https://docs.python.org/3/tutorial/classes.html)
- [Data Model](https://docs.python.org/3/reference/datamodel.html)

## Exercises

- [x] `first_class.py` — Study this: class, __init__, methods, __str__
- [ ] `special_methods.py` — Implement: __repr__, __eq__, __lt__, __len__, __add__
- [ ] `encapsulation.py` — Implement: private attrs, @property, validation
- [ ] `composition.py` — Implement: objects containing other objects
- [ ] `bank_account.py` — Implement: BankAccount class with full functionality
