import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import calculate # Импорт функции calculate из домашнего задания
from tests.constant_test_cases import PUBLIC_TEST_CASES, SECRET_TEST_CASES

ALL_TEST_CASES = PUBLIC_TEST_CASES + SECRET_TEST_CASES


def test_calculate():
    for test_case in ALL_TEST_CASES:
        test_input = test_case.get("test_input")
        expected = test_case.get("expected")
        assert calculate(test_input) == expected
