"""An ASP program as the solvers take it."""

from dataclasses import dataclass


@dataclass(frozen=True)
class AspProgram:
    """Rules, and facts that reach clingo through its backend rather than its parser."""

    rules: str
    facts: str = ""
