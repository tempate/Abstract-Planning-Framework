import argparse
import os
import time

from core.execution import create_run_dir, get_logger, setup_debug_logger
from core.integrations.clingo import run_clingo
from core.integrations.fast_downward import run_fast_downward
from core.integrations.plasp import generate_lp_with_plasp

from .utils.reporting import print_planning_result, save_result_summary


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
    time_step=False,
):
    """Translate and solve one concrete PDDL planning problem."""
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

    # Fast Downward expects binary input streams.
    with (
        open(domain_path, "rb") as domain_file,
        open(problem_path, "rb") as problem_file,
    ):
        downward_result = run_fast_downward(
            base_dir=base_dir,
            domain_file=domain_file,
            problem_file=problem_file,
        )

    concrete_task = downward_result["concrete"]

    fd_time = time.perf_counter() - fd_start

    if horizon is None:
        horizon = concrete_task["horizon"]

    logger.info(f"Fast Downward time: {fd_time:.3f}s")

    concrete_lp_path = os.path.join(base_dir, "output_c.lp")

    lp_start = time.perf_counter()

    generate_lp_with_plasp(
        sas_or_pddl_path=concrete_task["sasFile"],
        lp_output_path=concrete_lp_path,
        encoding_type=encoding,
        abstract_time_steps=time_step,
    )

    lp_time = time.perf_counter() - lp_start
    logger.info(f"LP generation time: {lp_time:.3f}s")

    solve_start = time.perf_counter()

    plans = run_clingo([concrete_lp_path], horizon)

    solve_time = time.perf_counter() - solve_start

    total_time = time.perf_counter() - total_start

    logger.info(f"Plans found: {len(plans)}")
    logger.info(f"Total runtime: {total_time:.3f}s")
    logger.info("=" * 70)

    print(f"[DONE] Total time: {total_time:.3f}s")

    return {
        "horizon": horizon,
        "numPlans": len(plans),
        "plans": plans,
        "success": bool(plans),
        "timings": {
            "iterations": None,
            "fd_conc": fd_time,
            "fd_abs": None,
            "fd_total": fd_time,
            "lp_concrete_time": lp_time,
            "lp_abstract_time": None,
            "lp_total_time": lp_time,
            "abstract_solve_time": None,
            "concrete_solve_time": solve_time,
            "total_time": total_time,
            "run_id": base_dir,
        },
    }


if __name__ == "__main__":
    main()
