"""String Basics — indexing, slicing, and immutability."""


def main():
    s = "Hello, World!"

    # Indexing
    print(f"First char: {s[0]!r}")
    print(f"Last char:  {s[-1]!r}")

    # Slicing
    print(f"s[0:5] = {s[0:5]!r}")
    print(f"s[7:]  = {s[7:]!r}")
    print(f"s[::2] = {s[::2]!r}")  # every 2nd char
    print(f"Reversed: {s[::-1]!r}")

    # Length and membership
    print(f"\nLength: {len(s)}")
    print(f"'World' in s: {'World' in s}")

    # Iteration
    vowel_count = sum(1 for c in s.lower() if c in "aeiou")
    print(f"Vowels: {vowel_count}")

    # Immutability — strings can't be changed in place
    # s[0] = "h"  # This would raise TypeError
    new_s = "h" + s[1:]
    print(f"\nOriginal:  {s}")
    print(f"Modified:  {new_s}")

    # Multi-line and raw strings
    raw = r"C:\new\folder\test"
    print(f"\nRaw string: {raw}")


if __name__ == "__main__":
    main()
