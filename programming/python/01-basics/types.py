"""Types — Python's basic data types and type inspection."""


def main():
    # Integer
    age = 25
    print(f"age = {age}, type = {type(age).__name__}")

    # Float
    pi = 3.14159
    print(f"pi = {pi}, type = {type(pi).__name__}")

    # String
    name = "Zed"
    print(f"name = {name!r}, type = {type(name).__name__}")

    # Boolean
    learning = True
    print(f"learning = {learning}, type = {type(learning).__name__}")

    # NoneType
    nothing = None
    print(f"nothing = {nothing}, type = {type(nothing).__name__}")

    # Type conversion
    x = "42"
    print(f"\n{x!r} -> int: {int(x)}")
    print(f"{x!r} -> float: {float(x)}")
    print(f"42 -> str: {str(42)!r}")
    print(f"0 -> bool: {bool(0)}, 1 -> bool: {bool(1)}")


if __name__ == "__main__":
    main()
