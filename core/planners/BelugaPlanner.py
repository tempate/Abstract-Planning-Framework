from core.asp import read_abstract_actions
from core.planners.BasePlanner import BasePlanner


class BelugaPlanner(BasePlanner):
    """Beluga's object-substitution abstraction mapping."""

    profile_name = "beluga"
    run_directory = "beluga"
    requires_mapping_arguments = True

    def build_mapping(
        self, occurs_path, map_path, abstract_symbol, concrete_objects
    ):
        actions = read_abstract_actions(occurs_path)

        lines = []
        switch_map = {}
        for action, time in actions:
            switch_id = time
            switch = f"switch({switch_id})"
            lines.append(f"0 {{ {switch} }} 1.")
            is_abstract = bool(abstract_symbol and abstract_symbol in action)
            if is_abstract:
                choices = [
                    f"occurs({action.replace(abstract_symbol, obj)}, {time})"
                    for obj in concrete_objects or []
                ]
                lines.append(
                    f"1 {{ {'; '.join(choices)} }} 1 :- "
                    f"occurs_abstract({action},{time}), {switch}."
                )
            else:
                lines.append(
                    f"occurs({action},{time}) :- "
                    f"occurs_abstract({action},{time}), {switch}."
                )
            switch_map[switch_id] = {
                "atom": f"occurs_abstract({action},{time})",
                "is_abstract": is_abstract,
            }
        return self._write_mapping(map_path, lines, switch_map, "beluga")
