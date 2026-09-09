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
            '1 { occurs(action(("inspect","item1")),T) : action(action(("inspect","item1"))) } 1'
            " :- abstract_step(1,T).",
            mapping,
        )

    def test_every_time_step_is_a_gap(self):
        abstract_plan = (PlanAction("inspect", ("item1",), 1), PlanAction("inspect", ("item2",), 2))
        abstraction = SimpleNamespace(name="item_abs", objects=("item1", "item2"))

        mapping = build_mapping(abstract_plan, abstraction)

        # The two actions are free to take any of the five steps.
        for time_step in range(1, 6):
            self.assertIn(f"gap({time_step}).", mapping)
        self.assertNotIn("gap(6).", mapping)

    def test_the_abstract_actions_keep_their_order(self):
        abstract_plan = (PlanAction("first", ("item1",), 1), PlanAction("second", ("item1",), 2))
        abstraction = SimpleNamespace(name="item_abs", objects=("item1",))
        mapping = build_mapping(abstract_plan, abstraction)
        program = """
action(action(("first","item1"))).
action(action(("second","item1"))).
switch(1).
switch(2).
""" + mapping

        models = self._models(program, horizon=5)

        self.assertTrue(models)
        placements = set()
        for model in models:
            steps = {}
            for position in (1, 2):
                for time_step in range(1, 6):
                    if f"abstract_step({position},{time_step})" in model:
                        steps[position] = time_step
            self.assertLess(steps[1], steps[2])
            placements.add((steps[1], steps[2]))

        # The order is all that is fixed, so the pair takes every ordered slot.
        self.assertEqual(len(placements), 10)

    def test_a_gap_holds_any_concrete_action_or_none(self):
        abstract_plan = (PlanAction("inspect", ("item1",), 1),)
        abstraction = SimpleNamespace(name="item_abs", objects=("item1",))
        mapping = build_mapping(abstract_plan, abstraction)
        program = add_switch_to_asp_rule(OCCURRENCE_ENCODING) + """
action(action(("inspect","item1"))).
action(action(("unrelated","x"))).
switch(1).
""" + mapping

        models = self._models(program, horizon=3)
        on_first_step = {'occurs(action(("inspect","item1")),1)', 'occurs(action(("unrelated","x")),1)'}

        self.assertTrue(any('occurs(action(("unrelated","x")),1)' in model for model in models))
        self.assertTrue(any(not model & on_first_step for model in models))
        for model in models:
            self.assertTrue(any(f'occurs(action(("inspect","item1")),{step})' in model for step in (1, 2, 3)))

    def test_grounded_action_relation_filters_incompatible_combinations(self):
        abstract_plan = (PlanAction("link", ("node_abs", "node_abs"), 1),)
        abstraction = SimpleNamespace(name="node_abs", objects=("a", "b"))
        mapping = build_mapping(abstract_plan, abstraction)
        program = """
action(action(("link","a","b"))).
switch(1).
""" + mapping

        models = self._models(program, horizon=3)

        self.assertTrue(models)
        for model in models:
            self.assertTrue(any(f'occurs(action(("link","a","b")),{step})' in model for step in (1, 2, 3)))
            for step in (1, 2, 3):
                self.assertNotIn(f'occurs(action(("link","a","a")),{step})', model)

    def test_mapping_rejects_plan_actions_that_are_not_concrete_actions(self):
        abstraction = SimpleNamespace(name="item_abs", objects=("item1", "item2"))
        abstract_plan = (PlanAction("inspect", ("item1",), 1),)
        mapping = build_mapping(abstract_plan, abstraction)
        program = """
action(action(("move","item1"))).
switch(1).
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
