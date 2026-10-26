"""Exercise 02: compose Bot with a replaceable strategy.

Tasks:
1. Create Bot(strategy) and choose_action(state).
2. Write defensive, balanced and aggressive strategy functions.
3. Use state keys position, opponent_position and goal.
4. Return only the course-local actions: left, right or wait.
5. Support both goal=0 and goal=4; do not hardcode a single direction.
6. Show that swapping strategy changes behavior without rewriting Bot.

Policy guide:
- defensive waits when the opponent is one step away, otherwise heads to goal;
- balanced always takes one step toward goal;
- aggressive chases the opponent when within two steps, otherwise heads to goal.
"""

# TODO: define a Strategy type alias if it helps readability.
# TODO: implement Bot and a small move_toward(state, target) helper.
# TODO: implement the three strategy functions and demonstrate strategy swap.
