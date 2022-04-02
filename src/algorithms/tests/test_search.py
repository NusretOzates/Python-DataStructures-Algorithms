from unittest import TestCase
from typing import Union
import enum
from ..search.binary import binary_search
from ..search.recursive_binary import recursive_binary_search
from ..search.linear import linear_search


class Result(enum.Enum):
    SUCCESS = "success"
    FAILURE = "failure"


class AcceptanceThreshold:
    def __init__(self, result: Union[int, None]) -> None:
        self._result = result

    def status(self):
        if self._result is None or self._result is False:
            return Result.FAILURE

        return Result.SUCCESS


class TestSearch(TestCase):
    def setUp(self) -> None:
        self.linear_test_data = (
            (([1, 2, 3, 4, 5, 6], 2), Result.SUCCESS),
            (([1, 2, 3, 4, 5, 6], 8), Result.FAILURE),
            (([], 5), Result.FAILURE),
            (([1, 2, 3, 4, 5], None), Result.FAILURE),
        )

        self.binary_test_data = (
            (([1, 2, 3, 4, 5, 6], 2), Result.SUCCESS),
            (([1, 2, 3, 4, 5, 6], 5), Result.SUCCESS),
            (([1, 2, 3, 4, 5, 6], 8), Result.FAILURE),
            (([], 5), Result.FAILURE),
            (([1, 2, 3, 4, 5], None), Result.FAILURE),
        )

    def test_linear_search(self):
        for test_data, expected in self.linear_test_data:
            with self.subTest(test_data=test_data):
                result = AcceptanceThreshold(linear_search(*test_data)).status()
                self.assertEqual(result, expected)

    def test_binary_search(self):
        for test_data, expected in self.binary_test_data:
            with self.subTest(test_data=test_data):
                result = AcceptanceThreshold(binary_search(*test_data)).status()
                self.assertEqual(result, expected)

    def test_recursive_binary_search(self):
        for test_data, expected in self.binary_test_data:
            with self.subTest(test_data=test_data):
                result = AcceptanceThreshold(recursive_binary_search(*test_data)).status()
                self.assertEqual(result, expected)
