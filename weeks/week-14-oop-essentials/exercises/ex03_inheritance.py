"""Exercise 03: one clear basic inheritance example.

Run from the repository root:
    python weeks/week-14-oop-essentials/exercises/ex03_inheritance.py
"""


class Animal:
    """Base class for animals with a name."""

    def __init__(self, name: str) -> None:
        self.name = name


class Dog(Animal):
    """A dog inherits its name from Animal and adds a sound."""

    def speak(self) -> str:
        return f"{self.name}: woof"


def main() -> None:
    dog = Dog("Milo")
    print(dog.speak())

    # Dog is an Animal because it inherits Animal's shared attributes
    # and can be used wherever an Animal instance is expected.
    assert isinstance(dog, Animal)
    print("Inheritance check: PASS")


if __name__ == "__main__":
    main()
