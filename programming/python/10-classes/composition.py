"""Composition — objects containing other objects.

Exercises:
  1. Create an Engine class and a Car class that has-an Engine
  2. Create an Address class and a Person class that has-an Address
  3. Create a Deck class composed of Card objects
  4. Show how composition enables flexible design
"""


class Engine:
    """A car engine."""
    # TODO: __init__ with horsepower and fuel_type
    # TODO: __str__ returning description
    pass


class Car:
    """A car that has-an engine."""
    # TODO: __init__ with make, model, and Engine
    # TODO: __str__ returning full description
    # TODO: start() method that delegates to engine
    pass


def main():
    # TODO: Create Engine and Car, demonstrate composition
    # Hint: engine = Engine(200, "gasoline")
    # Hint: car = Car("Toyota", "Camry", engine)
    # Hint: print(car)
    pass  # Remove when done


if __name__ == "__main__":
    main()
