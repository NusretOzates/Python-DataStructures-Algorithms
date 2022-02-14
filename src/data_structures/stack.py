class Stack:
    """
    Stack is a linear data structure which follows a particular order in which the operations are performed.
    The order may be LIFO(Last In First Out) or FILO(First In Last Out).
    """
    stack = []

    def __init__(self):
        self.stack = []

    def is_empty(self) -> bool:
        """ Check if the stack is empty

        Returns:

        """
        return len(self.stack) == 0

    def pop(self):
        """ Removes and returns the element in the top

        Returns:
            Top element in the stack
        """
        if self.is_empty():
            return None

        return self.stack.pop()

    def push(self, value):
        """ Add element to the top

        Args:
            value: A value to add

        Returns:
            None
        """
        self.stack.append(value)

    def peek(self):
        """ Returns the element at the top

        Returns:

        """
        if self.is_empty():
            return None
        return self.stack[-1]

    def __len__(self):
        return len(self.stack)

    def __iter__(self):
        for element in self.stack:
            yield element

    def __repr__(self):

        result = ""

        for element in reversed(self.stack):
            result += f"|{element}| \n"
        return result
