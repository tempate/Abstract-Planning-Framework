import os
import time

import argparse

from .fastdownward_service import *
from core.plasp_utils import *
from core.clingo_utils_api import *
from core.log_utils import *
from .create_excel import *
from core.json_logger import *

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--abstract-domain", required=True)
    parser.add_argument("--abstract-problem", required=True)
    parser.add_argument("--concrete-domain", required=True)
    parser.add_argument("--concrete-problem", required=True)
    parser.add_argument("--horizon", type=int, default=None)
    parser.add_argument("--encoding", default="exact")
    parser.add_argument("--time-step", action="store_true")
    parser.add_argument(
        "--abstract-symbol",
        required=True,
        help="Abstract symbol used in abstraction mapping"
    )
    parser.add_argument(
        "--concrete-objects",
        nargs="+",
        required=True,
        help="One or more concrete objects mapped to the abstract symbol"
    )
    parser.add_argument(
        "--mode",
        choices=["inc", "dec"],
        default="inc"
    )
    parser.add_argument(
        "--plan-source",
        choices=["fd", "clingo"],
        default="clingo",
        help="Use Fast Downward plan directly or compute plan with clingo"
    )

    args = parser.parse_args()

    print("Starting")

    logger = get_logger()

    result = compute_concrete_from_abstract(
        abstract_domain_path=args.abstract_domain,
        abstract_problem_path=args.abstract_problem,
        concrete_domain_path=args.concrete_domain,
        concrete_problem_path=args.concrete_problem,
        horizon=args.horizon,
        encoding=args.encoding,
        time_step=args.time_step,
        abstract_symbol=args.abstract_symbol,
        concrete_objects=args.concrete_objects,
        solving_mode=args.mode,
        plan_source=args.plan_source,
    )

    print("\n=== RESULT ===")
    print(f"Horizon: {result['horizon']}")
    print(f"Plans found: {result['numPlans']}")

    logger.info(f"Success: {result['success']}")
    logger.info(f"Plans found: {result['numPlans']}")

    for i, plan in enumerate(result["plans"], 1):
        print(f"\nPlan {i}:")

        # sort by timestep (last argument of occurs)
        sorted_plan = sorted(plan, key=lambda a: int(str(a).split(",")[-1].rstrip(")")))

        for atom in sorted_plan:
            print(" ", atom)

    timings = result["timings"]

    row = {
        "Problem": args.abstract_problem.split("/")[-1],
        "Version": "abstract",
        "Mode": args.mode,
        "horizon": result["horizon"],
        "iterations": timings["iterations"],
        "fd_conc": timings["fd_concrete_time"],
        "fd_abs": timings["fd_abstract_time"],
        "fd_total": timings["fd_total_time"],
        "lp_concrete_time": timings["lp_concrete_time"],
        "lp_abstract_time": timings["lp_abstract_time"],
        "lp_total_time": timings["lp_total_time"],
        "abstract_solve_time": timings["abstract_solve_time"],
        "concrete_solve_time": timings["concrete_solve_time"],
        "total": timings["total_time"],
        "result": "SAT" if result["success"] else "UNSAT",
        "id": timings["run_id"]
    }
    append_to_excel(row)


