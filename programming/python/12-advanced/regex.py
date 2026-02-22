"""Regular Expressions — pattern matching with the re module.

Exercises:
  1. Use re.search and re.match
  2. Use re.findall to extract matches
  3. Use groups to capture parts of a match
  4. Use re.sub for search-and-replace
"""

import re


def main():
    # TODO: Search for a pattern in a string
    # Hint: match = re.search(r"\d+", "Order 12345 confirmed")
    # Hint: if match: print(f"Found: {match.group()}")

    # TODO: Find all email-like patterns
    # Hint: text = "Contact alice@example.com or bob@test.org"
    # Hint: emails = re.findall(r"\w+@\w+\.\w+", text)

    # TODO: Use groups to extract parts
    # Hint: pattern = r"(\d{4})-(\d{2})-(\d{2})"
    # Hint: m = re.search(pattern, "Date: 2026-02-22")
    # Hint: print(f"Year: {m.group(1)}, Month: {m.group(2)}")

    # TODO: Use re.sub to replace patterns
    # Hint: result = re.sub(r"\d", "#", "Phone: 555-1234")
    # Hint: print(result)  # "Phone: ###-####"

    # TODO: Validate a simple pattern (e.g., phone number format)
    # Hint: pattern = r"^\d{3}-\d{4}$"
    # Hint: re.match(pattern, "555-1234")

    pass  # Remove when done


if __name__ == "__main__":
    main()
