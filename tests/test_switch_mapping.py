import tempfile
import unittest
from pathlib import Path

from core.planners.BelugaPlanner import BelugaPlanner
from core.planners.NoMysteryPlanner import NoMysteryPlanner
from core.solvers.IncrementalSolver import IncrementalSolver


class SwitchMappingTests(unittest.TestCase):
    reversed_plan = "\n".join(
        [
            'occurs_abstract(action("finish"),2).',
            'occurs_abstract(action("prep"),1).',
        ]
    )
    sparse_reversed_plan = "\n".join(
        [
            'occurs_abstract(action("finish"),3).',
            'occurs_abstract(action("prep"),1).',
        ]
    )

    def test_switch_ids_match_time_steps_for_every_profile(self):
        for planner in (BelugaPlanner(), NoMysteryPlanner()):
            with self.subTest(profile=planner.profile_name):
                with tempfile.TemporaryDirectory() as directory:
                    directory = Path(directory)
                    occurrences = directory / "occurrences.lp"
                    occurrences.write_text(
                        self.sparse_reversed_plan,
                        encoding="utf-8",
                    )

                    switch_map = planner.build_mapping(
                        occurrences,
                        directory / "mapping.lp",
                        abstract_symbol=None,
                        concrete_objects=None,
                    )

                    self.assertEqual(
                        'occurs_abstract(action("prep"),1)',
                        switch_map[1]["atom"],
                    )
                    self.assertEqual(
                        'occurs_abstract(action("finish"),3)',
                        switch_map[3]["atom"],
                    )
                    self.assertEqual({1, 3}, set(switch_map))

    def test_incremental_solver_accepts_reversed_model_order(self):
        with tempfile.TemporaryDirectory() as directory:
            directory = Path(directory)
            occurrences = directory / "occurrences.lp"
            occurrences.write_text(self.reversed_plan, encoding="utf-8")
            mapping = directory / "mapping.lp"
            switch_map = BelugaPlanner().build_mapping(
                occurrences,
                mapping,
                abstract_symbol=None,
                concrete_objects=None,
            )

            task = directory / "task.lp"
            task.write_text(
                "\n".join(
                    [
                        "time(1..2).",
                        'action(action("prep")).',
                        'action(action("finish")).',
                        "1 { occurs(Action,T) : action(Action) } 1 :- "
                        "time(T), not switch(T).",
                        'prepared :- occurs(action("prep"),1).',
                        ':- occurs(action("finish"),2), not prepared.',
                        ':- not occurs(action("finish"),2).',
                        "#show occurs/2.",
                    ]
                ),
                encoding="utf-8",
            )

            success, plans, _, operations = IncrementalSolver().solve(
                [str(task), str(occurrences), str(mapping)],
                horizon=2,
                switch_map=switch_map,
            )

            self.assertTrue(success)
            self.assertTrue(plans)
            self.assertEqual(2, operations)


if __name__ == "__main__":
    unittest.main()
