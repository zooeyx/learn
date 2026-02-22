"""Dictionaries — creation, access, methods, and comprehensions."""


def main():
    # Creation
    person = {"name": "Zed", "age": 25, "language": "Python"}
    from_pairs = dict([("a", 1), ("b", 2), ("c", 3)])
    from_keys = dict.fromkeys(["x", "y", "z"], 0)
    print(f"person: {person}")
    print(f"from_pairs: {from_pairs}")
    print(f"from_keys: {from_keys}")

    # Access
    print(f"\nname: {person['name']}")
    print(f"get city: {person.get('city', 'unknown')}")

    # Modification
    person["city"] = "Austin"
    person.update({"level": "beginner", "age": 26})
    print(f"updated: {person}")

    # Removal
    age = person.pop("age")
    print(f"popped age: {age}, person: {person}")

    # Iteration
    print("\nKeys and values:")
    for key, value in person.items():
        print(f"  {key}: {value}")

    # Comprehension
    squares = {x: x**2 for x in range(1, 6)}
    print(f"\nsquares: {squares}")

    # Counting pattern
    text = "hello world"
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    print(f"frequency: {freq}")


if __name__ == "__main__":
    main()
