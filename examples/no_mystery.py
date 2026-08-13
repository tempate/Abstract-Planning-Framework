"""Run the checked-in NoMystery example through the Python API."""

import argparse
from pathlib import Path

from core.execution import get_logger
from core.planning.abstract import compute_abstract_plan
from core.planning.concrete import compute_concrete_plan
from scripts.utils.reporting import print_planning_result


PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = PROJECT_ROOT / "data" / "examples" / "no_mystery"


def run_concrete():
    return compute_concrete_plan(
        domain_path=EXAMPLE / "concrete" / "domain.pddl",
        problem_path=EXAMPLE / "concrete" / "problem.pddl",
    )


def run_abstract():
    return compute_abstract_plan(
        abstract_domain_path=EXAMPLE / "abstract" / "domain.pddl",
        abstract_problem_path=EXAMPLE / "abstract" / "problem.pddl",
        concrete_domain_path=EXAMPLE / "concrete" / "domain.pddl",
        concrete_problem_path=EXAMPLE / "concrete" / "problem.pddl",
        plan_source="clingo",
        profile_name="no_mystery",
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
