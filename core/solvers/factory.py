"""Concrete solver strategy selection."""

from core.solvers.DecrementalSolver import DecrementalSolver
from core.solvers.IncrementalSolver import IncrementalSolver


SOLVER_TYPES = {
    "dec": DecrementalSolver,
    "inc": IncrementalSolver,
}


def get_solver(mode):
    """Return the concrete solver selected by its short mode name."""
    try:
        return SOLVER_TYPES[mode]()
    except KeyError as error:
        valid_modes = ", ".join(SOLVER_TYPES)
        raise ValueError(
            f"Unknown solving mode: {mode}. Choose one of: {valid_modes}"
        ) from error
