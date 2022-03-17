from collections import defaultdict
from typing import List

visited = set()


def build_graph(edges: List[List[str]]):
    graph = defaultdict(lambda: [])

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    return dict(graph)


def has_path_dfs(graph: dict, src, dst):
    if src == dst:
        return True
    if src in visited:
        return False
    visited.add(src)

    neighbours = graph[src]
    for neighbour in neighbours:
        if has_path_dfs(graph, neighbour, dst):
            return True

    return False


def undirected_path(edges: List[List[str]], node_a, node_b):
    graph = build_graph(edges)
    return has_path_dfs(graph, node_a, node_b)


edges = [
    ["i", "j"],
    ["k", "i"],
    ["m", "k"],
    ["k", "l"],
    ["o", "n"],
]

print(undirected_path(edges, "j", "m"))
