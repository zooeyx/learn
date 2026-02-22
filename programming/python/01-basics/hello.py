"""Hello World — print basics and string formatting."""


def main():
    print("Hello, World!")

    name = "Zed"
    language = "Python"
    print(f"Name:\t\t{name}")
    print(f"Learning:\t{language}")

    # Escape characters
    print("Line 1\nLine 2")
    print("Tab\there")
    print('Quote: "hello"')

    # Multi-line string
    print(
        """
    This is a
    multi-line string
    """.strip()
    )

    # String repetition and concatenation
    print("-" * 30)
    print("Hello" + " " + "World")


if __name__ == "__main__":
    main()
