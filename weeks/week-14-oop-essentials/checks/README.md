# Week 14 machine check

Run from the repository root with Python 3.12 or newer:

```bash
python weeks/week-14-oop-essentials/checks/check_week.py
```

The check runs the official reference solution and verifies:

- valid progress percentages and readable `__str__` output;
- invalid progress values raise `ValueError`;
- all three strategies return the expected action for both goal directions;
- a bot can swap strategies without changing the `Bot` class;
- the inheritance example preserves the shared `name` attribute and adds
  `Dog.speak()`.

The files in `exercises/` are intentionally unfinished learner starters. This
check does not claim that those TODOs have been completed.
