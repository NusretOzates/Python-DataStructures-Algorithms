from src.data_structures.custom_queue import CustomQueue
from typing import List, Tuple, Optional, Dict
from collections import defaultdict


def build_graph(edges: List[List[str]]) -> Dict[str, List[str]]:
    graph = defaultdict(lambda: [])

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    return dict(graph)


def bfs(graph: dict, node: str, distance: int, dst: str) -> Optional[int]:
    queue: CustomQueue[Tuple[str, int]] = CustomQueue()
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

    return None


def shortest_path(edges: List[List[str]], src: str, dst: str) -> Optional[int]:
    graph = build_graph(edges)
    return bfs(graph, src, 0, dst)


test_edges = [
    ["w", "x"],
    ["x", "y"],
    ["z", "y"],
    ["z", "v"],
    ["w", "v"],
]

print(shortest_path(test_edges, "w", "z"))
