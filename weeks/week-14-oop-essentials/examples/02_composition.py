"""Compose a bot with replaceable, independently testable strategies."""

from collections.abc import Callable

State = dict[str, int]
Strategy = Callable[[State], str]


class Bot:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def choose_action(self, state: State) -> str:
        return self.strategy(state)


def move_toward(state: State, target: int) -> str:
    if state["position"] < target:
        return "right"
    if state["position"] > target:
        return "left"
    return "wait"


def defensive(state: State) -> str:
    if abs(state["position"] - state["opponent_position"]) <= 1:
        return "wait"
    return move_toward(state, state["goal"])


def balanced(state: State) -> str:
    return move_toward(state, state["goal"])


def aggressive(state: State) -> str:
    if abs(state["position"] - state["opponent_position"]) <= 2:
        return move_toward(state, state["opponent_position"])
    return move_toward(state, state["goal"])


state = {"position": 3, "opponent_position": 4, "goal": 0}
for name, strategy in (
    ("defensive", defensive),
    ("balanced", balanced),
    ("aggressive", aggressive),
):
    bot = Bot(strategy)
    print(f"{name}: {bot.choose_action(state)}")
