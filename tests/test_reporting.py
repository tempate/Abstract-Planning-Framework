import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import Mock

from scripts.utils.reporting import print_planning_result


class ReportingTests(unittest.TestCase):
    def test_time_step_plan_ignores_occurs_sometime_atoms(self):
        result = {
            "horizon": 2,
            "numPlans": 1,
            "plans": [[
                'occurs(action(("unload","truck")),2)',
                'occurs_sometime(action(("drive","destination")))',
                'occurs(action(("drive","destination")),1)',
            ]],
            "success": True,
            "timings": {"total_time": 0.0},
        }

        output = io.StringIO()
        with redirect_stdout(output):
            print_planning_result(result, Mock())

        reported = output.getvalue()
        self.assertNotIn("occurs_sometime", reported)
        self.assertLess(
            reported.index('occurs(action(("drive","destination")),1)'),
            reported.index('occurs(action(("unload","truck")),2)'),
        )


if __name__ == "__main__":
    unittest.main()
