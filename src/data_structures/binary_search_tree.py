import enum

from .custom_queue import CustomQueue


class TraversalOrder(enum.Enum):
    """
    Enum class to choose traversing type of BST
    """

    PRE_ORDER = 1
    IN_ORDER = 2
    POST_ORDER = 3
    LEVEL_ORDER = 4


class Node:
    """
    A node object to store a value and node's children if any
    """

    value: int = None
    left: "Node" = None
    right: "Node" = None

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.value}"


class BinarySearchTree:
    """
    Binary Search Tree is a node-based binary tree data structure which has the following properties:

    The left subtree of a node contains only nodes with keys lesser than the node’s key.
    The right subtree of a node contains only nodes with keys greater than the node’s key.
    The left and right subtree each must also be a binary search tree.
    """

    def __init__(self):
        self.root: Node = None
        self.node_size = 0

    def __len__(self):
        return self.size

    def __contains__(self, item):

        return self._contains(self.root, item)

    def __delitem__(self, key):
        if key not in self:
            return False
        return self._remove(self.root, key)

    def traverse(self, type: TraversalOrder):
        """
        Traverse and print the values in the given order
        Args:
            type: Type of the tree traversal

        Returns:

        """

        if type.PRE_ORDER:
            self._preorder(self.root)
        if type.IN_ORDER:
            self._inorder(self.root)
        if type.POST_ORDER:
            self._postorder(self.root)
        if type.LEVEL_ORDER:
            self._levelorder(self.root)

    def _contains(self, node: Node, value) -> bool:
        """Check if a value is in the tree. This is a recursive function

        Args:
            node: Start node to check
            value: Value which we search for

        Returns:
            True if value is in the tree otherwise False
        """
        if node is None:
            return False

        if value > node.value:
            return self._contains(node.right, value)
        if value < node.value:
            return self._contains(node.left, value)

        return True

    @property
    def size(self) -> int:
        """Node count

        Returns:
            Node count
        """
        return self.node_size

    @property
    def height(self) -> int:
        """Height of the tree

        Returns:
            Height of the tree as int
        """
        return self._height(self.root)

    def _preorder(self, node: Node):
        if node is None:
            return
        print(node.value)
        self._preorder(node.left)
        self._preorder(node.right)

    def _inorder(self, node: Node):
        if node is None:
            return
        self._preorder(node.left)
        print(node.value)
        self._preorder(node.right)

    def _postorder(self, node: Node):
        if node is None:
            return
        self._preorder(node.left)
        self._preorder(node.right)
        print(node.value)

    def _levelorder(self, node: Node):

        queue = CustomQueue()
        queue.enqueue(node)

        while queue.size() > 0:
            node: Node = queue.dequeue()
            left = node.left
            right = node.right
            if left:
                print(left)
                queue.enqueue(left)

            if right:
                print(right)
                queue.enqueue(right)

    def add(self, value) -> bool:
        """Adds a value to the tree
        If it is a duplicate value I don't allow it. But still return True anyway
        Args:
            value: Any value.

        Returns:
            True
        """

        node = Node(value)

        if not self.root:
            self.root = node
            return True

        self.root = self._add(self.root, value)
        self.node_size += 1
        return True

    def _add(self, root: Node, value):

        if root is None:
            root = Node(value)
            return root

        if root.value == value:
            return root

        if root.value < value:
            root.right = self._add(root.right, value)
            return root
        root.left = self._add(root.left, value)
        return root

    def dig_left(self, node: Node) -> Node:
        """Go left as many as we can

        Args:
            node: Starting node

        Returns:
            The node in the left
        """
        if node.left is None:
            return node

        return self.dig_left(node.left)

    def dig_right(self, node: Node) -> Node:
        """Go right as many as we can

        Args:
            node: Starting node

        Returns:
            The node in the right
        """

        if node.right is None:
            return node

        return self.dig_right(node.left)

    def _remove(self, root: Node, value):

        if value < root.value:
            root.left = self._remove(root.left, value)
            return root
        if value > root.value:
            root.right = self._remove(root.right, value)
            return root

        # If we are here root = value
        if root.left and root.right:
            # find smallest value on the right
            smallest = self.dig_left(root.right)
            # Change the values
            root.value = smallest.value
            # remove the smallest node on the right
            root.right = self._remove(root.right, smallest.value)

            return root

        if root.left:
            root = root.left
            return root

        if root.right:
            root = root.right
            return root

        # If we are here this means it is a leaf node
        return None

    def _height(self, node: Node):

        if node is None:
            return 0

        max_depth = max(self._height(node.left), self._height(node.right))

        return max_depth + 1
