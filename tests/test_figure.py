import unittest

from experiments.figure import extra_actions_class, scaled_coverage, select


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

    def test_old_mode_names_read_as_the_new_ones(self):
        rows = [_row("fd-lmcut"), _row("abs-fd", rank="2")]
        manifests = [_manifest("opt/symmetries", ("abs-fd", "p01.pddl", 2))]

        selected = select(rows, "opt", "symmetries", manifests)

        self.assertEqual({row["mode"] for row in selected}, {"lmcut", "abs-lmcut"})


class ExtraActionsTests(unittest.TestCase):
    def test_extra_actions_fall_into_the_figures_colour_classes(self):
        def problem(abstract_length, optimal_length="10"):
            return {
                "asp": {"status": "success", "plan_length": optimal_length},
                "lmcut": {"status": "timed out", "plan_length": ""},
                "abs-asp": {"status": "success" if abstract_length else "timed out", "plan_length": abstract_length},
            }

        classes = [extra_actions_class(problem(length), "abs-asp", "lmcut") for length in ("10", "12", "15", "16", "")]

        self.assertEqual(classes, [0, 1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()


class ScaledFigureTests(unittest.TestCase):
    def test_coverage_is_the_share_proved_of_each_size_half_the_base_problems_reach(self):
        def problem(domain, size, ms, abs_ms):
            def row(seconds):
                return {
                    "domain": f"{domain}/size-{size}",
                    "problem": "p01.pddl",
                    "status": "success" if seconds else "out of memory",
                    "verdict": "unsolvable" if seconds else "",
                    "wall_time_seconds": str(seconds or 0),
                }

            return {"ms": row(ms), "abs-ms": row(abs_ms)}

        problems = [
            problem("a", 2, 1.0, 10.0),
            problem("b", 2, None, 20.0),
            problem("c", 2, 2.0, 40.0),
            problem("d", 2, 9.0, None),
            # Size 50 reaches one of the four base problems, fewer than half.
            problem("a", 50, 1.0, 1.0),
        ]

        self.assertEqual(scaled_coverage(problems, "ms"), [(2, 75.0)])
        self.assertEqual(scaled_coverage(problems, "abs-ms"), [(2, 75.0)])
