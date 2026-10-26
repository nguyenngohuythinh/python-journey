"""Official Week 14 OOP essentials solutions.

These models are deliberately small: they demonstrate responsibility,
composition, and one clear inheritance relationship.
"""

from collections.abc import Callable

State = dict[str, int]
Action = str
Strategy = Callable[[State], Action]


class Progress:
    """Track completed items out of a positive total."""

    def __init__(self, completed: int, total: int):
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
        """Return a short, human-readable progress summary."""
        return f"Progress: {self.completed}/{self.total} ({self.percentage():.0f}%)"


class Bot:
    """Delegate action selection to a replaceable strategy."""

    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def choose_action(self, state: State) -> Action:
        """Ask the configured strategy to choose an action."""
        return self.strategy(state)


def move_toward(state: State, target: int) -> Action:
    """Return one step toward target, or wait when already there."""
    if state["position"] < target:
        return "right"
    if state["position"] > target:
        return "left"
    return "wait"


def move_toward_goal(state: State) -> Action:
    """Move toward this bot's goal, regardless of which end it uses."""
    return move_toward(state, state["goal"])


def defensive(state: State) -> Action:
    """Pause when the opponent is adjacent; otherwise move toward the goal."""
    opponent = state.get("opponent_position")
    if opponent is not None and abs(opponent - state["position"]) <= 1:
        return "wait"
    return move_toward_goal(state)


def balanced(state: State) -> Action:
    """Take the direct one-step route toward the goal."""
    return move_toward_goal(state)


def aggressive(state: State) -> Action:
    """Chase a nearby opponent; otherwise continue toward the goal.

    This is a teaching policy, not a claim that chasing is always a good
    game strategy.
    """
    opponent = state.get("opponent_position")
    if opponent is not None and abs(opponent - state["position"]) <= 2:
        return move_toward(state, opponent)
    return move_toward_goal(state)


class Animal:
    """A simple base class with one shared attribute."""

    def __init__(self, name: str):
        self.name = name


class Dog(Animal):
    """A dog is an animal and adds dog-specific behavior."""

    def speak(self) -> str:
        return f"{self.name}: woof"
