from data_structures.array import MyArray
from data_structures.linked_list import LinkedList
from data_structures.deque import Deque
from data_structures.avl_tree import AVLTree

def test_array():
    arr = MyArray()
    arr.append(1)
    arr.append(2)
    assert arr.get(0) == 1
    assert arr.size() == 2

def test_linked_list():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    assert ll.to_list() == [1, 2]
    ll.remove(1)
    assert ll.to_list() == [2]

def test_deque():
    dq = Deque()
    dq.append_left(1)
    dq.append_right(2)
    assert dq.pop_left() == 1
    assert dq.pop_right() == 2

def test_avl_tree():
    tree = AVLTree()
    root = None
    keys = [10, 20, 30, 40, 50, 25]
    for key in keys:
        root = tree.insert(root, key)
    assert root.key == 30
    assert root.left.key == 20
    assert root.right.key == 40