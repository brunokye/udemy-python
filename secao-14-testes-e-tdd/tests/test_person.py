"""
class Person
    __init__
        first_name str
        last_name str
        get_data bool (initial value False)

    API:
        get_all_data -> method
            OK
            404
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
from unittest.mock import patch
from Person import Person  # type: ignore


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.p1 = Person("John", "Doe")
        self.p2 = Person("Mary", "Jane")

    def test_person_first_name_have_correct_value(self):
        self.assertEqual(self.p1.first_name, "John")
        self.assertEqual(self.p2.first_name, "Mary")

    def test_person_last_name_have_correct_value(self):
        self.assertEqual(self.p1.last_name, "Doe")
        self.assertEqual(self.p2.last_name, "Jane")

    def test_person_first_name_is_str(self):
        self.assertIsInstance(self.p1.first_name, str)
        self.assertIsInstance(self.p2.first_name, str)

    def test_person_last_name_is_str(self):
        self.assertIsInstance(self.p1.last_name, str)
        self.assertIsInstance(self.p2.last_name, str)

    def test_person_get_data_initial_value_false(self):
        self.assertFalse(self.p1.get_data)
        self.assertFalse(self.p2.get_data)

    def test_person_get_all_data_sucess_ok(self):
        with patch("requests.get") as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.get_all_data(), "CONNECTED")
            self.assertTrue(self.p1.get_data)

            self.assertEqual(self.p2.get_all_data(), "CONNECTED")
            self.assertTrue(self.p2.get_data)

    def test_person_get_all_data_failure_404(self):
        with patch("requests.get") as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.get_all_data(), "ERROR 404")
            self.assertFalse(self.p1.get_data)

            self.assertEqual(self.p2.get_all_data(), "ERROR 404")
            self.assertFalse(self.p2.get_data)

    def test_person_get_all_data_sucess_and_failure_sequencial(self):
        with patch("requests.get") as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.get_all_data(), "CONNECTED")
            self.assertTrue(self.p1.get_data)

            self.assertEqual(self.p2.get_all_data(), "CONNECTED")
            self.assertTrue(self.p2.get_data)

            fake_request.return_value.ok = False

            self.assertEqual(self.p1.get_all_data(), "ERROR 404")
            self.assertFalse(self.p1.get_data)

            self.assertEqual(self.p2.get_all_data(), "ERROR 404")
            self.assertFalse(self.p2.get_data)


if __name__ == "__main__":
    unittest.main(verbosity=2)
