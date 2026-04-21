import os
import time
import argparse

from fastdownward_service import run_fastdownward_service
from plasp_utils import generate_lp_with_plasp
from clingo_utils_api import run_clingo
from log_utils import *


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--domain", required=True)
    parser.add_argument("--problem", required=True)
    parser.add_argument("--horizon", type=int, default=None)
    parser.add_argument("--encoding", default="exact")
    parser.add_argument("--time-step", action="store_true")

    args = parser.parse_args()

    print("Starting")

    logger = get_logger()

    result = compute_concrete_plan(
        domain_path=args.domain,
        problem_path=args.problem,
        horizon=args.horizon,
        encoding=args.encoding,
        time_step=args.time_step,
    )

    print("result: ", result)

    print("\n=== RESULT ===")
    print(f"Horizon: {result['horizon']}")
    print(f"Plans found: {result['numPlans']}")

    logger.info(f"Plans found: {result['numPlans']}")

    for i, plan in enumerate(result["plans"], 1):
        print(f"\nPlan {i}:")

        # sort by timestep (last argument of occurs)
        sorted_plan = sorted(plan, key=lambda a: int(str(a).split(",")[-1].rstrip(")")))

        for atom in sorted_plan:
            print(" ", atom)

def compute_concrete_plan(
    domain_path,
    problem_path,
    horizon=None,
    encoding="exact",
    time_step=False,
):
    total_start = time.perf_counter()

    fd_start = time.perf_counter()

    # Fast Downward expects binary files
    with open(domain_path, "rb") as d, open(problem_path, "rb") as p:
        result, _ = run_fastdownward_service(
            domain_file=d,
            problem_file=p
        )

    fd_time = time.perf_counter() - fd_start

    # If horizon was not provided, use Fast Downward's horizon
    if horizon is None:
        horizon = result["horizon"]

    base_dir = os.path.dirname(result["sasFile"])
    output_lp = os.path.join(base_dir, "output_c.lp")

    logger, debug_dir = setup_debug_logger(base_dir)

    logger.info("=" * 70)
    logger.info("NEW CONCRETE PLANNING RUN STARTED")
    logger.info(f"Horizon: {horizon}")
    logger.info(f"Encoding: {encoding}")
    logger.info(f"Fast Downward time: {fd_time:.3f}s")

    print("Directory:", base_dir)

    # Generate LP with plasp
    lp_start = time.perf_counter()

    generate_lp_with_plasp(
        sas_or_pddl_path=result["sasFile"],
        lp_output_path=output_lp,
        encoding_type=encoding,
        is_pddl_instance=False,
        abstract_time_steps=time_step
    )

    log_phase(logger, "LP generation time", lp_start)

    # Solve with clingo
    solve_start = time.perf_counter()

    models = run_clingo([output_lp], horizon)

    log_phase(logger, "Clingo solving time", solve_start)

    plans = [[atom for atom in model] for model in models]

    total_time = time.perf_counter() - total_start

    logger.info(f"Plans found: {len(plans)}")
    logger.info(f"Total runtime: {total_time:.3f}s")
    logger.info("=" * 70)

    print(f"[DONE] Total time: {total_time:.3f}s")

    return {
        "horizon": horizon,
        "numPlans": len(plans),
        "plans": plans
    }


if __name__ == "__main__":
    main()

