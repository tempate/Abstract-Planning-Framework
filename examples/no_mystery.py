"""Run quick, refinement, and performance NoMystery examples."""

import argparse
from pathlib import Path

from core.planning.config import (
    AbstractPlanningConfig,
    ConcretePlanningConfig,
)
from core.planning.abstract import compute_abstract_plan
from core.planning.concrete import compute_concrete_plan
from examples._runner import all_succeeded, run_and_print, run_comparison


PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = PROJECT_ROOT / "data" / "examples" / "no_mystery"
BENCHMARK = PROJECT_ROOT / "data" / "benchmarks" / "nomystery"
REFINEMENT_PROBLEM = "p01"
REFINEMENT_HORIZON = 11
PERFORMANCE_PROBLEM = "p04"
PERFORMANCE_HORIZON = 19
BASELINE_HORIZON = 14


def run_concrete():
    config = ConcretePlanningConfig(
        domain_path=EXAMPLE / "concrete" / "domain.pddl",
        problem_path=EXAMPLE / "concrete" / "problem.pddl",
        horizon=BASELINE_HORIZON,
        encoding="exact",
        time_step=False,
    )
    return compute_concrete_plan(config)


def run_abstract():
    config = AbstractPlanningConfig(
        abstract_domain_path=EXAMPLE / "abstract" / "domain.pddl",
        abstract_problem_path=EXAMPLE / "abstract" / "problem.pddl",
        concrete_domain_path=EXAMPLE / "concrete" / "domain.pddl",
        concrete_problem_path=EXAMPLE / "concrete" / "problem.pddl",
        horizon=BASELINE_HORIZON,
        encoding="exact",
        time_step=False,
        plan_source="clingo",
        profile_name="no_mystery",
        abstract_symbol=None,
        concrete_objects=None,
    )
    return compute_abstract_plan(config)


def run_refinement():
    """Run a plan whose abstract fuel route cannot be fully realized."""
    config = AbstractPlanningConfig(
        abstract_domain_path=BENCHMARK / "abstract" / "domain.pddl",
        abstract_problem_path=(
            BENCHMARK / "abstract" / f"{REFINEMENT_PROBLEM}.pddl"
        ),
        concrete_domain_path=BENCHMARK / "concrete" / "domain.pddl",
        concrete_problem_path=(
            BENCHMARK / "concrete" / f"{REFINEMENT_PROBLEM}.pddl"
        ),
        horizon=REFINEMENT_HORIZON,
        encoding="exact",
        time_step=False,
        plan_source="clingo",
        profile_name="no_mystery",
        abstract_symbol=None,
        concrete_objects=None,
    )
    return compute_abstract_plan(config)


def run_refinement_concrete():
    """Solve the concrete problem used by :func:`run_refinement`."""
    config = ConcretePlanningConfig(
        domain_path=BENCHMARK / "concrete" / "domain.pddl",
        problem_path=BENCHMARK / "concrete" / f"{REFINEMENT_PROBLEM}.pddl",
        horizon=REFINEMENT_HORIZON,
        encoding="exact",
        time_step=False,
    )
    return compute_concrete_plan(config)


def run_performance_concrete():
    """Run the deliberately expensive concrete side of the comparison."""
    config = ConcretePlanningConfig(
        domain_path=BENCHMARK / "concrete" / "domain.pddl",
        problem_path=BENCHMARK / "concrete" / f"{PERFORMANCE_PROBLEM}.pddl",
        horizon=PERFORMANCE_HORIZON,
        encoding="exact",
        time_step=False,
    )
    return compute_concrete_plan(config)


def run_performance_abstract():
    """Solve the same performance problem through the fuel abstraction."""
    config = AbstractPlanningConfig(
        abstract_domain_path=BENCHMARK / "abstract" / "domain.pddl",
        abstract_problem_path=(
            BENCHMARK / "abstract" / f"{PERFORMANCE_PROBLEM}.pddl"
        ),
        concrete_domain_path=BENCHMARK / "concrete" / "domain.pddl",
        concrete_problem_path=(
            BENCHMARK / "concrete" / f"{PERFORMANCE_PROBLEM}.pddl"
        ),
        horizon=PERFORMANCE_HORIZON,
        encoding="exact",
        time_step=False,
        plan_source="clingo",
        profile_name="no_mystery",
        abstract_symbol=None,
        concrete_objects=None,
    )
    return compute_abstract_plan(config)


def _run_quick() -> list[dict]:
    results = [
        run_and_print("concrete baseline", run_concrete),
        run_and_print("abstract baseline", run_abstract),
    ]
    results.extend(
        run_comparison(
            "refinement comparison",
            run_refinement_concrete,
            run_refinement,
        )
    )
    return results


def _run_performance() -> list[dict]:
    return list(
        run_comparison(
            "performance comparison",
            run_performance_concrete,
            run_performance_abstract,
        )
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "workflow",
        choices=(
            "concrete",
            "abstract",
            "refinement",
            "performance",
            "quick",
            "all",
        ),
        nargs="?",
        default="quick",
    )
    args = parser.parse_args()

    if args.workflow == "concrete":
        results = [run_and_print("concrete baseline", run_concrete)]
    elif args.workflow == "abstract":
        results = [run_and_print("abstract baseline", run_abstract)]
    elif args.workflow == "refinement":
        results = list(
            run_comparison(
                "refinement comparison",
                run_refinement_concrete,
                run_refinement,
            )
        )
    elif args.workflow == "performance":
        results = _run_performance()
    elif args.workflow == "quick":
        results = _run_quick()
    else:
        results = _run_quick() + _run_performance()

    return 0 if all_succeeded(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
