# 08 — File I/O

## Concepts

Python provides built-in functions for reading and writing files. The `with` statement ensures files are properly closed, even if errors occur. Python handles text files (strings) and binary files (bytes) with the same `open()` function.

The `csv` and `json` modules in the standard library make working with structured data straightforward. Error handling with `try`/`except` is essential for robust file operations.

## Key Points

- Always use `with open(...)` — it closes the file automatically
- Modes: `"r"` read, `"w"` write (truncates), `"a"` append, `"x"` create
- `read()` returns entire content; `readlines()` returns list of lines
- `csv.reader` / `csv.writer` for CSV; `json.load` / `json.dump` for JSON
- Handle `FileNotFoundError`, `PermissionError`, `IOError`

## Resources

**Helsinki MOOC**
- [Part 6: File Handling](https://programming-24.mooc.fi/part-6/1-reading-files)
- [Part 7: More File Handling](https://programming-24.mooc.fi/part-7/1-modules)

**Real Python**
- [Reading and Writing Files](https://realpython.com/read-write-files-python/)
- [Working with JSON](https://realpython.com/python-json/)

**Python Docs**
- [Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [csv Module](https://docs.python.org/3/library/csv.html)
- [json Module](https://docs.python.org/3/library/json.html)

## Exercises

- [x] `read_file.py` — Study this: open, read, readlines, with statement
- [ ] `write_file.py` — Implement: write, append, writelines
- [ ] `csv_files.py` — Implement: read/write CSV with csv module
- [ ] `json_files.py` — Implement: read/write JSON with json module
- [ ] `error_handling.py` — Implement: try/except for file operations
