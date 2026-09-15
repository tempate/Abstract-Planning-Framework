"""Unified Planning boundary for parsing, rewriting and serializing paired PDDL tasks."""

from dataclasses import dataclass
from pathlib import Path

from unified_planning.environment import get_environment
from unified_planning.io import PDDLReader, PDDLWriter
from unified_planning.model import Problem
from unified_planning.model.metrics import MinimizeActionCosts, MinimizeExpressionOnFinalState

# A domain stating its own metric, as `(:metric minimize (total-cost))`, reads
# back as an expression over the final state rather than as action costs.
COST_METRICS = (MinimizeActionCosts, MinimizeExpressionOnFinalState)


class PddlError(ValueError):
    """Raised when a paired PDDL task cannot be parsed or serialized."""


@dataclass(frozen=True)
class PddlText:
    """A domain and problem serialized as one matched PDDL pair."""

    domain: str
    problem: str


def read_problem(domain_path, problem_path):
    """Read a PDDL pair from disk into a Unified Planning problem."""
    domain = Path(domain_path).read_text(encoding="utf-8")
    problem = Path(problem_path).read_text(encoding="utf-8")
    return parse_problem(domain, problem)


def parse_problem(domain_text, problem_text):
    """Parse a PDDL pair into a Unified Planning problem."""
    try:
        environment = get_environment()
        environment.error_used_name = False
        return PDDLReader(environment).parse_problem_string(domain_text, problem_text)
    except Exception as error:
        raise PddlError(f"Could not parse PDDL task: {error}") from error


def write_problem(problem: Problem):
    """Serialize a Unified Planning problem as a matched PDDL pair."""
    try:
        writer = PDDLWriter(problem)
        return PddlText(writer.get_domain(), writer.get_problem())
    except Exception as error:
        raise PddlError(f"Could not serialize PDDL task: {error}") from error


def without_action_costs(problem):
    """Copy a problem with the action costs Fast Downward will not read taken out.

    The writer asks for ``:numeric-fluents`` as soon as a problem carries a cost,
    whether in an effect that accumulates one or in a metric that minimises one,
    and the Fast Downward translator rejects that requirement. The search is for
    the shortest plan, not the cheapest, so nothing downstream misses them.

    A cost effect is recognised by the shape ``:action-costs`` gives it, a numeric
    fluent taking no parameters. Numeric state the task actually models is indexed
    by the objects it describes, and is left alone to fail loudly rather than be
    dropped behind the caller's back.
    """
    stripped = problem.clone()
    if stripped.quality_metrics and isinstance(stripped.quality_metrics[0], COST_METRICS):
        stripped.clear_quality_metrics()

    for action in stripped.actions:
        kept = []
        for effect in action.effects:
            fluent = effect.fluent.fluent()
            if fluent.type.is_bool_type() or fluent.arity > 0:
                kept.append(effect)
        if len(kept) == len(action.effects):
            continue
        action.clear_effects()
        for effect in kept:
            # Re-added by kind, or an increase the task does model comes back
            # as an assignment to the amount it meant to add.
            if effect.is_increase():
                action.add_increase_effect(effect.fluent, effect.value, effect.condition)
            elif effect.is_decrease():
                action.add_decrease_effect(effect.fluent, effect.value, effect.condition)
            else:
                action.add_effect(effect.fluent, effect.value, effect.condition)
    return stripped
