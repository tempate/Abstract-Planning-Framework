import os
import time

import argparse

from fastdownward_service import run_fastdownward_service
from plasp_utils import generate_lp_with_plasp
from clingo_utils_api import run_clingo, write_occurs_abs_lp, create_map_lp

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
    )

    print("\n=== RESULT ===")
    print(f"Horizon: {result['horizon']}")
    print(f"Plans found: {result['numPlans']}")
    for i, plan in enumerate(result["plans"], 1):
        print(f"\nPlan {i}:")
        for atom in plan:
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
        horizon = abstract_result["horizon"]

    base_dir = os.path.dirname(concrete_result["sasFile"])
    output_c_lp = os.path.join(base_dir, "output_c.lp")
    output_a_lp = os.path.join(base_dir, "abstract", "output_a.lp")

    clingo_dir = os.path.join(base_dir, "clingo")
    os.makedirs(clingo_dir, exist_ok=True)

    occurs_abs_lp_path = os.path.join(clingo_dir, "occurs_abs.lp")
    map_lp_path = os.path.join(clingo_dir, "map.lp")

    t2_1 = time.perf_counter()

    # Concrete LP
    generate_lp_with_plasp(
        sas_or_pddl_path=concrete_result["sasFile"],
        lp_output_path=output_c_lp,
        encoding_type=encoding,
        is_pddl_instance=False,
        abstract_time_steps=time_step
    )

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

    # Solve abstract LP
    t_abs_solve_start = time.perf_counter()
    abstract_models = run_clingo([output_a_lp], horizon)
    abstract_atoms = abstract_models[0] if abstract_models else []
    t_abs_solve_end = time.perf_counter()
    print(f"Abstract solve: {t_abs_solve_end - t_abs_solve_start:.3f}s")

    t_occurs_start = time.perf_counter()
    write_occurs_abs_lp(abstract_atoms, occurs_abs_lp_path)
    t_occurs_end = time.perf_counter()
    print(f"occurs_abs.lp generation: {t_occurs_end - t_occurs_start:.3f}s")

    # ---- abstraction mapping ----
    t_map_start = time.perf_counter()

    create_map_lp(
        occurs_abs_path=occurs_abs_lp_path,
        output_path=map_lp_path,
        abstract_symbol=abstract_symbol,
        concrete_objects=concrete_objects
    )
    t_map_end = time.perf_counter()
    print(f"Mapping LP generation: {t_map_end - t_map_start:.3f}s")

    # Solve concrete LP
    t_conc_solve_start = time.perf_counter()
    concrete_models = run_clingo(
        [output_c_lp, occurs_abs_lp_path, map_lp_path],
        horizon
    )
    t_conc_solve_end = time.perf_counter()
    print(f"Concrete solve: {t_conc_solve_end - t_conc_solve_start:.3f}s")

    t3 = time.perf_counter()
    print(f"Concrete solve: {t3 - t2:.3f}s")

    plans = [[atom for atom in model] for model in concrete_models]

    print(f"[DONE] Total time: {time.perf_counter() - start_time:.3f}s")

    return {
        "horizon": horizon,
        "numPlans": len(plans),
        "plans": plans,
    }


if __name__ == "__main__":
    main()

