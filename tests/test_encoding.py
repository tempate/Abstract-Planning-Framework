import unittest
from types import SimpleNamespace

from core.plan import PlanAction
from core.refinement.encoding import (
    add_concrete_objects,
    add_switches,
    drop_action_choice,
    make_steps_optional,
    map_abstract_actions,
    switches,
)
from core.search.incremental import IncrementalSolver
from core.encodings.program import AspProgram

OCCURRENCE_ENCODING = "#program step(t).\n1 {occurs(Action, t) : action(Action)} 1.\n#program base.\n"


class EncodingTests(unittest.TestCase):
    def test_a_switched_off_step_may_stay_empty(self):
        # The only action can occur once, so the abstract plan's second step
        # refines only once its switch is off and it holds nothing.
        abstract_plan = (PlanAction("inspect", ("item1",), 1), PlanAction("inspect", ("item1",), 2))
        abstraction = SimpleNamespace(name="item_abs", objects=("item1",))
        mapping = _switched(abstract_plan, abstraction)
        program = make_steps_optional(OCCURRENCE_ENCODING) + """
action(action(("inspect","item1"))).
#program step(t).
:- occurs(Action, t), occurs(Action, T), T < t.
#program base.
""" + mapping
        solver = IncrementalSolver(AspProgram(program), init_horizon=2 * 2 + 1)
        first, second = sorted(switches(abstract_plan))

        self.assertIsNone(solver.solve([(first, True), (second, True)]))
        self.assertIsNotNone(solver.solve([(first, True), (second, False)]))

    def test_a_gap_holds_any_concrete_action_or_none(self):
        abstract_plan = (PlanAction("inspect", ("item1",), 1),)
        abstraction = SimpleNamespace(name="item_abs", objects=("item1",))
        mapping = _switched(abstract_plan, abstraction)
        program = make_steps_optional(OCCURRENCE_ENCODING) + """
action(action(("inspect","item1"))).
action(action(("unrelated","x"))).
switch(2).
""" + mapping

        models = self._models(program, horizon=3)
        in_first_gap = {'occurs(action(("inspect","item1")),1)', 'occurs(action(("unrelated","x")),1)'}

        self.assertTrue(all('occurs(action(("inspect","item1")),2)' in model for model in models))
        self.assertTrue(any('occurs(action(("unrelated","x")),1)' in model for model in models))
        self.assertTrue(any(not model & in_first_gap for model in models))

    def test_without_gaps_an_abstract_action_keeps_its_time_step(self):
        abstract_plan = (PlanAction("inspect", ("item1",), 1),)
        abstraction = SimpleNamespace(name="item_abs", objects=("item1",))
        mapping = _switched(abstract_plan, abstraction, gaps=False)
        program = OCCURRENCE_ENCODING + """
action(action(("inspect","item1"))).
action(action(("unrelated","x"))).
""" + mapping

        models = self._models(program + "switch(1).", horizon=1)

        self.assertEqual([str(switch) for switch in switches(abstract_plan, gaps=False)], ["switch(1)"])
        self.assertTrue(models)
        self.assertTrue(all('occurs(action(("inspect","item1")),1)' in model for model in models))

    def test_an_exponential_horizon_lets_the_steps_above_the_abstract_plan_stay_empty(self):
        abstract_plan = (PlanAction("inspect", ("item1",), 1),)
        abstraction = SimpleNamespace(name="item_abs", objects=("item1",))
        mapping = _switched(abstract_plan, abstraction)
        program = make_steps_optional(OCCURRENCE_ENCODING) + """
action(action(("inspect","item1"))).
switch(2).
""" + mapping

        models = self._models(program, horizon=5)
        above = {f'occurs(action(("inspect","item1")),{step})' for step in (4, 5)}

        self.assertTrue(all('occurs(action(("inspect","item1")),2)' in model for model in models))
        self.assertTrue(any(not model & above for model in models))

    def test_a_held_step_takes_exactly_one_grounding_of_its_abstract_action(self):
        abstract_plan = (PlanAction("inspect", ("item_abs",), 1),)
        abstraction = SimpleNamespace(name="item_abs", objects=("item1", "item2"))
        choices = map_abstract_actions(abstract_plan, abstraction, gaps=False)
        program = (
            drop_action_choice(OCCURRENCE_ENCODING)
            + "\n".join([*add_concrete_objects(abstraction), *choices.values()])
            + """
action(action(("inspect","item1"))).
action(action(("inspect","item2"))).
action(action(("unrelated","x"))).
"""
        )

        models = self._models(program, horizon=1)
        groundings = {f'occurs(action(("inspect","{item}")),1)' for item in ("item1", "item2")}

        self.assertEqual({len(model & groundings) for model in models}, {1})
        self.assertTrue(all('occurs(action(("unrelated","x")),1)' not in model for model in models))

    def test_grounded_action_relation_filters_incompatible_combinations(self):
        abstract_plan = (PlanAction("link", ("node_abs", "node_abs"), 1),)
        abstraction = SimpleNamespace(name="node_abs", objects=("a", "b"))
        mapping = _switched(abstract_plan, abstraction)
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
        mapping = _switched(abstract_plan, abstraction)
        program = """
action(action(("move","item1"))).
switch(2).
""" + mapping

        result = IncrementalSolver(AspProgram(program), init_horizon=2).control.solve()

        self.assertTrue(result.unsatisfiable)

    def test_switches_give_up_the_abstract_plan_from_its_end(self):
        abstract_plan = (PlanAction("inspect", ("item1",), 1), PlanAction("inspect", ("item2",), 5))

        # Steps 10 and 2, ordered by number rather than as text.
        self.assertEqual([str(switch) for switch in switches(abstract_plan)], ["switch(10)", "switch(2)"])

    def _models(self, program, horizon):
        control = IncrementalSolver(AspProgram(program), horizon).control
        control.configuration.solve.models = 0
        models = []
        with control.solve(yield_=True) as handle:
            for model in handle:
                models.append({str(symbol) for symbol in model.symbols(atoms=True)})
        return models


def _switched(abstract_plan, abstraction, gaps=True):
    choices = map_abstract_actions(abstract_plan, abstraction, gaps)
    return "\n".join([*add_concrete_objects(abstraction), *add_switches(choices)])


if __name__ == "__main__":
    unittest.main()
