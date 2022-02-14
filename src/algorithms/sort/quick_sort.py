from typing import List


def quick_sort(elements: List[int]) -> List[int]:
    """
    Select a pivot element (first element in this case), create two lists
    that one contains elements smaller than pivot and other contains bigger than
    pivot. Then merge them together and you will have a sorted list.
    Takes O(n^2) time. Try reverse sorted list and you will see.
    Args:
        elements:

    Returns:

    """
    if len(elements) <= 1:
        return elements

    pivot = elements[0]

    first_list = [element for element in elements[1:] if element <= pivot]
    second_list = [element for element in elements[1:] if element > pivot]

    return quick_sort(first_list) + [pivot] + quick_sort(second_list)
