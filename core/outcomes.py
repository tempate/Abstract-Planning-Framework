"""Typed outcomes that can terminate a planning pipeline cleanly."""

# What the decide pipeline reports instead of a plan. These reach the verdict
# column of the collected CSV, so both modes spell them from here.
SOLVABLE = "solvable"
UNSOLVABLE = "unsolvable"
UNKNOWN = "unknown"


class PlanningOutcomeError(RuntimeError):
    """Base class for expected, machine-classifiable planning outcomes."""

    status = "error"
    exit_code = 2
    label = "Error"


class UnsolvableTaskError(PlanningOutcomeError):
    """Raised when an integration proves that the planning task is unsolvable."""

    status = "no_plan"
    exit_code = 1
    label = "No plan"


class NoSymmetriesError(PlanningOutcomeError):
    """Raised when symmetry discovery finds no usable object class."""

    status = "no_symmetries"
    exit_code = 4
    label = "No symmetries"


class OutOfMemoryError(PlanningOutcomeError):
    """Raised when a planning task is killed for outgrowing the memory it has."""

    status = "out_of_memory"
    exit_code = 5
    label = "Out of memory"


class IntegrationError(PlanningOutcomeError):
    """Raised when an external planning integration fails."""


class SymmetryTimeoutError(IntegrationError):
    """Raised when only the PDDL Symmetries phase reaches its time limit."""

    status = "symmetry_timeout"
    exit_code = 3
    label = "Symmetry timeout"


STATUS_BY_EXIT_CODE = {
    0: "success",
    UnsolvableTaskError.exit_code: UnsolvableTaskError.status,
    IntegrationError.exit_code: IntegrationError.status,
    SymmetryTimeoutError.exit_code: SymmetryTimeoutError.status,
    NoSymmetriesError.exit_code: NoSymmetriesError.status,
    OutOfMemoryError.exit_code: OutOfMemoryError.status,
}
