from ..sort import merge_sort, lms, selection_sort, quick_sort
from ...data_structures.linked_list import LinkedList


def test_merge_sort():
    result = merge_sort([])
    assert result == []

    result = merge_sort([1])
    assert result == [1]

    result = merge_sort([4, 1, 5])
    assert result == [1, 4, 5]

    result = merge_sort([4, 4, 4, 4, 4])
    assert result == [4, 4, 4, 4, 4]

    result = merge_sort([1, 2, 2, 3, 4])
    assert result == [1, 2, 2, 3, 4]


def test_selection_sort():
    result = selection_sort([])
    assert result == []

    result = selection_sort([1])
    assert result == [1]

    result = selection_sort([4, 1, 5])
    assert result == [1, 4, 5]

    result = selection_sort([4, 4, 4, 4, 4])
    assert result == [4, 4, 4, 4, 4]

    result = selection_sort([1, 2, 2, 3, 4])
    assert result == [1, 2, 2, 3, 4]


def test_quick_sort():
    result = quick_sort([])
    assert result == []

    result = quick_sort([1])
    assert result == [1]

    result = quick_sort([4, 1, 5])
    assert result == [1, 4, 5]

    result = quick_sort([4, 4, 4, 4, 4])
    assert result == [4, 4, 4, 4, 4]

    result = quick_sort([1, 2, 2, 3, 4])
    assert result == [1, 2, 2, 3, 4]


def test_linked_merge_sort():
    l_list = LinkedList([])
    result = lms(l_list)
    assert result.to_list() == []

    l_list = LinkedList([1])
    result = lms(l_list)
    assert result.to_list() == [1]

    l_list = LinkedList([4, 1, 5])
    result = lms(l_list)
    assert result.to_list() == [1, 4, 5]

    l_list = LinkedList([4, 4, 4, 4, 4])
    result = lms(l_list)
    assert result.to_list() == [4, 4, 4, 4, 4]

    l_list = LinkedList([1, 2, 2, 3, 4])
    result = lms(l_list)
    assert result.to_list() == [1, 2, 2, 3, 4]
