from core.asp import read_abstract_actions
from core.planners.AbstractPlanner import AbstractPlanner
import re


class NoMysteryPlanner(AbstractPlanner):
    """NoMystery's fuel-aware mapping and drive-action refinement."""

    profile_name = "no_mystery"
    run_directory = "noMystery"
    append_concrete_pddl_facts = True

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
            if '"drive"' in action:
                match = re.search(r'action\(\((.*)\)\)', action)
                if not match:
                    raise ValueError(f"Cannot parse action: {action}")
                arguments = [
                    item.strip().strip('"') for item in match.group(1).split(",")
                ]
                if arguments[0] != "drive":
                    raise ValueError(f"Unexpected action: {arguments}")
                truck, origin, destination = arguments[1:4]
                lines.append(
                    f'''1 {{
    occurs(action(("drive","{truck}","{origin}","{destination}",Post,Diff,Pre)),{time_step}) :
        fuelcost(Diff,"{origin}","{destination}"),
        sum(Post,Diff,Pre)
}} 1 :-
    occurs_abstract({action},{time_step}), {switch}.'''
                )
                is_abstract = True
            elif abstract_symbol and abstract_symbol in action:
                choices = [
                    f"occurs({action.replace(abstract_symbol, obj)}, {time_step})"
                    for obj in concrete_objects or []
                ]
                lines.append(
                    f"1 {{ {'; '.join(choices)} }} 1 :- "
                    f"occurs_abstract({action},{time_step}), {switch}."
                )
                is_abstract = True
            else:
                lines.append(
                    f"occurs({action},{time_step}) :- "
                    f"occurs_abstract({action},{time_step}), {switch}."
                )
                is_abstract = False
            switch_map[switch_id] = {
                "atom": f"occurs_abstract({action},{time_step})",
                "is_abstract": is_abstract,
            }
        return self._write_mapping(map_path, lines, switch_map, "no_mystery")

    def should_refine(self, atom, abstract_symbol):
        return super().should_refine(atom, abstract_symbol) or '"drive"' in atom
