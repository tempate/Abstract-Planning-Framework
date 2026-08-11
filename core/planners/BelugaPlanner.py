from core.asp import read_abstract_actions
from core.planners.AbstractPlanner import AbstractPlanner


class BelugaPlanner(AbstractPlanner):
    """Beluga's object-substitution abstraction mapping."""

    profile_name = "beluga"
    run_directory = "beluga"
    requires_mapping_arguments = True

    def build_mapping(
        self, occurs_path, map_path, abstract_symbol, concrete_objects
    ):
        lines = []
        switch_map = {}
        for switch_id, (action, time_step) in enumerate(
            read_abstract_actions(occurs_path), start=1
        ):
            switch = f"switch({switch_id})"
            lines.append(f"0 {{ {switch} }} 1.")
            is_abstract = bool(abstract_symbol and abstract_symbol in action)
            if is_abstract:
                choices = [
                    f"occurs({action.replace(abstract_symbol, obj)}, {time_step})"
                    for obj in concrete_objects or []
                ]
                lines.append(
                    f"1 {{ {'; '.join(choices)} }} 1 :- "
                    f"occurs_abstract({action},{time_step}), {switch}."
                )
            else:
                lines.append(
                    f"occurs({action},{time_step}) :- "
                    f"occurs_abstract({action},{time_step}), {switch}."
                )
            switch_map[switch_id] = {
                "atom": f"occurs_abstract({action},{time_step})",
                "is_abstract": is_abstract,
            }
        return self._write_mapping(map_path, lines, switch_map, "beluga")
