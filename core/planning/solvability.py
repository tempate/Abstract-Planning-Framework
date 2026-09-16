"""Decide solvability with Fast Downward, on a concrete task or on its abstraction."""

from core.abstraction.factory import build_abstract_problem
from core.integrations.fast_downward import has_plan
from core.metrics import PlanningMetrics
from core.outcomes import UnsolvableTaskError
from core.planning.abstract import report_abstraction, write_abstract_problem
from core.planning.config import AbstractPlanningConfig, PlanningConfig
from core.planning.execution import temp_run_dir

SOLVABLE = "solvable"
UNSOLVABLE = "unsolvable"
UNKNOWN = "unknown"


def compute_concrete_verdict(config: PlanningConfig, on_update=None):
    """Search the concrete task, which settles it either way."""
    metrics = PlanningMetrics(on_update=on_update)
    with metrics.measure("total"):
        with temp_run_dir("concrete") as (base_dir, run_id):
            with metrics.measure("concrete_fd"):
                found = has_plan(base_dir, config.domain_path, config.problem_path, "concrete")

    return _result(config, run_id, SOLVABLE if found else UNSOLVABLE, metrics)


def compute_abstract_verdict(config: AbstractPlanningConfig, on_update=None):
    """Search the abstraction, which can only settle the task one way.

    The abstraction drops deletes and relaxes inequalities, so it
    over-approximates: no abstract plan means no concrete plan, but an abstract
    plan may exist only because of the relaxation.
    """
    metrics = PlanningMetrics(on_update=on_update)
    with metrics.measure("total"):
        with temp_run_dir("abstract") as (base_dir, run_id):
            try:
                abstract_problem = build_abstract_problem(config, metrics)
                report_abstraction(abstract_problem, metrics)

                with metrics.measure("abstract_pddl_writing"):
                    domain_path, problem_path = write_abstract_problem(abstract_problem.problem, base_dir)

                with metrics.measure("abstract_fd"):
                    found = has_plan(base_dir, domain_path, problem_path, "abstract")
            except UnsolvableTaskError:
                # Symmetry discovery reads the concrete task, so proving it
                # unsolvable there is the verdict, not a failure to reach one.
                found = False

    return _result(config, run_id, UNKNOWN if found else UNSOLVABLE, metrics)


def _result(config, run_id, verdict, metrics):
    return {"configuration": config.as_dict(), "verdict": verdict, "run_id": run_id, "metrics": metrics.as_dict()}
