import unittest
from types import SimpleNamespace

from core.integrations.clingo import IncrementalSolver
from core.plan import PlanAction
from core.refinement.mapping import build_mapping
from core.refinement.switches import disabled_switches, switches_off

ABSTRACT_PLAN = (PlanAction("inspect", ("item1",), 1), PlanAction("inspect", ("item2",), 2))
ABSTRACTION = SimpleNamespace(name="item_abs", objects=("item1", "item2"))
# The real program concatenates an encoding that shows occurs/2 and nothing
# else, so the switches are only readable if the mapping shows them too.
ACTIONS = """
action(action(("inspect","item1"))).
action(action(("inspect","item2"))).
#show occurs/2.
"""


class GuidedSwitchTests(unittest.TestCase):
    def _solve(self, extra=""):
        program = "\n".join((build_mapping(ABSTRACT_PLAN, ABSTRACTION), ACTIONS, extra))
        solver = IncrementalSolver(program, horizon=5, domain_heuristic=True)
        return solver, solver.solve()

    def test_the_whole_abstract_plan_is_followed_when_it_refines(self):
        solver, plan = self._solve()

        self.assertIn("switch(2)", plan)
        self.assertIn("switch(4)", plan)
        self.assertEqual(switches_off(solver, plan), 0)

    def test_only_the_abstract_action_a_conflict_forbids_is_given_up(self):
        # The first action cannot be refined, so a search that dropped whole
        # suffixes would have to give up the second one too.
        solver, plan = self._solve(':- occurs(action(("inspect","item1")),2).')

        self.assertNotIn("switch(2)", plan)
        self.assertIn("switch(4)", plan)
        self.assertEqual(switches_off(solver, plan), 1)

    def test_an_unrefinable_plan_counts_every_abstract_action_as_given_up(self):
        solver, _plan = self._solve()

        self.assertEqual(switches_off(solver, None), 2)

    def test_the_abstract_plan_can_be_turned_off_entirely(self):
        solver, _plan = self._solve()

        plan = solver.solve(disabled_switches(solver))

        self.assertNotIn("switch(2)", plan)
        self.assertNotIn("switch(4)", plan)


if __name__ == "__main__":
    unittest.main()
