"""Collapse all concrete Beluga hangars into one abstract hangar."""

import argparse
import re
from pathlib import Path


def collapse_hangars(pddl_text: str, abstract_name: str = "hangarabs") -> str:
    """Return a problem in which all hangar objects share one identity."""
    text = re.sub(
        r"(\s*;\s*hangars:\s*\n)(?:\s*hangar\w+\s*-\s*hangar\s*\n)+",
        rf"\1\t\t{abstract_name} - hangar\n",
        pddl_text,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"(\s*;\s*hangars:\s*\n)(?:\s*\(empty\s+hangar\w+\)\s*\n)+",
        rf"\1\t\t(empty {abstract_name})\n",
        text,
        flags=re.MULTILINE,
    )
    return re.sub(r"\bhangar\w+\b", abstract_name, text)


def count_hangars(pddl_text: str) -> int:
    """Count concrete hangar declarations in a Beluga problem."""
    return len(re.findall(r"\bhangar\w+\s*-\s*hangar\b", pddl_text))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Concrete Beluga problem")
    parser.add_argument("output", type=Path, help="Abstract problem to write")
    parser.add_argument("--name", default="hangarabs", help="Abstract object name")
    args = parser.parse_args()

    pddl = args.input.read_text(encoding="utf-8")
    args.output.write_text(
        collapse_hangars(pddl, args.name),
        encoding="utf-8",
    )
    print(f"Collapsed {count_hangars(pddl)} hangars into {args.name}")
    print(f"Written output to: {args.output}")


if __name__ == "__main__":
    main()
