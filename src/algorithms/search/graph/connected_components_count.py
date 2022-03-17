"""
Time: O(edges)
Space: O(n)
"""


def dfs(graph: dict, start: str, visited: set):
    if start in visited:
        return

    visited.add(start)
    for negihbour in graph[start]:
        dfs(graph, negihbour, visited)


def connect_components_count(graph: dict):
    count = 0
    visited = set()
    for node in graph.keys():
        if node not in visited:
            dfs(graph, node, visited)
            count += 1
    return count


graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2],
}  # answer is 2

print(connect_components_count(graph))
