"""
|W L W W L W|
|L L W W L W|
|W L W W W W|
|W W W L L W|
|W W W W W W|

Find land count

Time O(rc)
Space O(rc)
"""
from typing import List


def explore(area: List[List[str]], row: int, col: int, visited: set):
    row_in_bounds = 0 <= row <= len(area)
    col_in_bounds = 0 <= col <= len(area[0])
    is_visited = (row, col) in visited
    is_water = area[row][col] == "W"
    if not row_in_bounds or not col_in_bounds or is_visited or is_water:
        return False

    visited.add((row, col))

    explore(area, row - 1, col, visited)
    explore(area, row + 1, col, visited)
    explore(area, row, col - 1, visited)
    explore(area, row, col + 1, visited)

    return True


def island_count(area: List[List[str]]) -> int:
    visited = set()
    count = 0
    for r, row in enumerate(area):
        for c, column in enumerate(row):
            if explore(area, r, c, visited):
                count += 1
    return count


area = [
    ["W", "L", "W", "W", "L", "W"],
    ["L", "L", "W", "W", "L", "W"],
    ["W", "L", "W", "W", "W", "W"],
    ["W", "W", "W", "L", "L", "W"],
    ["W", "W", "W", "W", "W", "W"],
]

print(island_count(area))
