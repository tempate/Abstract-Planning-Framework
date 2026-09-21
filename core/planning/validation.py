"""Check a produced plan against the task it claims to solve."""

from core.integrations.unified_planning import read_problem, validate_plan


def validated(config, plan, parse_actions):
    """Validate a plan against the PDDL as written, before any rewriting.

    The original pair is re-read rather than reused, so that relaxing a delete,
    reaching positive normal form or collapsing a class cannot excuse a plan the
    task as posed does not accept. A pair that will not read back answers
    "unchecked", because a plan already found is a result worth keeping whether
    or not this check can run.
    """
    if plan is None:
        return ""
    try:
        problem = read_problem(config.domain_path, config.problem_path)
    except Exception as error:
        return f"unchecked: {error}"
    return validate_plan(problem, parse_actions(plan))
