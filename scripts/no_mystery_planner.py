"""No-Mystery planner using the shared abstraction workflow."""

from .abstract_planner import compute_concrete_from_abstract as _compute
from .abstract_planner import main as _main
from core.asp.no_mystery import build_no_mystery_switch_mapping


def _no_mystery_options(abstract_symbol=None):
    options = {
        "run_directory": "noMystery",
        "append_concrete_pddl_facts": True,
        "map_builder": build_no_mystery_switch_mapping,
    }
    if abstract_symbol is not None:
        options["refinement_filter"] = lambda atom: (
            bool(abstract_symbol and abstract_symbol in atom) or '"drive"' in atom
        )
    return options


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
):
    return _compute(
        abstract_domain_path,
        abstract_problem_path,
        concrete_domain_path,
        concrete_problem_path,
        horizon=horizon,
        encoding=encoding,
        time_step=time_step,
        abstract_symbol=abstract_symbol,
        concrete_objects=concrete_objects,
        solving_mode=solving_mode,
        plan_source=plan_source,
        **_no_mystery_options(abstract_symbol),
    )


def main():
    _main(
        mapping_required=False,
        **_no_mystery_options(),
        include_drive_refinements=True,
    )


if __name__ == "__main__":
    main()
