"""Behavior checks for Week 14 composition and inheritance."""

import sys
from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parents[1]
if str(WEEK_ROOT) not in sys.path:
    sys.path.insert(0, str(WEEK_ROOT))

from solutions.oop_models import (  # noqa: E402
    Animal,
    Bot,
    Dog,
    Progress,
    aggressive,
    balanced,
    defensive,
)


def check_progress() -> None:
    progress = Progress(3, 4)
    assert progress.percentage() == 75
    assert str(progress) == "Progress: 3/4 (75%)"
    assert Progress(0, 4).percentage() == 0
    assert Progress(4, 4).percentage() == 100

    for completed, total in ((0, 0), (-1, 4), (5, 4)):
        try:
            Progress(completed, total)
        except ValueError:
            pass
        else:
            raise AssertionError("Progress should reject invalid values")


def check_composition_and_strategies() -> None:
    right_goal = {"position": 1, "opponent_position": 4, "goal": 4}
    left_goal = {"position": 3, "opponent_position": 4, "goal": 0}
    at_goal = {"position": 4, "opponent_position": 0, "goal": 4}

    assert Bot(defensive).choose_action(right_goal) == "right"
    assert Bot(balanced).choose_action(right_goal) == "right"
    assert Bot(aggressive).choose_action(right_goal) == "right"

    assert Bot(defensive).choose_action(left_goal) == "wait"
    assert Bot(balanced).choose_action(left_goal) == "left"
    assert Bot(aggressive).choose_action(left_goal) == "right"

    assert Bot(balanced).choose_action(at_goal) == "wait"

    # Replacing the strategy changes behavior without changing Bot itself.
    bot = Bot(balanced)
    assert bot.choose_action(left_goal) == "left"
    bot.strategy = defensive
    assert bot.choose_action(left_goal) == "wait"


def check_basic_inheritance() -> None:
    dog = Dog("Milo")
    assert isinstance(dog, Animal)
    assert dog.name == "Milo"
    assert dog.speak() == "Milo: woof"


if __name__ == "__main__":
    check_progress()
    check_composition_and_strategies()
    check_basic_inheritance()
    print("Week 14 solution checks: PASS")
