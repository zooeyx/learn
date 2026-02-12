# CLAUDE.md

## Project Overview

Structured learning repository. Code locally in Zed, syncs to homelab server via `bin/sync`.

## Structure

- `programming/c/` — C programming, chapters 01-11
- `ai-ml/` — AI/ML learning (placeholder)

## C Build System

Each chapter has a 2-line Makefile that includes `../common/common.mk`.

```bash
# Build and run in any chapter
make                    # compile all .c files
make run                # build + run all binaries
make clean              # remove build/
make ASAN=1             # enable AddressSanitizer

# From programming/c/ root
make                    # build all chapters
make clean              # clean all chapters
```

Compiler: Apple clang, C17, `-Wall -Wextra -Wpedantic -g`.
Binaries go into `build/` subdirectory (gitignored).

## Conventions

- One concept per `.c` file with a `main()` — each file is self-contained
- Use `debug.h` macros for assertions and debug printing
- Chapter READMEs have exercise checklists
