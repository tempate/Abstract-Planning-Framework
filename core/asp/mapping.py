"""Shared parsing and file-writing helpers for ASP mapping programs."""


def read_abstract_actions(path):
    """Yield ``(action, time_step)`` pairs from ``occurs_abstract`` facts."""
    with open(path, "r") as source:
        for line in source:
            line = line.strip()
            if not line.startswith("occurs_abstract("):
                continue
            inner = line[len("occurs_abstract("):].rstrip(").")
            if "," in inner:
                yield tuple(part.strip() for part in inner.rsplit(",", 1))


def write_lp_lines(path, lines):
    with open(path, "w") as output_file:
        output_file.write("\n".join(lines))
