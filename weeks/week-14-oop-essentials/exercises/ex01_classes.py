"""Exercise 01: class, object and methods.

Run from the repository root:
    python weeks/week-14-oop-essentials/exercises/ex01_classes.py
"""


class Progress:
    """Represent completed items out of a positive total."""

    def __init__(self, completed: int, total: int) -> None:
        if total < 1:
            raise ValueError("total must be positive")
        if not 0 <= completed <= total:
            raise ValueError("completed must be between 0 and total")

        self.completed = completed
        self.total = total

    def percentage(self) -> float:
        """Return completion as a percentage from 0 to 100."""
        return self.completed / self.total * 100

    def __str__(self) -> str:
        """Return a readable summary of this progress."""
        return (
            f"Progress: {self.completed}/{self.total} "
            f"({self.percentage():.0f}%)"
        )


def main() -> None:
    progress = Progress(3, 4)
    print(f"Percentage: {progress.percentage():.1f}%")
    print(progress)

    try:
        Progress(5, 4)
    except ValueError as error:
        print(f"Invalid input handled: {error}")


if __name__ == "__main__":
    main()
