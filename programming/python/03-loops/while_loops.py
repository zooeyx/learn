"""While Loops — repetition with conditions."""


def main():
    # Basic while
    count = 0
    while count < 5:
        print(f"Count: {count}")
        count += 1

    # Break and continue
    print("\nSearching for 7:")
    n = 0
    while True:
        n += 1
        if n % 2 == 0:
            continue
        if n > 10:
            print("Not found in range")
            break
        if n == 7:
            print(f"Found: {n}")
            break

    # Input validation pattern
    # (Simulated — not actually reading input)
    attempts = ["", "abc", "42"]
    for attempt in attempts:
        if attempt.isdigit():
            print(f"Valid input: {attempt}")
            break
        print(f"Invalid: {attempt!r}")

    # While with else (runs if no break)
    n = 2
    while n < 10:
        if n == 15:  # won't trigger
            break
        n += 1
    else:
        print(f"\nLoop completed without break, n={n}")


if __name__ == "__main__":
    main()
