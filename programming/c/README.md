# C Programming Roadmap

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
