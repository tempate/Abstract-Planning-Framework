"""No-Mystery specialization of the shared Clingo solver helpers."""

import re
import time

from core.asp.mapping import read_abstract_actions, write_lp_lines
from core.runtime.run_artifacts import get_logger, log_phase


def build_no_mystery_switch_mapping(
    occurs_abs_path, output_path, abstract_symbol, concrete_objects
):
    """Create mapping rules, expanding No-Mystery drive actions by fuel cost."""
    logger = get_logger()
    start = time.perf_counter()

    lines = []
    switch_map = {}
    for switch_id, (action, time_step) in enumerate(read_abstract_actions(occurs_abs_path), start=1):
        switch = f"switch({switch_id})"
        lines.append(f"0 {{ {switch} }} 1.")

        if '"drive"' in action:
            match = re.search(r'action\(\((.*)\)\)', action)
            if not match:
                raise ValueError(f"Cannot parse action: {action}")
            arguments = [item.strip().strip('"') for item in match.group(1).split(",")]
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
    write_lp_lines(output_path, lines)

    logger.info(f"[MAP] Switches created={len(switch_map)}")
    logger.info(f"[FILES] wrote {output_path}")
    logger.info("[MAP] Grounded plan:")
    for line in lines:
        logger.info(f"  {line}")
    log_phase(logger, "[MAP] build_no_mystery_switch_mapping", start)
    return switch_map
