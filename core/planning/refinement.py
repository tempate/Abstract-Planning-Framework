"""Realize an abstract plan as a concrete plan."""

from dataclasses import dataclass, field

from core.abstraction.factory import Abstraction
from core.integrations.clingo import parse_plan_actions, run_clingo
from core.metrics import PlanningMetrics
from core.planning.config import AbstractPlanningConfig
from core.planning.mapping import build_mapping
from core.planning.plan import PlanAction
from core.solvers.decremental import solve_decrementally


@dataclass
class RefinementContext:
    """Configuration and run state for abstract-plan refinement."""

    config: AbstractPlanningConfig
    abstraction: Abstraction
    relaxed_deletes: tuple
    run_id: str
    metrics: PlanningMetrics
    concrete_task: dict = field(default_factory=dict)
    abstract_task: dict = field(default_factory=dict)
    concrete_asp: str = ""
    abstract_asp: str | None = None
    horizon: int = 0


def refine(context: RefinementContext):
    """Obtain an abstract plan and use it to guide concrete search."""
    abstract_plan = _get_abstract_plan(context)
    if abstract_plan is None:
        context.metrics.set_counter("decrements", 0)
        context.metrics.set_counter("increments", 0)
        context.metrics.set_counter("final_horizon", context.horizon)
        context.metrics.set_counter("concrete_solve_calls", 0)
        return _build_result(context, success=False, plan=None)

    mapping = build_mapping(abstract_plan, context.abstraction)

    asp = "\n".join((context.concrete_asp, mapping))
    with context.metrics.measure("guided_concrete_solving"):
        success, plan, solver_operations = solve_decrementally(asp, context.horizon)

    increments = 0
    if not success:
        with context.metrics.measure("extended_concrete_solving"):
            plan, increments = _extend_concrete_search(context)
        success = True

    context.metrics.set_counter("decrements", solver_operations)
    context.metrics.set_counter("increments", increments)
    context.metrics.set_counter("final_horizon", context.horizon)
    context.metrics.set_counter("concrete_solve_calls", solver_operations + 1 + increments)

    return _build_result(context, success=success, plan=plan)


def _get_abstract_plan(context):
    if context.config.plan_source == "clingo":
        context.metrics.set_counter("abstract_solve_calls", 1)
        return _solve_abstract_plan(context)

    if context.config.plan_source == "fd":
        context.metrics.set_counter("abstract_solve_calls", 0)
        return read_fast_downward_plan(context.abstract_task["planFile"])

    raise ValueError(f"Unknown abstract plan source: {context.config.plan_source}")


def _solve_abstract_plan(context):
    with context.metrics.measure("abstract_solving"):
        abstract_atoms = run_clingo(context.abstract_asp, context.horizon)

    if abstract_atoms is None:
        return None

    return parse_plan_actions(abstract_atoms)


def _extend_concrete_search(context):
    """Search above the abstract horizon without abstract-plan constraints."""
    initial_horizon = context.horizon
    while True:
        context.horizon += 1
        plan = run_clingo(context.concrete_asp, context.horizon)
        if plan is not None:
            increments = context.horizon - initial_horizon
            return plan, increments


def read_fast_downward_plan(plan_file_path):
    """Read a Fast Downward plan into chronological plan actions."""
    abstract_plan = []
    with open(plan_file_path, "r") as plan_file:
        time_step = 1
        for line in plan_file:
            line = line.strip()
            if not line or line.startswith(";"):
                continue
            action_name, *arguments = line.strip("()").split()
            abstract_plan.append(PlanAction(action_name, tuple(arguments), time_step))
            time_step += 1

    return tuple(abstract_plan)


def _build_result(context, *, success, plan):
    return {
        "abstraction": {
            "abstract_symbol": context.abstraction.name,
            "objects_to_abstract": list(context.abstraction.objects),
            "object_type": context.abstraction.object_type,
            "relaxed_unary_deletes": len(context.relaxed_deletes),
        },
        "configuration": context.config.as_dict(),
        "horizon": context.horizon,
        "plan": plan if success else None,
        "success": success,
        "run_id": context.run_id,
    }
