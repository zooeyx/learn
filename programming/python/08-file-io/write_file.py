"""Write File — writing, appending, and writelines.

Exercises:
  1. Write a list of lines to a new file
  2. Append a line to an existing file
  3. Use writelines() to write multiple lines
  4. Copy a file's content to a new file
"""

from pathlib import Path
import tempfile

DATA = Path(__file__).parent / "data"


def main():
    # Use a temp directory so we don't litter the repo
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)

        # TODO: Write a list of names to a file, one per line
        # Hint: with open(tmp / "output.txt", "w") as f:
        #           for name in ["Alice", "Bob"]: f.write(name + "\n")

        # TODO: Append a name to the file
        # Hint: with open(tmp / "output.txt", "a") as f:

        # TODO: Use writelines() with a list
        # Hint: f.writelines([line + "\n" for line in lines])

        # TODO: Copy names.txt to a new file
        # Hint: content = (DATA / "names.txt").read_text()
        # Hint: (tmp / "copy.txt").write_text(content)

        # TODO: Print the contents of each file you created
        pass  # Remove when done


if __name__ == "__main__":
    main()
