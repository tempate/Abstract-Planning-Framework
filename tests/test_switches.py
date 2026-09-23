import unittest

from core.refinement.pipeline import _switches
from core.search.incremental import IncrementalSolver

PROGRAM = """
{ switch(2) }.
{ switch(10) }.
"""


class SwitchTests(unittest.TestCase):
    def test_switches_are_ordered_by_time_step_instead_of_lexically(self):
        switches = _switches(IncrementalSolver(PROGRAM))

        self.assertEqual([str(switch) for switch in switches], ["switch(2)", "switch(10)"])


if __name__ == "__main__":
    unittest.main()
