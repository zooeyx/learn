"""CSV Files — reading and writing CSV with the csv module.

Exercises:
  1. Read grades.csv and print as a table
  2. Calculate average grade per student
  3. Write results to a new CSV file
  4. Use csv.DictReader for named access
"""

import csv
import tempfile
from pathlib import Path

DATA = Path(__file__).parent / "data"


def main():
    # TODO: Read grades.csv with csv.reader and print rows
    # Hint: with open(DATA / "grades.csv") as f:
    #           reader = csv.reader(f)
    #           header = next(reader)
    #           for row in reader: print(row)

    # TODO: Use csv.DictReader for named column access
    # Hint: with open(DATA / "grades.csv") as f:
    #           for row in csv.DictReader(f):
    #               print(f"{row['name']}: math={row['math']}")

    # TODO: Calculate average per student, print results

    # TODO: Write results to a temp CSV file
    # Hint: with open(outpath, "w", newline="") as f:
    #           writer = csv.writer(f)
    #           writer.writerow(["name", "average"])

    pass  # Remove when done


if __name__ == "__main__":
    main()
