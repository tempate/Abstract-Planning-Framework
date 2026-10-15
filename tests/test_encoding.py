import unittest
from types import SimpleNamespace

from core.plan import PlanAction
from core.refinement.encoding import add_gaps, concretize_abstract_actions, mapped_horizon, switches
from core.search.incremental import IncrementalSolver

OCCURRENCE_ENCODING = "#program step(t).\n1 {occurs(Action, t) : action(Action)} 1.\n#program base.\n"


class EncodingTests(unittest.TestCase):
    def test_every_step_without_an_abstract_action_is_a_gap(self):
        abstract_plan = (PlanAction("inspect", ("item1",), 1), PlanAction("inspect", ("item2",), 2))
        actions = sorted(_step(switch) for switch in switches(abstract_plan))
        mapping = add_gaps(OCCURRENCE_ENCODING, 2)
        gaps = {step for step in range(1, mapped_horizon(2) + 1) if f"gap({step})." in mapping}

        self.assertEqual(gaps, set(range(1, mapped_horizon(2) + 1)) - set(actions))
        # One gap between the actions, and more than one before the first and after the last.
        self.assertEqual(actions[1] - actions[0], 2)
        self.assertGreater(actions[0] - 1, 1)
        self.assertGreater(mapped_horizon(2) - actions[1], 1)

    def test_a_gap_holds_any_concrete_action_or_none(self):
        abstract_plan = (PlanAction("inspect", ("item1",), 1),)
        abstraction = SimpleNamespace(name="item_abs", objects=("item1",))
        mapping = concretize_abstract_actions(abstract_plan, abstraction)
        step = _step(switches(abstract_plan)[0])
        program = add_gaps(OCCURRENCE_ENCODING, 1) + f"""
action(action(("inspect","item1"))).
action(action(("unrelated","x"))).
switch({step}).
""" + mapping

        models = self._models(program, horizon=mapped_horizon(1))
        in_first_gap = {'occurs(action(("inspect","item1")),1)', 'occurs(action(("unrelated","x")),1)'}

        self.assertTrue(all(f'occurs(action(("inspect","item1")),{step})' in model for model in models))
        self.assertTrue(any('occurs(action(("unrelated","x")),1)' in model for model in models))
        self.assertTrue(any(not model & in_first_gap for model in models))

    def test_minimized_gaps_stay_empty_when_they_can(self):
        abstract_plan = (PlanAction("inspect", ("item1",), 1),)
        abstraction = SimpleNamespace(name="item_abs", objects=("item1",))
        mapping = concretize_abstract_actions(abstract_plan, abstraction)
        step = _step(switches(abstract_plan)[0])
        program = add_gaps(OCCURRENCE_ENCODING, 1, minimize=True) + f"""
action(action(("inspect","item1"))).
action(action(("unrelated","x"))).
switch({step}).
""" + mapping

        control = IncrementalSolver(program, init_horizon=mapped_horizon(1)).control
        control.configuration.solve.opt_mode = "optN"
        optimal = self._models(program, horizon=mapped_horizon(1), control=control, optimal_only=True)
        gaps = set(range(1, mapped_horizon(1) + 1)) - {step}
        in_gaps = {f'occurs(action(("unrelated","x")),{gap})' for gap in gaps}

        self.assertTrue(optimal)
        self.assertTrue(all(not model & in_gaps for model in optimal))

    def test_grounded_action_relation_filters_incompatible_combinations(self):
        abstract_plan = (PlanAction("link", ("node_abs", "node_abs"), 1),)
        abstraction = SimpleNamespace(name="node_abs", objects=("a", "b"))
        mapping = concretize_abstract_actions(abstract_plan, abstraction)
        step = _step(switches(abstract_plan)[0])
        program = f"""
action(action(("link","a","b"))).
switch({step}).
""" + mapping

        models = self._models(program, horizon=step)

        self.assertTrue(models)
        self.assertTrue(all(f'occurs(action(("link","a","b")),{step})' in model for model in models))
        self.assertTrue(all(f'occurs(action(("link","a","a")),{step})' not in model for model in models))

    def test_mapping_rejects_plan_actions_that_are_not_concrete_actions(self):
        abstraction = SimpleNamespace(name="item_abs", objects=("item1", "item2"))
        abstract_plan = (PlanAction("inspect", ("item1",), 1),)
        mapping = concretize_abstract_actions(abstract_plan, abstraction)
        step = _step(switches(abstract_plan)[0])
        program = f"""
action(action(("move","item1"))).
switch({step}).
""" + mapping

        result = IncrementalSolver(program, init_horizon=step).control.solve()

        self.assertTrue(result.unsatisfiable)

    def test_switches_give_up_the_abstract_plan_from_its_end(self):
        abstract_plan = (PlanAction("inspect", ("item1",), 1), PlanAction("inspect", ("item2",), 5))

        # Ordered by number rather than as text, which would put a two-digit step first.
        steps = [_step(switch) for switch in switches(abstract_plan)]
        self.assertEqual(steps, sorted(steps, reverse=True))
        self.assertGreaterEqual(steps[0], 10)

    def _models(self, program, horizon, control=None, optimal_only=False):
        control = control or IncrementalSolver(program, horizon).control
        control.configuration.solve.models = 0
        models = []
        with control.solve(yield_=True) as handle:
            for model in handle:
                if not optimal_only or model.optimality_proven:
                    models.append({str(symbol) for symbol in model.symbols(atoms=True)})
        return models


def _step(switch):
    return switch.arguments[0].number


if __name__ == "__main__":
    unittest.main()
