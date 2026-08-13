"""Prepare and dispatch abstraction-based planning workflows."""

import os

from core.execution import create_run_dir, setup_debug_logger, timed_phase
from core.integrations.fast_downward import run_fast_downward
from core.integrations.plasp import (
    add_switch_to_asp_rule,
    append_pddl_facts_to_asp,
    plan_to_asp,
)
from core.planning.refinement.BaseRefinement import PlanningPaths, RefinementContext
from core.planning.refinement.factory import get_refinement_strategy
from core.planners.factory import get_planner


def compute_abstract_plan(
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
    attempt_recorder=None,
):
    """Prepare an abstract planning run and dispatch its refinement strategy."""
    planner = get_planner(profile_name)
    planner.validate_configuration(abstract_symbol, concrete_objects)

    refinement_filter = lambda atom: planner.should_refine(atom, abstract_symbol)

    base_dir, run_id = create_run_dir(planner.run_directory)
    logger, debug_dir = setup_debug_logger(base_dir)

    logger.info("=" * 70)
    logger.info("NEW PLANNING RUN STARTED")
    logger.info(f"Requested horizon: {horizon if horizon is not None else 'auto'}")
    logger.info(f"Encoding: {encoding}")
    logger.info(f"Mode: {solving_mode}")
    logger.info(f"Profile: {profile_name}")
    logger.info(f"Run ID: {run_id}")
    logger.info(f"Base dir: {base_dir}")

    print("Directory:", base_dir)

    with timed_phase() as run_timing:
        with timed_phase(logger, "Fast Downward time") as fd_total:
            # Translate the concrete problem into SAS.
            with (open(concrete_domain_path, "rb") as domain,
                  open(concrete_problem_path, "rb") as problem):
                concrete_task, concrete_time = run_fast_downward(
                    os.path.join(base_dir, "concrete"),
                    domain.read(), problem.read(), "concrete", "translate"
                )

            # Plan the abstract problem.
            with (open(abstract_domain_path, "rb") as domain,
                  open(abstract_problem_path, "rb") as problem):
                abstract_task, abstract_time = run_fast_downward(
                    os.path.join(base_dir, "abstract"),
                    domain.read(), problem.read(), "abstract", "plan",
                )

        fd_timings = {
            "fd_concrete_time": concrete_time,
            "fd_abstract_time": abstract_time,
            "fd_total_time": fd_total.elapsed,
        }

        horizon = _select_abstract_horizon(
            horizon,
            abstract_task.get("horizon", 0),
            plan_source,
        )
        logger.info(f"Effective horizon: {horizon}")

        paths = _get_planning_paths(base_dir)

        with timed_phase(logger, "Total ASP generation") as asp_total_timing:

            # Generate the ASP representation of the concrete problem.
            with timed_phase(logger, "Concrete ASP generation") as concrete_timing:
                plan_to_asp(
                    concrete_task["sasFile"], paths.concrete_asp, encoding, time_step
                )

                add_switch_to_asp_rule(paths.concrete_asp, encoding)
                if planner.append_concrete_pddl_facts:
                    append_pddl_facts_to_asp(concrete_problem_path, paths.concrete_asp)

            # Generate the ASP representation of the abstract problem.
            abstract_time = 0.0
            if plan_source == "clingo":
                with timed_phase(logger, "Abstract ASP generation") as abstract_timing:
                    plan_to_asp(
                        abstract_task["sasFile"], paths.abstract_asp, encoding, time_step
                    )
                abstract_time = abstract_timing.elapsed

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
            concrete_asp_time=concrete_timing.elapsed,
            abstract_asp_time=abstract_time,
            asp_total_time=asp_total_timing.elapsed,
            total_timing=run_timing,
            base_dir=base_dir,
            debug_dir=debug_dir,
            logger=logger,
            attempt_recorder=attempt_recorder,
        )
        return get_refinement_strategy(plan_source, context).refine()


def _get_planning_paths(base_dir):
    dir = os.path.join(base_dir, "clingo")

    # Create the directory for the task if it doesn't exist
    os.makedirs(dir, exist_ok=True)

    # Define the paths for the input and output files
    return PlanningPaths(
        concrete_asp=os.path.join(base_dir, "output_c.lp"),
        abstract_asp=os.path.join(base_dir, "abstract", "output_a.lp"),
        occurrences=os.path.join(dir, "occurs_abs.lp"),
        mapping=os.path.join(dir, "map.lp"),
        forbidden_actions=os.path.join(dir, "forbid_abstract.lp"),
    )


def _select_abstract_horizon(requested_horizon, plan_horizon, plan_source):
    """Select a horizon that can contain a Fast Downward-sourced plan."""
    if requested_horizon is None:
        return plan_horizon
    if plan_source == "fd" and requested_horizon < plan_horizon:
        raise ValueError(
            f"Fast Downward plan length {plan_horizon} exceeds "
            f"the explicit horizon {requested_horizon}"
        )
    return requested_horizon
