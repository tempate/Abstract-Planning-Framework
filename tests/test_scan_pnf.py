"""Tests for the positive-normal-form scan over benchmark domains."""

import tempfile
import unittest
from pathlib import Path

from scripts.scan_pnf import INERT, NEEDS_PNF, POSITIVE, scan

DOMAIN = """
(define (domain example)
  (:requirements :strips :typing)
  (:types truck)
  (:predicates (loaded ?t - truck) (seen ?t - truck) (ready))
  (:action drive
    :parameters (?t - truck)
    :precondition (and {precondition})
    :effect (and (seen ?t) {effect}))
)
"""

PROBLEM = """
(define (problem task)
  (:domain example)
  (:objects t1 - truck)
  (:init (ready))
  (:goal (and {goal})))
"""


class ScanPnfTests(unittest.TestCase):
    def _scan(self, precondition, effect, goal="(seen t1)", collapsed=()):
        """Write a one-action domain with one problem, and scan the directory."""
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        path = Path(directory.name)
        (path / "domain.pddl").write_text(DOMAIN.format(precondition=precondition, effect=effect), encoding="utf-8")
        (path / "p01.pddl").write_text(PROBLEM.format(goal=goal), encoding="utf-8")
        return scan(path, collapsed)

    def test_a_negated_predicate_that_an_action_deletes_needs_pnf(self):
        result = self._scan("(not (loaded ?t))", "(not (loaded ?t))")

        self.assertEqual(result["verdict"], NEEDS_PNF)
        self.assertIn("loaded", result["reachable"])

    def test_a_negated_predicate_nothing_deletes_is_inert(self):
        # Nothing can relax a delete that does not exist, so the negation is safe.
        result = self._scan("(not (loaded ?t))", "(loaded ?t)")

        self.assertEqual(result["verdict"], INERT)
        self.assertEqual(result["reachable"], [])

    def test_negated_equality_alone_leaves_a_domain_positive(self):
        result = self._scan("(not (= ?t ?t))", "(loaded ?t)")

        self.assertEqual(result["verdict"], POSITIVE)
        self.assertEqual(result["inequalities"], 1)

    def test_a_negated_goal_counts_like_a_negated_precondition(self):
        result = self._scan("(ready)", "(not (loaded ?t))", goal="(not (loaded t1))")

        self.assertEqual(result["verdict"], NEEDS_PNF)
        self.assertEqual(result["negated_fluent_goal"], 1)

    def test_a_reachable_negation_is_reported_against_the_collapsed_type(self):
        result = self._scan("(not (loaded ?t))", "(not (loaded ?t))", collapsed=("truck",))

        self.assertEqual(result["on_collapsed"], ["loaded"])


if __name__ == "__main__":
    unittest.main()
