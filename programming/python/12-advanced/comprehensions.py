"""Comprehensions — list, dict, and set comprehensions."""


def main():
    # List comprehension
    squares = [x**2 for x in range(1, 11)]
    print(f"Squares: {squares}")

    # With condition
    evens = [x for x in range(1, 21) if x % 2 == 0]
    print(f"Evens: {evens}")

    # Nested comprehension — flatten
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flat = [x for row in matrix for x in row]
    print(f"Flattened: {flat}")

    # Dict comprehension
    word = "mississippi"
    freq = {c: word.count(c) for c in set(word)}
    print(f"\nFrequency: {freq}")

    # Invert a dict
    grades = {"Alice": "A", "Bob": "B", "Charlie": "A"}
    by_grade = {}
    for name, grade in grades.items():
        by_grade.setdefault(grade, []).append(name)
    print(f"By grade: {by_grade}")

    # Set comprehension
    words = ["hello", "world", "hello", "python", "world"]
    lengths = {len(w) for w in words}
    print(f"\nUnique lengths: {lengths}")

    # Nested comprehension — transpose matrix
    transposed = [[row[i] for row in matrix] for i in range(3)]
    print(f"\nOriginal:   {matrix}")
    print(f"Transposed: {transposed}")

    # Conditional expression in comprehension
    labels = ["even" if x % 2 == 0 else "odd" for x in range(1, 6)]
    print(f"\nLabels: {labels}")


if __name__ == "__main__":
    main()
