"""Unified Planning boundary for parsing, rewriting and serializing paired PDDL tasks."""

import copy
from dataclasses import dataclass
from pathlib import Path
from unittest.mock import patch

from unified_planning.engines import CompilationKind, ValidationResultStatus
from unified_planning.engines.compilers import negative_conditions_remover
from unified_planning.engines.compilers.negative_conditions_remover import NegativeFluentRemover
from unified_planning.environment import get_environment
from unified_planning.exceptions import UPException
from unified_planning.io import PDDLReader, PDDLWriter
from unified_planning.model import Problem
from unified_planning.model.fluent import get_all_fluent_exp
from unified_planning.model.metrics import MinimizeActionCosts, MinimizeExpressionOnFinalState
from unified_planning.plans import ActionInstance, SequentialPlan
from unified_planning.shortcuts import Compiler, PlanValidator

# `(:metric minimize (total-cost))` reads back as a final-state expression.
COST_METRICS = (MinimizeActionCosts, MinimizeExpressionOnFinalState)


class PddlError(ValueError):
    """Raised when a paired PDDL task cannot be parsed or serialized."""


@dataclass(frozen=True)
class PddlText:
    """A domain and problem serialized as one matched PDDL pair."""

    domain: str
    problem: str
    # Written name to original, for the actions and objects the writer had to
    # rename, such as an action sharing its name with a predicate.
    renamings: dict[str, str]


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
        writer = PDDLWriter(_with_explicit_initial_state(problem))
        domain, problem_text = writer.get_domain(), writer.get_problem()
    except Exception as error:
        raise PddlError(f"Could not serialize PDDL task: {error}") from error

    renamings = {}
    for item in (*problem.actions, *problem.all_objects):
        try:
            written = writer.get_pddl_name(item)
        except UPException:
            # The writer drops an action whose precondition is false, so it has no written name.
            # No plan can use that action, so it needs no entry here.
            continue
        if written != item.name:
            renamings[written] = item.name
    return PddlText(domain, problem_text, renamings)


def _with_explicit_initial_state(problem):
    """A view of the problem whose initial values leave out the false facts the closed world implies.

    The writer prints `problem.initial_values`, which grounds every fluent over
    every object and stores the result in the problem: 8 million facts for a
    rovers task that sets 27 thousand. A false fact prints nothing, so the
    file is the same without them.

    A workaround for Unified Planning 1.3.0: remove it when an upgrade's
    PDDLWriter no longer iterates `initial_values` to write the init.
    """

    def initial_values(view):
        values = dict(view.explicit_initial_values)
        for fluent, default in view.fluents_defaults.items():
            if default.is_bool_constant() and default.is_false():
                continue
            for expression in get_all_fluent_exp(view, fluent):
                values.setdefault(expression, default)
        return values

    view = copy.copy(problem)
    view.__class__ = type("ExplicitInitialState", (type(problem),), {"initial_values": property(initial_values)})
    return view


class _InequalityKeeper(NegativeFluentRemover):
    # An inequality between objects is static, so no relaxed delete can falsify
    # it, and the translation would rewrite it into a disjunction over pairs of
    # objects, which Fast Downward's translator expands into a copy of the
    # action per pair. Leave it negated.
    def walk_not(self, expression, args, **kwargs):
        if args[0].is_equals() and args[0].arg(0).type.is_user_type():
            return self._env.expression_manager.Not(args[0])
        return super().walk_not(expression, args, **kwargs)


def negates_a_fluent(problem):
    """Whether a condition of the problem negates anything other than an inequality between objects."""
    conditions = list(problem.goals)
    for action in problem.actions:
        conditions += action.preconditions
        conditions += [effect.condition for effect in action.conditional_effects]

    for condition in conditions:
        if _negates_a_fluent(condition):
            return True
    return False


def _negates_a_fluent(expression):
    if expression.is_not():
        negated = expression.arg(0)
        return not (negated.is_equals() and negated.arg(0).type.is_user_type())
    for argument in expression.args:
        if _negates_a_fluent(argument):
            return True
    return False


def to_positive_normal_form(problem):
    """Rewrite a problem so that no condition negates a fluent, leaving its inequalities as they are.

    Every negated fluent gains a companion that carries its complement, which
    the actions keep opposite, so relaxing a delete can no longer falsify a
    condition and lose plans the concrete task has.
    """
    get_environment().credits_stream = None
    try:
        # Selected by name, not by problem kind: the kind lookup refuses a task
        # over features the translation never touches, such as the undefined
        # initial numeric every action-costs domain in the suite carries.
        with (
            patch.object(negative_conditions_remover, "NegativeFluentRemover", _InequalityKeeper),
            Compiler(name="up_negative_conditions_remover") as compiler,
        ):
            translated = compiler.compile(problem, CompilationKind.NEGATIVE_CONDITIONS_REMOVING).problem
    except Exception as error:
        raise PddlError(f"Could not translate the task to PNF: {error}") from error

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


def validate_plan(problem, actions):
    """Say whether a plan achieves the goal of the problem it claims to solve.

    Answers "unchecked" rather than "invalid" when the plan cannot be expressed
    against the problem at all, so that a name the plan source spells
    differently reads as a gap in this check and not as an unsound plan.
    """
    try:
        plan = SequentialPlan(
            [
                ActionInstance(problem.action(action.name), tuple(problem.object(name) for name in action.args))
                for action in actions
            ]
        )
    except Exception as error:
        return f"unchecked: {error}"

    try:
        with PlanValidator(problem_kind=problem.kind, plan_kind=plan.kind) as validator:
            status = validator.validate(problem, plan).status
    except Exception as error:
        return f"unchecked: {error}"

    return "valid" if status == ValidationResultStatus.VALID else "invalid"
