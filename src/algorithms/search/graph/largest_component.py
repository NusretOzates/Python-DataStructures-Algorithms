"""
Time: O(edges)
Space: O(n)
"""


def dfs(graph: dict, start: str, visited: set):
    if start in visited:
        return 0

    visited.add(start)
    size = 1

    for negihbour in graph[start]:
        size += dfs(graph, negihbour, visited)

    return size


def largest_components_count(graph: dict):
    longest = 0
    visited = set()
    for node in graph.keys():
        count = dfs(graph, node, visited)
        if count > longest:
            longest = count
    return longest


graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2],
}  # answer is 2

print(largest_components_count(graph))
