"""Stateful strategies for realizing abstract plans concretely."""

from core.planning.refinement.base import PlanningPaths, RefinementContext
from core.planning.refinement.clingo import ClingoRefinement
from core.planning.refinement.fast_downward import FastDownwardRefinement


REFINEMENT_STRATEGIES = {
    "clingo": ClingoRefinement,
    "fd": FastDownwardRefinement,
}


def get_refinement_strategy(plan_source, context):
    """Construct the refinement strategy selected by its plan source."""
    try:
        strategy = REFINEMENT_STRATEGIES[plan_source]
    except KeyError as error:
        valid_sources = ", ".join(REFINEMENT_STRATEGIES)
        raise ValueError(
            f"Unknown plan source: {plan_source}. Choose one of: {valid_sources}"
        ) from error
    return strategy(context)


__all__ = [
    "ClingoRefinement",
    "FastDownwardRefinement",
    "PlanningPaths",
    "RefinementContext",
    "get_refinement_strategy",
]
