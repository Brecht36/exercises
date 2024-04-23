from mergesort import *
import pytest
import itertools


@pytest.mark.parametrize('ns', [
    list(range(i)) for i in range(1001)
])
def test_split_in_two(ns):
    left, right = split_in_two(ns)
    assert left + right == ns
    assert abs(len(left) - len(right)) <= 1

@pytest.mark.parametrize('left', [
    [],
    [1,2,3,4,6,9],
    [1,4,5],
    [7],
    [0,1,1,3,3,6,7,8,9]
])
@pytest.mark.parametrize('right', [
    [],
    [0,0,0],
    [1,2,3,4,6,9],
    [1,4,5],
    [7],
    [0,1,1,3,3,6,7,8,9]
])
def test_merge_sorted(left, right):
    assert merge_sorted(left, right) == sorted(left + right)

@pytest.mark.parametrize('ns, expected', [
    (list(permutation), ns)
    for ns in [[], [1], [1, 2], [1, 2, 3], [1, 2, 2, 3 ,4], [1, 2, 2, 3, 6, 12, 18]]
    for permutation in itertools.permutations(ns)
])
def test_merge_sort(ns, expected):
    assert merge_sort(ns) == expected