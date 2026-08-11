import argparse
import os
import time
from pprint import pformat

from core.asp import write_abstract_occurrences, write_forbidden_actions
from core.execution import (
    copy_iteration_file,
    create_run_dir,
    get_logger,
    log_phase,
    save_iteration_file,
    save_json_iteration_file,
    setup_debug_logger,
)
from core.integrations.clingo import run_clingo
from core.integrations.fast_downward import (
    fast_downward_plan_to_abstract_atoms,
    run_fast_downward,
)
from core.integrations.plasp import (
    add_switch_to_lp_rule,
    append_pddl_facts_to_lp,
    generate_lp_with_plasp,
)
from core.planners.factory import PLANNER_TYPES, get_planner
from core.solvers.factory import get_solver

from .utils.abstract_plan_log import (
    get_plan_log_path,
    initialize_plan_log,
    record_plan_attempt,
)
from .utils.reporting import print_planning_result, save_result_summary


def _build_result(
    *,
    horizon,
    success,
    plans,
    iteration_times,
    fd_timings,
    concrete_lp_time,
    abstract_lp_time,
    lp_total_time,
    abstract_solve_time,
    concrete_solve_time,
    total_time,
    run_id,
):
    return {
        "horizon": horizon,
        "numPlans": len(plans) if success else 0,
        "plans": plans if success else [],
        "success": success,
        "timings": {
            "iterations": len(iteration_times),
            "fd_concrete_time": fd_timings["fd_concrete_time"],
            "fd_abstract_time": fd_timings["fd_abstract_time"],
            "fd_total_time": fd_timings["fd_total_time"],
            "lp_concrete_time": concrete_lp_time,
            "lp_abstract_time": abstract_lp_time,
            "lp_total_time": lp_total_time,
            "abstract_solve_time": abstract_solve_time,
            "concrete_solve_time": concrete_solve_time,
            "total_time": total_time,
            "run_id": run_id,
        },
    }


def _log_iteration_totals(logger, iteration_times):
    totals = {
        phase: sum(timing[phase] for timing in iteration_times)
        for phase in ("abs", "occ", "map", "conc", "ref", "iter")
    }
    logger.info("=" * 70)
    logger.info(
        "ITERATIONS TOTAL SUMMARY | "
        f"iters={len(iteration_times)} | "
        f"abs={totals['abs']:.3f}s | occ={totals['occ']:.3f}s | "
        f"map={totals['map']:.3f}s | conc={totals['conc']:.3f}s | "
        f"ref={totals['ref']:.3f}s | iter_total={totals['iter']:.3f}s"
    )


def _iteration_timing(abstract, occurs, mapping, concrete, refinement, total):
    return {
        "abs": abstract,
        "occ": occurs,
        "map": mapping,
        "conc": concrete,
        "ref": refinement,
        "iter": total,
    }


def _log_atoms(logger, heading, atoms):
    logger.info(heading)
    for atom in atoms:
        logger.info(f"  {atom}")


def _add_new_forbidden_actions(forbidden_actions, bad_actions, refinement_filter):
    new_forbidden = []
    for atom in bad_actions:
        if refinement_filter(atom) and atom not in forbidden_actions:
            forbidden_actions.append(atom)
            new_forbidden.append(atom)
    return new_forbidden


def _build_mapping(
    planner,
    occurrences_path,
    output_path,
    abstract_symbol,
    objects,
    logger,
):
    start = time.perf_counter()
    switch_map = planner.build_mapping(
        occurrences_path,
        output_path,
        abstract_symbol,
        objects,
    )
    elapsed = log_phase(logger, "Mapping generation time", start)
    return switch_map, elapsed


def _solve_concrete(mode, lp_files, horizon, switch_map, logger):
    start = time.perf_counter()
    success, plans, bad_actions = get_solver(mode).solve(
        lp_files,
        horizon,
        switch_map,
    )
    elapsed = log_phase(logger, "Concrete solving time", start)
    return success, plans, bad_actions, elapsed


