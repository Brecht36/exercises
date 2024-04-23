from intervals import overlapping_intervals


def test_overlapping_intervals():
    assert not overlapping_intervals((1, 5), (3, 6))
    assert not overlapping_intervals((1, 2), (1, 2))
    assert not overlapping_intervals((5, 6), (5, 0))
    assert overlapping_intervals((2, 5), (7, 10))
    assert overlapping_intervals((1, 2), (3, 4))
    assert overlapping_intervals((1, 5), (5, 6))
    assert overlapping_intervals((8, 8), (8, 8))
    assert overlapping_intervals((0, 4), (4, 0))