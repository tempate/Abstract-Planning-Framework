import re
import sys
from pathlib import Path


def collapse_hangars(pddl_text: str, new_name="hangarabs") -> str:

    # Replace hangar object block
    text = re.sub(
        r'(\s*;\s*hangars:\s*\n)(?:\s*hangar\w+\s*-\s*hangar\s*\n)+',
        rf'\1\t\t{new_name} - hangar\n',
        pddl_text,
        flags=re.MULTILINE
    )

    # Replace empty hangar block
    text = re.sub(
        r'(\s*;\s*hangars:\s*\n)(?:\s*\(empty\s+hangar\w+\)\s*\n)+',
        rf'\1\t\t(empty {new_name})\n',
        text,
        flags=re.MULTILINE
    )

    # Replace remaining references
    text = re.sub(r'\bhangar\w+\b', new_name, text)

    return text

def count_hangars(pddl_text: str) -> int:
    # matches: hangar1 - hangar, hangar2 - hangar, etc.
    return len(re.findall(r'\bhangar\w+\s*-\s*hangar\b', pddl_text))

def main():
    if len(sys.argv) != 3:
        print("Usage:")
        print("  python collapse_hangars.py input.pddl output.pddl")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    pddl = Path(input_file).read_text()
    new_pddl = collapse_hangars(pddl)
    
    num_hangars = count_hangars(pddl)
    print(f"[INFO] Found {num_hangars} hangars in {input_file}")

    Path(output_file).write_text(new_pddl)

    print(f"Written output to: {output_file}")


if __name__ == "__main__":
    main()
