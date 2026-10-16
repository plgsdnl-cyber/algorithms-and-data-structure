from sorting.bubble_sort import bubble_sort
from sorting.quick_sort import quick_sort

def test_bubble_sort():
    assert bubble_sort([3, 3, 1, 2, 2]) == [1, 2, 2, 3, 3]
    assert bubble_sort([5, 5, 5]) == [5, 5, 5]
    assert bubble_sort([]) == []

def test_quick_sort():
    assert quick_sort([4, 2, 7, 1]) == [1, 2, 4, 7]
    assert quick_sort([3, 3, 3]) == [3, 3, 3]
