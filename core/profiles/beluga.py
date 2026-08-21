from core.asp import parse_abstract_actions
from core.profiles.base import PlanningProfile


class BelugaProfile(PlanningProfile):
    """Beluga's object-substitution abstraction mapping."""

    profile_name = "beluga"
    run_directory = "beluga"
    requires_mapping_arguments = True

    def build_mapping(self, occurrences, abstract_name, objects):
        abstract_actions = parse_abstract_actions(occurrences)

        mapping_rules = []
        switch_map = {}
        for abstract_action, time_step in abstract_actions:
            switch_id = time_step
            switch = f"switch({switch_id})"
            mapping_rules.append(f"0 {{ {switch} }} 1.")
            is_abstract = bool(abstract_name and abstract_name in abstract_action)
            if is_abstract:
                choices = [
                    f"occurs({abstract_action.replace(abstract_name, concrete_object)}, {time_step})"
                    for concrete_object in objects or []
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
        return self._build_mapping(mapping_rules, switch_map, "beluga")
