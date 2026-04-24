import os
import time

import argparse

from fastdownward_service import run_fastdownward_service
from plasp_utils import *
from plasp_utils import *
from clingo_utils_api import *
from log_utils import *

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
        required=False,
        default=None,
        help="Abstract symbol used in abstraction mapping (optional)"
    )
    parser.add_argument(
        "--concrete-objects",
        nargs="+",
        required=False,
        default=None,
        help="One or more concrete objects mapped to the abstract symbol (optional)"
    )
    parser.add_argument(
        "--mode",
        choices=["inc", "dec"],
        default="inc"
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
    solving_mode="inc"
):
    total_start = time.perf_counter()

    fd_start = time.perf_counter()

    # Open files as binary (Fast Downward expects bytes)
    with open(concrete_domain_path, "rb") as cd, \
         open(concrete_problem_path, "rb") as cp, \
         open(abstract_domain_path, "rb") as ad, \
         open(abstract_problem_path, "rb") as ap:

        concrete_result, abstract_result = run_fastdownward_service(
            domain_file=cd,
            problem_file=cp,
            abstract_domain_file=ad,
            abstract_problem_file=ap
        )

    fd_time = time.perf_counter() - fd_start

    base_dir = os.path.dirname(concrete_result["sasFile"])

    # If horizon was not provided, use Fast Downward's horizon
    if horizon is None:
        horizon = max(
            abstract_result.get("horizon", 0),
            concrete_result.get("horizon", 0)
        )

    logger = get_logger()

    logger.info("=" * 70)
    logger.info("NEW PLANNING RUN STARTED")
    logger.info(f"Horizon: {horizon}")
    logger.info(f"Encoding: {encoding}")
    logger.info(f"Mode: {solving_mode}")
    logger.info(f"Fast Downward time: {fd_time:.3f}s")

    print("Directory: ", base_dir)

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
        sas_or_pddl_path=concrete_result["sasFile"],
        lp_output_path=output_c_lp,
        encoding_type=encoding,
        is_pddl_instance=False,
        abstract_time_steps=time_step
    )

    add_switch_to_lp_rule(output_c_lp, encoding)
    append_pddl_facts_to_lp(concrete_problem_path, output_c_lp)

    concrete_lp_time = time.perf_counter() - concrete_lp_start
    logger.info(f"Concrete LP generation: {concrete_lp_time:.3f}s")

    abstract_lp_start = time.perf_counter()

    # Abstract LP
    generate_lp_with_plasp(
        sas_or_pddl_path=abstract_result["sasFile"],
        lp_output_path=output_a_lp,
        encoding_type=encoding,
        is_pddl_instance=False,
        abstract_time_steps=time_step
    )

    abstract_lp_time = time.perf_counter() - abstract_lp_start
    logger.info(f"Abstract LP generation: {abstract_lp_time:.3f}s")

    lp_total = time.perf_counter() - lp_start
    logger.info(f"Total LP generation: {lp_total:.3f}s")

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

            """ save_iteration_file(
                debug_dir,
                iteration,
                "forbidden.lp",
                "\n".join(forbid_atoms)
            ) """
        
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
            }

        abstract_atoms = abstract_models[0]

        logger.info("Abstract plan:")
        for atom in abstract_atoms:
            logger.info(f"  {atom}")

        # Generate occurs_abs.lp from abstract plan 
        occ_start = time.perf_counter()

        write_occurs_abs_lp(abstract_atoms, occurs_abs_lp_path)

        occ_time = log_phase(logger, "occurs_abs generation time", occ_start)

        """ copy_iteration_file(
            debug_dir,
            iteration,
            occurs_abs_lp_path
        ) """

        # Create mapping LP with switches
        map_start = time.perf_counter()

        switch_map = create_map_lp_with_switch_atoms(
            occurs_abs_lp_path,
            map_lp_path,
            abstract_symbol,
            concrete_objects,
        )

        map_time = log_phase(logger, "Mapping generation time", map_start)

        """ copy_iteration_file(
            debug_dir,
            iteration,
            map_lp_path
        ) """

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

            #save_json(debug_dir, iteration, "concrete_plans.json", plans)

            iter_time = time.perf_counter() - iter_start
            total_time = time.perf_counter() - total_start

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
                "success": True
            }

        # Refine abstraction: only forbid actions with the abstract symbol
        ref_start = time.perf_counter()

        logger.info("Concrete solve failed.")

        bad_hangar_actions = []

        for atom in bad_abstract_actions:
            if abstract_symbol and abstract_symbol in atom:
                bad_hangar_actions.append(atom)
            elif '"drive"' in atom:
                bad_hangar_actions.append(atom)

        logger.info("Bad abstract actions:")
        
        for atom in bad_abstract_actions:
            logger.info(f"  {atom}")

        """ save_iteration_file(
            debug_dir,
            iteration,
            "bad_actions.lp",
            "\n".join(bad_abstract_actions)
        ) """

        new_forbidden = []

        # Avoid duplicates
        for atom in bad_hangar_actions:
            if atom not in forbid_atoms:
                forbid_atoms.append(atom)
                new_forbidden.append(atom)

        logger.info("New forbidden atoms:")

        for atom in new_forbidden:
            logger.info(f"  {atom}")

        """ save_iteration_file(
            debug_dir,
            iteration,
            "new_forbidden.lp",
            "\n".join(new_forbidden)
        ) """

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

        # Loop continues for next iteration

if __name__ == "__main__":
    main()

