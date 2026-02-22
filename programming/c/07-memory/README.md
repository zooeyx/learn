# 07 — Memory

## Resources

**CS50x**
- [Week 4: Memory](https://cs50.harvard.edu/x/2025/weeks/4/) — stack, heap, malloc, valgrind

**learn-c.org**
- [Dynamic Allocation](https://www.learn-c.org/en/Dynamic_allocation)

**Beej's Guide to C**
- [Manual Memory Allocation](https://beej.us/guide/bgc/html/split/manual-memory-allocation.html)

**MIT 6.087**
- [Lecture 11: Dynamic Memory](https://ocw.mit.edu/courses/6-087-practical-programming-in-c-january-iap-2010/resources/mit6_087iap10_lec11/) — malloc, valgrind, garbage collection

**Modern C**
- [Levels 1-2: Memory Model](https://gustedt.gitlabpages.inria.fr/modern-c/) ([PDF](https://hal.inria.fr/hal-02383654))

**Reference**
- [cppreference — memory](https://en.cppreference.com/w/c/memory) — malloc, calloc, realloc, free

## Exercises

- [ ] `malloc_free.c` — Dynamic allocation, free, NULL checks
- [ ] `memory_layout.c` — Stack vs heap, static vs automatic
- [ ] `leaks.c` — Intentional leaks, find with `make ASAN=1`
