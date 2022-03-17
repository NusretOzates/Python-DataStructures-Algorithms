"""
|W L W W L W|
|L L W W L W|
|W L W W W W|
|W W W L L W|
|W W W W W W|

Find minumum land size

Time O(rc)
Space O(rc)
"""
from typing import List


def explore(area: List[List[str]], row: int, col: int, visited: set):
    row_in_bounds = 0 <= row < len(area)
    col_in_bounds = 0 <= col < len(area[0])
    is_visited = (row, col) in visited

    if not row_in_bounds or not col_in_bounds or is_visited:
        return 0

    is_water = area[row][col] == "W"
    if is_water:
        return 0
    visited.add((row, col))
    size = 1
    size += explore(area, row - 1, col, visited)
    size += explore(area, row + 1, col, visited)
    size += explore(area, row, col - 1, visited)
    size += explore(area, row, col + 1, visited)

    return size


def island_count(area: List[List[str]]) -> int:
    visited = set()
    smallest = 9999
    for r, row in enumerate(area):
        for c, column in enumerate(row):
            island_size = explore(area, r, c, visited)
            if island_size != 0 and island_size < smallest:
                smallest = island_size
    return smallest


area = [
    ["W", "L", "W", "W", "W"],
    ["W", "L", "W", "W", "W"],
    ["W", "W", "W", "L", "W"],
    ["W", "W", "L", "L", "W"],
    ["L", "W", "W", "L", "L"],
    ["L", "L", "W", "W", "W"],
]

print(island_count(area))
