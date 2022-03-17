from typing import List, Union


def best_sum(target_sum: int, numbers: List[int], memory: dict) -> Union[List[int], None]:
    """ Find the shortest sum using numbers in the array

    Is it passible to generate target sum using these numbers
    You can use element of the array as many times needed
    numbers are non negative
    Args:
        target_sum: Target number to find as a sum of numbers in the list
        numbers: Numbers you can use to get targer sum
        memory: A memory to get previously calculated results

    Returns:
        List of ints to get the target sum or None
    """
    if target_sum in memory:
        return memory[target_sum]

    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    shortest_com = None

    for element in numbers:

        remainder = target_sum - element
        remainder_comb = best_sum(remainder, numbers, memory)

        if remainder_comb is not None:
            combination = remainder_comb + [element]
            memory[target_sum] = combination
            if shortest_com is None or len(combination) < len(shortest_com):
                shortest_com = combination

    memory[target_sum] = shortest_com
    return shortest_com



