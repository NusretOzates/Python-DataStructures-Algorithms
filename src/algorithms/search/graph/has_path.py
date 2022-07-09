from typing import List, Dict
from src.data_structures.custom_queue import CustomQueue

# Probably a better way to do this is that using this set as a function parameter
# otherwise testing would be a pain
visited = set()


def has_path_dfs(graph: dict, src: str, dst: str) -> bool:
    global visited
    if src in visited:
        return False
    if src == dst:
        return True
    visited.add(src)
    neighbours: List[str] = graph[src]

    for neighbour in neighbours:
        if has_path_dfs(graph, neighbour, dst):
            return True

    return False


def has_path_bfs(graph: Dict[str, List[str]], src: str, dst: str) -> bool:
    queue: CustomQueue[str] = CustomQueue()
    queue.enqueue(src)

    while queue.size > 0:

        current = queue.dequeue()
        if current == dst:
            return True
        for n in graph[current]:
            queue.enqueue(n)

    return False


test_graph = {
    "f": ["g", "i"],
    "g": ["h"],
    "h": [],
    "i": ["g", "k"],
    "j": ["i"],
    "k": [],
}

print(has_path_bfs(test_graph, "f", "k"))
