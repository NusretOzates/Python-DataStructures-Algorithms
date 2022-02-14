from typing import List


def linear_search(number_list: List[int], target: int):
    """Search the given target linearly in the list

    Args:
        number_list: A list of integers
        target: A target number to search

    Returns:
         The index position of the target if found else None
    """

    if target is None or number_list is None:
        return None

    for index, number in enumerate(number_list):
        if number == target:
            return index

    return None
