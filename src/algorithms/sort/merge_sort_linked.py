from ...data_structures.linked_list import LinkedList


def merge(left: LinkedList, right: LinkedList) -> LinkedList:
    """Compare and merge two linked list in ascending order
    Takes O(n log n) time
    Args:
        left: First list
        right: Second list

    Returns:
        A merged list in ascending order
    """
    merged_list = LinkedList()

    while left.head and right.head:
        if left.head.value < right.head.value:
            merged_list.append(left.head.value)
            left.remove(0)
            continue

        merged_list.append(right.head.value)
        right.remove(0)

    last_position = merged_list.size() - 1

    # If any number left on the left size, add them all
    if left.head:
        merged_list.valueof(last_position).next_node = left.head

    # If any number left on the right size, add them all
    if right.head:
        merged_list.valueof(last_position).next_node = right.head

    return merged_list


def merge_sort(values: LinkedList) -> LinkedList:
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

    if values.size() <= 1:
        return values

    left_half, right_half = split(values)

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linked_list: LinkedList):
    """
    Divide the unsorted linked list at midpoint into sublists
    Args:
        linked_list:

    Returns:

    """

    if linked_list.head is None:
        left_half = linked_list
        right_half = None
        return left_half, right_half

    mid_point = (linked_list.size() - 1) // 2

    middle_node = linked_list.valueof(mid_point)

    left_half = linked_list
    right_half = LinkedList()
    right_half.head = middle_node.next_node
    middle_node.next_node = None

    return left_half, right_half
