from core.planning.refinement.ClingoRefinement import ClingoRefinement
from core.planning.refinement.FastDownwardRefinement import FastDownwardRefinement


def get_refinement_strategy(plan_source, context):
    if "clingo" == plan_source:
        return ClingoRefinement(context)
    elif "fd" == plan_source:
        return FastDownwardRefinement(context)
