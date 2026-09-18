import unittest
from unittest.mock import patch

from core.search.solver import Solver


class SolverTests(unittest.TestCase):
    @patch("core.search.solver.clingo.Control")
    def test_control_always_uses_one_thread(self, control):
        Solver("")

        # Single-threaded solving keeps benchmark runs reproducible.
        arguments = control.call_args.args[0]
        self.assertEqual(arguments[arguments.index("-t") + 1], "1")

    def test_the_base_program_is_grounded_and_shown(self):
        plan = Solver("ready. #show ready/0.").solve()

        self.assertEqual(plan, ["ready"])

    def test_unsatisfiable_program_has_no_plan(self):
        self.assertIsNone(Solver(":-.\n").solve())


if __name__ == "__main__":
    unittest.main()
