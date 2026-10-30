import tempfile
import unittest
from pathlib import Path

from experiments.deletes import TRANSLATOR, count

DOMAIN = """
(define (domain movers)
  (:requirements :strips :typing)
  (:types mover location)
  (:predicates (at ?m - mover ?l - location) (path ?from ?to - location))
  (:action walk
    :parameters (?m - mover ?from ?to - location)
    :precondition (and (at ?m ?from) (path ?from ?to))
    :effect (and (at ?m ?to) (not (at ?m ?from)))))
"""

PROBLEM = """
(define (problem movers-task)
  (:domain movers)
  (:objects m1 m2 m3 - mover truck house - location)
  (:init (at m1 truck) (at m2 truck) (at m3 truck) (path truck house) (path house truck))
  (:goal (and (at m1 house) (at m3 house))))
"""


@unittest.skipUnless(TRANSLATOR.is_dir(), "needs the Fast Downward translator in lib/downward")
class GroundedDeleteTests(unittest.TestCase):
    def test_a_relaxed_delete_counts_every_grounding_and_separates_the_ones_on_the_class(self):
        with tempfile.TemporaryDirectory() as directory:
            domain, problem = Path(directory) / "domain.pddl", Path(directory) / "problem.pddl"
            domain.write_text(DOMAIN)
            problem.write_text(PROBLEM)
            spec = {
                "domain": "movers",
                "problem": "problem.pddl",
                "domain_file": str(domain),
                "problem_file": str(problem),
                "classes": [[0, "m1 m2"]],
            }

            (row,) = count(spec)

        # Every walk relaxes its delete, but only the walks of m1 and m2 name the class.
        self.assertEqual(row["ground_relaxed"], row["ground_deletes"])
        self.assertLess(row["ground_relaxed_on_class"], row["ground_relaxed"])
        self.assertGreater(row["ground_relaxed_on_class"], 0)
