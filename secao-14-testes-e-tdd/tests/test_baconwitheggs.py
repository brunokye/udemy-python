"""
TDD - Test Driven Development (Desenvolvimento guiado por testes)

RED
Parte 1 - Criar o teste e ver falhar

GREEN
Parte 2 - Criar o codigo e ver o teste passar

Refactor
Parte 3 - Melhorar o codigo
"""

try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "../src",
            )
        )
    )
except Exception as e:
    print(f"An unexpected error occurred: {e}")

import unittest
from baconwitheggs import bacon_with_eggs  # type: ignore


class TestBaconWithEggs(unittest.TestCase):
    def test_baconwitheggs_raise_error_if_not_int(self):
        with self.assertRaises(Exception):
            bacon_with_eggs("0")

    def test_baconwitheggs_return_bacon_with_eggs_if_multiple_of_3_and_5(self):
        entries = (15, 30, 45, 60)
        output = "Bacon with eggs"

        for entry in entries:
            with self.subTest(entry=entry):
                self.assertEqual(
                    bacon_with_eggs(entry),
                    output,
                    msg=f"{entry} does not returned {output}",
                )

    def test_baconwitheggs_return_starve_if_not_multiple_of_3_and_5(self):
        entries = (1, 2, 4, 7, 8)
        output = "Starve"

        for entry in entries:
            with self.subTest(entry=entry):
                self.assertEqual(
                    bacon_with_eggs(entry),
                    output,
                    msg=f"{entry} does not returned {output}",
                )

    def test_baconwitheggs_return_bacon_if__multiple_of_3(self):
        entries = (3, 6, 9, 12)
        output = "Bacon"

        for entry in entries:
            with self.subTest(entry=entry):
                self.assertEqual(
                    bacon_with_eggs(entry),
                    output,
                    msg=f"{entry} does not returned {output}",
                )

    def test_baconwitheggs_return_eggs_if__multiple_of_5(self):
        entries = (5, 10, 20, 25)
        output = "Eggs"

        for entry in entries:
            with self.subTest(entry=entry):
                self.assertEqual(
                    bacon_with_eggs(entry),
                    output,
                    msg=f"{entry} does not returned {output}",
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
