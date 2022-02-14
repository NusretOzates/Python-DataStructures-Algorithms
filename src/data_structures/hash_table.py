from typing import Hashable, Iterable


class Entity:

    def __init__(self, key: Hashable, value):
        self.key = key
        self.value = value
        self.hash = hash(key)

    def __eq__(self, other):
        if self.hash != other.hash:
            return False
        return self.key == other.key

    def __repr__(self):
        return f"{self.key} => {self.value}"


class HashTableSeperateChaining(Iterable):
    pass

