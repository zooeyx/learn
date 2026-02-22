import math
from dataclasses import dataclass


@dataclass
class Circle:
    radius: float

    def area(self):
        return math.pi * self.radius**2

    def circumference(self):
        return 2 * math.pi * self.radius


radius = float(input("Enter the radius: "))
c = Circle(radius)

print(f"Area: {c.area():.2f} - Circumference: {c.circumference():.2f}")
