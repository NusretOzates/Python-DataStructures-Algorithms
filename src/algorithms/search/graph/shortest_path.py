from src.data_structures.custom_queue import CustomQueue
from typing import List
from collections import defaultdict


def build_graph(edges: List[List[str]]):
    graph = defaultdict(lambda: [])

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    return dict(graph)


def bfs(graph: dict, node: str, distance: int, dst):
    queue = CustomQueue()
    queue.enqueue((node, distance))
    visited = set()
    while queue.size > 0:
        current, distance = queue.dequeue()
        if current == dst:
            return distance
        visited.add(current)
        for neighbour in graph[current]:
            if neighbour not in visited:
                queue.enqueue((neighbour, distance + 1))


def shortest_path(edges: str, src: str, dst: str):
    graph = build_graph(edges)
    return bfs(graph, src, 0, dst)


edges = [
    ["w", "x"],
    ["x", "y"],
    ["z", "y"],
    ["z", "v"],
    ["w", "v"],
]

print(shortest_path(edges, "w", "z"))
