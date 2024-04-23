from mystatistics import average
from pytest import approx
import pytest

@pytest.mark.parametrize('ns, expected', [
    ([1,2,3], 2),
    ([4,3,8], 5),
    ([7,5,4,0], 4)
])
def test_average(ns, expected):
    assert approx(expected, abs=0.1) == average(ns)