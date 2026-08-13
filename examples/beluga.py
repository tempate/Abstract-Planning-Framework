"""Run a checked-in Beluga hangar-abstraction example through the Python API."""

import argparse
from pathlib import Path

from core.execution import get_logger
from core.planning.abstract import compute_abstract_plan
from core.planning.concrete import compute_concrete_plan
from scripts.utils.reporting import print_planning_result


PROJECT_ROOT = Path(__file__).resolve().parents[1]
BENCHMARK = PROJECT_ROOT / "data" / "benchmarks" / "beluga"
PROBLEM_NAME = "problem_3_s45_j3_r2_oc44_f3"
CONCRETE_DOMAIN = BENCHMARK / "concrete" / "standard" / "domain.pddl"
CONCRETE_PROBLEM = (
    BENCHMARK / "concrete" / "standard" / f"{PROBLEM_NAME}.pddl"
)
ABSTRACT_DOMAIN = BENCHMARK / "abstract" / "hangar" / "domain.pddl"
ABSTRACT_PROBLEM = (
    BENCHMARK / "abstract" / "hangar" / f"{PROBLEM_NAME}_abs.pddl"
)
CONCRETE_HANGARS = ["hangar1", "hangar2", "hangar3"]


def run_concrete():
    return compute_concrete_plan(
        domain_path=CONCRETE_DOMAIN,
        problem_path=CONCRETE_PROBLEM,
    )


def run_abstract():
    return compute_abstract_plan(
        abstract_domain_path=ABSTRACT_DOMAIN,
        abstract_problem_path=ABSTRACT_PROBLEM,
        concrete_domain_path=CONCRETE_DOMAIN,
        concrete_problem_path=CONCRETE_PROBLEM,
        abstract_symbol="hangarabs",
        concrete_objects=CONCRETE_HANGARS,
        plan_source="clingo",
        profile_name="beluga",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "workflow",
        choices=("concrete", "abstract", "all"),
        nargs="?",
        default="all",
    )
    args = parser.parse_args()

    workflows = {
        "concrete": (run_concrete,),
        "abstract": (run_abstract,),
        "all": (run_concrete, run_abstract),
    }
    exit_code = 0
    for workflow in workflows[args.workflow]:
        print(f"\n=== {workflow.__name__.removeprefix('run_').upper()} ===")
        result = workflow()
        print_planning_result(result, get_logger())
        if not result["success"]:
            exit_code = 1
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