def compute_concrete_from_abstract(
    abstract_domain_path,
    abstract_problem_path,
    concrete_domain_path,
    concrete_problem_path,
    horizon=None,
    encoding="exact",
    time_step=False,
    abstract_symbol=None,
    concrete_objects=None,
    solving_mode="inc",
    plan_source="clingo",
):
    dir_name = "beluga"

    base_dir, run_id = create_run_dir(dir_name)

    logger, debug_dir = setup_debug_logger(base_dir)

    logger.info("=" * 70)
    logger.info("NEW PLANNING RUN STARTED")
    logger.info(f"Horizon: {horizon}")
    logger.info(f"Encoding: {encoding}")
    logger.info(f"Mode: {solving_mode}")
    logger.info(f"Run ID: {run_id}")
    logger.info(f"Base dir: {base_dir}")

    print("Directory:", base_dir)

    # Create json log for abstract plans
    json_log_path, problem_hash = get_json_path(
        abstract_problem_path,
        concrete_problem_path,
        dir_name
    )

    init_plan_file(
        json_log_path,
        problem_hash,
        abstract_problem_path,
        concrete_problem_path,
        abstract_symbol=abstract_symbol,
        concrete_objects=concrete_objects
    )

    total_start = time.perf_counter()

    fd_start = time.perf_counter()

    # Open files as binary (Fast Downward expects bytes)
    with open(concrete_domain_path, "rb") as cd, \
        open(concrete_problem_path, "rb") as cp, \
        open(abstract_domain_path, "rb") as ad, \
        open(abstract_problem_path, "rb") as ap:

        fd_result = run_fastdownward_service(
            base_dir=base_dir,
            domain_file=cd,
            problem_file=cp,
            abstract_domain_file=ad,
            abstract_problem_file=ap,
            fd_task="translate",
        )

    concrete_result = fd_result["concrete"]
    abstract_result = fd_result["abstract"]
    fd_timings = fd_result["timings"]

    fd_time = time.perf_counter() - fd_start

    # If horizon was not provided, use Fast Downward's horizon
    if horizon is None:
        horizon = abstract_result.get("horizon", 0)
        """ horizon = max(
            abstract_result.get("horizon", 0),
            concrete_result.get("horizon", 0)
        ) """

    concrete_input = concrete_result["sasFile"]
    abstract_input = abstract_result["sasFile"]

    is_pddl = False

    logger.info(f"Fast Downward time: {fd_time:.3f}s")

    output_c_lp = os.path.join(base_dir, "output_c.lp")
    output_a_lp = os.path.join(base_dir, "abstract", "output_a.lp")

    clingo_dir = os.path.join(base_dir, "clingo")
    os.makedirs(clingo_dir, exist_ok=True)

    occurs_abs_lp_path = os.path.join(clingo_dir, "occurs_abs.lp")
    map_lp_path = os.path.join(clingo_dir, "map.lp")
    forbid_lp_path = os.path.join(clingo_dir, "forbid_abstract.lp")

    lp_start = time.perf_counter()

    concrete_lp_start = time.perf_counter()

    # Concrete LP
    generate_lp_with_plasp(
        sas_or_pddl_path=concrete_input,
        lp_output_path=output_c_lp,
        encoding_type=encoding,
        is_pddl_instance=is_pddl,
        domain_file=concrete_domain_path,
        abstract_time_steps=time_step
    )

    add_switch_to_lp_rule(output_c_lp, encoding)

    concrete_lp_time = time.perf_counter() - concrete_lp_start
    logger.info(f"Concrete LP generation: {concrete_lp_time:.3f}s")

    abstract_lp_start = time.perf_counter()

    # Abstract LP
    if plan_source == "clingo":
        generate_lp_with_plasp(
            sas_or_pddl_path=abstract_input,
            lp_output_path=output_a_lp,
            encoding_type=encoding,
            is_pddl_instance=is_pddl,
            domain_file=abstract_domain_path,
            abstract_time_steps=time_step
        )

        abstract_lp_time = time.perf_counter() - abstract_lp_start
        logger.info(f"Abstract LP generation: {abstract_lp_time:.3f}s")

    lp_total = time.perf_counter() - lp_start
    logger.info(f"Total LP generation: {lp_total:.3f}s")


    #######################################################################

    if plan_source == "fd":
        logger.info("Using Fast Downward plan")

        # Generate occurs_abs.lp from fastdownward plan
        occ_start = time.perf_counter()

        abstract_atoms = fd_plan_to_occurs_abstract(
                abstract_result["planFile"],
                occurs_abs_lp_path
            )

        occ_time = log_phase(logger, "occurs_abs from fd generation time", occ_start)

        iter_start = time.perf_counter()
        iteration_times = []

        # Create mapping LP with switches
        map_start = time.perf_counter()

        switch_map = create_map_lp_with_switch_atoms(
            occurs_abs_lp_path,
            map_lp_path,
            abstract_symbol,
            concrete_objects,
        )

        map_time = log_phase(logger, "Mapping generation time", map_start)

         # Concrete incremental solving
        conc_start = time.perf_counter()

        if solving_mode == "inc":
            ok, plans, bad_abstract_actions = solve_concrete_incremental(
                [output_c_lp, occurs_abs_lp_path, map_lp_path],
                horizon,
                switch_map,
            )
        if solving_mode == "dec":
            ok, plans, bad_abstract_actions = solve_concrete_decremental(
                [output_c_lp, occurs_abs_lp_path, map_lp_path],
                horizon,
                switch_map
            )

        conc_time = log_phase(logger, "Concrete solving time", conc_start)

        if ok:
            logger.info("SUCCESS: Concrete plan found.")
            logger.info("Plans:")
            logger.info(pformat(plans))

            iter_time = time.perf_counter() - iter_start
            total_time = time.perf_counter() - total_start

            update_plan(
                json_log_path,
                abstract_atoms,
                success=True,
                bad_actions=[],
                mode=solving_mode
            )

            iteration_times.append({
                "abs": 0,
                "occ": occ_time,
                "map": map_time,
                "conc": conc_time,
                "ref": 0.0,
                "iter": iter_time
            })

            logger.info("=" * 70)
            logger.info(
                f"ITERATIONS TOTAL SUMMARY | "
                f"iters={len(iteration_times)} | "
                f"abs={sum(t['abs'] for t in iteration_times):.3f}s | "
                f"occ={sum(t['occ'] for t in iteration_times):.3f}s | "
                f"map={sum(t['map'] for t in iteration_times):.3f}s | "
                f"conc={sum(t['conc'] for t in iteration_times):.3f}s | "
                f"ref={sum(t['ref'] for t in iteration_times):.3f}s | "
                f"iter_total={sum(t['iter'] for t in iteration_times):.3f}s"
            )

            logger.info(f"TOTAL TIME: {total_time:.3f}s")

            return {
                "horizon": horizon,
                "numPlans": len(plans),
                "plans": plans,
                "success": True,
                "timings": {
                    "iterations": len(iteration_times),
                    "fd_concrete_time": fd_timings["fd_concrete_time"],
                    "fd_abstract_time": fd_timings["fd_abstract_time"],
                    "fd_total_time": fd_timings["fd_total_time"],
                    "lp_concrete_time": concrete_lp_time,
                    "lp_abstract_time": 0,
                    "lp_total_time": lp_total,
                    "abstract_solve_time": 0,
                    "concrete_solve_time": conc_time,
                    "total_time": total_time,
                    "run_id": base_dir
                }
            }

        # Refine abstraction: only forbid actions with the abstract symbol
        ref_start = time.perf_counter()

        logger.info("Concrete solve failed.")
        logger.info("Bad abstract actions:")

        for atom in bad_abstract_actions:
            logger.info(f"  {atom}")

        logger.info("=" * 70)
        logger.info(
            f"ITERATIONS TOTAL SUMMARY | "
            f"iters={len(iteration_times)} | "
            f"abs={sum(t['abs'] for t in iteration_times):.3f}s | "
            f"occ={sum(t['occ'] for t in iteration_times):.3f}s | "
            f"map={sum(t['map'] for t in iteration_times):.3f}s | "
            f"conc={sum(t['conc'] for t in iteration_times):.3f}s | "
            f"ref={sum(t['ref'] for t in iteration_times):.3f}s | "
            f"iter_total={sum(t['iter'] for t in iteration_times):.3f}s"
        )

        logger.info("No abstract plan possible.")
        logger.info("FAILED")

        total_time = time.perf_counter() - total_start
        logger.info(f"TOTAL TIME: {total_time:.3f}s")

        update_plan(
            json_log_path,
            abstract_atoms,
            success=False,
            bad_actions=bad_abstract_actions,
            mode=solving_mode
        )

        return {
            "horizon": horizon,
            "numPlans": 0,
            "plans": [],
            "success": False,
            "timings": {
                "iterations": len(iteration_times),
                "fd_concrete_time": fd_timings["fd_concrete_time"],
                "fd_abstract_time": fd_timings["fd_abstract_time"],
                "fd_total_time": fd_timings["fd_total_time"],
                "lp_concrete_time": concrete_lp_time,
                "lp_abstract_time": 0,
                "lp_total_time": lp_total,
                "abstract_solve_time": 0,
                "concrete_solve_time": conc_time,
                "total_time": total_time,
                "run_id": base_dir
            }
        }

    ################################################################################

    iteration = 0
    forbid_atoms = []
    iteration_times = []

    while True:
        iteration += 1
        iter_start = time.perf_counter()

        logger.info("")
        logger.info("=" * 50)
        logger.info(f"ITERATION {iteration}")
        logger.info("=" * 50)

        # Solve abstract plan
        abs_start = time.perf_counter()

        abstract_lp_files = [output_a_lp]

        if forbid_atoms:
            write_forbid_abstract_lp(forbid_atoms, forbid_lp_path)
            abstract_lp_files.append(forbid_lp_path)

            save_iteration_file(
                debug_dir,
                iteration,
                "forbidden.lp",
                "\n".join(forbid_atoms)
            )

        abstract_models = run_clingo(abstract_lp_files, horizon)

        abs_time = log_phase(logger, "Abstract solving time", abs_start)

        if not abstract_models:
            logger.info("No abstract plan possible.")
            logger.info("FAILED")

            total_time = time.perf_counter() - total_start
            logger.info(f"TOTAL TIME: {total_time:.3f}s")

            return {
                "horizon": horizon,
                "numPlans": 0,
                "plans": [],
                "success": False,
                "timings": {
                    "iterations": len(iteration_times),
                    "fd_concrete_time": fd_timings["fd_concrete_time"],
                    "fd_abstract_time": fd_timings["fd_abstract_time"],
                    "fd_total_time": fd_timings["fd_total_time"],
                    "lp_concrete_time": concrete_lp_time,
                    "lp_abstract_time": abstract_lp_time,
                    "lp_total_time": lp_total,
                    "abstract_solve_time": abs_time,
                    "concrete_solve_time": conc_time,
                    "total_time": total_time,
                    "run_id": base_dir
                }
            }

        abstract_atoms = abstract_models[0]

        logger.info("Abstract plan:")
        for atom in abstract_atoms:
            logger.info(f"  {atom}")

        # Generate occurs_abs.lp from abstract plan
        occ_start = time.perf_counter()

        write_occurs_abs_lp(abstract_atoms, occurs_abs_lp_path)

        occ_time = log_phase(logger, "occurs_abs generation time", occ_start)

        copy_iteration_file(
            debug_dir,
            iteration,
            occurs_abs_lp_path
        )

        # Create mapping LP with switches
        map_start = time.perf_counter()

        switch_map = create_map_lp_with_switch_atoms(
            occurs_abs_lp_path,
            map_lp_path,
            abstract_symbol,
            concrete_objects,
        )

        map_time = log_phase(logger, "Mapping generation time", map_start)

        copy_iteration_file(
            debug_dir,
            iteration,
            map_lp_path
        )

        # Concrete incremental solving
        conc_start = time.perf_counter()

        if solving_mode == "inc":
            ok, plans, bad_abstract_actions = solve_concrete_incremental(
                [output_c_lp, occurs_abs_lp_path, map_lp_path],
                horizon,
                switch_map,
            )
        if solving_mode == "dec":
            ok, plans, bad_abstract_actions = solve_concrete_decremental(
                [output_c_lp, occurs_abs_lp_path, map_lp_path],
                horizon,
                switch_map
            )

        conc_time = log_phase(logger, "Concrete solving time", conc_start)

        if ok:
            logger.info("SUCCESS: Concrete plan found.")
            logger.info("Plans:")
            logger.info(pformat(plans))

            save_json_iteration_file(debug_dir, iteration, "concrete_plans.json", plans)

            iter_time = time.perf_counter() - iter_start
            total_time = time.perf_counter() - total_start

            update_plan(
                json_log_path,
                abstract_atoms,
                success=True,
                bad_actions=[], # maybe add here from the other actions?
                mode=solving_mode
            )

            iteration_times.append({
                "abs": abs_time,
                "occ": occ_time,
                "map": map_time,
                "conc": conc_time,
                "ref": 0.0,
                "iter": iter_time
            })

            logger.info("=" * 70)
            logger.info(
                f"ITERATIONS TOTAL SUMMARY | "
                f"iters={len(iteration_times)} | "
                f"abs={sum(t['abs'] for t in iteration_times):.3f}s | "
                f"occ={sum(t['occ'] for t in iteration_times):.3f}s | "
                f"map={sum(t['map'] for t in iteration_times):.3f}s | "
                f"conc={sum(t['conc'] for t in iteration_times):.3f}s | "
                f"ref={sum(t['ref'] for t in iteration_times):.3f}s | "
                f"iter_total={sum(t['iter'] for t in iteration_times):.3f}s"
            )

            logger.info(f"TOTAL TIME: {total_time:.3f}s")

            return {
                "horizon": horizon,
                "numPlans": len(plans),
                "plans": plans,
                "success": True,
                "timings": {
                    "iterations": len(iteration_times),
                    "fd_concrete_time": fd_timings["fd_concrete_time"],
                    "fd_abstract_time": fd_timings["fd_abstract_time"],
                    "fd_total_time": fd_timings["fd_total_time"],
                    "lp_concrete_time": concrete_lp_time,
                    "lp_abstract_time": abstract_lp_time,
                    "lp_total_time": lp_total,
                    "abstract_solve_time": abs_time,
                    "concrete_solve_time": conc_time,
                    "total_time": total_time,
                    "run_id": base_dir
                }
            }

        # Refine abstraction: only forbid actions with the abstract symbol
        ref_start = time.perf_counter()

        logger.info("Concrete solve failed.")
        logger.info("Bad abstract actions:")

        for atom in bad_abstract_actions:
            logger.info(f"  {atom}")

        save_iteration_file(
            debug_dir,
            iteration,
            "bad_actions.lp",
            "\n".join(bad_abstract_actions)
        )

        new_forbidden = []

        for atom in bad_abstract_actions:
            if abstract_symbol in atom and atom not in forbid_atoms:
                forbid_atoms.append(atom)
                new_forbidden.append(atom)

        logger.info("New forbidden atoms:")

        for atom in new_forbidden:
            logger.info(f"  {atom}")

        save_iteration_file(
            debug_dir,
            iteration,
            "new_forbidden.lp",
            "\n".join(new_forbidden)
        )

        ref_time = log_phase(logger, "Refinement time", ref_start)

        iter_time = time.perf_counter() - iter_start

        iteration_times.append({
            "abs": abs_time,
            "occ": occ_time,
            "map": map_time,
            "conc": conc_time,
            "ref": ref_time,
            "iter": iter_time
        })

        logger.info(
            f"ITER {iteration} SUMMARY | "
            f"abs={abs_time:.3f}s | "
            f"occ={occ_time:.3f}s | "
            f"map={map_time:.3f}s | "
            f"conc={conc_time:.3f}s | "
            f"ref={ref_time:.3f}s | "
            f"forbidden={len(forbid_atoms)} | "
            f"iter={iter_time:.3f}s"
        )

        update_plan(
            json_log_path,
            abstract_atoms,
            success=False,
            bad_actions=bad_abstract_actions,
            mode=solving_mode
        )

        # Loop continues for next iteration

if __name__ == "__main__":
    main()
