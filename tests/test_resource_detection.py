import tempfile
import unittest
from pathlib import Path

from core.integrations.numeric_fast_downward import parse_resources, read_sas_variables, varying_objects

DETECTOR_OUTPUT = """we are here
Detection time: 0.374387s
Found 2/9 resource variables
Found 1222/1294 consumer actions
Found 0/1294 producer actions
1 var6 propositional 
8 var0 propositional 
0 var8 resource 
2 var7 resource 
"""

FUEL = ("Atom fuel(t0, level0)", "Atom fuel(t0, level1)", "Atom fuel(t0, level2)")
AXIOM = ("Atom new-axiom@0()", "NegatedAtom new-axiom@0()")
TRUCK = ("Atom at(t0, l0)", "Atom at(t0, l1)")


class VaryingObjectTests(unittest.TestCase):
    def test_the_objects_are_the_ones_that_tell_the_values_apart(self):
        # t0 is the same in every value, so only the levels are the ladder.
        self.assertEqual(varying_objects(FUEL), ("level0", "level1", "level2"))

    def test_a_variable_without_arguments_carries_no_objects(self):
        self.assertEqual(varying_objects(AXIOM), ())


class ParseResourceTests(unittest.TestCase):
    def test_resource_variables_come_back_with_their_objects(self):
        resources = parse_resources(DETECTOR_OUTPUT, {"var7": FUEL, "var8": AXIOM})

        self.assertEqual([resource.name for resource in resources], ["var7"])
        self.assertEqual(resources[0].objects, ("level0", "level1", "level2"))

    def test_the_widest_variable_comes_first(self):
        resources = parse_resources(
            DETECTOR_OUTPUT.replace("var8 resource", "var9 resource"), {"var7": TRUCK, "var9": FUEL}
        )

        self.assertEqual([len(resource.objects) for resource in resources], [3, 2])


class SasReadingTests(unittest.TestCase):
    def test_every_variable_is_read_with_its_values(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory, "output.sas")
            path.write_text(
                "begin_version\n4\nend_version\n"
                "begin_variable\nvar0\n-1\n2\nAtom at(t0, l0)\nAtom at(t0, l1)\nend_variable\n"
                "begin_variable\nvar1\n-1\n1\nAtom fuel(t0, level0)\nend_variable\n",
                encoding="utf-8",
            )
            variables = read_sas_variables(path)

        self.assertEqual(variables["var0"], ("Atom at(t0, l0)", "Atom at(t0, l1)"))
        self.assertEqual(variables["var1"], ("Atom fuel(t0, level0)",))


if __name__ == "__main__":
    unittest.main()
