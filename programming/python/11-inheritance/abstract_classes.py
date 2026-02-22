"""Abstract Classes — ABC and @abstractmethod.

Exercises:
  1. Create an abstract Vehicle class with abstract methods
  2. Implement concrete Car and Bicycle classes
  3. Show that abstract classes can't be instantiated
  4. Add a non-abstract method in the base class
"""

from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Abstract base class for vehicles."""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def max_speed(self):
        """Return maximum speed in km/h."""
        pass

    @abstractmethod
    def fuel_type(self):
        """Return the fuel type."""
        pass

    def describe(self):
        """Non-abstract method — inherited by all subclasses."""
        return f"{self.name}: {self.max_speed()}km/h, fuel={self.fuel_type()}"


# TODO: class Car(Vehicle):
#     Implement max_speed() and fuel_type()

# TODO: class Bicycle(Vehicle):
#     Implement max_speed() and fuel_type()


def main():
    # TODO: Try to instantiate Vehicle (should fail)
    # Hint: try: Vehicle("test") except TypeError as e: print(e)

    # TODO: Create Car and Bicycle, call describe()

    pass  # Remove when done


if __name__ == "__main__":
    main()
