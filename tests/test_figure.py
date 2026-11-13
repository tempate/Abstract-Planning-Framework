import unittest

from experiments.figure import select


def _row(mode, problem="p01.pddl", rank=""):
    return {"domain": "d", "problem": problem, "mode": mode, "class": rank}


def _manifest(track, *entries):
    return {
        "track": track,
        "expected_results": [{"domain": "d", "mode": m, "problem": p, "class": c} for m, p, c in entries],
    }


class FigureSelectionTests(unittest.TestCase):
    def test_a_manifest_keeps_only_the_classes_its_track_submitted(self):
        rows = [_row("abs-asp", rank="0"), _row("abs-asp", rank="1"), _row("abs-lama", rank="0"), _row("asp")]
        manifests = [
            _manifest("sat/symmetries", ("abs-asp", "p01.pddl", 1)),
            # Another track's run of the same problem says nothing about this one.
            _manifest("sat/resources", ("abs-asp", "p01.pddl", 0)),
        ]

        selected = select(rows, "sat", "symmetries", manifests)

        # abs-lama ran no class here, so its rows all stay, and so does the baseline.
        self.assertEqual(
            {(row["mode"], row["class"]) for row in selected},
            {("abs-asp", "1"), ("abs-lama", "0"), ("asp", "")},
        )
