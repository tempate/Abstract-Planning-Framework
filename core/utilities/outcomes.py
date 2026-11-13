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


class NoResourcesError(PlanningOutcomeError):
    """Raised when resource detection finds no variable with objects to collapse."""

    status = "no_resources"
    exit_code = 6
    label = "No resources"


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


class ResourceTimeoutError(IntegrationError):
    """Raised when only the resource detection phase reaches its time limit."""

    status = "resource_timeout"
    exit_code = 7
    label = "Resource timeout"


STATUS_BY_EXIT_CODE = {
    0: "success",
    UnsolvableTaskError.exit_code: UnsolvableTaskError.status,
    IntegrationError.exit_code: IntegrationError.status,
    SymmetryTimeoutError.exit_code: SymmetryTimeoutError.status,
    ResourceTimeoutError.exit_code: ResourceTimeoutError.status,
    NoSymmetriesError.exit_code: NoSymmetriesError.status,
    NoResourcesError.exit_code: NoResourcesError.status,
    OutOfMemoryError.exit_code: OutOfMemoryError.status,
}


def tool_failure(tool, completed, out_of_memory_codes):
    """The error a failed tool run raises, carrying what the tool printed."""
    message = f"{tool} failed with exit code {completed.returncode}"
    for output in (completed.stdout, completed.stderr):
        if output.strip():
            message += "\n" + output.strip()

    # A Python tool can die on a MemoryError of its own, which leaves an ordinary exit code.
    if completed.returncode in out_of_memory_codes or "MemoryError" in message:
        return OutOfMemoryError(message)

    return IntegrationError(message)
