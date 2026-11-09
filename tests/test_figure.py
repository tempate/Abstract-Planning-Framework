import unittest

from experiments.figure import load_tracks, scaled_coverage, select


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


class ScaledFigureTests(unittest.TestCase):
    def test_coverage_is_the_share_proved_of_each_size(self):
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
            problem("a", 50, 1.0, None),
        ]

        self.assertEqual(scaled_coverage(problems, "ms"), [(2, 75.0), (50, 100.0)])
        self.assertEqual(scaled_coverage(problems, "abs-ms"), [(2, 75.0), (50, 0.0)])


class LoadTracksTests(unittest.TestCase):
    def test_the_scaled_track_loads_under_the_source_its_manifests_name(self):
        # Its manifests name it scaled/symmetries, which is how compare and paper look it up.
        tracks = load_tracks("HEAD", "scaled", [])

        self.assertEqual(list(tracks), ["symmetries"])
        self.assertTrue(tracks["symmetries"])
