# Python Programming Roadmap

## Learning Path

### Phase 1: Foundations (Chapters 01-03)
- [ ] [Helsinki MOOC — Python Programming](https://programming-24.mooc.fi/) — Parts 1-2
- [ ] [Real Python — Python Basics](https://realpython.com/python-first-steps/)
- [ ] Work through **chapters 01-03** below

### Phase 2: Data & Functions (Chapters 04-07)
- [ ] [Helsinki MOOC](https://programming-24.mooc.fi/) — Parts 3-5
- [ ] [Python Tutorial](https://docs.python.org/3/tutorial/)
- [ ] Work through **chapters 04-07** below

### Phase 3: Real-World Python (Chapters 08-09)
- [ ] [Helsinki MOOC](https://programming-24.mooc.fi/) — Parts 6-7
- [ ] [Automate the Boring Stuff](https://automatetheboringstuff.com/) — chapters on files & modules
- [ ] Work through **chapters 08-09** below

### Phase 4: OOP (Chapters 10-11)
- [ ] [Helsinki MOOC](https://programming-24.mooc.fi/) — Parts 8-10
- [ ] [Real Python — OOP in Python](https://realpython.com/python3-object-oriented-programming/)
- [ ] Work through **chapters 10-11** below

### Phase 5: Advanced & Projects (Chapters 12-13)
- [ ] [Helsinki MOOC](https://programming-24.mooc.fi/) — Parts 11-14
- [ ] Build real things — **chapter 13**
- [ ] [Fluent Python](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/) — deep-dive reference (stretch goal)

### Reference
- [Python Docs](https://docs.python.org/3/) — official documentation
- [Real Python](https://realpython.com/) — tutorials and guides
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/)

## Chapters

- [ ] **01 — Basics**: hello world, variables, types, operators, input/output
- [ ] **02 — Conditionals**: if/else/elif, boolean logic, combining conditions
- [ ] **03 — Loops**: while, for, range, nested loops, break/continue
- [ ] **04 — Strings**: string methods, formatting, slicing, exercises
- [ ] **05 — Functions**: def, scope, default args, recursion, higher-order
- [ ] **06 — Lists**: creation, methods, iteration, references, comprehensions
- [ ] **07 — Dicts & Tuples**: dictionaries, tuples, sets, practical exercises
- [ ] **08 — File I/O**: reading, writing, CSV, JSON, error handling
- [ ] **09 — Modules**: imports, stdlib, random, datetime, packages
- [ ] **10 — Classes**: OOP basics, special methods, encapsulation, composition
- [ ] **11 — Inheritance**: subclasses, polymorphism, abstract classes, design patterns
- [ ] **12 — Advanced**: comprehensions, generators, lambdas, decorators, regex
- [ ] **13 — Projects**: todo CLI, text adventure, web scraper, API client

## Build

```bash
make              # run all chapters
make test         # run all tests
make clean        # remove __pycache__

# Per-chapter
cd 01-basics
make              # run all exercises
make test         # run chapter tests
make lint         # syntax check
```
