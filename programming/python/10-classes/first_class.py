"""First Class — introduction to classes and objects."""


class Dog:
    """A simple Dog class."""

    species = "Canis familiaris"  # Class attribute

    def __init__(self, name, age, breed="Mixed"):
        """Initialize a Dog with name, age, and breed."""
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} ({self.breed}, {self.age}yr)"

    def __repr__(self):
        return f"Dog({self.name!r}, {self.age}, {self.breed!r})"

    def speak(self):
        return f"{self.name} says Woof!"

    def human_age(self):
        return self.age * 7


def main():
    # Creating objects
    rex = Dog("Rex", 5, "German Shepherd")
    buddy = Dog("Buddy", 3)

    print(rex)
    print(buddy)
    print(f"\n{rex.speak()}")
    print(f"{rex.name}'s human age: {rex.human_age()}")

    # Class attribute shared by all instances
    print(f"\nSpecies: {Dog.species}")
    print(f"Same species: {rex.species == buddy.species}")

    # repr for debugging
    print(f"\nrepr: {rex!r}")

    # isinstance check
    print(f"\nIs rex a Dog? {isinstance(rex, Dog)}")

    # Objects are mutable
    rex.age = 6
    print(f"Updated: {rex}")


if __name__ == "__main__":
    main()
