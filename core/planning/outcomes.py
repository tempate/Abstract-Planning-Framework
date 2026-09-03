"""Typed outcomes that can terminate a planning pipeline cleanly."""


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
}
