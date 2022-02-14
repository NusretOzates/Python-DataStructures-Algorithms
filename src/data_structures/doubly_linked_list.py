"""
This time we will try Generic Python! Wait isn't it already generic...
Well we will force the type of the List! Wait no we can't do it by default...
But we have mypy anyway :)
"""

from typing import List, TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    value: T
    previous_node: "Node[T]" = None
    next_node: "Node[T]" = None

    def __init__(self, value: T):
        self.value = value

    def __repr__(self):
        return f"Node: {self.value}"


class DoublyLinkedList(Generic[T]):
    def __init__(self):
        self.head: Node[T] = None
        self.tail: Node[T] = None
        self.length = 0

    def clear(self):
        head = self.head
        while head:
            next_node = head.next_node
            head.next_node = None
            head.previous_node = None
            head.value = None
            head = next_node

        self.head = None
        self.tail = None
        self.length = 0

    def size(self) -> int:
        return self.length

    def __len__(self):
        return self.length

    def is_empty(self):
        return self.size() == 0

    def add_last(self, value: T) -> bool:
        node = Node(value)

        if self.tail is None:
            self.tail = node
            self.head = node
            return True

        old_tail = self.tail
        node.previous_node = old_tail
        old_tail.next_node = node
        self.tail = node
        self.length += 1
        return True

    def add_first(self, value: T) -> bool:
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
            self.length += 1
            return True

        old_head = self.head
        node.next_node = old_head
        old_head.previous_node = node
        self.head = node
        self.length += 1
        return True

    def remove_first(self) -> bool:

        if self.is_empty():
            return False

        if self.size() == 1:
            self.head.value = None
            self.tail.value = None
            self.length -= 1

        head = self.head
        # Set new head
        new_head = head.next_node
        new_head.previous_node = None
        self.head = new_head

        # Clean old head
        head.next_node = None
        head.value = None

        self.length -= 1

        return True

    def remove_last(self) -> bool:
        if self.is_empty():
            return False

        if self.size() == 1:
            self.head.value = None
            self.tail.value = None
            self.length -= 1

        old_tail = self.tail

        new_tail = old_tail.previous_node
        new_tail.next_node = None
        self.tail = new_tail

        old_tail.value = None
        old_tail.previous_node = None

        self.length -= 1
        return True

    def _remove_node(self, node: Node[T]) -> bool:
        if node is None:
            return False
        if node.previous_node is None:
            return self.remove_first()
        if node.next_node is None:
            return self.remove_last()

        prev_node = node.previous_node
        next_node = node.next_node

        prev_node.next_node = next_node
        next_node.previous_node = prev_node

        node.next_node = None
        node.previous_node = None
        node.value = None

        self.length -= 1
        return True

    def remove(self, value: T):

        if self.head.value == value:
            return self.remove_first()

        node = self.find(value)
        return self._remove_node(node)

    def remove_at(self, index: int):

        list_size = self.size()

        if self.size() <= index:
            return False

        if index <= (list_size // 2):
            head = self.head
            position = 0
            while position < index:
                position += 1
                head = head.next_node

            return self._remove_node(head)

        tail = self.tail
        position = list_size - 1
        while position > index:
            position -= 1
            tail = tail.previous_node
        return self._remove_node(tail)

    def find(self, value: T):

        if self.is_empty():
            return None

        if self.size() == 1 and self.head.value == value:
            return self.head

        head = self.head

        while head:
            if head.value == value:
                return head
            head = head.next_node

        return None

    def index_of(self, value: T):

        if self.is_empty():
            return -1

        if self.size() == 1 and self.head.value == value:
            return 0

        head = self.head
        position = 0
        while head:
            if head.value == value:
                return position
            head = head.next_node
            position += 1
        return None

    def __repr__(self):
        head = self.head
        nodes = []
        while head:
            nodes.append(str(head))
            head = head.next_node

        return " -> ".join(nodes)


dll: DoublyLinkedList[int] = DoublyLinkedList()
dll.add_first(12)
dll.add_first(13)
dll.add_first(14)
print(dll)
dll.remove_first()
dll.remove_first()
print(dll.find(13))
print(dll)
