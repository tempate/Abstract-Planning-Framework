import os
import time
import argparse

from core.integrations.fast_downward import run_fast_downward
from .utils.reporting import print_planning_result, save_result_summary
from core.runtime.run_artifacts import create_run_dir, get_logger, setup_debug_logger
from core.integrations.plasp import generate_lp_with_plasp
from core.integrations.clingo import run_clingo

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--domain", required=True)
    parser.add_argument("--problem", required=True)
    parser.add_argument("--horizon", type=int, default=None)
    parser.add_argument("--encoding", default="exact")
    parser.add_argument("--time-step", action="store_true")

    args = parser.parse_args()

    print("Starting")

    result = compute_concrete_plan(
        domain_path=args.domain,
        problem_path=args.problem,
        horizon=args.horizon,
        encoding=args.encoding,
        time_step=args.time_step,
    )

    print_planning_result(result, get_logger())
    save_result_summary(args.problem, "concrete", "N/A", result)

def compute_concrete_plan(
    domain_path,
    problem_path,
    horizon=None,
    encoding="exact",
    time_step=False
):
    base_dir, run_id = create_run_dir()

    logger, _ = setup_debug_logger(base_dir)

    logger.info("=" * 70)
    logger.info("NEW PLANNING RUN STARTED")
    logger.info(f"Horizon: {horizon}")
    logger.info(f"Encoding: {encoding}")
    logger.info(f"Run ID: {run_id}")
    logger.info(f"Base dir: {base_dir}")

    print("Directory:", base_dir)

    total_start = time.perf_counter()

    fd_start = time.perf_counter()

    # Fast Downward expects binary files
    with open(domain_path, "rb") as domain, \
            open(problem_path, "rb") as problem:
        planner_result = run_fast_downward(
            base_dir=base_dir,
            domain_file=domain,
            problem_file=problem
        )

    concrete_result = planner_result["concrete"]

    fd_time = time.perf_counter() - fd_start

    # If horizon was not provided, use Fast Downward's horizon
    if horizon is None:
        horizon = concrete_result["horizon"]

    logger.info(f"Fast Downward time: {fd_time:.3f}s")

    output_lp = os.path.join(base_dir, "output_c.lp")

    # Generate LP with plasp
    lp_start = time.perf_counter()

    generate_lp_with_plasp(
        sas_or_pddl_path=concrete_result["sasFile"],
        lp_output_path=output_lp,
        encoding_type=encoding,
        abstract_time_steps=time_step
    )

    lp_time = time.perf_counter() - lp_start
    logger.info(f"LP generation time: {lp_time:.3f}s")

    # Solve with clingo
    solve_start = time.perf_counter()

    models = run_clingo([output_lp], horizon)

    solve_time = time.perf_counter() - solve_start

    plans = models

    total_time = time.perf_counter() - total_start

    logger.info(f"Plans found: {len(plans)}")
    logger.info(f"Total runtime: {total_time:.3f}s")
    logger.info("=" * 70)

    print(f"[DONE] Total time: {total_time:.3f}s")

    return {
        "horizon": horizon,
        "numPlans": len(plans),
        "plans": plans,
        "success": len(plans) > 0,
        "timings": {
            "iterations": None,

            # Fast Downward (concrete only)
            "fd_conc": fd_time,
            "fd_abs": None,
            "fd_total": fd_time,

            # LP
            "lp_concrete_time": lp_time,
            "lp_abstract_time": None,
            "lp_total_time": lp_time,

            # Solve
            "abstract_solve_time": None,
            "concrete_solve_time": solve_time,

            "total_time": total_time,
            "run_id": base_dir
        }
    }


if __name__ == "__main__":
    main()
