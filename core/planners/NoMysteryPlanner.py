import re

from core.asp import read_abstract_actions
from core.planners.BasePlanner import BasePlanner


class NoMysteryPlanner(BasePlanner):
    """NoMystery's fuel-aware mapping and drive-action refinement."""

    profile_name = "no_mystery"
    run_directory = "noMystery"
    append_concrete_pddl_facts = True

    def build_mapping(self, occurs_path, map_path, abstract_symbol, concrete_objects):
        abstract_actions = read_abstract_actions(occurs_path)

        mapping_rules = []
        switch_map = {}
        for abstract_action, time_step in abstract_actions:
            switch_id = time_step
            switch = f"switch({switch_id})"
            mapping_rules.append(f"0 {{ {switch} }} 1.")
            if '"drive"' in abstract_action:
                match = re.search(r"action\(\((.*)\)\)", abstract_action)
                if not match:
                    raise ValueError(f"Cannot parse action: {abstract_action}")
                arguments = [item.strip().strip('"') for item in match.group(1).split(",")]
                if arguments[0] != "drive":
                    raise ValueError(f"Unexpected action: {arguments}")
                truck, origin, destination = arguments[1:4]
                mapping_rules.append(f"""1 {{
    occurs(action(("drive","{truck}","{origin}","{destination}",Post,Diff,Pre)),{time_step}) :
        fuelcost(Diff,"{origin}","{destination}"),
        sum(Post,Diff,Pre)
}} 1 :-
    occurs_abstract({abstract_action},{time_step}), {switch}.""")
                is_abstract = True
            elif abstract_symbol and abstract_symbol in abstract_action:
                choices = [
                    f"occurs({abstract_action.replace(abstract_symbol, concrete_object)}, {time_step})"
                    for concrete_object in concrete_objects or []
                ]
                mapping_rules.append(
                    f"1 {{ {'; '.join(choices)} }} 1 :- occurs_abstract({abstract_action},{time_step}), {switch}."
                )
                is_abstract = True
            else:
                mapping_rules.append(
                    f"occurs({abstract_action},{time_step}) :- "
                    f"occurs_abstract({abstract_action},{time_step}), {switch}."
                )
                is_abstract = False
            switch_map[switch_id] = {
                "atom": f"occurs_abstract({abstract_action},{time_step})",
                "is_abstract": is_abstract,
            }
        return self._write_mapping(map_path, mapping_rules, switch_map, "no_mystery")
