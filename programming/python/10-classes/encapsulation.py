"""Encapsulation — private attributes and @property.

Exercises:
  1. Use _private convention for internal attributes
  2. Create @property for computed/validated access
  3. Add setter with validation
  4. Show name mangling with __double_underscore
"""


class Temperature:
    """Temperature with Celsius storage and Fahrenheit conversion."""

    def __init__(self, celsius=0):
        # TODO: Store celsius using a private attribute
        # Hint: self._celsius = celsius
        pass

    # TODO: @property for celsius with validation (>= -273.15)

    # TODO: @property for fahrenheit (computed from celsius)
    # Hint: return self._celsius * 9/5 + 32

    # TODO: @fahrenheit.setter that converts back to celsius

    # TODO: __str__ showing both units

    pass  # Remove when done


def main():
    # TODO: Create Temperature, test getters/setters
    # Hint: t = Temperature(100)
    # Hint: print(f"Celsius: {t.celsius}, Fahrenheit: {t.fahrenheit}")
    # Hint: t.fahrenheit = 32; print(f"After setting F=32: {t.celsius}°C")
    # Hint: Try setting below absolute zero
    pass  # Remove when done


if __name__ == "__main__":
    main()
