"""If/Else — conditional branching in Python."""


def main():
    # Basic if/elif/else
    score = 85
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    print(f"Score {score} -> Grade {grade}")

    # Ternary operator
    age = 20
    status = "adult" if age >= 18 else "minor"
    print(f"Age {age} -> {status}")

    # Truthiness
    values = [0, 1, "", "hello", None, [], [1]]
    for v in values:
        print(f"  {str(v):>10} -> {'truthy' if v else 'falsy'}")

    # Membership testing
    vowels = "aeiou"
    letter = "e"
    if letter in vowels:
        print(f"{letter!r} is a vowel")

    # Match/case (Python 3.10+)
    command = "greet"
    match command:
        case "greet":
            print("Hello!")
        case "bye":
            print("Goodbye!")
        case _:
            print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
