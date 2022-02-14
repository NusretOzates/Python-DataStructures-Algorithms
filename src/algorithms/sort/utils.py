"""
Contains helper functions
"""

from typing import List


def is_sorted(elements: List[int]):
    """Checks if the elements in the list are sorted in ascending order

    Args:
        elements: List of integer

    Returns:
        True if sorted else False
    """

    if len(elements) <= 1:
        return True

    prev = elements[0]

    for element in elements[1:]:
        if prev > element:
            return False

        prev = element
    return True
