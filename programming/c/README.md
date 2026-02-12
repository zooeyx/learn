# C Programming Roadmap

## Learning Path

### Phase 1: Foundations
- [ ] [Harvard CS50x](https://cs50.harvard.edu/x/) — weeks 1-5 (C portion). Video lectures + problem sets.
- [ ] [learn-c.org](https://www.learn-c.org/) — interactive practice alongside CS50
- [ ] Work through **chapters 01-04** below

### Phase 2: Reinforce
- [ ] [Beej's Guide to C Programming](https://beej.us/guide/bgc/) — read cover to cover
- [ ] Work through **chapters 05-06** below

### Phase 3: Modern C
- [ ] [Modern C](https://gustedt.gitlabpages.inria.fr/modern-c/) by Jens Gustedt — free CC-licensed PDF ([download](https://hal.inria.fr/hal-02383654)). Covers C23, organized in levels 0-3.
- [ ] Work through **chapters 07-09** below

### Phase 4: Systems Depth
- [ ] [MIT 6.087 — Practical Programming in C](https://ocw.mit.edu/courses/6-087-practical-programming-in-c-january-iap-2010/) — lecture notes + labs, covers threading & data structures
- [ ] Work through **chapter 10** below

### Phase 5: Projects
- [ ] Build real things — **chapter 11** below
- [ ] [Crafting Interpreters](https://craftinginterpreters.com/) Part III — bytecode VM in C (stretch goal)

### Reference
- [cppreference.com/c](https://en.cppreference.com/w/c) — definitive C standard library reference
- [C17 standard draft](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2310.pdf) — the spec itself

## Chapters

- [ ] **01 — Basics**: hello world, variables, types, operators
- [ ] **02 — Control Flow**: if/else, switch, loops, fizzbuzz
- [ ] **03 — Functions**: declaration, scope, recursion, static
- [ ] **04 — Pointers**: addresses, dereferencing, pointer arithmetic, arrays
- [ ] **05 — Strings**: C strings, string.h, parsing, manipulation
- [ ] **06 — Structs**: structs, unions, enums, typedef
- [ ] **07 — Memory**: malloc/free, memory layout, valgrind/ASAN
- [ ] **08 — File I/O**: fopen/fclose, reading/writing, binary files
- [ ] **09 — Preprocessor**: macros, conditional compilation, include guards
- [ ] **10 — Data Structures**: linked list, stack, queue, hash table
- [ ] **11 — Projects**: calculator, shell (multi-file builds)

## Build

```bash
make              # build all chapters
make clean        # clean all
make ASAN=1       # with AddressSanitizer

# Per-chapter
cd 01-basics
make              # build
make run          # build + run all
make clean        # clean
```
