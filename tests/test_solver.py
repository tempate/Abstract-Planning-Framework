import unittest

from core.asp.program import AspProgram
from core.asp.solver import Solver


class SolverTests(unittest.TestCase):
    def test_the_base_program_is_grounded_and_shown(self):
        plan = Solver(AspProgram("ready. #show ready/0.")).solve()

        self.assertEqual(plan, ["ready"])

    def test_rules_ground_over_the_facts_given_apart(self):
        facts = '% variables\ncontains(variable(0), value("at(a)", true)).\n\n'
        rules = "found(V) :- contains(variable(V), value(_, true)). #show found/1."

        self.assertEqual(Solver(AspProgram(rules, facts)).solve(), ["found(0)"])

    def test_unsatisfiable_program_has_no_plan(self):
        self.assertIsNone(Solver(AspProgram(":-.\n")).solve())


if __name__ == "__main__":
    unittest.main()
