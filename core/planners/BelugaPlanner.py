from core.asp import read_abstract_actions
from core.planners.BasePlanner import BasePlanner


class BelugaPlanner(BasePlanner):
    """Beluga's object-substitution abstraction mapping."""

    profile_name = "beluga"
    run_directory = "beluga"
    requires_mapping_arguments = True

    def build_mapping(self, occurs_path, map_path, abstract_symbol, concrete_objects):
        abstract_actions = read_abstract_actions(occurs_path)

        mapping_rules = []
        switch_map = {}
        for abstract_action, time_step in abstract_actions:
            switch_id = time_step
            switch = f"switch({switch_id})"
            mapping_rules.append(f"0 {{ {switch} }} 1.")
            is_abstract = bool(abstract_symbol and abstract_symbol in abstract_action)
            if is_abstract:
                choices = [
                    f"occurs({abstract_action.replace(abstract_symbol, concrete_object)}, {time_step})"
                    for concrete_object in concrete_objects or []
                ]
                mapping_rules.append(
                    f"1 {{ {'; '.join(choices)} }} 1 :- occurs_abstract({abstract_action},{time_step}), {switch}."
                )
            else:
                mapping_rules.append(
                    f"occurs({abstract_action},{time_step}) :- "
                    f"occurs_abstract({abstract_action},{time_step}), {switch}."
                )
            switch_map[switch_id] = {
                "atom": f"occurs_abstract({abstract_action},{time_step})",
                "is_abstract": is_abstract,
            }
        return self._write_mapping(map_path, mapping_rules, switch_map, "beluga")
