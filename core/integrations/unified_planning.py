"""Unified Planning boundary for parsing, rewriting and serializing paired PDDL tasks."""

from dataclasses import dataclass
from pathlib import Path

from unified_planning.engines import CompilationKind
from unified_planning.environment import get_environment
from unified_planning.io import PDDLReader, PDDLWriter
from unified_planning.model import Problem
from unified_planning.model.metrics import MinimizeActionCosts, MinimizeExpressionOnFinalState
from unified_planning.shortcuts import Compiler

# `(:metric minimize (total-cost))` reads back as a final-state expression.
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


def to_positive_normal_form(problem):
    """Rewrite a problem so that no condition negates a fluent.

    Every negated fluent gains a companion that carries its complement, which
    the actions keep opposite, so relaxing a delete can no longer falsify a
    condition and lose plans the concrete task has.
    """
    get_environment().credits_stream = None
    try:
        # Selected by name, not by problem kind: the kind lookup refuses a task
        # over features the translation never touches, such as the undefined
        # initial numeric every action-costs domain in the suite carries.
        with Compiler(name="up_negative_conditions_remover") as compiler:
            translated = compiler.compile(problem, CompilationKind.NEGATIVE_CONDITIONS_REMOVING).problem
    except Exception as error:
        raise PddlError(f"Could not translate the task to positive normal form: {error}") from error

    # Unified Planning rebuilds a cost metric before it has mapped any new
    # action to the one it came from, so the rebuilt metric still keys on the
    # actions the translation replaced and the collapse cannot look them up.
    # The pipeline searches for the shortest plan, not the cheapest, so drop
    # the metric rather than key it back on.
    if translated.quality_metrics and isinstance(translated.quality_metrics[0], MinimizeActionCosts):
        translated.clear_quality_metrics()

    return translated


def without_action_costs(problem):
    """Copy a problem without the costs, which make the writer ask for :numeric-fluents.

    A cost is a numeric fluent taking no parameters; numeric state indexed by
    objects is left alone.
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
            # By kind, or a surviving increase comes back as an assignment.
            if effect.is_increase():
                action.add_increase_effect(effect.fluent, effect.value, effect.condition)
            elif effect.is_decrease():
                action.add_decrease_effect(effect.fluent, effect.value, effect.condition)
            else:
                action.add_effect(effect.fluent, effect.value, effect.condition)
    return stripped
