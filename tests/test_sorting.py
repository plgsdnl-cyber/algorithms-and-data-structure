from sorting.bubble_sort import bubble_sort
from sorting.quick_sort import quick_sort

def test_bubble_sort():
    assert bubble_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
    assert bubble_sort([]) == []

def test_quick_sort():
    assert quick_sort([10, 7, 8, 9, 1, 5]) == [1, 5, 7, 8, 9, 10]
    assert quick_sort([3, 3, 3]) == [3, 3, 3]