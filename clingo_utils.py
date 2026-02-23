import subprocess
import os

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
CLINGO_BIN = os.path.join(CURRENT_DIRECTORY, "lib", "clingo", "build", "bin", "clingo")

def run_clingo(lp_files, horizon):
    cmd = [CLINGO_BIN] + lp_files + ["-c", f"horizon={horizon}"]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    output = result.stdout

    models = []
    current_model = []

    collecting = False
    for line in output.splitlines():
        line = line.strip()

        if line.startswith("Answer:"):
            collecting = True
            current_model = []
            continue

        if collecting:
            if line == "" or line.startswith("SATISFIABLE") or line.startswith("UNSATISFIABLE"):
                if current_model:
                    models.append(current_model)
                collecting = False
                continue
            # Add each atom
            current_model.extend(line.split())

    return models

def write_occurs_abs_lp(atoms, output_path):
    lines = []

    for atom in atoms:
        atom = atom.strip()

        if atom.startswith("occurs("):
            # occurs(action(...),T) → occurs_abstract(action(...),T)
            lines.append("occurs_abstract" + atom[len("occurs"): ] + ".")

        elif atom.startswith("occurs_abstract("):
            # already abstract (defensive)
            lines.append(atom + ".")

    with open(output_path, "w") as f:
        f.write("\n".join(lines))


def create_map_lp(occurs_abs_path, output_path, abstract_symbol, concrete_objects):
    # concrete_hangars = ["hangar1", "hangar2"]
    with open(occurs_abs_path, "r") as f:
        lines_in = [line.strip() for line in f if line.strip()]

    lines_out = []
    for line in lines_in:
        if not line.startswith("occurs_abstract("):
            continue

        # Extract the inner part: occurs_abstract(inner)
        inner = line[len("occurs_abstract("):].rstrip(").")
        # Split into action_term and time by the last comma
        if ',' not in inner:
            continue
        action_str, time_str = inner.rsplit(",", 1)
        action_str = action_str.strip()
        time_str = time_str.strip()

        # Case 1: this action uses the abstract symbol -> choice rule
        if abstract_symbol in action_str:
            choices = []
            for obj in concrete_objects:
                new_action = action_str.replace(abstract_symbol, obj)
                choices.append(f"occurs({new_action}, {time_str})")
            
            lines_out.append(f"1 {{ {'; '.join(choices)} }} 1 :- occurs_abstract({action_str},{time_str}).")
        else:
            # case 2: no abstraction -> direct mapping
            lines_out.append(f"occurs({action_str},{time_str}) :- occurs_abstract({action_str},{time_str}).")

    # Write the map.lp
    with open(output_path, "w") as f:
        f.write("\n".join(lines_out))