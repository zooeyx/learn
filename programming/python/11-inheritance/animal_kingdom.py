"""Animal Kingdom — class hierarchy exercise.

Exercises:
  1. Create Animal base class with name, speak(), and move()
  2. Create Mammal and Bird intermediate classes
  3. Create specific animals: Dog, Cat, Eagle, Penguin
  4. Demonstrate polymorphism with a mixed list
"""


class Animal:
    """Base class for all animals."""
    # TODO: __init__ with name
    # TODO: speak() — abstract (raise NotImplementedError)
    # TODO: move() — abstract
    # TODO: __str__ returning name and type
    pass


class Mammal(Animal):
    """Mammals — warm-blooded, fur/hair."""
    # TODO: Add body_temp attribute
    # TODO: Override move() to return "walks"
    pass


class Bird(Animal):
    """Birds — warm-blooded, feathers."""
    # TODO: Add can_fly attribute
    # TODO: Override move() based on can_fly
    pass


# TODO: class Dog(Mammal) — speak returns "Woof!"
# TODO: class Cat(Mammal) — speak returns "Meow!"
# TODO: class Eagle(Bird) — can_fly=True, speak returns "Screech!"
# TODO: class Penguin(Bird) — can_fly=False, speak returns "Honk!"


def main():
    # TODO: Create animals, loop through and demonstrate polymorphism
    # Hint: animals = [Dog("Rex"), Cat("Whiskers"), Eagle("Goldie"), Penguin("Tux")]
    # Hint: for a in animals: print(f"{a}: {a.speak()}, {a.move()}")
    pass  # Remove when done


if __name__ == "__main__":
    main()
