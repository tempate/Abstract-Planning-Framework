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

    def __init__(self, asp):
        self._setup_control(asp)

    def _setup_control(self, asp):
        """Create the control, load the program and ground its base."""
        self.control = clingo.Control(["-t", str(THREADS), "--warn=none"])
        self.control.configuration.solve.models = 1

        # Parsing the facts as program text takes about 18 times their size, 3 GB for
        # 146 MB of blocksworld; one term per fact through the backend takes a sixth of that.
        with self.control.backend() as backend:
            for line in asp.facts.splitlines():
                line = line.strip()
                if line and not line.startswith("%"):
                    backend.add_rule([backend.add_atom(clingo.parse_term(line.removesuffix(".")))])

        self.control.add("base", [], asp.rules)
        self.control.ground([("base", [])])

    def solve(self, assumptions=()):
        """Return the shown atoms of a model, or None when there is none."""
        with self.control.solve(yield_=True, assumptions=assumptions) as handle:
            for model in handle:
                return [str(atom) for atom in model.symbols(shown=True)]
        return None
