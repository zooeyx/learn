"""Inheritance — base and derived classes."""


class Shape:
    """Base class for shapes."""

    def __init__(self, color="black"):
        self.color = color

    def area(self):
        return 0

    def describe(self):
        return f"{self.color} {self.__class__.__name__} (area={self.area():.2f})"


class Circle(Shape):
    """Circle with radius."""

    def __init__(self, radius, color="black"):
        super().__init__(color)
        self.radius = radius

    def area(self):
        from math import pi
        return pi * self.radius ** 2


class Rectangle(Shape):
    """Rectangle with width and height."""

    def __init__(self, width, height, color="black"):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    """Square — special case of Rectangle."""

    def __init__(self, side, color="black"):
        super().__init__(side, side, color)


def main():
    shapes = [
        Circle(5, "red"),
        Rectangle(4, 6, "blue"),
        Square(3, "green"),
    ]

    for shape in shapes:
        print(shape.describe())

    # isinstance and issubclass
    sq = Square(4)
    print(f"\nSquare is Rectangle? {isinstance(sq, Rectangle)}")
    print(f"Square is Shape? {isinstance(sq, Shape)}")
    print(f"Square subclass of Rectangle? {issubclass(Square, Rectangle)}")

    # MRO
    print(f"\nSquare MRO: {[c.__name__ for c in Square.__mro__]}")


if __name__ == "__main__":
    main()
