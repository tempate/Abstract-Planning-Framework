import os
import clingo


def run_clingo(lp_files, horizon):
    models = []

    # Equivalent to CLI: clingo files -c horizon=X
    ctl = clingo.Control(["-c", f"horizon={horizon}"])

    # Load all input files
    for lp in lp_files:
        ctl.load(lp)

    # Ground base program
    ctl.ground([("base", [])])

    # Solve and collect models (same behavior as parsing stdout)
    with ctl.solve(yield_=True) as handle:
        for model in handle:
            atoms = [str(symbol) for symbol in model.symbols(shown=True)]
            models.append(atoms)

    return models


def write_occurs_abs_lp(atoms, output_path):
    lines = []

    for atom in atoms:
        atom = atom.strip()

        if atom.startswith("occurs("):
            # occurs(action(...),T) → occurs_abstract(action(...),T)
            lines.append("occurs_abstract" + atom[len("occurs"):] + ".")

        elif atom.startswith("occurs_abstract("):
            # already abstract (defensive)
            lines.append(atom + ".")

    with open(output_path, "w") as f:
        f.write("\n".join(lines))


def create_map_lp(occurs_abs_path, output_path, abstract_symbol, concrete_objects):
    # Example: concrete_objects = ["hangar1", "hangar2"]

    with open(occurs_abs_path, "r") as f:
        lines_in = [line.strip() for line in f if line.strip()]

    lines_out = []

    for line in lines_in:
        if not line.startswith("occurs_abstract("):
            continue

        # Extract inner part: occurs_abstract(inner)
        inner = line[len("occurs_abstract("):].rstrip(").")

        # Split into action_term and time by last comma
        if ',' not in inner:
            continue

        action_str, time_str = inner.rsplit(",", 1)
        action_str = action_str.strip()
        time_str = time_str.strip()

        # Case 1: action contains abstract symbol → choice rule
        if abstract_symbol in action_str:
            choices = []
            for obj in concrete_objects:
                new_action = action_str.replace(abstract_symbol, obj)
                choices.append(f"occurs({new_action}, {time_str})")

            lines_out.append(
                f"1 {{ {'; '.join(choices)} }} 1 :- "
                f"occurs_abstract({action_str},{time_str})."
            )

        # Case 2: no abstraction → direct mapping
        else:
            lines_out.append(
                f"occurs({action_str},{time_str}) :- "
                f"occurs_abstract({action_str},{time_str})."
            )

    # Write map.lp
    with open(output_path, "w") as f:
        f.write("\n".join(lines_out))

def create_map_lp_with_switch_atoms(occurs_abs_path, output_path, abstract_symbol, concrete_objects):
    with open(occurs_abs_path, "r") as f:
        lines_in = [line.strip() for line in f if line.strip()]

    lines_out = []
    switch_id = 0
    switch_map = {}  # switch_id -> abstract action

    for line in lines_in:
        if not line.startswith("occurs_abstract("):
            continue

        inner = line[len("occurs_abstract("):].rstrip(").")

        if ',' not in inner:
            continue

        action_str, time_str = inner.rsplit(",", 1)
        action_str = action_str.strip()
        time_str = time_str.strip()

        switch_atom = f"switch({switch_id})"

        # choice over switches
        lines_out.append(f"0 {{ {switch_atom} }} 1.")

        if abstract_symbol in action_str:
            choices = []
            for obj in concrete_objects:
                new_action = action_str.replace(abstract_symbol, obj)
                choices.append(f"occurs({new_action}, {time_str})")

            lines_out.append(
                f"1 {{ {'; '.join(choices)} }} 1 :- "
                f"occurs_abstract({action_str},{time_str}), {switch_atom}."
            )
        else:
            lines_out.append(
                f"occurs({action_str},{time_str}) :- "
                f"occurs_abstract({action_str},{time_str}), {switch_atom}."
            )

        switch_map[switch_id] = f"occurs_abstract({action_str},{time_str})"
        switch_id += 1

    with open(output_path, "w") as f:
        f.write("\n".join(lines_out))

    return switch_map

def solve_concrete_incremental(lp_files, horizon, switch_map):
    ctl = clingo.Control(["-c", f"horizon={horizon}"])

    for lp in lp_files:
        ctl.load(lp)

    ctl.ground([("base", [])])

    switch_symbols = []
    symbol_to_switch = {}

    for atom in ctl.symbolic_atoms:
        if atom.symbol.name == "switch":
            switch_symbols.append(atom.symbol)
            symbol_to_switch[atom.symbol] = atom.symbol.arguments[0].number

    print(f"[DEBUG] Found {len(switch_symbols)} switches")

    active_switches = []

    for sym in switch_symbols:
        active_switches.append(sym)

        assumptions = []

        # active = true
        for s in active_switches:
            assumptions.append((s, True))

        # inactive = false
        for s in switch_symbols:
            if s not in active_switches:
                assumptions.append((s, False))

        result = ctl.solve(assumptions=assumptions)

        if result.unsatisfiable:
            switch_id = symbol_to_switch[sym]
            print("Conflict at switch:", switch_id)
            print("Abstract action:", switch_map[switch_id])
            return False, []

    # SAT → collect models
    plans = []

    assumptions = [(s, True) for s in switch_symbols]

    with ctl.solve(yield_=True, assumptions=assumptions) as handle:
        for model in handle:
            atoms = [str(a) for a in model.symbols(shown=True)]
            plans.append(atoms)

    return True, plans