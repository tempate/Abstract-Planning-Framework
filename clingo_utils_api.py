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

         # store as dict
        switch_map[switch_id] = {
            "atom": f"occurs_abstract({action_str},{time_str})",
            "is_abstract": abstract_symbol in action_str
        }

        switch_id += 1

    with open(output_path, "w") as f:
        f.write("\n".join(lines_out))

    return switch_map

def solve_concrete_incremental(lp_files, horizon, switch_map):
    ctl = clingo.Control(["-c", f"horizon={horizon}"])

    for lp in lp_files:
        ctl.load(lp)

    ctl.ground([("base", [])])

    # Collect all switch(ID) atoms from the grounded program
    switch_symbols = []
    symbol_to_id = {}

    for atom in ctl.symbolic_atoms:
        if atom.symbol.name == "switch":
            switch_symbols.append(atom.symbol)
            symbol_to_id[atom.symbol] = atom.symbol.arguments[0].number

     # Ensure switches are processed in numeric order
    switch_symbols.sort(key=lambda s: symbol_to_id[s])

    print(f"[DEBUG] Found {len(switch_symbols)} switches")

    active_switches = []

    # Incrementally activate switches and test satisfiability
    for i, sym in enumerate(switch_symbols):
        switch_id = symbol_to_id[sym]
        action_info = switch_map[switch_id]

        active_switches.append(sym)

        # Look ahead: test if next action is abstract
        next_is_abstract = False
        if i + 1 < len(switch_symbols):
            next_id = symbol_to_id[switch_symbols[i + 1]]
            next_is_abstract = switch_map[next_id]["is_abstract"]

        if next_is_abstract:
            # Build assumptions: currently active = True, others = False
            assumptions = [(s, True) for s in active_switches] + \
                          [(s, False) for s in switch_symbols if s not in active_switches]

            print("\n[DEBUG] Testing before abstract action:", next_id)
            print("   Active switches:", [symbol_to_id[s] for s in active_switches])

            result = ctl.solve(assumptions=assumptions)

            if result.unsatisfiable:
                failing_abstract_actions = [
                    switch_map[symbol_to_id[s]]["atom"]
                    for s in active_switches
                    if switch_map[symbol_to_id[s]]["is_abstract"]
                ]
                print("INCONSISTENT before abstract action:", next_id)
                print("   Failing abstract actions:")
                for a in failing_abstract_actions:
                    print("   ", a)
                return False, [], failing_abstract_actions

    # If all switches are consistent, compute concrete plans
    print("All switches consistent.")

    plans = []

    assumptions = [(s, True) for s in switch_symbols]

    with ctl.solve(yield_=True, assumptions=assumptions) as handle:
        for model in handle:
            atoms = [str(a) for a in model.symbols(shown=True)]
            plans.append(atoms)

    activated_abstract_actions = [
        switch_map[symbol_to_id[s]]["atom"]
        for s in switch_symbols
        if switch_map[symbol_to_id[s]]["is_abstract"]
    ]

    return True, plans, activated_abstract_actions


def solve_concrete_decremental(lp_files, horizon, switch_map):
    ctl = clingo.Control(["-c", f"horizon={horizon}"])

    for lp in lp_files:
        ctl.load(lp)

    ctl.ground([("base", [])])

    switch_symbols = []
    symbol_to_id = {}

    for atom in ctl.symbolic_atoms:
        if atom.symbol.name == "switch":
            switch_symbols.append(atom.symbol)
            symbol_to_id[atom.symbol] = atom.symbol.arguments[0].number

    switch_symbols.sort(key=lambda s: symbol_to_id[s])

    print(f"[DEBUG] Found {len(switch_symbols)} switches")

    # Start with everything active
    active_switches = set(switch_symbols)

    def solve_with_active():
        assumptions = [
            (s, True) if s in active_switches else (s, False)
            for s in switch_symbols
        ]
        return ctl.solve(assumptions=assumptions)

    print("[DEBUG] Testing with all switches active")

    result = solve_with_active()

    # If SAT immediately -> return plans
    if not result.unsatisfiable:
        print("All switches consistent.")

        plans = []

        assumptions = [(s, True) for s in switch_symbols]

        with ctl.solve(yield_=True, assumptions=assumptions) as handle:
            for model in handle:
                atoms = [str(a) for a in model.symbols(shown=True)]
                plans.append(atoms)

        activated_abstract_actions = [
            switch_map[symbol_to_id[s]]["atom"]
            for s in switch_symbols
            if switch_map[symbol_to_id[s]]["is_abstract"]
        ]

        return True, plans, activated_abstract_actions

    print("[DEBUG] Full plan UNSAT, starting reverse disabling")

    # Disable abstract actions from the end
    disabled_abstract = None

    for sym in reversed(switch_symbols):

        switch_id = symbol_to_id[sym]

        if not switch_map[switch_id]["is_abstract"]:
            continue

        print("[DEBUG] Disabling abstract action:", switch_id)

        active_switches.remove(sym)
        disabled_abstract = sym

        result = solve_with_active()

        if not result.unsatisfiable:
            print("SAT after disabling switch:", switch_id)

            plans = []

            assumptions = [
                (s, True) if s in active_switches else (s, False)
                for s in switch_symbols
            ]

            with ctl.solve(yield_=True, assumptions=assumptions) as handle:
                for model in handle:
                    atoms = [str(a) for a in model.symbols(shown=True)]
                    plans.append(atoms)

            activated_abstract_actions = [
                switch_map[symbol_to_id[s]]["atom"]
                for s in active_switches
                if switch_map[symbol_to_id[s]]["is_abstract"]
            ]

            return True, plans, activated_abstract_actions

    # If still UNSAT → forbid earliest active abstract action
    print("[DEBUG] Still UNSAT → computing minimal refinement")

    earliest_abstract = None

    for s in switch_symbols:
        sid = symbol_to_id[s]

        if switch_map[sid]["is_abstract"]:
            earliest_abstract = switch_map[sid]["atom"]
            break

    print("[DEBUG] Earliest failing abstract action:")
    print("   ", earliest_abstract)

    return False, [], [earliest_abstract]

def write_forbid_abstract_lp(abstract_atoms_to_forbid, output_path):
    lines = []

    print("\n[DEBUG] Forbidding the following abstract actions:")

    for atom in abstract_atoms_to_forbid:
        atom_str = str(atom)

        # convert occurs_abstract(...) → occurs(...)
        concrete_atom = atom_str.replace("occurs_abstract", "occurs")

        print("   ", concrete_atom)

        lines.append(f":- {concrete_atom}.")

    with open(output_path, "w") as f:
        f.write("\n".join(lines))