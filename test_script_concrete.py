import os
import time
import argparse

from fastdownward_service import run_fastdownward_service
from plasp_utils import generate_lp_with_plasp
from clingo_utils import run_clingo


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--domain", required=True)
    parser.add_argument("--problem", required=True)
    parser.add_argument("--horizon", type=int, default=None)
    parser.add_argument("--encoding", default="exact")
    parser.add_argument("--time-step", action="store_true")

    args = parser.parse_args()

    result = compute_concrete_plan(
        domain_path=args.domain,
        problem_path=args.problem,
        horizon=args.horizon,
        encoding=args.encoding,
        time_step=args.time_step,
    )

    print("\n=== RESULT ===")
    print(f"Horizon: {result['horizon']}")
    print(f"Plans found: {result['numPlans']}")
    for i, plan in enumerate(result["plans"], 1):
        print(f"\nPlan {i}:")
        for atom in plan:
            print(" ", atom)

def compute_concrete_plan(
    domain_path,
    problem_path,
    horizon=None,
    encoding="exact",
    time_step=False,
):
    start_time = time.perf_counter()

    # Fast Downward expects binary files
    with open(domain_path, "rb") as d, open(problem_path, "rb") as p:
        result, _ = run_fastdownward_service(
            domain_file=d,
            problem_file=p
        )

    t1 = time.perf_counter()
    print(f"Fast Downward: {t1 - start_time:.3f}s")

    # If horizon was not provided, use Fast Downward's horizon
    if horizon is None:
        horizon = result["horizon"]

    base_dir = os.path.dirname(result["sasFile"])
    output_lp = os.path.join(base_dir, "output_c.lp")

    # Generate LP with plasp
    generate_lp_with_plasp(
        sas_or_pddl_path=result["sasFile"],
        lp_output_path=output_lp,
        encoding_type=encoding,
        is_pddl_instance=False,
        abstract_time_steps=time_step
    )

    t2 = time.perf_counter()
    print(f"LP generation: {t2 - t1:.3f}s")

    # Solve with clingo
    models = run_clingo([output_lp], horizon)

    t3 = time.perf_counter()
    print(f"Clingo solve: {t3 - t2:.3f}s")

    plans = [[atom for atom in model] for model in models]

    print(f"[DONE] Total time: {time.perf_counter() - start_time:.3f}s")

    return {
        "horizon": horizon,
        "numPlans": len(plans),
        "plans": plans,
    }


if __name__ == "__main__":
    main()

