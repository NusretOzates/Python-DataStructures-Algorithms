from src.data_structures.stack import Stack


def depthFirstSearch(graph: dict, start: str):
    stack = Stack()
    stack.push(start)

    while not stack.is_empty():

        current = stack.pop()
        print(current)
        for neighbour in graph[current]:
            stack.push(neighbour)


def depthFirstRecursiveSearch(graph: dict, start: str):
    print(start)
    for neighbour in graph[start]:
        depthFirstRecursiveSearch(graph, neighbour)


graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
}

depthFirstRecursiveSearch(graph, "a")
