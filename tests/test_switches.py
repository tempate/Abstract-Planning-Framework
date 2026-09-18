import unittest

from core.refinement.switches import collect_switches
from core.search.incremental import IncrementalSolver

PROGRAM = """
{ switch(2) }.
{ switch(10) }.
"""


class SwitchTests(unittest.TestCase):
    def test_switches_are_ordered_by_time_step_instead_of_lexically(self):
        switches = collect_switches(IncrementalSolver(PROGRAM))

        self.assertEqual([str(switch) for switch in switches], ["switch(2)", "switch(10)"])


if __name__ == "__main__":
    unittest.main()
