import contextlib
import csv
import io
import json
import os
import shlex
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import experiments.report
import experiments.submit
from core.integrations.paths import PARTIAL_GROUNDING_TRANSLATOR
from experiments.collect import FIELDS
from experiments.run import PROJECT_ROOT
from experiments.submit import (
    MANIFEST_NAME,
    _benchmark_tasks,
    _check_worktree_is_built,
    _missing_results,
    _not_submitted,
    _only,
    _set_aside_results_dir,
    _write_copperbench_config,
)
from scripts.setup import ARTIFACTS, ROOT as SETUP_ROOT
from scripts.utils.arguments import find_domain


class SubmitTests(unittest.TestCase):
    def test_new_suite_run_keeps_previous_results_beside_an_empty_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            results = Path(directory) / "runs"
            old_run = results / "old-run" / "result.json"
            old_run.parent.mkdir(parents=True)
            old_run.write_text("old result\n", encoding="utf-8")

            _set_aside_results_dir(results)

            self.assertTrue(results.is_dir())
            self.assertEqual(list(results.iterdir()), [])
            kept = [path for path in results.parent.iterdir() if path != results]
            self.assertEqual([path.name for path in kept[0].iterdir()], ["old-run"])

    def test_a_dry_run_submits_nothing_and_leaves_the_results_alone(self):
        argv = ["submit", "--dry-run", "--domains", "driverlog", "--problems", "p07"]
        with (
            patch("sys.argv", argv),
            patch.object(experiments.submit, "_check_worktree_is_built"),
            patch.object(experiments.submit, "_set_aside_results_dir") as set_aside,
            patch.object(experiments.submit, "_write_manifest") as manifest,
            patch.object(experiments.submit, "subprocess") as subprocesses,
            contextlib.redirect_stdout(io.StringIO()),
        ):
            experiments.submit.main()

        set_aside.assert_not_called()
        manifest.assert_not_called()
        subprocesses.run.assert_not_called()

    def test_only_a_built_worktree_submits(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaises(SystemExit) as refusal:
                _check_worktree_is_built(project_root=root)
            for artifact in (*ARTIFACTS.values(), Path(PARTIAL_GROUNDING_TRANSLATOR)):
                path = root / artifact.relative_to(SETUP_ROOT)
                path.parent.mkdir(parents=True, exist_ok=True)
                path.touch()

            _check_worktree_is_built(project_root=root)

        self.assertIn("plasp", str(refusal.exception))

    def test_prepares_one_copperbench_job_per_mode_and_problem(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            project = root / "project"
            project.mkdir()
            domain = project / "domain.pddl"
            problem = project / "p01.pddl"
            domain.touch()
            problem.touch()
            definition_dir = root / "definition"
            definition_dir.mkdir()

            config_file = _write_copperbench_config(
                [("abs-asp", "example", domain, problem, 0), ("asp", "example", domain, problem, None)],
                definition_dir=definition_dir,
            )
            config = json.loads(config_file.read_text(encoding="utf-8"))
            worker = shlex.split((definition_dir / "configs.txt").read_text(encoding="utf-8"))
            instances = (definition_dir / "instances.txt").read_text(encoding="utf-8").splitlines()

        self.assertEqual(config["working_dir"], os.path.relpath(PROJECT_ROOT, definition_dir))
        self.assertIn("experiments.run", worker)
        self.assertEqual(
            instances,
            [
                f"abs-asp example {domain.resolve()} {problem.resolve()} 0",
                f"asp example {domain.resolve()} {problem.resolve()} 0",
            ],
        )

    def test_discovers_the_problem_and_its_domain(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            benchmark = root / "example"
            benchmark.mkdir()
            domain = benchmark / "domain.pddl"
            problem = benchmark / "p01.pddl"
            domain.touch()
            problem.touch()

            runnable = {("example", "p01.pddl")}
            self.assertEqual(
                list(_benchmark_tasks(root, ["example"], runnable)), [("abs-asp", "example", domain, problem, 0)]
            )
            self.assertEqual(
                list(_benchmark_tasks(root, ["example"], runnable, modes=("abs-asp", "asp", "lama"))),
                [
                    ("abs-asp", "example", domain, problem, 0),
                    ("asp", "example", domain, problem, None),
                    ("lama", "example", domain, problem, None),
                ],
            )

    def test_an_abstract_mode_runs_once_per_class_from_the_first_rank_asked_for(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            benchmark = root / "example"
            benchmark.mkdir()
            (benchmark / "domain.pddl").touch()
            (benchmark / "p01.pddl").touch()

            tasks = _benchmark_tasks(
                root,
                ["example"],
                None,
                modes=("abs-asp", "asp"),
                class_counts={("example", "p01.pddl"): 3},
                from_rank=1,
            )

            self.assertEqual(
                [(mode, rank) for mode, _n, _d, _p, rank in tasks], [("abs-asp", 1), ("abs-asp", 2), ("asp", None)]
            )

    def test_an_abstract_mode_runs_only_the_class_another_mode_did_best_with(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            benchmark = root / "example"
            benchmark.mkdir()
            (benchmark / "domain.pddl").touch()
            (benchmark / "p01.pddl").touch()
            (benchmark / "p02.pddl").touch()

            tasks = _benchmark_tasks(
                root,
                ["example"],
                None,
                class_counts={("example", "p01.pddl"): 3, ("example", "p02.pddl"): 3},
                best={("example", "p01.pddl", "abs-lama"): 2, ("example", "p02.pddl", "abs-asp"): 1},
                best_of="abs-lama",
            )

            self.assertEqual([(problem.name, rank) for _m, _n, _d, problem, rank in tasks], [("p01.pddl", 2)])

    def test_concrete_modes_skip_the_problems_that_do_not_ground(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            benchmark = root / "example"
            benchmark.mkdir()
            (benchmark / "domain.pddl").touch()
            (benchmark / "p01.pddl").touch()
            (benchmark / "p02.pddl").touch()

            tasks = _benchmark_tasks(
                root, ["example"], None, modes=("abs-asp", "asp"), ungroundable={("example", "p02.pddl")}
            )

            self.assertEqual(
                [(mode, problem.name) for mode, _n, _d, problem, _r in tasks],
                [("abs-asp", "p01.pddl"), ("asp", "p01.pddl"), ("abs-asp", "p02.pddl")],
            )

    def test_a_run_leaves_out_what_an_earlier_run_submitted(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            benchmark = root / "example"
            benchmark.mkdir()
            (benchmark / "domain.pddl").touch()
            (benchmark / "p01.pddl").touch()
            manifest = root / MANIFEST_NAME
            earlier = [{"domain": "example", "problem": "p01.pddl", "mode": "abs-asp", "class": 1}]
            manifest.write_text(json.dumps({"expected_results": earlier}))

            tasks = _benchmark_tasks(root, ["example"], None, class_counts={("example", "p01.pddl"): 3})
            ranks = [rank for _mode, _domain, _domain_file, _problem, rank in _not_submitted(tasks, [manifest])]

        self.assertEqual(ranks, [0, 2])

    def test_a_retry_resubmits_only_the_results_a_run_never_returned_with_their_classes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            benchmark = root / "example"
            benchmark.mkdir()
            (benchmark / "domain.pddl").touch()
            (benchmark / "p01.pddl").touch()
            run = root / "run"
            run.mkdir()
            expected = [
                {"domain": "example", "problem": "p01.pddl", "mode": "abs-asp", "class": 1},
                {"domain": "example", "problem": "p01.pddl", "mode": "abs-asp", "class": 2},
                {"domain": "example", "problem": "p01.pddl", "mode": "asp", "class": None},
            ]
            (run / MANIFEST_NAME).write_text(json.dumps({"track": "sat/symmetries", "expected_results": expected}))
            for mode, rank in (("abs-asp", 2), ("asp", None)):
                result = {"domain": "example", "problem": "p01.pddl", "mode": mode, "class": rank, "status": "success"}
                result |= {
                    "return_code": 0,
                    "timed_out": False,
                    "wall_time_seconds": 1.0,
                    "output": "Plan found: yes\n",
                }
                (run / f"{mode}-{rank}.json").write_text(json.dumps(result))

            track, missing = _missing_results(run)
            tasks = _benchmark_tasks(
                root, ["example"], None, modes=("abs-asp", "asp"), class_counts={("example", "p01.pddl"): 3}
            )
            kept = [(mode, rank) for mode, _domain, _domain_file, _problem, rank in _only(tasks, missing)]

        self.assertEqual(track, "sat/symmetries")
        self.assertEqual(kept, [("abs-asp", 1)])

    def test_an_abstract_mode_runs_only_its_best_class_where_one_is_known(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            benchmark = root / "example"
            benchmark.mkdir()
            (benchmark / "domain.pddl").touch()
            (benchmark / "p01.pddl").touch()
            (benchmark / "p02.pddl").touch()
            results = root / "results.csv"
            with results.open("w", encoding="utf-8", newline="") as stream:
                writer = csv.DictWriter(stream, fieldnames=FIELDS)
                writer.writeheader()
                # p01 ran every class and the middle one solved fastest. p02 never ran.
                for rank, status, seconds in (
                    ("0", "timed out", "1800"),
                    ("1", "success", "40"),
                    ("2", "success", "90"),
                ):
                    writer.writerow(
                        {field: "" for field in FIELDS}
                        | {"domain": "example", "problem": "p01.pddl", "mode": "abs-asp", "class": rank}
                        | {"status": status, "wall_time_seconds": seconds}
                    )

            tasks = _benchmark_tasks(
                root,
                ["example"],
                None,
                class_counts={("example", "p01.pddl"): 3, ("example", "p02.pddl"): 2},
                best=experiments.report.best_classes(results),
            )

            self.assertEqual(
                [(problem.name, rank) for _m, _n, _d, problem, rank in tasks],
                [("p01.pddl", 1), ("p02.pddl", 0), ("p02.pddl", 1)],
            )

    def test_only_problems_with_an_abstraction_class_are_submitted(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            benchmark = root / "example"
            benchmark.mkdir()
            (benchmark / "domain.pddl").touch()
            (benchmark / "p01.pddl").touch()
            (benchmark / "p02.pddl").touch()

            required = list(_benchmark_tasks(root, ["example"], runnable={("example", "p02.pddl")}))
            not_required = list(_benchmark_tasks(root, ["example"], runnable=None))

        self.assertEqual([task[3].name for task in required], ["p02.pddl"])
        self.assertEqual([task[3].name for task in not_required], ["p01.pddl", "p02.pddl"])

    def test_a_subset_run_names_its_domains_and_problems(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for domain_name in ("one", "two"):
                benchmark = root / domain_name
                benchmark.mkdir()
                (benchmark / "domain.pddl").touch()
                (benchmark / "p01.pddl").touch()
                (benchmark / "p02.pddl").touch()
            suite = ["one", "two"]

            by_domain = _benchmark_tasks(root, suite, runnable=None, domains=["two"])
            by_problem = _benchmark_tasks(root, suite, runnable=None, domains=["two"], problems=["p02"])
            by_file_name = _benchmark_tasks(root, suite, runnable=None, problems=["p02.pddl"])

            self.assertEqual({name for _m, name, _d, _p, _r in by_domain}, {"two"})
            self.assertEqual([(n, p.name) for _m, n, _d, p, _r in by_problem], [("two", "p02.pddl")])
            self.assertEqual({p.name for _m, _n, _d, p, _r in by_file_name}, {"p02.pddl"})

    def test_flags_that_would_change_nothing_are_refused(self):
        combinations = (
            ["--best-class-of", "abs-asp", "--classes", "all"],
            ["--from-rank", "2"],
            ["--retry-missing", "runs", "--modes", "asp"],
        )
        for flags in combinations:
            with (
                self.subTest(flags=flags),
                patch("sys.argv", ["submit", *flags]),
                contextlib.redirect_stderr(io.StringIO()),
                self.assertRaises(SystemExit) as refusal,
            ):
                experiments.submit.main()
            self.assertEqual(refusal.exception.code, 2)

    def test_a_misspelled_domain_is_refused_rather_than_submitting_nothing(self):
        with self.assertRaises(SystemExit) as refusal:
            list(_benchmark_tasks(Path("/nowhere"), ["driverlog"], runnable=None, domains=["driverlgo"]))

        self.assertIn("driverlgo", str(refusal.exception))

    def test_a_problem_whose_name_holds_dom_is_still_a_problem(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "example").mkdir()
            for name in ("domain.pddl", "p01-domain.pddl", "random01.pddl"):
                (root / "example" / name).touch()

            tasks = list(_benchmark_tasks(root, ["example"], runnable=None))

        self.assertEqual([task[3].name for task in tasks], ["random01.pddl"])


class DomainLookupTests(unittest.TestCase):
    def _collection(self, names):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        directory = Path(temporary.name)
        for name in names:
            (directory / name).write_text("", encoding="utf-8")
        return directory

    def test_finds_a_domain_shared_by_every_problem(self):
        directory = self._collection(["domain.pddl", "p01.pddl"])

        self.assertEqual(find_domain(directory / "p01.pddl").name, "domain.pddl")

    def test_reports_a_problem_with_no_domain(self):
        directory = self._collection(["p01.pddl"])

        with self.assertRaises(FileNotFoundError):
            find_domain(directory / "p01.pddl")


if __name__ == "__main__":
    unittest.main()
