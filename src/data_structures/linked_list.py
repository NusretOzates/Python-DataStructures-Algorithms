from typing import List


class Node:
    """
    An object for storing a single node of a linked list

    """

    value: int = None
    next_node: "Node" = None  # https://stackoverflow.com/a/36193829/6458479

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Node value: {self.value}"


class LinkedList:
    def __init__(self, values=None):
        if values is None:
            values = []

        self.head: Node = None
        self.tail: Node = None
        for value in values:
            self.append(value)

    def is_empty(self) -> bool:
        """Return if the list is empty

        Returns:
            Bool
        """
        return self.head is None

    def insert(self, index: int, value: int) -> bool:
        """Inserts a new now at index position
        Insertion takes O(1) time but finding the node at the insertion point takes O(n) time.
        Takes overall O(n) time.
        Args:
            index: Index to asssign
            value: Value of the new Node

        Returns:
            True if successful otherwise False
        """
        if index > self.size or value is None:
            return False
        if index == 0:
            self.add(value)
            return True
        if index == self.size:
            self.append(value)
            return True

        node = Node(value)

        current_node = self.head
        current_index = 0

        while current_index < index - 1:
            current_node = current_node.next_node
            current_index += 1

        next_node = current_node.next_node
        current_node.next_node = node
        node.next_node = next_node
        return True

    def remove_at(self, index: int) -> bool:
        """Removes the node at index position
        Removal takes O(1) time but finding the node at the insertion point takes O(n) time.
        Takes overall O(n) time.
        Args:
            index: Index to asssign

        Returns:
            True if successful otherwise False
        """
        if index >= self.size:
            return False
        if index == 0:
            self.head = self.head.next_node
            return True

        current_node = self.head
        current_index = 0

        while current_index < index - 1:
            current_node = current_node.next_node
            current_index += 1

        node_to_remove = current_node.next_node
        current_node.next_node = node_to_remove.next_node
        return True

    def remove_value(self, value: int) -> bool:
        """Remove the node with the given value
        Takes O(n) time
        Args:
            value: A value to remove

        Returns:
            True if remove successfully else False
        """

        if self.is_empty():
            return False

        if self.head.value == value:
            self.head = self.head.next_node
            return True

        prev = self.head
        head = self.head.next_node
        while head:
            if head.value == value:
                prev.next_node = head.next_node
                return True
            prev = head
            head = head.next_node

        return False

    def add(self, value: int) -> bool:
        """Adds new Node at head of the list
        Takes O(1) time
        Args:
            value: A value to add at the head of the list

        Returns:
            True
        """

        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return True

        new_node.next_node = self.head
        self.head = new_node
        return True

    def append(self, value: int) -> bool:
        """Adds new Node at head of the list
        Takes O(1) time
        Args:
            value: A value to add at the head of the list

        Returns:
            True
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return True

        self.tail.next_node = new_node
        self.tail = new_node
        return True

    def delete(self, value: int) -> bool:
        """Deletes a value from the list
        Takes O(n) time
        Args:
            value: An integer value to remove from list

        Returns:
            True if deleted else False
        """

        head = self.head
        if self.is_empty():
            return False

        if head.value == value:
            self.head = head.next_node
            return True

        while head.next_node:
            next_node = head.next_node
            if next_node.value == value:
                head.next_node = next_node.next_node
                return True
            head = next_node

        return False

    def indexof(self, value: int) -> int:
        """Find the index of the first Node with the given value
        Takes O(n) time
        Args:
            value: An int value to find its index

        Returns:
            index of the value if found else -1
        """

        head = self.head
        if self.is_empty():
            return -1

        count = 0
        while head:
            if head.value == value:
                return count
            count += 1
            head = head.next_node

        return -1

    def valueof(self, index: int) -> Node:
        """Returns the node in the given index

        Args:
            index: Index of the node

        Returns:

        """

        if index > self.size:
            return None

        if index == 0:
            return self.head

        current = self.head

        position = 0
        while position < index:
            current = current.next_node
            position += 1

        return current
    @property
    def size(self) -> int:
        """Number of nodes in the list
        Takes O(n) time
        Returns:
            An integer
        """
        head = self.head
        count = 0
        while head:
            count += 1
            head = head.next_node
        return count

    def traverse(self):
        """Prints all elements in the list
        Takes O(n) time
        Returns:
            None
        """

        head = self.head

        while head:
            print(head)
            head = head.next_node

    def __repr__(self):
        """Returns a string representation of the list
        Takes O(n) time
        Returns:
            A string representation of the list
        """
        nodes = []
        head = self.head

        while head:
            nodes.append(f"{head}")
            head = head.next_node

        return " -> ".join(nodes)

    def to_list(self) -> List:
        """Converts Linked list to a list

        Returns:
            List
        """

        if self.head is None:
            return []
        head = self.head

        elements = []

        while head:
            elements.append(head.value)
            head = head.next_node

        return elements
