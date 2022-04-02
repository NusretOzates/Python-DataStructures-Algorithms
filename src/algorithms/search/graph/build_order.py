"""
Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of projects,
where the second project is dependent on the first project).All of a project's dependencies must be built before the
project is. Find a build order that will allow the projects to be built. If there is no valid build order,
return an error.
EXAMPLE
Input:
projects: a, b, c, d, e, f
dependencies: (a, d), (f, b), (b, d), (f, a), (d, c) Output:f, e, a, b, d, c
"""
import collections
from typing import List, Tuple, Dict

class Node:



    def __init__(self, value):
        self.value = value
        self.edges: List['Node'] = []
        self.dependencies: List['Node'] = []

def create_graph(projects: List[str], dependencies: List[Tuple[str, str]]) -> Dict[str, Node]:
    graph: Dict[str,Node] = {project: Node(project) for project in projects}
    for dependency, project in dependencies:
        graph[dependency].edges.append(graph[project])
        graph[project].dependencies.append(graph[dependency])

    return graph


def get_wo_dependencies(graph: Dict[str, Node]):

    nodes = []

    for key, node in graph.items():
        if not node.dependencies:
            nodes.append((key,node))

    return nodes

def build_order(projects: List[str], dependencies: List[Tuple[str, str]]) -> List[str]:
    # Create a graph
    graph = create_graph(projects, dependencies)
    build_list = []

    while len(graph) > 0:
        nodes = get_wo_dependencies(graph)
        if not nodes:
            raise AssertionError('Not possible to build')
        # Add them to build list
        for key, node in nodes:
            build_list.append(key)
            # Remove the node as dependency
            for edge in node.edges:
                edge.dependencies.remove(node)

            del graph[key]

    return build_list

print(build_order(['a', 'b', 'c', 'd', 'e', 'f'],
            [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c'),('e', 'f'),('d', 'e')]))
