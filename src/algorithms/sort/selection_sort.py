from typing import List


def index_of_min(elements: List[int]) -> int:
    minimum_index = 0
    for index, element in enumerate(elements):
        if element < elements[minimum_index]:
            minimum_index = index
            continue
    return minimum_index


def selection_sort(elements: List[int]) -> List[int]:
    """Selection sort algorithm for sorting in ascending order
    It finds the minimum element in the unsorted list O(n)
    Adds it to the sorted list
    Remove the element from the unsorted list
    Takes O(n^2) times
    Args:
        elements: List of int to sort

    Returns:
        Sorted list of int
    """
    final_list = []

    while len(elements) > 0:
        min_index = index_of_min(elements)
        final_list.append(elements[min_index])
        elements.pop(min_index)

    return final_list
