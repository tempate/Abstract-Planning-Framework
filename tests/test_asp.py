import unittest

from core.asp import format_abstract_plan, join_asp, parse_abstract_actions


class AbstractProgramTests(unittest.TestCase):
    def test_parse_actions_ignores_other_atoms_and_orders_by_time(self):
        content = """\
helper(value).
occurs_abstract(action(("unload","p0","t0","l1")), 3).
occurs_abstract(action(("drive","t0","l0","l1")), 2).
occurs_abstract(action(("load","p0","t0","l0")), 1).
"""

        actions = list(parse_abstract_actions(content))

        self.assertEqual(
            actions,
            [
                ('action(("load","p0","t0","l0"))', 1),
                ('action(("drive","t0","l0","l1"))', 2),
                ('action(("unload","p0","t0","l1"))', 3),
            ],
        )

    def test_parse_actions_preserves_commas_inside_an_action(self):
        asp = 'occurs_abstract(action(("move","a","b")), 7).\n'
        self.assertEqual(list(parse_abstract_actions(asp)), [('action(("move","a","b"))', 7)])

    def test_format_abstract_plan_normalizes_supported_atoms(self):
        atoms = [
            'occurs(action(("load","p0","t0","l0")),1)',
            "cost(4)",
            'occurs_abstract(action(("drive","t0","l0","l1")),2).',
        ]

        self.assertEqual(
            format_abstract_plan(atoms),
            "\n".join(
                [
                    'occurs_abstract(action(("load","p0","t0","l0")),1).',
                    'occurs_abstract(action(("drive","t0","l0","l1")),2).',
                ]
            ),
        )

    def test_join_asp_normalizes_fragment_boundaries(self):
        self.assertEqual(join_asp("first.\n", "second."), "first.\nsecond.\n")


if __name__ == "__main__":
    unittest.main()
