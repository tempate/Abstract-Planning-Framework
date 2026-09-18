"""One Clingo control over a grounded ASP program."""

import clingo

THREADS = 1


class Solver:
    """A Clingo control holding the base program, solved one call at a time."""

    def __init__(self, asp):
        arguments = ["-t", str(THREADS), "--warn=none"]
        self.control = clingo.Control(arguments)
        self.control.configuration.solve.models = 1
        self.control.add("base", [], asp)
        self.control.ground([("base", [])])

    def solve(self, assumptions=()):
        """Return the shown atoms from the first model, or None when there is none."""
        with self.control.solve(yield_=True, assumptions=assumptions) as handle:
            for plan in handle:
                return [str(atom) for atom in plan.symbols(shown=True)]
        return None
