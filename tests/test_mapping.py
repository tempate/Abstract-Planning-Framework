import unittest
from types import SimpleNamespace

from core.integrations.clingo import create_control
from core.planning.mapping import build_mapping
from core.planning.plan import PlanAction


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
            '1 { occurs(action(("inspect","item1")),1) : action(action(("inspect","item1"))) } 1 :- switch(1).', mapping
        )

    def test_grounded_action_relation_filters_incompatible_combinations(self):
        abstract_plan = (PlanAction("link", ("node_abs", "node_abs"), 1),)
        abstraction = SimpleNamespace(name="node_abs", objects=("a", "b"))
        mapping = build_mapping(abstract_plan, abstraction)
        program = """
action(action(("link","a","b"))).
switch(1).
""" + mapping

        control = create_control(program, horizon=1)
        models = []
        with control.solve(yield_=True) as handle:
            for model in handle:
                models.append({str(symbol) for symbol in model.symbols(atoms=True)})

        self.assertTrue(models)
        self.assertTrue(all('occurs(action(("link","a","b")),1)' in model for model in models))
        self.assertTrue(all('occurs(action(("link","a","a")),1)' not in model for model in models))

    def test_mapping_rejects_plan_actions_that_are_not_concrete_actions(self):
        abstraction = SimpleNamespace(name="item_abs", objects=("item1", "item2"))
        abstract_plan = (PlanAction("inspect", ("item1",), 1),)
        mapping = build_mapping(abstract_plan, abstraction)
        program = """
action(action(("move","item1"))).
switch(1).
""" + mapping

        result = create_control(program, horizon=1).solve()

        self.assertTrue(result.unsatisfiable)


if __name__ == "__main__":
    unittest.main()
