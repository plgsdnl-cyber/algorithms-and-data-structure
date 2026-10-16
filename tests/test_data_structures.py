from data_structures.array import MyArray
from data_structures.linked_list import LinkedList
from data_structures.deque import Deque
from data_structures.avl_tree import AVLTree

def test_array():
    arr = MyArray()
    arr.append(10)
    arr.append(20)
    assert arr.get(0) == 10
    assert arr.size() == 2

def test_linked_list():
    ll = LinkedList()
    ll.append(100)
    ll.append(200)
    assert ll.to_list() == [100, 200]
    ll.remove(100)
    assert ll.to_list() == [200]

def test_deque():
    dq = Deque()
    dq.append_left(10)
    dq.append_right(20)
    assert dq.pop_left() == 10
    assert dq.pop_right() == 20

def test_avl_tree():
    tree = AVLTree()
    root = None
    for key in [10, 20, 30]:
        root = tree.insert(root, key)
    assert root.key == 20
    assert root.left.key == 10
    assert root.right.key == 30
