from src.algorithms.dynamic_programming.best_sum import best_sum


def test_best_sum():

    assert best_sum(7, [5, 3, 4, 7], {}) == [7]
    assert best_sum(8, [2, 3, 5], {}) == [5, 3] or best_sum(8, [2, 3, 5], {}) == [3, 5]
    assert best_sum(8, [1, 4, 5], {}) == [4, 4]
    assert best_sum(100, [1, 2, 5, 25], {}) == [25, 25, 25, 25]
