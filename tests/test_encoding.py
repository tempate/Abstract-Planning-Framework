import unittest
from types import SimpleNamespace

from core.utilities.plan import PlanAction
from core.pipeline.refinement.encoding import (
    add_concrete_objects,
    add_switches,
    drop_action_choice,
    expand_abstract_actions,
    map_abstract_actions,
    switches,
)
from core.asp.solver import Solver
from core.asp.program import AspProgram, make_steps_optional

OCCURRENCE_ENCODING = "#program step(t).\n1 {occurs(Action, t) : action(Action)} 1.\n#program base.\n"


class EncodingTests(unittest.TestCase):
    def test_a_switched_off_step_may_stay_empty(self):
        # The only action can occur once, so the abstract plan's second step
        # refines only once its switch is off and it holds nothing.
        abstract_plan = (PlanAction("inspect", ("item1",), 1), PlanAction("inspect", ("item1",), 2))
        collapsed_set = SimpleNamespace(name="item_abs", objects=("item1",))
        mapping = _switched(abstract_plan, collapsed_set)
        program = make_steps_optional(OCCURRENCE_ENCODING) + """
action(action(("inspect","item1"))).
#program step(t).
:- occurs(Action, t), occurs(Action, T), T < t.
#program base.
""" + mapping
        solver = Solver(AspProgram(program), init_horizon=2 * 2 + 1)
        first, second = sorted(switches(abstract_plan))

        self.assertIsNone(solver.solve([(first, True), (second, True)]))
        self.assertIsNotNone(solver.solve([(first, True), (second, False)]))

    def test_an_abstract_action_follows_a_gap_only_when_there_are_gaps(self):
        # With gaps the k-th abstract action sits on step 2k, with a gap before it; without, on step k.
        abstract_plan = (PlanAction("inspect", ("item1",), 1), PlanAction("inspect", ("item1",), 2))
        collapsed_set = SimpleNamespace(name="item_abs", objects=("item1",))

        for gaps, steps in ((True, [2, 4]), (False, [1, 2])):
            with self.subTest(gaps=gaps):
                self.assertEqual(sorted(map_abstract_actions(abstract_plan, collapsed_set, gaps)), steps)

    def test_a_held_step_takes_exactly_one_grounding_of_its_abstract_action(self):
        abstract_plan = (PlanAction("inspect", ("item_abs",), 1),)
        collapsed_set = SimpleNamespace(name="item_abs", objects=("item1", "item2"))
        choices = map_abstract_actions(abstract_plan, collapsed_set, gaps=False)
        program = (
            drop_action_choice(OCCURRENCE_ENCODING)
            + "\n".join([*add_concrete_objects(collapsed_set), *choices.values()])
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

    def test_groundings_expand_only_the_collapsed_object(self):
        abstract_plan = (PlanAction("move", ("item_abs", "room1", "item_abs"), 0), PlanAction("open", ("door",), 1))
        collapsed_set = SimpleNamespace(name="item_abs", objects=("item1", "item2"))

        self.assertEqual(
            set(expand_abstract_actions(abstract_plan, collapsed_set)),
            {
                "(move item1 room1 item1)",
                "(move item1 room1 item2)",
                "(move item2 room1 item1)",
                "(move item2 room1 item2)",
                "(open door)",
            },
        )

    def test_grounded_action_relation_filters_incompatible_combinations(self):
        abstract_plan = (PlanAction("link", ("node_abs", "node_abs"), 1),)
        collapsed_set = SimpleNamespace(name="node_abs", objects=("a", "b"))
        mapping = _switched(abstract_plan, collapsed_set)
        program = """
action(action(("link","a","b"))).
switch(2).
""" + mapping

        models = self._models(program, horizon=2)

        self.assertTrue(models)
        self.assertTrue(all('occurs(action(("link","a","b")),2)' in model for model in models))
        self.assertTrue(all('occurs(action(("link","a","a")),2)' not in model for model in models))

    def test_mapping_rejects_plan_actions_that_are_not_concrete_actions(self):
        collapsed_set = SimpleNamespace(name="item_abs", objects=("item1", "item2"))
        abstract_plan = (PlanAction("inspect", ("item1",), 1),)
        mapping = _switched(abstract_plan, collapsed_set)
        program = """
action(action(("move","item1"))).
switch(2).
""" + mapping

        result = Solver(AspProgram(program), init_horizon=2).control.solve()

        self.assertTrue(result.unsatisfiable)

    def test_switches_give_up_the_abstract_plan_from_its_end(self):
        abstract_plan = (PlanAction("inspect", ("item1",), 1), PlanAction("inspect", ("item2",), 5))

        # Steps 10 and 2, ordered by number rather than as text.
        self.assertEqual([str(switch) for switch in switches(abstract_plan)], ["switch(10)", "switch(2)"])

    def _models(self, program, horizon):
        control = Solver(AspProgram(program), horizon).control
        control.configuration.solve.models = 0
        models = []
        with control.solve(yield_=True) as handle:
            for model in handle:
                models.append({str(symbol) for symbol in model.symbols(atoms=True)})
        return models


def _switched(abstract_plan, collapsed_set, gaps=True):
    choices = map_abstract_actions(abstract_plan, collapsed_set, gaps)
    return "\n".join([*add_concrete_objects(collapsed_set), *add_switches(choices)])


if __name__ == "__main__":
    unittest.main()
