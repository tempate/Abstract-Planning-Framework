import unittest
from types import SimpleNamespace

from core.plan import PlanAction
from core.refinement.encoding import add_gaps, concretize_abstract_actions, mapped_horizon, switches
from core.search.incremental import IncrementalSolver

OCCURRENCE_ENCODING = "#program step(t).\n1 {occurs(Action, t) : action(Action)} 1.\n#program base.\n"


class EncodingTests(unittest.TestCase):
    def test_every_abstract_action_is_surrounded_by_a_gap(self):
        mapping = add_gaps(OCCURRENCE_ENCODING, mapped_horizon(2))

        # The actions take the even steps 2 and 4, the gaps the odd ones around them.
        self.assertIn("gap(1).", mapping)
        self.assertIn("gap(3).", mapping)
        self.assertIn("gap(5).", mapping)
        self.assertNotIn("gap(2).", mapping)
        self.assertNotIn("gap(4).", mapping)

    def test_a_gap_holds_any_concrete_action_or_none(self):
        abstract_plan = (PlanAction("inspect", ("item1",), 1),)
        abstraction = SimpleNamespace(name="item_abs", objects=("item1",))
        mapping = concretize_abstract_actions(abstract_plan, abstraction)
        program = add_gaps(OCCURRENCE_ENCODING, mapped_horizon(1)) + """
action(action(("inspect","item1"))).
action(action(("unrelated","x"))).
switch(2).
""" + mapping

        models = self._models(program, horizon=3)
        in_first_gap = {'occurs(action(("inspect","item1")),1)', 'occurs(action(("unrelated","x")),1)'}

        self.assertTrue(all('occurs(action(("inspect","item1")),2)' in model for model in models))
        self.assertTrue(any('occurs(action(("unrelated","x")),1)' in model for model in models))
        self.assertTrue(any(not model & in_first_gap for model in models))

    def test_grounded_action_relation_filters_incompatible_combinations(self):
        abstract_plan = (PlanAction("link", ("node_abs", "node_abs"), 1),)
        abstraction = SimpleNamespace(name="node_abs", objects=("a", "b"))
        mapping = concretize_abstract_actions(abstract_plan, abstraction)
        program = """
action(action(("link","a","b"))).
switch(2).
""" + mapping

        models = self._models(program, horizon=2)

        self.assertTrue(models)
        self.assertTrue(all('occurs(action(("link","a","b")),2)' in model for model in models))
        self.assertTrue(all('occurs(action(("link","a","a")),2)' not in model for model in models))

    def test_mapping_rejects_plan_actions_that_are_not_concrete_actions(self):
        abstraction = SimpleNamespace(name="item_abs", objects=("item1", "item2"))
        abstract_plan = (PlanAction("inspect", ("item1",), 1),)
        mapping = concretize_abstract_actions(abstract_plan, abstraction)
        program = """
action(action(("move","item1"))).
switch(2).
""" + mapping

        result = IncrementalSolver(program, init_horizon=2).control.solve()

        self.assertTrue(result.unsatisfiable)

    def test_switches_give_up_the_abstract_plan_from_its_end(self):
        abstract_plan = (PlanAction("inspect", ("item1",), 1), PlanAction("inspect", ("item2",), 5))

        # Steps 10 and 2, ordered by number rather than as text.
        self.assertEqual([str(switch) for switch in switches(abstract_plan)], ["switch(10)", "switch(2)"])

    def _models(self, program, horizon):
        control = IncrementalSolver(program, horizon).control
        control.configuration.solve.models = 0
        models = []
        with control.solve(yield_=True) as handle:
            for model in handle:
                models.append({str(symbol) for symbol in model.symbols(atoms=True)})
        return models


if __name__ == "__main__":
    unittest.main()
