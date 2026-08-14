"""Run quick, refinement, and performance Beluga examples."""

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
BENCHMARK = PROJECT_ROOT / "data" / "benchmarks" / "beluga"
PROBLEM_NAME = "problem_3_s45_j3_r2_oc44_f3"
BASELINE_HORIZON = 17
CONCRETE_DOMAIN = BENCHMARK / "concrete" / "standard" / "domain.pddl"
CONCRETE_PROBLEM = (
    BENCHMARK / "concrete" / "standard" / f"{PROBLEM_NAME}.pddl"
)
ABSTRACT_DOMAIN = BENCHMARK / "abstract" / "hangar" / "domain.pddl"
ABSTRACT_PROBLEM = (
    BENCHMARK / "abstract" / "hangar" / f"{PROBLEM_NAME}_abs.pddl"
)
CONCRETE_HANGARS = ["hangar1", "hangar2", "hangar3"]
REFINEMENT_DOMAIN = BENCHMARK / "abstract" / "trailer" / "domain.pddl"
REFINEMENT_PROBLEM = (
    BENCHMARK / "abstract" / "trailer" / f"{PROBLEM_NAME}_abs.pddl"
)
CONCRETE_TRAILERS = ["beluga_trailer_1", "beluga_trailer_2"]
PERFORMANCE_PROBLEM_NAME = "problem_38_s81_j5_r2_oc31_f4"
PERFORMANCE_HORIZON = 26
PERFORMANCE_CONCRETE_DOMAIN = CONCRETE_DOMAIN
PERFORMANCE_CONCRETE_PROBLEM = (
    BENCHMARK
    / "concrete"
    / "standard"
    / f"{PERFORMANCE_PROBLEM_NAME}.pddl"
)
PERFORMANCE_ABSTRACT_PROBLEM = (
    BENCHMARK
    / "abstract"
    / "hangar"
    / f"{PERFORMANCE_PROBLEM_NAME}_abs.pddl"
)
PERFORMANCE_HANGARS = ["hangar1", "hangar2", "hangar3"]


def run_concrete():
    config = ConcretePlanningConfig(
        domain_path=CONCRETE_DOMAIN,
        problem_path=CONCRETE_PROBLEM,
        horizon=BASELINE_HORIZON,
        encoding="exact",
        time_step=False,
    )
    return compute_concrete_plan(config)


def run_abstract():
    config = AbstractPlanningConfig(
        abstract_domain_path=ABSTRACT_DOMAIN,
        abstract_problem_path=ABSTRACT_PROBLEM,
        concrete_domain_path=CONCRETE_DOMAIN,
        concrete_problem_path=CONCRETE_PROBLEM,
        horizon=BASELINE_HORIZON,
        encoding="exact",
        time_step=False,
        plan_source="clingo",
        profile_name="beluga",
        abstract_symbol="hangarabs",
        concrete_objects=CONCRETE_HANGARS,
    )
    return compute_abstract_plan(config)


def run_refinement():
    """Run a trailer-abstracted plan that cannot be fully realized."""
    config = AbstractPlanningConfig(
        abstract_domain_path=REFINEMENT_DOMAIN,
        abstract_problem_path=REFINEMENT_PROBLEM,
        concrete_domain_path=CONCRETE_DOMAIN,
        concrete_problem_path=CONCRETE_PROBLEM,
        horizon=BASELINE_HORIZON,
        encoding="exact",
        time_step=False,
        plan_source="clingo",
        profile_name="beluga",
        abstract_symbol="beluga_abs_trailer",
        concrete_objects=CONCRETE_TRAILERS,
    )
    return compute_abstract_plan(config)


def run_refinement_concrete():
    """Solve the concrete problem used by :func:`run_refinement`."""
    config = ConcretePlanningConfig(
        domain_path=CONCRETE_DOMAIN,
        problem_path=CONCRETE_PROBLEM,
        horizon=BASELINE_HORIZON,
        encoding="exact",
        time_step=False,
    )
    return compute_concrete_plan(config)


def run_performance_concrete():
    """Solve standard problem 38 without abstraction."""
    config = ConcretePlanningConfig(
        domain_path=PERFORMANCE_CONCRETE_DOMAIN,
        problem_path=PERFORMANCE_CONCRETE_PROBLEM,
        horizon=PERFORMANCE_HORIZON,
        encoding="exact",
        time_step=False,
    )
    return compute_concrete_plan(config)


def run_performance_abstract():
    """Collapse five hangars, then realize the resulting abstract plan."""
    config = AbstractPlanningConfig(
        abstract_domain_path=ABSTRACT_DOMAIN,
        abstract_problem_path=PERFORMANCE_ABSTRACT_PROBLEM,
        concrete_domain_path=PERFORMANCE_CONCRETE_DOMAIN,
        concrete_problem_path=PERFORMANCE_CONCRETE_PROBLEM,
        horizon=PERFORMANCE_HORIZON,
        encoding="exact",
        time_step=False,
        plan_source="clingo",
        profile_name="beluga",
        abstract_symbol="hangarabs",
        concrete_objects=PERFORMANCE_HANGARS,
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
