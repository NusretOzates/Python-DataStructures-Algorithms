def first_and_last(arr, target: int):
    for i in range(len(arr)):
        if arr[i] == target:
            start = i
            for index, element in enumerate(arr[start + 1 :]):
                if element != target:
                    return [start, start + index]

    return [-1, -1]


print(first_and_last([2, 4, 5, 5, 5, 5, 5, 7, 9, 9], 5))
print(first_and_last([2, 4, 5, 5, 5, 5, 5, 7, 9, 9], 3))
