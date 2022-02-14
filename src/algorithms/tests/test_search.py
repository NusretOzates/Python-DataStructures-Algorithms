from ..search.binary import binary_search
from ..search.recursive_binary import recursive_binary_search
from ..search.linear import linear_search


def test_linear_search():
    result = linear_search([1, 2, 3, 4, 5, 6], 2)
    assert result is not None

    result = linear_search([1, 2, 3, 4, 5, 6], 8)
    assert result is None

    result = linear_search([], 5)
    assert result is None

    result = linear_search([1, 2, 3, 4, 5], None)
    assert result is None


def test_binary_search():
    result = binary_search([1, 2, 3, 4, 5, 6], 2)
    assert result == 1

    result = binary_search([1, 2, 3, 4, 5, 6], 5)
    assert result == 4

    result = binary_search([1, 2, 3, 4, 5, 6], 8)
    assert result is None

    result = binary_search([], 5)
    assert result is None

    result = binary_search([1, 2, 3, 4, 5], None)
    assert result is None


def test_recursive_binary_search():
    result = recursive_binary_search([1, 2, 3, 4, 5, 6], 2)
    assert result

    result = recursive_binary_search([1, 2, 3, 4, 5, 6], 5)
    assert result

    result = recursive_binary_search([1, 2, 3, 4, 5, 6], 8)
    assert not result

    result = recursive_binary_search([], 5)
    assert not result

    result = recursive_binary_search([1, 2, 3, 4, 5], None)
    assert not result
