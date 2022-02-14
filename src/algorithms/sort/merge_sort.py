from typing import List


def merge(left: List[int], right: List[int]) -> List[int]:
    """Compare and merge two list in ascending order
    Takes O(n log n) time
    Args:
        left: First list
        right: Second list

    Returns:
        A merged list in ascending order
    """
    merged_array = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        # If left side is smaller add it and point to the next value on the left
        if left[i] < right[j]:
            merged_array.append(left[i])
            i += 1
            continue
        # If right side is smaller add it and point to the next value on the right

        merged_array.append(right[j])
        j += 1

    # If any number left on the left size, add them all
    while i < len(left):
        merged_array.append(left[i])
        i += 1
    # If any number left on the right size, add them all
    while j < len(right):
        merged_array.append(right[j])
        j += 1
    return merged_array


def merge_sort(values: List[int]) -> List[int]:
    """Sorts a list in ascending order

    Divide: Find the midpoint of the list and divide into sublists. Takes overall O(log n)
    Conquer: Recursively sort the sublists created in previous step Takes O(n log n)
    Combine: Merge the sorted sublists created in previous step
    Takes O(n log n) time. Takes O(n) space
    Args:
        values: A list of integers

    Returns:
     A new sorted list
    """

    if len(values) <= 1:
        return values

    midpoint = len(values) // 2

    left_half = values[:midpoint]
    right_half = values[midpoint:]

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)
