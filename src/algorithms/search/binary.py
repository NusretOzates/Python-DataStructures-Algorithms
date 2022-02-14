from typing import List


def binary_search(number_list: List[int], target: int):
    """Search the given target using binary search in the list

    Args:
        number_list: A list of integers
        target: A target number to search

    Returns:
         The index position of the target if found else None
    """

    if target is None or number_list is None:
        return None

    first_index = 0
    last_index = len(number_list) - 1

    while first_index <= last_index:
        # floor division
        middle_index = (first_index + last_index) // 2

        if number_list[middle_index] == target:
            return middle_index

        if number_list[middle_index] < target:
            first_index = middle_index + 1
            continue

        if number_list[middle_index] > target:
            last_index = middle_index - 1
            continue

    return None
