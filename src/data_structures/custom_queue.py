from .linked_list import LinkedList
from typing import Generic, TypeVar

T = TypeVar("T")


class CustomQueue(Generic[T]):
    """
    Usage:
        To get the auto complete advantage of TypeVar, you need to use type hinting like this:

        a: CustomQueue[int] = CustomQueue()

    """

    queue: LinkedList

    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, value: T):
        """Append a value to the queue

        Args:
            value: Any value to add

        Returns:
            None
        """
        self.queue.append(value)

    def dequeue(self) -> T:
        """Remove and return the first element

        Returns:
            Any value added to the queue
        """
        if self.queue.is_empty():
            return
        result = self.queue.head.value
        self.queue.remove_at(0)
        return result

    def peek(self) -> T:
        """
        Returns the first value but doesn't remove it
        Returns:
            A value
        """
        if self.queue.is_empty():
            return None
        return self.queue.head.value

    @property
    def size(self) -> int:
        """Size of the queue

        Returns:
            int size of the queue
        """
        return self.queue.size

    def __repr__(self):
        elements = self.queue.to_list()
        elements = map(lambda x: str(x), elements)
        return " <- ".join(elements)
