"""Build and parse ASP programs used for plan mapping and refinement."""


def parse_abstract_actions(asp):
    """Yield abstract actions in chronological order."""
    actions = []
    for line in asp.splitlines():
        line = line.strip()
        if not line.startswith("occurs_abstract("):
            continue
        inner = line[len("occurs_abstract(") :].rstrip(").")
        if "," in inner:
            action, raw_time_step = inner.rsplit(",", 1)
            actions.append((action.strip(), int(raw_time_step.strip())))

    return sorted(actions, key=lambda item: item[1])


def format_abstract_plan(atoms):
    """Return an abstract plan for the supplied action atoms."""
    statements = []
    for atom in atoms:
        atom = atom.strip()
        if atom.startswith("occurs("):
            statement = "occurs_abstract" + atom[len("occurs") :]
        elif atom.startswith("occurs_abstract("):
            statement = atom
        else:
            continue
        statements.append(statement.rstrip(".") + ".")
    return "\n".join(statements)


def join_asp(*programs):
    """Join nonempty ASP fragments with exactly one separating newline."""
    fragments = [program.rstrip("\n") for program in programs if program]
    return "\n".join(fragments) + ("\n" if fragments else "")
