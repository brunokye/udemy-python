import unittest
from calculator import new_sum


class TestCalculator(unittest.TestCase):
    def test_sum_5_and_5_returns_10(self):
        self.assertEqual(new_sum(5, 5), 10)

    def test_sum_5_negative_and_5_returns_0(self):
        self.assertEqual(new_sum(-5, 5), 0)

    def test_sum_many_entries(self):
        entries = (
            (10, 10, 20),
            (5, 5, 10),
            (1.5, 1.5, 3),
            (-5, 5, 0),
            (100, 100, 200),
            (0, 0, 0),
            (-1, 1, 0),
        )

        for entry in entries:
            with self.subTest(entry):
                x, y, output = entry
                self.assertEqual(new_sum(x, y), output)

    def test_sum_x_is_not_a_number(self):
        with self.assertRaises(AssertionError):
            new_sum("11", 5)

    def test_sum_y_is_not_a_number(self):
        with self.assertRaises(AssertionError):
            new_sum(5, "11")


unittest.main(verbosity=2)
