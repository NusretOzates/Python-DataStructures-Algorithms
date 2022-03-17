def can_sum(target_sum, numbers, memory: dict):
    # Is is passible to  generate target sum using these numbers
    # You can use element of the array as many times needed
    # numbers are non negative
    if target_sum in memory:
        return memory[target_sum]

    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for element in numbers:
        remainder = target_sum - element
        if can_sum(remainder, numbers, memory):
            memory[target_sum] = True
            return True

    memory[target_sum] = False
    return False


print(can_sum(7, [2, 3], {}))
print(can_sum(7, [5, 3, 4, 7], {}))
print(can_sum(7, [2, 4], {}))
print(can_sum(8, [2, 3, 5], {}))
print(can_sum(300, [7, 14], {}))
