"""Prepare and dispatch abstraction-based planning workflows."""

import os
import time

from core.execution import create_run_dir, setup_debug_logger
from core.integrations.fast_downward import run_fast_downward
from core.integrations.plasp import (
    add_switch_to_lp_rule,
    append_pddl_facts_to_lp,
    generate_lp_with_plasp,
)
from core.planning.refinement import (
    PlanningPaths,
    RefinementContext,
    get_refinement_strategy,
)
from core.planners.factory import get_planner


def refine_abstract_plan(
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
    attempt_recorder=None,
):
    """Prepare an abstract planning run and dispatch its refinement strategy."""
    planner = get_planner(profile_name)
    planner.validate_configuration(abstract_symbol, concrete_objects)
    if refinement_filter is None:
        refinement_filter = lambda atom: planner.should_refine(atom, abstract_symbol)

    base_dir, run_id = create_run_dir(planner.run_directory)
    logger, debug_dir = setup_debug_logger(base_dir)
    _log_run_start(
        logger,
        horizon=horizon,
        encoding=encoding,
        solving_mode=solving_mode,
        profile_name=planner.profile_name,
        run_id=run_id,
        base_dir=base_dir,
    )

    print("Directory:", base_dir)
    total_start = time.perf_counter()

    concrete_task, abstract_task, fd_timings = _translate_tasks(
        base_dir,
        concrete_domain_path,
        concrete_problem_path,
        abstract_domain_path,
        abstract_problem_path,
        logger,
    )
    if horizon is None:
        horizon = abstract_task.get("horizon", 0)

    paths = _planning_paths(base_dir)
    concrete_lp_time, abstract_lp_time, lp_total_time = _generate_lp_programs(
        concrete_task=concrete_task,
        abstract_task=abstract_task,
        concrete_problem_path=concrete_problem_path,
        paths=paths,
        encoding=encoding,
        time_step=time_step,
        plan_source=plan_source,
        append_concrete_pddl_facts=planner.append_concrete_pddl_facts,
        logger=logger,
    )

    context = RefinementContext(
        planner=planner,
        paths=paths,
        abstract_task=abstract_task,
        horizon=horizon,
        abstract_symbol=abstract_symbol,
        concrete_objects=concrete_objects,
        solving_mode=solving_mode,
        refinement_filter=refinement_filter,
        fd_timings=fd_timings,
        concrete_lp_time=concrete_lp_time,
        abstract_lp_time=abstract_lp_time,
        lp_total_time=lp_total_time,
        total_start=total_start,
        base_dir=base_dir,
        debug_dir=debug_dir,
        logger=logger,
        attempt_recorder=attempt_recorder,
    )
    return get_refinement_strategy(plan_source, context).refine()


def _translate_tasks(
    base_dir,
    concrete_domain_path,
    concrete_problem_path,
    abstract_domain_path,
    abstract_problem_path,
    logger,
):
    start = time.perf_counter()
    with (
        open(concrete_domain_path, "rb") as concrete_domain,
        open(concrete_problem_path, "rb") as concrete_problem,
        open(abstract_domain_path, "rb") as abstract_domain,
        open(abstract_problem_path, "rb") as abstract_problem,
    ):
        result = run_fast_downward(
            base_dir=base_dir,
            domain_file=concrete_domain,
            problem_file=concrete_problem,
            abstract_domain_file=abstract_domain,
            abstract_problem_file=abstract_problem,
            task="translate",
        )

    logger.info(f"Fast Downward time: {time.perf_counter() - start:.3f}s")
    return result["concrete"], result["abstract"], result["timings"]


def _planning_paths(base_dir):
    clingo_dir = os.path.join(base_dir, "clingo")
    os.makedirs(clingo_dir, exist_ok=True)
    return PlanningPaths(
        concrete_lp=os.path.join(base_dir, "output_c.lp"),
        abstract_lp=os.path.join(base_dir, "abstract", "output_a.lp"),
        occurrences=os.path.join(clingo_dir, "occurs_abs.lp"),
        mapping=os.path.join(clingo_dir, "map.lp"),
        forbidden_actions=os.path.join(clingo_dir, "forbid_abstract.lp"),
    )


def _generate_lp_programs(
    *,
    concrete_task,
    abstract_task,
    concrete_problem_path,
    paths,
    encoding,
    time_step,
    plan_source,
    append_concrete_pddl_facts,
    logger,
):
    total_start = time.perf_counter()

    concrete_start = time.perf_counter()
    generate_lp_with_plasp(
        sas_or_pddl_path=concrete_task["sasFile"],
        lp_output_path=paths.concrete_lp,
        encoding_type=encoding,
        abstract_time_steps=time_step,
    )
    add_switch_to_lp_rule(paths.concrete_lp, encoding)
    if append_concrete_pddl_facts:
        append_pddl_facts_to_lp(concrete_problem_path, paths.concrete_lp)
    concrete_time = time.perf_counter() - concrete_start
    logger.info(f"Concrete LP generation: {concrete_time:.3f}s")

    abstract_time = 0.0
    if plan_source == "clingo":
        abstract_start = time.perf_counter()
        generate_lp_with_plasp(
            sas_or_pddl_path=abstract_task["sasFile"],
            lp_output_path=paths.abstract_lp,
            encoding_type=encoding,
            abstract_time_steps=time_step,
        )
        abstract_time = time.perf_counter() - abstract_start
        logger.info(f"Abstract LP generation: {abstract_time:.3f}s")

    total_time = time.perf_counter() - total_start
    logger.info(f"Total LP generation: {total_time:.3f}s")
    return concrete_time, abstract_time, total_time


def _log_run_start(
    logger,
    *,
    horizon,
    encoding,
    solving_mode,
    profile_name,
    run_id,
    base_dir,
):
    logger.info("=" * 70)
    logger.info("NEW PLANNING RUN STARTED")
    logger.info(f"Horizon: {horizon}")
    logger.info(f"Encoding: {encoding}")
    logger.info(f"Mode: {solving_mode}")
    logger.info(f"Profile: {profile_name}")
    logger.info(f"Run ID: {run_id}")
    logger.info(f"Base dir: {base_dir}")
