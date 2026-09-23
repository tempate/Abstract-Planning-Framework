import unittest

from core.search.solver import Solver


class SolverTests(unittest.TestCase):
    def test_the_base_program_is_grounded_and_shown(self):
        plan = Solver("ready. #show ready/0.").solve()

        self.assertEqual(plan, ["ready"])

    def test_unsatisfiable_program_has_no_plan(self):
        self.assertIsNone(Solver(":-.\n").solve())


if __name__ == "__main__":
    unittest.main()
