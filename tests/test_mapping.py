import unittest
from types import SimpleNamespace

from core.integrations.clingo import IncrementalSolver
from core.integrations.plasp import add_switch_to_asp_rule
from core.plan import PlanAction
from core.refinement.mapping import build_mapping

OCCURRENCE_ENCODING = "#program step(t).\n1 {occurs(Action, t) : action(Action)} 1.\n#program base.\n"


class MappingTests(unittest.TestCase):
    def test_maps_an_abstract_argument_to_existing_grounded_actions(self):
        abstract_plan = (PlanAction("move", ("item_abs", "dock"), 2),)
        abstraction = SimpleNamespace(name="item_abs", objects=("item1", "item2"))

        mapping = build_mapping(abstract_plan, abstraction)

        self.assertIn('concrete_object("item1").', mapping)
        self.assertIn('concrete_object("item2").', mapping)
        self.assertIn('action(("move",ConcreteObject1,"dock"))', mapping)
        self.assertIn('action(action(("move",ConcreteObject1,"dock")))', mapping)

    def test_each_abstract_argument_is_grounded_independently(self):
        abstract_plan = (PlanAction("link", ("node_abs", "node_abs"), 1),)
        abstraction = SimpleNamespace(name="node_abs", objects=("a", "b"))

        mapping = build_mapping(abstract_plan, abstraction)

        self.assertIn('action(("link",ConcreteObject1,ConcreteObject2))', mapping)
        self.assertIn("concrete_object(ConcreteObject1)", mapping)
        self.assertIn("concrete_object(ConcreteObject2)", mapping)

    def test_non_abstract_actions_are_mapped_directly(self):
        abstract_plan = (PlanAction("inspect", ("item1",), 1),)
        abstraction = SimpleNamespace(name="item_abs", objects=("item1", "item2"))

        mapping = build_mapping(abstract_plan, abstraction)

        self.assertIn(
            '1 { occurs(action(("inspect","item1")),3) : action(action(("inspect","item1"))) } 1 :- switch(3).', mapping
        )

    def test_every_abstract_action_is_surrounded_by_a_gap(self):
        abstract_plan = (PlanAction("inspect", ("item1",), 1), PlanAction("inspect", ("item2",), 2))
        abstraction = SimpleNamespace(name="item_abs", objects=("item1", "item2"))

        mapping = build_mapping(abstract_plan, abstraction)

        # The actions take the steps 3 and 6, the gaps the two steps around each.
        for time_step in (1, 2, 4, 5, 7, 8):
            self.assertIn(f"gap({time_step}).", mapping)
        self.assertNotIn("gap(3).", mapping)
        self.assertNotIn("gap(6).", mapping)

    def test_a_gap_holds_any_concrete_action_or_none(self):
        abstract_plan = (PlanAction("inspect", ("item1",), 1),)
        abstraction = SimpleNamespace(name="item_abs", objects=("item1",))
        mapping = build_mapping(abstract_plan, abstraction)
        program = add_switch_to_asp_rule(OCCURRENCE_ENCODING) + """
action(action(("inspect","item1"))).
action(action(("unrelated","x"))).
switch(3).
""" + mapping

        models = self._models(program, horizon=5)
        in_first_gap = {
            f'occurs(action(("{name}","{argument}")),{time_step})'
            for name, argument in (("inspect", "item1"), ("unrelated", "x"))
            for time_step in (1, 2)
        }

        self.assertTrue(all('occurs(action(("inspect","item1")),3)' in model for model in models))
        self.assertTrue(any('occurs(action(("unrelated","x")),1)' in model for model in models))
        self.assertTrue(any('occurs(action(("unrelated","x")),2)' in model for model in models))
        self.assertTrue(any(not model & in_first_gap for model in models))

    def test_grounded_action_relation_filters_incompatible_combinations(self):
        abstract_plan = (PlanAction("link", ("node_abs", "node_abs"), 1),)
        abstraction = SimpleNamespace(name="node_abs", objects=("a", "b"))
        mapping = build_mapping(abstract_plan, abstraction)
        program = """
action(action(("link","a","b"))).
switch(3).
""" + mapping

        models = self._models(program, horizon=3)

        self.assertTrue(models)
        self.assertTrue(all('occurs(action(("link","a","b")),3)' in model for model in models))
        self.assertTrue(all('occurs(action(("link","a","a")),3)' not in model for model in models))

    def test_mapping_rejects_plan_actions_that_are_not_concrete_actions(self):
        abstraction = SimpleNamespace(name="item_abs", objects=("item1", "item2"))
        abstract_plan = (PlanAction("inspect", ("item1",), 1),)
        mapping = build_mapping(abstract_plan, abstraction)
        program = """
action(action(("move","item1"))).
switch(3).
""" + mapping

        result = IncrementalSolver(program, horizon=3).control.solve()

        self.assertTrue(result.unsatisfiable)

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
