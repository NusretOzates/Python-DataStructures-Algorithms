from src.data_structures.stack import Stack


def depth_first_search(graph: dict, start: str):
    stack = Stack()
    stack.push(start)

    while not stack.is_empty():

        current = stack.pop()
        print(current)
        for neighbour in graph[current]:
            stack.push(neighbour)


def depth_first_recursive_search(graph: dict, start: str) -> None:
    print(start)
    for neighbour in graph[start]:
        depth_first_recursive_search(graph, neighbour)


test_graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
}

depth_first_recursive_search(test_graph, "a")
