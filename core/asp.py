"""Build ASP programs used for plan mapping and refinement."""


def join_asp(*programs):
    """Join nonempty ASP fragments with exactly one separating newline."""
    fragments = [program.rstrip("\n") for program in programs if program]
    return "\n".join(fragments) + ("\n" if fragments else "")
