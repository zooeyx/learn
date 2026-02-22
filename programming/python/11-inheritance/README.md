# 11 — Inheritance

## Concepts

Inheritance lets classes derive from other classes, inheriting attributes and methods. The child class can override parent methods and add new functionality. `super()` calls the parent's implementation.

Python supports multiple inheritance and uses the Method Resolution Order (MRO) to determine which method to call. Abstract base classes (ABC) define interfaces that subclasses must implement.

## Key Points

- `class Child(Parent):` — inherit from Parent
- `super().__init__()` — call parent's initializer
- Override methods by redefining them in the child
- `isinstance(obj, Class)` and `issubclass(Child, Parent)` for checks
- `abc.ABC` and `@abstractmethod` for abstract base classes

## Resources

**Helsinki MOOC**
- [Part 10: Class Hierarchies](https://programming-24.mooc.fi/part-10/1-class-hierarchies)

**Real Python**
- [Inheritance and Composition](https://realpython.com/inheritance-composition-python/)
- [Abstract Base Classes](https://realpython.com/python-interface/)

**Python Docs**
- [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [abc Module](https://docs.python.org/3/library/abc.html)

## Exercises

- [x] `inheritance.py` — Study this: base/derived classes, super(), overriding
- [ ] `polymorphism.py` — Implement: different behaviors through same interface
- [ ] `abstract_classes.py` — Implement: ABC, @abstractmethod
- [ ] `design_patterns.py` — Implement: Template Method, Strategy patterns
- [ ] `animal_kingdom.py` — Implement: class hierarchy for animals
