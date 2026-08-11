import re
import sys
from pathlib import Path


def count_trailers(pddl_text: str) -> int:
    return len(re.findall(r'\bbeluga_trailer_\d+\s*-\s*trailer\b', pddl_text))


def collapse_trailers(pddl_text: str, new_name="beluga_abs_trailer") -> str:

    # Replace trailer declarations block
    pddl_text = re.sub(
        r'(\s*;\s*trailers:\s*\n)(?:\s*beluga_trailer_\d+\s*-\s*trailer\s*\n)+',
        rf'\1\t\t{new_name} - trailer\n',
        pddl_text,
        flags=re.MULTILINE
    )

    # Replace empty + at-side blocks
    pddl_text = re.sub(
        r'(\s*;\s*trailers\s*\(Beluga side\):\s*\n)(?:\s*\(empty\s+beluga_trailer_\d+\)\s*\n\s*\(at-side\s+beluga_trailer_\d+\s+bside\)\s*\n)+',
        rf'\1\t\t(empty {new_name})\n\t\t(at-side {new_name} bside)\n',
        pddl_text,
        flags=re.MULTILINE
    )

    # Cleanup leftover references
    pddl_text = re.sub(r'\bbeluga_trailer_\d+\b', new_name, pddl_text)

    return pddl_text


def main():
    if len(sys.argv) != 3:
        print("Usage:")
        print("  python createAbstractTrailerAutomatically.py input.pddl output.pddl")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    pddl = Path(input_file).read_text()

    # 👇 PRINT COUNT BEFORE MODIFICATION
    num_trailers = count_trailers(pddl)
    print(f"[INFO] Found {num_trailers} trailers in {input_file}")

    new_pddl = collapse_trailers(pddl)

    Path(output_file).write_text(new_pddl)

    print(f"Written output to: {output_file}")


if __name__ == "__main__":
    main()
