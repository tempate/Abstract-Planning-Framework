import unittest

from core.abstraction.detect_ladders import _find_sas_ladders
from core.integrations.sas import read_sas


def _variable(name, values):
    lines = ["begin_variable", name, "-1", str(len(values))]
    lines.extend(values)
    lines.append("end_variable")
    return lines


def _operator(name, effects):
    lines = ["begin_operator", name, "0", str(len(effects))]
    for variable, before, after in effects:
        lines.append(f"0 {variable} {before} {after}")
    lines.extend(["1", "end_operator"])
    return lines


def _task(variables, operators):
    lines = ["begin_version", "3", "end_version", "begin_metric", "0", "end_metric", str(len(variables))]
    for name, values in variables:
        lines.extend(_variable(name, values))
    lines.append(str(len(operators)))
    for name, effects in operators:
        lines.extend(_operator(name, effects))
    return "\n".join(lines) + "\n"


FUEL = ("var0", [f"Atom fuel(truck, f{step})" for step in range(8)])
SMALL = [("var1", ["Atom at(truck, l0)", "Atom at(truck, l1)"]), ("var2", ["Atom clear(l0)", "Atom clear(l1)"])]
# Fuel only ever drops, so its transitions never return to a value they left.
BURN = [("drive", [(0, step, step - 1)]) for step in range(1, 8)]


class SasLadderTests(unittest.TestCase):
    def test_an_outlying_variable_with_no_cycle_is_a_ladder(self):
        ladders = _find_sas_ladders(read_sas(_task([FUEL, *SMALL], BURN)))

        self.assertEqual(len(ladders), 1)
        self.assertEqual(ladders[0].predicate, "fuel")
        self.assertEqual(ladders[0].objects, tuple(f"f{step}" for step in range(8)))

    def test_a_variable_whose_transitions_cycle_is_not_a_ladder(self):
        refuel = BURN + [("refuel", [(0, 0, 7)])]

        self.assertEqual(_find_sas_ladders(read_sas(_task([FUEL, *SMALL], refuel))), ())

    def test_a_variable_no_larger_than_the_others_is_not_a_ladder(self):
        peers = [(f"var{index}", [f"Atom at(p{index}, l{step})" for step in range(8)]) for index in range(1, 4)]

        self.assertEqual(_find_sas_ladders(read_sas(_task([FUEL, *peers], BURN))), ())

    def test_a_variable_holding_one_predicate_over_two_objects_is_not_a_ladder(self):
        pairs = ("var0", [f"Atom road(l{step}, l{step + 1})" for step in range(8)])

        self.assertEqual(_find_sas_ladders(read_sas(_task([pairs, *SMALL], BURN))), ())


if __name__ == "__main__":
    unittest.main()
