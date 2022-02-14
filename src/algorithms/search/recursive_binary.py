from typing import List


def recursive_binary_search(number_list: List[int], target: int):
    """Search the given target using recusive binary search in the list

    Args:
        number_list: A list of integers
        target: A target number to search

    Returns:
         True if found else False
    """

    if target is None or number_list is None:
        return False

    if not number_list:
        return False

    middle_index = len(number_list) // 2

    if number_list[middle_index] == target:
        return True

    if number_list[middle_index] < target:
        return recursive_binary_search(number_list[middle_index + 1 :], target)

    if number_list[middle_index] > target:
        return recursive_binary_search(number_list[:middle_index], target)