def _argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--profile",
        choices=sorted(PLANNER_TYPES),
        default="beluga",
        help="Domain-specific mapping and refinement configuration",
    )
    parser.add_argument("--abstract-domain", required=True)
    parser.add_argument("--abstract-problem", required=True)
    parser.add_argument("--concrete-domain", required=True)
    parser.add_argument("--concrete-problem", required=True)
    parser.add_argument("--horizon", type=int, default=None)
    parser.add_argument("--encoding", default="exact")
    parser.add_argument("--time-step", action="store_true")
    parser.add_argument(
        "--abstract-symbol",
        default=None,
        help="Abstract symbol used in abstraction mapping",
    )
    parser.add_argument(
        "--concrete-objects",
        nargs="+",
        default=None,
        help=(
            "One or more concrete objects mapped to the abstract symbol "
            "(required by the beluga profile)"
        ),
    )
    parser.add_argument("--mode", choices=["inc", "dec"], default="inc")
    parser.add_argument(
        "--plan-source",
        choices=["fd", "clingo"],
        default="clingo",
        help="Use a Fast Downward plan directly or compute one with Clingo",
    )
    return parser


def main():
    parser = _argument_parser()

    args = parser.parse_args()
    planner = get_planner(args.profile)
    try:
        planner.validate_configuration(args.abstract_symbol, args.concrete_objects)
    except ValueError as error:
        parser.error(str(error))

    print("Starting")

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
        profile_name=args.profile,
    )

    print_planning_result(result, get_logger())
    save_result_summary(args.abstract_problem, "abstract", args.mode, result)


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
    profile_name="beluga",
    refinement_filter=None,
):
    """Refine an abstract plan until it has a valid concrete realization."""
    planner = get_planner(profile_name)
    planner.validate_configuration(abstract_symbol, concrete_objects)
    run_directory = planner.run_directory
    append_concrete_pddl_facts = planner.append_concrete_pddl_facts
    if refinement_filter is None:
        refinement_filter = lambda atom: planner.should_refine(atom, abstract_symbol)

    base_dir, run_id = create_run_dir(run_directory)

    logger, debug_dir = setup_debug_logger(base_dir)

    logger.info("=" * 70)
    logger.info("NEW PLANNING RUN STARTED")
    logger.info(f"Horizon: {horizon}")
    logger.info(f"Encoding: {encoding}")
    logger.info(f"Mode: {solving_mode}")
    logger.info(f"Profile: {planner.profile_name}")
    logger.info(f"Run ID: {run_id}")
    logger.info(f"Base dir: {base_dir}")

    print("Directory:", base_dir)

    plan_log_path, problem_hash = get_plan_log_path(
        abstract_problem_path,
        concrete_problem_path,
        run_directory,
    )

    initialize_plan_log(
        plan_log_path,
        problem_hash,
        abstract_problem_path,
        concrete_problem_path,
        abstract_symbol=abstract_symbol,
        concrete_objects=concrete_objects,
    )

    total_start = time.perf_counter()

    fd_start = time.perf_counter()

    # Fast Downward expects binary input streams.
    with (
        open(concrete_domain_path, "rb") as concrete_domain,
        open(concrete_problem_path, "rb") as concrete_problem,
        open(abstract_domain_path, "rb") as abstract_domain,
        open(abstract_problem_path, "rb") as abstract_problem,
    ):
        downward_result = run_fast_downward(
            base_dir=base_dir,
            domain_file=concrete_domain,
            problem_file=concrete_problem,
            abstract_domain_file=abstract_domain,
            abstract_problem_file=abstract_problem,
            task="translate",
        )

    concrete_task = downward_result["concrete"]
    abstract_task = downward_result["abstract"]
    fd_timings = downward_result["timings"]

    fd_time = time.perf_counter() - fd_start

    if horizon is None:
        horizon = abstract_task.get("horizon", 0)

    logger.info(f"Fast Downward time: {fd_time:.3f}s")

    concrete_lp_path = os.path.join(base_dir, "output_c.lp")
    abstract_lp_path = os.path.join(base_dir, "abstract", "output_a.lp")

    clingo_dir = os.path.join(base_dir, "clingo")
    os.makedirs(clingo_dir, exist_ok=True)

    occurrences_path = os.path.join(clingo_dir, "occurs_abs.lp")
    mapping_path = os.path.join(clingo_dir, "map.lp")
    forbidden_actions_path = os.path.join(clingo_dir, "forbid_abstract.lp")

    lp_start = time.perf_counter()

    concrete_lp_start = time.perf_counter()

    # Concrete LP
    generate_lp_with_plasp(
        sas_or_pddl_path=concrete_task["sasFile"],
        lp_output_path=concrete_lp_path,
        encoding_type=encoding,
        abstract_time_steps=time_step,
    )

    add_switch_to_lp_rule(concrete_lp_path, encoding)
    if append_concrete_pddl_facts:
        append_pddl_facts_to_lp(concrete_problem_path, concrete_lp_path)

    concrete_lp_time = time.perf_counter() - concrete_lp_start
    logger.info(f"Concrete LP generation: {concrete_lp_time:.3f}s")

    abstract_lp_time = 0.0

    # Abstract LP
    if plan_source == "clingo":
        abstract_lp_start = time.perf_counter()
        generate_lp_with_plasp(
            sas_or_pddl_path=abstract_task["sasFile"],
            lp_output_path=abstract_lp_path,
            encoding_type=encoding,
            abstract_time_steps=time_step,
        )

        abstract_lp_time = time.perf_counter() - abstract_lp_start
        logger.info(f"Abstract LP generation: {abstract_lp_time:.3f}s")

    lp_total_time = time.perf_counter() - lp_start
    logger.info(f"Total LP generation: {lp_total_time:.3f}s")

    if plan_source == "fd":
        logger.info("Using Fast Downward plan")

        occurrence_start = time.perf_counter()

        abstract_atoms = fast_downward_plan_to_abstract_atoms(
            abstract_task["planFile"],
            occurrences_path,
        )

        occurrence_time = log_phase(
            logger,
            "Abstract occurrences from Fast Downward",
            occurrence_start,
        )

        iter_start = time.perf_counter()
        iteration_times = []

        switch_map, mapping_time = _build_mapping(
            planner,
            occurrences_path,
            mapping_path,
            abstract_symbol,
            concrete_objects,
            logger,
        )

        success, plans, bad_abstract_actions, concrete_solve_time = _solve_concrete(
            solving_mode,
            [concrete_lp_path, occurrences_path, mapping_path],
            horizon,
            switch_map,
            logger,
        )

        if success:
            logger.info("SUCCESS: Concrete plan found.")
            logger.info("Plans:")
            logger.info(pformat(plans))

            iteration_time = time.perf_counter() - iter_start
            total_time = time.perf_counter() - total_start

            record_plan_attempt(
                plan_log_path,
                abstract_atoms,
                success=True,
                bad_actions=[],
                mode=solving_mode,
            )

            iteration_times.append(
                _iteration_timing(
                    0,
                    occurrence_time,
                    mapping_time,
                    concrete_solve_time,
                    0.0,
                    iteration_time,
                )
            )

            _log_iteration_totals(logger, iteration_times)

            logger.info(f"TOTAL TIME: {total_time:.3f}s")

            return _build_result(
                horizon=horizon,
                success=True,
                plans=plans,
                iteration_times=iteration_times,
                fd_timings=fd_timings,
                concrete_lp_time=concrete_lp_time,
                abstract_lp_time=0.0,
                lp_total_time=lp_total_time,
                abstract_solve_time=0.0,
                concrete_solve_time=concrete_solve_time,
                total_time=total_time,
                run_id=base_dir,
            )

        logger.info("Concrete solve failed.")
        _log_atoms(logger, "Bad abstract actions:", bad_abstract_actions)

        _log_iteration_totals(logger, iteration_times)

        logger.info("No abstract plan possible.")
        logger.info("FAILED")

        total_time = time.perf_counter() - total_start
        logger.info(f"TOTAL TIME: {total_time:.3f}s")

        record_plan_attempt(
            plan_log_path,
            abstract_atoms,
            success=False,
            bad_actions=bad_abstract_actions,
            mode=solving_mode,
        )

        return _build_result(
            horizon=horizon,
            success=False,
            plans=[],
            iteration_times=iteration_times,
            fd_timings=fd_timings,
            concrete_lp_time=concrete_lp_time,
            abstract_lp_time=0.0,
            lp_total_time=lp_total_time,
            abstract_solve_time=0.0,
            concrete_solve_time=concrete_solve_time,
            total_time=total_time,
            run_id=base_dir,
        )

    iteration = 0
    forbidden_actions = []
    iteration_times = []

    while True:
        iteration += 1
        iter_start = time.perf_counter()

        logger.info("")
        logger.info("=" * 50)
        logger.info(f"ITERATION {iteration}")
        logger.info("=" * 50)

        # Solve abstract plan
        abstract_solve_start = time.perf_counter()

        abstract_lp_files = [abstract_lp_path]

        if forbidden_actions:
            write_forbidden_actions(forbidden_actions, forbidden_actions_path)
            abstract_lp_files.append(forbidden_actions_path)

            save_iteration_file(
                debug_dir,
                iteration,
                "forbidden.lp",
                "\n".join(forbidden_actions),
            )

        abstract_models = run_clingo(abstract_lp_files, horizon)

        abstract_solve_time = log_phase(
            logger,
            "Abstract solving time",
            abstract_solve_start,
        )

        if not abstract_models:
            logger.info("No abstract plan possible.")
            logger.info("FAILED")

            total_time = time.perf_counter() - total_start
            logger.info(f"TOTAL TIME: {total_time:.3f}s")

            return _build_result(
                horizon=horizon,
                success=False,
                plans=[],
                iteration_times=iteration_times,
                fd_timings=fd_timings,
                concrete_lp_time=concrete_lp_time,
                abstract_lp_time=abstract_lp_time,
                lp_total_time=lp_total_time,
                abstract_solve_time=abstract_solve_time,
                concrete_solve_time=0.0,
                total_time=total_time,
                run_id=base_dir,
            )

        abstract_atoms = abstract_models[0]

        _log_atoms(logger, "Abstract plan:", abstract_atoms)

        occurrence_start = time.perf_counter()

        write_abstract_occurrences(abstract_atoms, occurrences_path)

        occurrence_time = log_phase(
            logger,
            "Abstract occurrence generation time",
            occurrence_start,
        )

        copy_iteration_file(
            debug_dir,
            iteration,
            occurrences_path,
        )

        switch_map, mapping_time = _build_mapping(
            planner,
            occurrences_path,
            mapping_path,
            abstract_symbol,
            concrete_objects,
            logger,
        )

        copy_iteration_file(
            debug_dir,
            iteration,
            mapping_path,
        )

        success, plans, bad_abstract_actions, concrete_solve_time = _solve_concrete(
            solving_mode,
            [concrete_lp_path, occurrences_path, mapping_path],
            horizon,
            switch_map,
            logger,
        )

        if success:
            logger.info("SUCCESS: Concrete plan found.")
            logger.info("Plans:")
            logger.info(pformat(plans))

            save_json_iteration_file(
                debug_dir,
                iteration,
                "concrete_plans.json",
                plans,
            )

            iteration_time = time.perf_counter() - iter_start
            total_time = time.perf_counter() - total_start

            record_plan_attempt(
                plan_log_path,
                abstract_atoms,
                success=True,
                bad_actions=[],
                mode=solving_mode,
            )

            iteration_times.append(
                _iteration_timing(
                    abstract_solve_time,
                    occurrence_time,
                    mapping_time,
                    concrete_solve_time,
                    0.0,
                    iteration_time,
                )
            )

            _log_iteration_totals(logger, iteration_times)

            logger.info(f"TOTAL TIME: {total_time:.3f}s")

            return _build_result(
                horizon=horizon,
                success=True,
                plans=plans,
                iteration_times=iteration_times,
                fd_timings=fd_timings,
                concrete_lp_time=concrete_lp_time,
                abstract_lp_time=abstract_lp_time,
                lp_total_time=lp_total_time,
                abstract_solve_time=abstract_solve_time,
                concrete_solve_time=concrete_solve_time,
                total_time=total_time,
                run_id=base_dir,
            )

        # Refine abstraction: only forbid actions with the abstract symbol
        refinement_start = time.perf_counter()

        logger.info("Concrete solve failed.")
        _log_atoms(logger, "Bad abstract actions:", bad_abstract_actions)

        save_iteration_file(
            debug_dir,
            iteration,
            "bad_actions.lp",
            "\n".join(bad_abstract_actions),
        )

        new_forbidden = _add_new_forbidden_actions(
            forbidden_actions,
            bad_abstract_actions,
            refinement_filter,
        )
        _log_atoms(logger, "New forbidden atoms:", new_forbidden)

        save_iteration_file(
            debug_dir,
            iteration,
            "new_forbidden.lp",
            "\n".join(new_forbidden),
        )

        refinement_time = log_phase(logger, "Refinement time", refinement_start)

        iteration_time = time.perf_counter() - iter_start

        iteration_times.append(
            _iteration_timing(
                abstract_solve_time,
                occurrence_time,
                mapping_time,
                concrete_solve_time,
                refinement_time,
                iteration_time,
            )
        )

        logger.info(
            f"ITER {iteration} SUMMARY | "
            f"abs={abstract_solve_time:.3f}s | "
            f"occ={occurrence_time:.3f}s | "
            f"map={mapping_time:.3f}s | "
            f"conc={concrete_solve_time:.3f}s | "
            f"ref={refinement_time:.3f}s | "
            f"forbidden={len(forbidden_actions)} | "
            f"iter={iteration_time:.3f}s"
        )

        record_plan_attempt(
            plan_log_path,
            abstract_atoms,
            success=False,
            bad_actions=bad_abstract_actions,
            mode=solving_mode,
        )


if __name__ == "__main__":
    main()
