import os
import time
import argparse

from fastdownward_service import run_fastdownward_service
from plasp_utils import generate_lp_with_plasp
from clingo_utils_api import run_clingo
from log_utils import *
from create_excel import *

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

    #print("result: ", result)

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
    
    timings = result["timings"]

    row = {
        "Problem": args.abstract_problem.split("/")[-1] if hasattr(args, "abstract_problem") else args.problem.split("/")[-1],
        "Version": "concrete",
        "Mode": getattr(args, "mode", "N/A"),

        "horizon": result["horizon"],
        "iterations": timings.get("iterations"),

        "fd_conc": timings.get("fd_conc"),
        "fd_abs": timings.get("fd_abs"),
        "fd_total": timings.get("fd_total"),

        "lp_concrete_time": timings.get("lp_concrete_time"),
        "lp_abstract_time": timings.get("lp_abstract_time"),
        "lp_total_time": timings.get("lp_total_time"),

        "abstract_solve_time": timings.get("abstract_solve_time"),
        "concrete_solve_time": timings.get("concrete_solve_time"),

        "total": timings.get("total_time"),

        "result": "SAT" if result["success"] else "UNSAT",
        "id": timings.get("run_id")
    }

    append_to_excel(row)

def compute_concrete_plan(
    domain_path,
    problem_path,
    horizon=None,
    encoding="exact",
    time_step=False
):
    base_dir, run_id = create_run_dir()

    logger, debug_dir = setup_debug_logger(base_dir)

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
    with open(domain_path, "rb") as d, open(problem_path, "rb") as p:
        result = run_fastdownward_service(
            base_dir=base_dir,
            domain_file=d,
            problem_file=p
        )
    
    result = result["concrete"]

    input = result["sasFile"]

    fd_time = time.perf_counter() - fd_start

    # If horizon was not provided, use Fast Downward's horizon
    if horizon is None:
        horizon = result["horizon"]
    
    is_pddl = False

    logger.info(f"Fast Downward time: {fd_time:.3f}s")

    output_lp = os.path.join(base_dir, "output_c.lp")

    logger, debug_dir = setup_debug_logger(base_dir)

    # Generate LP with plasp
    lp_start = time.perf_counter()

    generate_lp_with_plasp(
        sas_or_pddl_path=input,
        lp_output_path=output_lp,
        encoding_type=encoding,
        is_pddl_instance=is_pddl,
        domain_file=domain_path,
        abstract_time_steps=time_step
    )

    lp_time = time.perf_counter() - lp_start
    logger.info(f"LP generation time: {lp_time:.3f}s")

    # Solve with clingo
    solve_start = time.perf_counter()

    models = run_clingo([output_lp], horizon)

    solve_time = time.perf_counter() - solve_start

    plans = [[atom for atom in model] for model in models]

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

