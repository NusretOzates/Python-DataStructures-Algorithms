"""
Balanced Binary Search Tree. O(log(n)) insertion, deletion and search

Other BBST types: 2-3 Tree, AA tree, scapegoat tree, red-black tree

Balance factor:

BF(node) = H(node.right) - H(node.left)
H(X) = Number of edges between x and the furthest leaf

Invariant in AVL is balance factor must be either -1, 0 or 1
"""
import random


class Node:
    value: int
    balance_factor: int = None
    height: int = 0  # height of this node in the tree
    left: "Node" = None
    right: "Node" = None

    def __init__(self, value: int):
        self.value = value


class AVLTree:
    root: Node = None
    node_count = 0

    @property
    def height(self):
        if self.root is None:
            return 0
        return self.root.height

    @property
    def size(self):
        return self.node_count

    def __len__(self):
        return self.node_count

    def is_empty(self):
        return self.node_count == 0

    def __contains__(self, item):
        return self._contains(self.root, item)

    def _contains(self, node: Node, value: int):
        if node is None:
            return False

        if node.value == value:
            return True

        if value > node.value:
            return self._contains(node.right, value)

        return self._contains(node.left, value)

    def insert(self, value: int):
        if (
            value is None
        ):  # Friendly reminder, "if not value" won't work because if not 0 is True :)
            return False
        if value not in self:
            self.root = self._insert(self.root, value)
            self.node_count += 1
            return True
        return False

    def _insert(self, node: Node, value: int):

        if node is None:
            return Node(value)

        if value > node.value:
            node.right = self._insert(node.right, value)
        else:
            node.left = self._insert(node.left, value)

        self._update(node)

        return self._balance(node)

    def _update(self, node: Node):

        left_node_height = node.left.height if node.left else -1
        right_node_height = node.right.height if node.right else -1

        node.height = 1 + max(left_node_height, right_node_height)

        node.balance_factor = right_node_height - left_node_height

    def _balance(self, node: Node):

        # Left heavy
        if node.balance_factor == -2:
            # Left left case
            if node.left.balance_factor <= 0:
                return self._left_left_case(node)

            return self._left_right_case(node)
        # Right heavy
        if node.balance_factor == 2:
            # Right tight case
            if node.right.balance_factor >= 0:
                return self._right_right_case(node)

            return self._right_left_case(node)

        return node

    def _left_left_case(self, node: Node):
        return self._right_rotation(node)

    def _left_right_case(self, node):
        node.left = self._left_rotation(node.left)
        return self._left_left_case(node)

    def _right_right_case(self, node):
        return self._left_rotation(node)

    def _right_left_case(self, node):
        node.right = self._right_rotation(node.right)
        return self._right_right_case(node)

    def _left_rotation(self, node: Node):

        parent = node.right
        node.right = parent.left
        parent.left = node

        self._update(node)
        self._update(parent)
        return parent

    def _right_rotation(self, node: Node):

        parent = node.left
        node.left = parent.right
        parent.right = node
        self._update(node)
        self._update(parent)
        return parent

    def find_min(self, node: Node) -> Node:
        if not node.left:
            return Node
        return self.find_min(node.left)

    def find_max(self, node: Node):
        if not node.right:
            return Node
        return self.find_max(node.right)

    def remove(self, value: int):
        if value in self:
            self.root = self._remove(self.root, value)
            self.node_count -= 1
            return True
        return False

    def _remove(self, node: Node, value: int):

        if node is None:
            return Node

        if value < node.value:
            node.left = self._remove(node.left, value)

        elif value > node.value:
            node.right = self._remove(node.right, value)

        else:
            # We fond the node
            right = node.right
            left = node.left
            # there is right node or no subtree
            if not left:
                return right
            # there isn't a right node return left node or none
            if not right:
                return left

            # Both nodes are there, choose with the tallest one eg. bigger height
            if left.height > right.height:
                successor = self.find_max(left)
                node.value = successor.value
                node.left = self._remove(node.left, successor.value)
            else:
                successor = self.find_min(right)
                node.value = successor.value
                node.right = self._remove(node.right, successor.value)

        self._update(node)
        return self._balance(node)


avl = AVLTree()
for i in range(50):
    avl.insert(random.randint(0, 100))
