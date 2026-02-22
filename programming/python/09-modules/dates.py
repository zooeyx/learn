"""Dates — the datetime module for dates and times.

Exercises:
  1. Get current date and time
  2. Create specific dates, calculate differences
  3. Format dates with strftime
  4. Parse date strings with strptime
"""

from datetime import datetime, date, timedelta


def main():
    # TODO: Get and print current date and time
    # Hint: now = datetime.now(); print(f"Now: {now}")

    # TODO: Create a specific date, calculate days until
    # Hint: birthday = date(2026, 12, 25)
    # Hint: delta = birthday - date.today()

    # TODO: Date arithmetic with timedelta
    # Hint: next_week = date.today() + timedelta(weeks=1)

    # TODO: Format with strftime
    # Hint: now.strftime("%Y-%m-%d %H:%M:%S")
    # Hint: now.strftime("%B %d, %Y")  # "February 22, 2026"

    # TODO: Parse with strptime
    # Hint: parsed = datetime.strptime("2026-01-15", "%Y-%m-%d")

    pass  # Remove when done


if __name__ == "__main__":
    main()
