import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius**2


def main():
    radius = float(input("Enter the radius: "))
    circle = Circle(radius)
    print(f"Area: {circle.area():.2f}")
    print(f"Circumference: {circle.circumference():.2f}")


if __name__ == "__main__":
    main()
