"""List Basics — creation, indexing, slicing, and methods."""


def main():
    # Creation
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, "hello", 3.14, True, None]
    empty = []
    from_range = list(range(1, 6))
    print(f"numbers: {numbers}")
    print(f"mixed:   {mixed}")
    print(f"range:   {from_range}")

    # Indexing and slicing
    print(f"\nFirst: {numbers[0]}, Last: {numbers[-1]}")
    print(f"Slice [1:4]: {numbers[1:4]}")
    print(f"Reversed: {numbers[::-1]}")

    # Common methods
    fruits = ["apple", "banana"]
    fruits.append("cherry")
    fruits.insert(1, "blueberry")
    print(f"\nFruits: {fruits}")

    fruits.remove("banana")
    last = fruits.pop()
    print(f"After remove+pop: {fruits}, popped: {last}")

    # Sorting
    nums = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"\nSorted: {sorted(nums)}")
    print(f"Reverse sorted: {sorted(nums, reverse=True)}")

    # Comprehension
    squares = [x**2 for x in range(1, 6)]
    evens = [x for x in range(1, 11) if x % 2 == 0]
    print(f"\nSquares: {squares}")
    print(f"Evens: {evens}")

    # Unpacking
    a, b, *rest = [1, 2, 3, 4, 5]
    print(f"\na={a}, b={b}, rest={rest}")


if __name__ == "__main__":
    main()
