class UnionFind:
    def __init__(self, size):

        # number of elements in this union find
        self.element_size = size
        # Size of each component
        self._component_size = [1] * size
        # id[i] points to the parent of i, if id[i] == i, then i is a root node
        self.id = [i for i in range(size)]  # Everyone links to itself
        # number of components
        self.n_components = size

    def find(self, p: int):

        root = p
        while self.id[root] != root:
            root = self.id[root]

        # Path compression
        while p != root:
            parent = self.id[p]
            self.id[p] = root
            p = parent

        return root

    def is_connected(self, p: int, q: int):

        return self.find(p) == self.find(q)

    def component_size(self, p: int):

        root = self.find(p)
        return self._component_size(root)

    def size(self):
        return self.element_size

    def components(self):
        return self.n_components

    def unify(self, p: int, q: int):

        root_p = self.find(p)
        root_q = self.find(q)

        if root_q == root_p:
            return

        self.n_components -= 1

        comp_size_q = self._component_size[root_q]
        comp_size_p = self._component_size[root_p]

        if comp_size_q < comp_size_p:
            self._component_size[root_p] += comp_size_q
            self.id[root_q] = root_p
            return

        self._component_size[root_q] += comp_size_p
        self.id[root_p] = root_q
