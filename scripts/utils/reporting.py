"""Console reporting shared by planner entry points."""


def print_planning_result(result, logger):
    """Print a result and log its high-level outcome."""
    print("\n=== RESULT ===")
    print(f"Horizon: {result['horizon']}")
    print(f"Plan found: {'yes' if result['plan'] is not None else 'no'}")
    timings = result["timings"]
    if timings.get("iterations") is not None:
        print(f"Refinement iterations: {timings['iterations']}")
    if timings.get("decrements") is not None:
        print(f"Decrements: {timings['decrements']}")
    print(f"Total time: {result['timings']['total_time']:.3f}s")

    logger.info(f"Success: {result['success']}")
    logger.info(f"Plan found: {result['plan'] is not None}")

    if result["plan"] is not None:
        print("\nPlan:")
        occurrences = [
            atom for atom in result["plan"] if atom.startswith("occurs(")
        ]
        for atom in sorted(occurrences, key=_time_step):
            print(" ", atom)


def _time_step(atom):
    return int(str(atom).split(",")[-1].rstrip(")"))
