"""Exercise 02: compose Bot with a replaceable strategy.

Run from the repository root:
    python weeks/week-14-oop-essentials/exercises/ex02_composition.py
"""

from collections.abc import Callable

State = dict[str, int]
Action = str
Strategy = Callable[[State], Action]
VALID_ACTIONS = {"left", "right", "wait"}


class Bot:
    """Keep strategy selection separate from strategy behavior."""

    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def choose_action(self, state: State) -> Action:
        action = self.strategy(state)
        if action not in VALID_ACTIONS:
            raise ValueError(f"strategy returned invalid action: {action!r}")
        return action


def move_toward(state: State, target: int) -> Action:
    """Move one position toward target, or wait when already there."""
    position = state["position"]
    if position < target:
        return "right"
    if position > target:
        return "left"
    return "wait"


def defensive(state: State) -> Action:
    """Wait if the opponent is adjacent; otherwise move toward the goal."""
    if abs(state["position"] - state["opponent_position"]) <= 1:
        return "wait"
    return move_toward(state, state["goal"])


def balanced(state: State) -> Action:
    """Always take one step toward the goal."""
    return move_toward(state, state["goal"])


def aggressive(state: State) -> Action:
    """Chase an opponent within two steps; otherwise move toward the goal."""
    if abs(state["position"] - state["opponent_position"]) <= 2:
        return move_toward(state, state["opponent_position"])
    return move_toward(state, state["goal"])


def main() -> None:
    states = (
        {"position": 1, "opponent_position": 4, "goal": 4},
        {"position": 3, "opponent_position": 4, "goal": 0},
        {"position": 4, "opponent_position": 0, "goal": 4},
    )

    for state in states:
        print(f"State: {state}")
        for name, strategy in (
            ("defensive", defensive),
            ("balanced", balanced),
            ("aggressive", aggressive),
        ):
            bot = Bot(strategy)
            print(f"  {name:10} -> {bot.choose_action(state)}")

    # Composition lets us change behavior without changing Bot's class.
    bot = Bot(balanced)
    left_goal_state = {"position": 3, "opponent_position": 4, "goal": 0}
    assert bot.choose_action(left_goal_state) == "left"
    bot.strategy = defensive
    assert bot.choose_action(left_goal_state) == "wait"
    print("Strategy swap checks: PASS")


if __name__ == "__main__":
    main()
