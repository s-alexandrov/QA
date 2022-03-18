import unittest
from tests.test_cases import TEST_CASES
from main import insert_table
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class BDTestCase(unittest.TestCase):
    """Такие же тестовые случаи, но реализованные через unittest."""

    def setUp(self):
        """Начальные условия для тестов."""
        self.test_cases = TEST_CASES

    def test_calculate(self):
        """Получения данных."""
        for test_case in self.test_cases:
            test_input = test_case.get("test_input")
            expected = test_case.get("expected")
            self.assertEqual(insert_table(test_input), expected)
