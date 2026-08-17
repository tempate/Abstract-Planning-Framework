"""Collapse exact NoMystery fuel arithmetic into two abstract levels."""

import argparse
import re
from pathlib import Path


def collapse_fuel_levels(pddl_text: str) -> str:
    """Return the two-level fuel abstraction used by this project."""
    text = re.sub(
        r"level0.*?- fuellevel",
        "abslevel1 abslevel2 - fuellevel",
        pddl_text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"^\s*\(sum level\d+ level\d+ level\d+\)\s*$",
        "",
        text,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"(\(:init\s*)",
        r"\1\n    (sum abslevel1 abslevel2 abslevel1)\n",
        text,
    )
    text = re.sub(
        r"\(fuel t0 level\d+\)",
        "(fuel t0 abslevel1)",
        text,
    )
    text = re.sub(
        r"\(fuelcost level\d+",
        "(fuelcost abslevel2",
        text,
    )
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Concrete NoMystery problem")
    parser.add_argument("output", type=Path, help="Abstract problem to write")
    args = parser.parse_args()

    args.output.write_text(
        collapse_fuel_levels(args.input.read_text(encoding="utf-8")),
        encoding="utf-8",
    )
    print(f"Written output to: {args.output}")


if __name__ == "__main__":
    main()
