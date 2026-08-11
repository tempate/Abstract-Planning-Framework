import re
import sys
from pathlib import Path


def transform_pddl(text: str) -> str:
    """
    Transforms the PDDL file:
    1. Replace all fuellevel objects with:
       abslevel1 abslevel2 - fuellevel

    2. Remove all (sum levelX levelY levelZ) lines
       Add:
       (sum abslevel1 abslevel2 abslevel1)

    3. Replace:
       (fuel t0 levelXYZ)
       with:
       (fuel t0 abslevel1)

    4. Replace all:
       (fuelcost levelXYZ ...)
       with:
       (fuelcost abslevel2 ...)
    """

    # -------------------------------------------------
    # 1. Replace fuellevel object section
    # -------------------------------------------------
    text = re.sub(
        r'level0.*?- fuellevel',
        'abslevel1 abslevel2 - fuellevel',
        text,
        flags=re.DOTALL
    )

    # -------------------------------------------------
    # 2. Remove all sum lines
    # -------------------------------------------------
    text = re.sub(
        r'^\s*\(sum level\d+ level\d+ level\d+\)\s*$',
        '',
        text,
        flags=re.MULTILINE
    )

    # Insert new sum line after (:init if present
    text = re.sub(
        r'(\(:init\s*)',
        r'\1\n    (sum abslevel1 abslevel2 abslevel1)\n',
        text
    )

    # -------------------------------------------------
    # 3. Replace fuel level of truck
    # -------------------------------------------------
    text = re.sub(
        r'\(fuel t0 level\d+\)',
        '(fuel t0 abslevel1)',
        text
    )

    # -------------------------------------------------
    # 4. Replace fuelcost levels
    # -------------------------------------------------
    text = re.sub(
        r'\(fuelcost level\d+',
        '(fuelcost abslevel2',
        text
    )

    # Remove excessive blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)

    return text.strip() + "\n"


def main():
    if len(sys.argv) != 3:
        print("Usage:")
        print("python script.py input.pddl output.pddl")
        return

    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2])

    text = input_file.read_text(encoding="utf-8")
    new_text = transform_pddl(text)
    output_file.write_text(new_text, encoding="utf-8")

    print(f"Saved transformed file to: {output_file}")


if __name__ == "__main__":
    main()
