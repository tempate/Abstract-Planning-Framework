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