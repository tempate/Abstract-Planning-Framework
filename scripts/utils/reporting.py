"""Console reporting shared by planner entry points."""

import json


def print_planning_result(result, logger):
    """Print a result and log its high-level outcome."""
    print("\n=== RESULT ===")
    print(f"Horizon: {result['horizon']}")
    print(f"Plan found: {'yes' if result['plan'] is not None else 'no'}")
    metrics = result["metrics"]
    counters = metrics["counters"]
    if "decrements" in counters:
        print(f"Decrements: {counters['decrements']}")
    if "increments" in counters:
        print(f"Increments: {counters['increments']}")
    print(f"Total time: {metrics['durations']['total']:.3f}s")
    print(f"Metrics: {json.dumps(metrics, sort_keys=True)}")

    logger.info(f"Success: {result['success']}")
    logger.info(f"Plan found: {result['plan'] is not None}")

    if result["plan"] is not None:
        print("\nPlan:")
        plan_actions = [atom for atom in result["plan"] if atom.startswith("occurs(")]
        for atom in sorted(plan_actions, key=_time_step):
            print(" ", atom)


def _time_step(atom):
    return int(str(atom).split(",")[-1].rstrip(")"))
