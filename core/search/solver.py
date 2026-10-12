"""One Clingo control over a grounded ASP program."""

from dataclasses import dataclass
import clingo

THREADS = 1


@dataclass(frozen=True)
class SolveResult:
    plan: list[str]
    horizon: int
    attempts: int = 0
    dropped: int = 0  # assumptions given up before the program became satisfiable


class Solver:
    """A Clingo control holding the base program, solved one call at a time."""

    def __init__(self, asp, optimize=False):
        arguments = ["-t", str(THREADS), "--warn=none"]
        self.control = clingo.Control(arguments)
        # Reaching the optimum takes every improving model, but the first model
        # is all a program without weak constraints needs.
        self.control.configuration.solve.models = 0 if optimize else 1
        self.control.add("base", [], asp)
        self.control.ground([("base", [])])

    def solve(self, assumptions=()):
        """Return the shown atoms from the best model, or None when there is none."""
        plan = None
        with self.control.solve(yield_=True, assumptions=assumptions) as handle:
            # Without weak constraints the first model is as good as any. With them,
            # each model improves on the last, and the last one is optimal.
            for model in handle:
                plan = [str(atom) for atom in model.symbols(shown=True)]
                if not model.cost:
                    break
        return plan
