import unittest

from core.integrations.clingo import create_control
from core.planning.mapping import OCCURRENCE_VALIDATION_CONSTRAINT, build_mapping


class MappingTests(unittest.TestCase):
    def test_maps_an_abstract_argument_to_existing_grounded_actions(self):
        occurrences = 'occurs_abstract(action(("move","item_abs","dock")),2).\n'

        mapping = build_mapping(occurrences, "item_abs", ("item1", "item2"))

        self.assertIn('concrete_object("item1").', mapping)
        self.assertIn('concrete_object("item2").', mapping)
        self.assertIn('action(("move",ConcreteObject1,"dock"))', mapping)
        self.assertIn('action(action(("move",ConcreteObject1,"dock")))', mapping)

    def test_each_abstract_argument_is_grounded_independently(self):
        occurrences = 'occurs_abstract(action(("link","node_abs","node_abs")),1).\n'

        mapping = build_mapping(occurrences, "node_abs", ("a", "b"))

        self.assertIn('action(("link",ConcreteObject1,ConcreteObject2))', mapping)
        self.assertIn("concrete_object(ConcreteObject1)", mapping)
        self.assertIn("concrete_object(ConcreteObject2)", mapping)

    def test_non_abstract_actions_are_mapped_directly(self):
        occurrences = 'occurs_abstract(action(("inspect","item1")),1).\n'

        mapping = build_mapping(occurrences, "item_abs", ("item1", "item2"))

        self.assertIn(
            'occurs(action(("inspect","item1")),1) :- ' 'occurs_abstract(action(("inspect","item1")),1), switch(1).',
            mapping,
        )

    def test_grounded_action_relation_filters_incompatible_combinations(self):
        occurrences = 'occurs_abstract(action(("link","node_abs","node_abs")),1).\n'
        mapping = build_mapping(occurrences, "node_abs", ("a", "b"))
        program = """
action(action(("link","a","b"))).
occurs_abstract(action(("link","node_abs","node_abs")),1).
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

    def test_mapping_rejects_occurrences_that_are_not_concrete_actions(self):
        mapping = build_mapping('occurs_abstract(action(("inspect","item1")),1).\n', "item_abs", ("item1", "item2"))

        self.assertIn(OCCURRENCE_VALIDATION_CONSTRAINT, mapping)


if __name__ == "__main__":
    unittest.main()
