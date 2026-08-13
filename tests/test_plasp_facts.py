import tempfile
import unittest
from pathlib import Path

from core.integrations.plasp import append_pddl_facts_to_asp


class PddlFactTests(unittest.TestCase):
    def test_indented_no_mystery_facts_are_appended(self):
        with tempfile.TemporaryDirectory() as directory:
            directory = Path(directory)
            problem = directory / "problem.pddl"
            problem.write_text(
                "    (fuelcost level5 l1 l2)\n"
                "\t(sum level90 level5 level95)\n",
                encoding="utf-8",
            )
            asp = directory / "problem.lp"
            asp.write_text("% existing encoding\n", encoding="utf-8")

            append_pddl_facts_to_asp(problem, asp)

            output = asp.read_text(encoding="utf-8")
            self.assertIn('fuelcost("level5","l1","l2").', output)
            self.assertIn('sum("level90","level5","level95").', output)


if __name__ == "__main__":
    unittest.main()
