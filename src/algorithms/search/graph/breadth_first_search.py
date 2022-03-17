from src.data_structures.custom_queue import CustomQueue


def breadth_first_search(graph: dict, start: str):
    queue = CustomQueue()
    queue.enqueue(start)

    while queue.size > 0:

        current = queue.dequeue()
        print(current)
        for neighbour in graph[current]:
            queue.enqueue(neighbour)


def breadth_first_recursive_search(graph: dict, start: str):
    print(start)
    for neighbour in graph[start]:
        breadth_first_recursive_search(graph, neighbour)


graph = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
}

breadth_first_search(graph, "a")
