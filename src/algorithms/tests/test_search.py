from typing import Union, Tuple
import enum
import pytest
from ..search.binary import binary_search
from ..search.recursive_binary import recursive_binary_search
from ..search.linear import linear_search


class Result(enum.Enum):
    SUCCESS = "success"
    FAILURE = "failure"


class AcceptanceThreshold:
    def __init__(self, result: Union[int, None]) -> None:
        self._result = result

    def status(self) -> Result:
        if self._result is None or self._result is False:
            return Result.FAILURE

        return Result.SUCCESS


@pytest.mark.parametrize(
    "test_data, expected",
    (
        (([1, 2, 3, 4, 5, 6], 2), Result.SUCCESS),
        (([1, 2, 3, 4, 5, 6], 8), Result.FAILURE),
        (([], 5), Result.FAILURE),
        (([1, 2, 3, 4, 5], None), Result.FAILURE),
    ),
)
def test_linear_search(test_data: Tuple[list, int], expected: Result) -> None:
    result = AcceptanceThreshold(linear_search(*test_data)).status()
    assert result == expected


@pytest.mark.parametrize(
    "test_data, expected",
    (
        (([1, 2, 3, 4, 5, 6], 2), Result.SUCCESS),
        (([1, 2, 3, 4, 5, 6], 5), Result.SUCCESS),
        (([1, 2, 3, 4, 5, 6], 8), Result.FAILURE),
        (([], 5), Result.FAILURE),
        (([1, 2, 3, 4, 5], None), Result.FAILURE),
    ),
)
def test_binary_search(test_data: Tuple[list, int], expected: Result) -> None:
    result = AcceptanceThreshold(binary_search(*test_data)).status()
    assert result == expected


@pytest.mark.parametrize(
    "test_data, expected",
    (
        (([1, 2, 3, 4, 5, 6], 2), Result.SUCCESS),
        (([1, 2, 3, 4, 5, 6], 5), Result.SUCCESS),
        (([1, 2, 3, 4, 5, 6], 8), Result.FAILURE),
        (([], 5), Result.FAILURE),
        (([1, 2, 3, 4, 5], None), Result.FAILURE),
    ),
)
def test_recursive_binary_search(test_data: Tuple[list, int], expected: Result) -> None:
    result = AcceptanceThreshold(recursive_binary_search(*test_data)).status()
    assert result == expected
