"""Console helpers for running and comparing planning examples."""

from collections.abc import Callable

from core.execution import get_logger
from scripts.utils.reporting import print_planning_result


PlanningResult = dict
Workflow = Callable[[], PlanningResult]


def run_and_print(label: str, workflow: Workflow) -> PlanningResult:
    """Run one workflow and print its detailed result."""
    print(f"\n=== {label.upper()} ===")
    result = workflow()
    print_planning_result(result, get_logger())
    return result


def run_comparison(
    label: str,
    concrete_workflow: Workflow,
    abstract_workflow: Workflow,
) -> tuple[PlanningResult, PlanningResult]:
    """Run matched workflows and print their results side by side."""
    concrete = run_and_print(f"{label}: concrete", concrete_workflow)
    abstract = run_and_print(
        f"{label}: abstraction + refinement",
        abstract_workflow,
    )
    print_comparison(label, concrete, abstract)
    return concrete, abstract


def print_comparison(
    label: str,
    concrete: PlanningResult,
    abstract: PlanningResult,
) -> None:
    """Print the end-to-end metrics that make a comparison meaningful."""
    concrete_time = concrete["timings"]["total_time"]
    abstract_time = abstract["timings"]["total_time"]
    decrements = abstract["timings"].get("decrements")

    rows = (
        (
            "Plan found",
            _yes_no(concrete["success"]),
            _yes_no(abstract["success"]),
        ),
        ("Horizon", str(concrete["horizon"]), str(abstract["horizon"])),
        ("Refinement decrements", "-", _optional_number(decrements)),
        ("Total time", f"{concrete_time:.3f}s", f"{abstract_time:.3f}s"),
    )

    print(f"\n=== {label.upper()}: SIDE-BY-SIDE ===")
    print(f"{'Metric':<24} {'Concrete':>14} {'Abstraction':>14}")
    for metric, concrete_value, abstract_value in rows:
        print(f"{metric:<24} {concrete_value:>14} {abstract_value:>14}")

    if concrete["success"] and abstract["success"] and abstract_time > 0:
        ratio = concrete_time / abstract_time
        if ratio >= 1:
            print(f"\nAbstraction was {ratio:.2f}x faster end to end.")
        elif concrete_time > 0:
            print(
                f"\nConcrete planning was {1 / ratio:.2f}x faster "
                "end to end."
            )


def all_succeeded(results: list[PlanningResult]) -> bool:
    """Return whether every workflow in a CLI invocation found a plan."""
    return all(result["success"] for result in results)


def _yes_no(value: bool) -> str:
    return "yes" if value else "no"


def _optional_number(value) -> str:
    return "-" if value is None else str(value)
