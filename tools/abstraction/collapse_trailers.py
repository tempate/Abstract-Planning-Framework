"""Collapse all Beluga-side trailers into one abstract trailer."""

import argparse
import re
from pathlib import Path


def collapse_trailers(
    pddl_text: str,
    abstract_name: str = "beluga_abs_trailer",
) -> str:
    """Return a problem with one Beluga-side trailer identity.

    Factory-side trailers remain concrete because they are not part of this
    abstraction.
    """
    text = re.sub(
        r"(\s*;\s*trailers:\s*\n)"
        r"(?:\s*beluga_trailer_\d+\s*-\s*trailer\s*\n)+",
        rf"\1\t\t{abstract_name} - trailer\n",
        pddl_text,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"(\s*;\s*trailers\s*\(Beluga side\):\s*\n)"
        r"(?:\s*\(empty\s+beluga_trailer_\d+\)\s*\n"
        r"\s*\(at-side\s+beluga_trailer_\d+\s+bside\)\s*\n)+",
        rf"\1\t\t(empty {abstract_name})\n"
        rf"\t\t(at-side {abstract_name} bside)\n",
        text,
        flags=re.MULTILINE,
    )
    return re.sub(r"\bbeluga_trailer_\d+\b", abstract_name, text)


def count_trailers(pddl_text: str) -> int:
    """Count concrete Beluga-side trailer declarations."""
    return len(
        re.findall(r"\bbeluga_trailer_\d+\s*-\s*trailer\b", pddl_text)
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Concrete Beluga problem")
    parser.add_argument("output", type=Path, help="Abstract problem to write")
    parser.add_argument(
        "--name",
        default="beluga_abs_trailer",
        help="Abstract object name",
    )
    args = parser.parse_args()

    pddl = args.input.read_text(encoding="utf-8")
    args.output.write_text(
        collapse_trailers(pddl, args.name),
        encoding="utf-8",
    )
    print(f"Collapsed {count_trailers(pddl)} trailers into {args.name}")
    print(f"Written output to: {args.output}")


if __name__ == "__main__":
    main()
