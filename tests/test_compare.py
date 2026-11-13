import unittest

from experiments.compare import tables


def _problem(name, **times):
    """One problem's rows, a mode solved when given a time and unsolved when given None."""
    rows = {}
    for mode, seconds in times.items():
        rows[mode] = {
            "domain": "d",
            "problem": name,
            "status": "success" if seconds else "timed out",
            "wall_time_seconds": str(seconds or 0),
        }
    return rows


class CompareTablesTests(unittest.TestCase):
    def test_tables_bold_the_better_count_and_take_runtimes_over_problems_both_solve(self):
        base = [
            _problem("p1", **{"abs-asp": 10.0}),
            _problem("p2", **{"abs-asp": None}),
            _problem("p3", **{"abs-asp": 30.0}),
        ]
        branch = [
            _problem("p1", **{"abs-asp": 20.0}),
            _problem("p2", **{"abs-asp": 5.0}),
            _problem("p3", **{"abs-asp": 40.0}),
        ]

        text = tables({"sat resources": (base, branch, {"abs-asp"}), "opt resources": (base, base, set())})

        # p2 is new on the branch, so the medians cover p1 and p3 alone.
        self.assertIn("| ASPᵅ | 2 → **3** | |", text)
        self.assertIn("| ASPᵅ | 20.0 → 30.0 s | |", text)
