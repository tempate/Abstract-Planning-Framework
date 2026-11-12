"""An ASP program as the solver takes it, and the rules of the sequential encoding that callers swap."""

from dataclasses import dataclass

# Must match the action rule in sequential-incremental.lp, or replacing it silently does nothing.
EXACTLY_ONE_ACTION = "1 {occurs(Action, t) : action(Action)} 1"
AT_MOST_ONE_ACTION = "{occurs(Action, t) : action(Action)} 1"


@dataclass(frozen=True)
class AspProgram:
    """Rules, and facts that reach clingo through its backend rather than its parser."""

    rules: str
    facts: str = ""


def make_steps_optional(asp):
    """Let every step stay empty, instead of taking exactly one action."""
    return asp.replace(f"{EXACTLY_ONE_ACTION}.", f"{AT_MOST_ONE_ACTION}.")
