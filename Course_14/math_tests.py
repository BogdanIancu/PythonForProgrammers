import unittest
from parameterized import parameterized


def division(a, b):
    return a / b


class MathTests(unittest.TestCase):
    def test_division_integer(self):
        self.assertEqual(2, division(10, 5), "The division doesn't work")

    def test_division_floating_point(self):
        self.assertAlmostEqual(0.66, division(2, 3), msg="The division doesn't work for floating points", delta=0.009)

    @parameterized.expand([
        (7, 3, 2.33),
        (5, 2, 2.5),
        (6, 4, 1.5),
        (10, 2, 5),
    ])
    def test_division(self, a, b, expected_result):
        self.assertAlmostEqual(division(a, b), expected_result, delta=0.01)
