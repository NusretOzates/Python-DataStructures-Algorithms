from ..linked_list import LinkedList
from ..binary_search_tree import BinarySearchTree, TraversalOrder

linked_list = LinkedList()


def test_linked_list():
    linked_list.add(5)
    assert linked_list.size() == 1

    linked_list.add(2)
    assert linked_list.head.value == 2

    linked_list.insert(0, 6)
    assert linked_list.indexof(6) == 0
    assert linked_list.indexof(2) == 1

    linked_list.remove(0)
    assert linked_list.head.value == 2

    linked_list.remove_value(5)
    assert linked_list.head.value == 2


def test_bst():
    bst = BinarySearchTree()
    bst.add(5)
    bst.add(7)
    bst.add(6)
    bst.add(8)
    bst.add(9)

    del bst[7]

    assert (7 in bst) is False
    assert (9 in bst) is True
    assert bst.height == 3
