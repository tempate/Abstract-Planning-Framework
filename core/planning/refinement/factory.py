from core.planning.refinement.clingo import ClingoRefinement
from core.planning.refinement.fast_downward import FastDownwardRefinement


def get_refinement_strategy(plan_source, context):
    if "clingo" == plan_source:
        return ClingoRefinement(context)
    elif "fd" == plan_source:
        return FastDownwardRefinement(context)
