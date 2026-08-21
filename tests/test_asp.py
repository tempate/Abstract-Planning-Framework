import unittest

from core.asp import join_asp


class AbstractProgramTests(unittest.TestCase):
    def test_join_asp_normalizes_fragment_boundaries(self):
        self.assertEqual(join_asp("first.\n", "second."), "first.\nsecond.\n")


if __name__ == "__main__":
    unittest.main()
