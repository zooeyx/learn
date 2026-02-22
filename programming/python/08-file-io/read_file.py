"""Read File — reading files with open() and the with statement."""

from pathlib import Path

DATA = Path(__file__).parent / "data"


def main():
    filepath = DATA / "names.txt"

    # Read entire file
    with open(filepath) as f:
        content = f.read()
    print(f"Full content ({len(content)} chars):")
    print(content)

    # Read lines into a list
    with open(filepath) as f:
        lines = f.readlines()
    print(f"Lines ({len(lines)}):")
    for i, line in enumerate(lines[:3]):
        print(f"  {i}: {line.rstrip()!r}")

    # Iterate line by line (memory efficient)
    print("\nIterating:")
    with open(filepath) as f:
        for line in f:
            name = line.strip()
            if name:
                print(f"  Hello, {name}!")

    # Using Path for convenience
    names = filepath.read_text().strip().split("\n")
    print(f"\nAll names: {names}")


if __name__ == "__main__":
    main()
