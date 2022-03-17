class IndexedPriorityQueue:
    def __init__(self):
        self.vals = []
        self.pm = []  # Position of key index, pm[9] = 1 means key index 9 is in node 1
        self.im = []  # Inverse map, im[1] = 9 means in the node 1, key index 9 stored
        self.nk = {}  # name to key dict

    def node_to_key_index(self, node_num: int):
        return self.im[node_num]

    def key_index_to_node(self, key_index: int):
        return self.pm[key_index]

    def key_index_to_value(self, key_index: int):
        return self.vals[key_index]

    def name_from_key_index(self, key_index: int):
        if key_index not in self.nk.values():
            return -1

        return list(filter(lambda key, value: value == key_index, self.nk.items()))[0]

    def key_index_from_name(self, name: str):
        return self.nk[name]

    def remove(self, name: str):
        key_index = self.key_index_from_name(name)  # 11
        replacement_key = self.node_to_key_index(key_index)  # 2
        self.pm[key_index] = self.im[replacement_key]
        self.pm[replacement_key] = self.im[key_index]
        node_of_key = self.key_index_to_node(key_index)
