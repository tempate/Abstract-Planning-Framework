import tempfile
import unittest
from pathlib import Path

from core.asp import read_abstract_actions, write_abstract_occurrences, write_asp_program


class AbstractActionIOTests(unittest.TestCase):
    def test_read_actions_ignores_other_atoms_and_orders_by_time(self):
        content = """\
helper(value).
occurs_abstract(action(("unload","p0","t0","l1")), 3).
occurs_abstract(action(("drive","t0","l0","l1")), 2).
occurs_abstract(action(("load","p0","t0","l0")), 1).
"""

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory, "occurrences.lp")
            path.write_text(content, encoding="utf-8")

            actions = list(read_abstract_actions(path))

        self.assertEqual(
            actions,
            [
                ('action(("load","p0","t0","l0"))', 1),
                ('action(("drive","t0","l0","l1"))', 2),
                ('action(("unload","p0","t0","l1"))', 3),
            ],
        )

    def test_read_actions_preserves_commas_inside_an_action(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory, "occurrences.lp")
            path.write_text('occurs_abstract(action(("move","a","b")), 7).\n', encoding="utf-8")

            self.assertEqual(list(read_abstract_actions(path)), [('action(("move","a","b"))', 7)])

    def test_write_occurrences_normalizes_supported_atoms(self):
        atoms = [
            'occurs(action(("load","p0","t0","l0")),1)',
            "cost(4)",
            'occurs_abstract(action(("drive","t0","l0","l1")),2)',
        ]

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory, "occurrences.lp")
            write_abstract_occurrences(atoms, path)

            self.assertEqual(
                path.read_text(encoding="utf-8"),
                "\n".join(
                    [
                        'occurs_abstract(action(("load","p0","t0","l0")),1).',
                        'occurs_abstract(action(("drive","t0","l0","l1")),2).',
                    ]
                ),
            )

    def test_write_program_accepts_a_single_pass_iterable(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory, "program.lp")
            statements = (f"value({number})." for number in range(3))

            write_asp_program(path, statements)

            self.assertEqual(path.read_text(encoding="utf-8"), "value(0).\nvalue(1).\nvalue(2).")


if __name__ == "__main__":
    unittest.main()
