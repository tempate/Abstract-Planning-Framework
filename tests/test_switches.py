import unittest

from core.refinement.switches import collect_switches, disabled_switches
from core.search.incremental import IncrementalSolver

PROGRAM = """
{ switch(2) }.
{ switch(10) }.
"""


class SwitchTests(unittest.TestCase):
    def test_switches_are_ordered_by_time_step_instead_of_lexically(self):
        switches = collect_switches(IncrementalSolver(PROGRAM))

        self.assertEqual([str(switch) for switch in switches], ["switch(2)", "switch(10)"])

    def test_disabling_turns_every_switch_off(self):
        assumptions = disabled_switches(IncrementalSolver(PROGRAM))

        self.assertEqual(
            [(str(switch), value) for switch, value in assumptions], [("switch(2)", False), ("switch(10)", False)]
        )


if __name__ == "__main__":
    unittest.main()
