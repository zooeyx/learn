"""Functions — defining and calling functions in Python."""


def greet(name, greeting="Hello"):
    """Greet someone with a custom greeting."""
    return f"{greeting}, {name}!"


def stats(*numbers):
    """Calculate basic stats for variable number of arguments."""
    if not numbers:
        return None
    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "mean": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers),
    }


def build_profile(name, **kwargs):
    """Build a user profile from keyword arguments."""
    profile = {"name": name}
    profile.update(kwargs)
    return profile


def make_multiplier(factor):
    """Return a function that multiplies by factor (closure)."""
    def multiply(x):
        return x * factor
    return multiply


def main():
    # Basic function calls
    print(greet("Zed"))
    print(greet("World", greeting="Hi"))

    # Variable arguments
    result = stats(4, 8, 15, 16, 23, 42)
    for key, val in result.items():
        print(f"  {key}: {val}")

    # Keyword arguments
    profile = build_profile("Zed", language="Python", level="beginner")
    print(f"\nProfile: {profile}")

    # Closure
    double = make_multiplier(2)
    triple = make_multiplier(3)
    print(f"\ndouble(5) = {double(5)}")
    print(f"triple(5) = {triple(5)}")

    # Functions are objects
    funcs = [double, triple]
    for f in funcs:
        print(f"  {f.__name__} is really make_multiplier.<locals>.multiply")


if __name__ == "__main__":
    main()
