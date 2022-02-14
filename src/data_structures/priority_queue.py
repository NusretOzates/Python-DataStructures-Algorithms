"""
A PQ is an abstract data type that operates similar to normal queue except that
each element has a certain priority. This will be used to determine which elements are removed
from the PQ. It only supports comparable data!
"""
from typing import DefaultDict, List
from collections import defaultdict


class PriorityQueue:
    def __init__(self, elements=None):

        self._heap = []
        self._map: DefaultDict[int, List[int]] = defaultdict(lambda: [])
        self._heap_size = 0
        if elements:
            count = len(elements)
            self._heap_size = count
            for index, element in enumerate(elements):
                self._map_add(element, index)
                self._heap.append(element)

            for i in reversed(range(max(0, (self._heap_size // 2) - 1))):
                self._sink(i)

    def is_empty(self):
        return self._heap_size == 0

    def clear(self):
        self._heap.clear()
        self._heap_size = 0
        self._map.clear()

    def size(self):
        return self._heap_size

    def peek(self):
        if self.is_empty():
            return None
        return self._heap[0]

    def poll(self):
        return self._remove_at(0)

    def add(self, item):

        if item is None:
            return item
        self._heap.append(item)
        self._map_add(item, self._heap_size)
        self._swim(self._heap_size)
        self._heap_size += 1

    def _map_add(self, item, index):

        self._map[item].append(index)

    def _map_remove(self, item, index):

        self._map[item].remove(index)

    def _less(self, first, second):

        first = self._heap[first]
        second = self._heap[second]

        return first <= second

    def _swim(self, k: int):

        parent_index = (k - 1) // 2

        while k > 0 and self._less(k, parent_index):
            self._swap(parent_index, k)
            k = parent_index
            parent_index = (k - 1) // 2

    def _sink(self, k: int):

        while True:
            left_child_index = (2 * k) + 1
            right_child_index = (2 * k) + 2
            smallest = left_child_index

            if right_child_index < self._heap_size and self._less(
                right_child_index, smallest
            ):
                smallest = right_child_index

            if left_child_index >= self._heap_size or self._less(k, smallest):
                break
            self._swap(k, smallest)
            k = smallest

    def _swap(self, first: int, second: int):

        first_value = self._heap[first]
        second_value = self._heap[second]

        self._heap[first], self._heap[second] = second_value, first_value

        self._map[first_value].remove(first)
        self._map[first_value].append(second)

        self._map[second_value].remove(second)
        self._map[second_value].append(first)

    def remove(self, item):

        if item is None:
            return False

        if item in self._map:
            return self._remove_at(self._map[item][0])

        return False

    def _remove_at(self, index: int):

        if self.is_empty():
            return None

        self._heap_size -= 1
        removed_data = self._heap[index]

        self._swap(index, self._heap_size)
        self._heap.pop()

        self._map_remove(removed_data, self._heap_size)

        if index == self._heap_size:
            return removed_data

        current = self._heap[index]
        self._sink(index)

        # If sinking doesn't work and nothing changed try swimming
        if self._heap[index] == current:
            self._swim(index)

        return removed_data

    def is_min_heap(self, k: int):

        heap_size = self._heap_size

        if k >= self._heap_size:
            return True

        left = (2 * k) + 1
        right = (2 * k) + 2

        if left < heap_size and not self._less(k, left):
            return False

        if right < heap_size and not self._less(k, right):
            return False

        return self.is_min_heap(left) and self.is_min_heap(right)

    def __contains__(self, item):
        if item is None:
            return False

        return item in self._map


pq = PriorityQueue([1, 2, 3, 5, 6, 7, 8])
print(pq.poll())
print(pq.poll())
print(pq.poll())
print(pq.add(99))
print(pq.add(-1))
print(pq.poll())
print(pq.is_min_heap(0))
