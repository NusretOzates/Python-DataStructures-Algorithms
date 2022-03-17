def how_sum(target_sum, numbers, memory: dict):
    # Is is passible to  generate target sum using these numbers
    # You can use element of the array as many times needed
    # numbers are non negative
    if target_sum in memory:
        return memory[target_sum]

    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    for element in numbers:
        remainder = target_sum - element
        comb = how_sum(remainder, numbers, memory)
        if comb is not None:
            memory[target_sum] = comb + [element]
            return comb + [element]

    memory[target_sum] = None
    return None


print(how_sum(7, [2, 3], {}))
print(how_sum(7, [5, 3, 4, 7], {}))
print(how_sum(7, [2, 4], {}))
print(how_sum(8, [2, 3, 5], {}))
print(how_sum(300, [7, 14], {}))
