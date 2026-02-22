"""Variables — declaration, types, and assignment.

Exercises:
  1. Create variables of each type (int, float, str, bool)
  2. Print each with a descriptive label
  3. Demonstrate type conversion between types
  4. Use type() to inspect each variable
"""


def main():
    # TODO: Create an integer variable 'age' and assign your age
    age = 39
    # TODO: Create a float variable 'height' in meters
    height = 1.90
    # TODO: Create a string variable 'name'
    name = "Andy"
    # TODO: Create a boolean variable 'is_learning'
    is_learning = True
    # TODO: Print all variables with labels using f-strings
    print(
        f"My name is {name}, I'm {height} meters tall and it is {is_learning} that I am learning."
    )
    # Hint: print(f"Name: {name}")

    # TODO: Print the type of each variable
    print(type(age))
    print(f"Age type is: {type(age).__name__}")
    print(type(name))
    print(type(height))
    print(type(is_learning))

    # TODO: Demonstrate type conversion
    string_number = "542"
    float_number = float(string_number)
    print(f"The magic number is {float_number:.2f}")


if __name__ == "__main__":
    main()
