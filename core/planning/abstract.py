"""Prepare and dispatch abstraction-based planning workflows."""

import os

from core.execution import create_run_dir, setup_debug_logger, timed_phase
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

    logger.info("=" * 70)
    logger.info("NEW PLANNING RUN STARTED")
    logger.info(f"Horizon: {horizon}")
    logger.info(f"Encoding: {encoding}")
    logger.info(f"Mode: {solving_mode}")
    logger.info(f"Profile: {profile_name}")
    logger.info(f"Run ID: {run_id}")
    logger.info(f"Base dir: {base_dir}")

    print("Directory:", base_dir)
    with timed_phase() as total_timing:
        # Translate the concrete problem into SAS and plan the abstract problem.
        with timed_phase(logger, "Fast Downward time") as fd_total:
            with (
                open(concrete_domain_path, "rb") as concrete_domain,
                open(concrete_problem_path, "rb") as concrete_problem,
            ):
                concrete_task, concrete_time = run_fast_downward(
                    base_dir,
                    concrete_domain,
                    concrete_problem,
                    "concrete",
                    "translate",
                )

            with (
                open(abstract_domain_path, "rb") as abstract_domain,
                open(abstract_problem_path, "rb") as abstract_problem,
            ):
                abstract_task, abstract_time = run_fast_downward(
                    base_dir,
                    abstract_domain,
                    abstract_problem,
                    "abstract",
                    "plan",
                )

        fd_timings = {
            "fd_concrete_time": concrete_time,
            "fd_abstract_time": abstract_time,
            "fd_total_time": fd_total.elapsed,
        }

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
            total_timing=total_timing,
            base_dir=base_dir,
            debug_dir=debug_dir,
            logger=logger,
            attempt_recorder=attempt_recorder,
        )
        return get_refinement_strategy(plan_source, context).refine()


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
    with timed_phase(logger, "Total LP generation") as total_timing:
        with timed_phase(logger, "Concrete LP generation") as concrete_timing:
            generate_lp_with_plasp(
                sas_or_pddl_path=concrete_task["sasFile"],
                lp_output_path=paths.concrete_lp,
                encoding_type=encoding,
                abstract_time_steps=time_step,
            )
            add_switch_to_lp_rule(paths.concrete_lp, encoding)
            if append_concrete_pddl_facts:
                append_pddl_facts_to_lp(concrete_problem_path, paths.concrete_lp)

        abstract_time = 0.0
        if plan_source == "clingo":
            with timed_phase(
                logger, "Abstract LP generation"
            ) as abstract_timing:
                generate_lp_with_plasp(
                    sas_or_pddl_path=abstract_task["sasFile"],
                    lp_output_path=paths.abstract_lp,
                    encoding_type=encoding,
                    abstract_time_steps=time_step,
                )
            abstract_time = abstract_timing.elapsed

    return concrete_timing.elapsed, abstract_time, total_timing.elapsed
