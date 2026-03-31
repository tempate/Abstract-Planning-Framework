import os
import time

import argparse

from fastdownward_service import run_fastdownward_service
from plasp_utils import generate_lp_with_plasp, append_pddl_facts_to_lp
from clingo_utils_api import *

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

    args = parser.parse_args()

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
    start_time = time.perf_counter()

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

    t1 = time.perf_counter()
    print(f"Fast Downward: {t1 - start_time:.3f}s")

    # If horizon was not provided, use Fast Downward's horizon
    if horizon is None:
        horizon = concrete_result["horizon"]

    base_dir = os.path.dirname(concrete_result["sasFile"])

    output_c_lp = os.path.join(base_dir, "output_c.lp")
    output_a_lp = os.path.join(base_dir, "abstract", "output_a.lp")
    
    clingo_dir = os.path.join(base_dir, "clingo")
    os.makedirs(clingo_dir, exist_ok=True)

    occurs_abs_lp_path = os.path.join(clingo_dir, "occurs_abs.lp")
    map_lp_path = os.path.join(clingo_dir, "map.lp")
    forbid_lp_path = os.path.join(clingo_dir, "forbid_abstract.lp")

    t2_1 = time.perf_counter()

    # Concrete LP
    generate_lp_with_plasp(
        sas_or_pddl_path=concrete_result["sasFile"],
        lp_output_path=output_c_lp,
        encoding_type=encoding,
        is_pddl_instance=False,
        abstract_time_steps=time_step
    )

    append_pddl_facts_to_lp(concrete_problem_path, output_c_lp)

    t2_2 = time.perf_counter()
    print(f"Concrete LP generation: {t2_2 - t2_1:.3f}s")

    # Abstract LP
    generate_lp_with_plasp(
        sas_or_pddl_path=abstract_result["sasFile"],
        lp_output_path=output_a_lp,
        encoding_type=encoding,
        is_pddl_instance=False,
        abstract_time_steps=time_step
    )

    t2 = time.perf_counter()
    print(f"Abstract LP generation: {t2 - t2_2:.3f}s")
    print(f"LP generation: {t2 - t2_1:.3f}s")

    iteration = 0
    forbid_atoms = []

    while True:
        iteration += 1
        print(f"\n=== ITERATION {iteration} ===")

        # Solve abstract plan
        abs_start = time.perf_counter()
        
        abstract_lp_files = [output_a_lp]

        if forbid_atoms:
            write_forbid_abstract_lp(forbid_atoms, forbid_lp_path)
            abstract_lp_files.append(forbid_lp_path)

        abstract_models = run_clingo(abstract_lp_files, horizon)

        abs_end = time.perf_counter()
        print(f"Abstract solving time: {abs_end - abs_start:.3f}s")

        if not abstract_models:
            print("No abstract plan possible with current constraints")
            print(f"Total runtime: {time.perf_counter() - start_time:.3f}s")

            return {
                "horizon": horizon,
                "numPlans": 0,
                "plans": [],
                "success": False,
            }

        abstract_atoms = abstract_models[0]

        # Generate occurs_abs.lp from abstract plan 
        occurs_start = time.perf_counter()

        write_occurs_abs_lp(abstract_atoms, occurs_abs_lp_path)

        occurs_end = time.perf_counter()
        print(f"occurs_abs generation time: {occurs_end - occurs_start:.3f}s")

        # Create mapping LP with switches
        map_start = time.perf_counter()

        switch_map = create_map_lp_with_switch_atoms(
            occurs_abs_lp_path,
            map_lp_path,
            abstract_symbol,
            concrete_objects,
        )

        map_end = time.perf_counter()
        print(f"Mapping generation time: {map_end - map_start:.3f}s")

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

        conc_end = time.perf_counter()
        print(f"Concrete solving time: {conc_end - conc_start:.3f}s")

        if ok:
            print("Concrete plan found")
            print(f"Total runtime: {time.perf_counter() - start_time:.3f}s")
            
            return {
                "horizon": horizon,
                "numPlans": len(plans),
                "plans": plans,
                "success": True
            }

        # Refine abstraction: only forbid actions with the abstract symbol
        refine_start = time.perf_counter()
        
        bad_hangar_actions = [
            atom for atom in bad_abstract_actions
            if abstract_symbol in atom
        ]

        print("Refining abstraction by forbidding hangar actions:")
        for atom in bad_hangar_actions:
            print("   ", atom)

        # Avoid duplicates
        for atom in bad_hangar_actions:
            if atom not in forbid_atoms:
                forbid_atoms.append(atom)

        refine_end = time.perf_counter()
        print(f"Refinement time: {refine_end - refine_start:.3f}s")

        # Loop continues for next iteration

if __name__ == "__main__":
    main()

