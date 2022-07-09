"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
"""
from typing import List


def zero_matrix(matrix: List[List[int]]):
    to_zero_row = set()
    to_zero_col = set()

    row_count = len(matrix)
    col_count = len(matrix[0])

    for row_index, row in enumerate(matrix):

        for col_index, col in enumerate(row):
            if col == 0:
                to_zero_col.add(col_index)
                to_zero_row.add(row_index)

    for row in to_zero_row:
        matrix[row] = [0] * col_count
    for col in to_zero_col:
        for row in range(row_count):
            matrix[row][col] = 0

    return matrix


print(
    zero_matrix(
        [
            [1, 2, 3, 4, 5],
            [1, 2, 3, 0, 0],
            [1, 2, 0, 4, 5],
            [1, 2, 3, 4, 5],
        ]
    )
)
