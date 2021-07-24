from src import day_6


def test_d6_p1():
    test_groups = [["abc"], ["a", "b", "c"], ["ab", "ac"], ["a", "a", "a", "a"], ["b"]]
    actual = day_6.d6_p1(test_groups)
    expected = 11
    assert actual == expected, f"Expected {expected}, got {actual}"


def test_d6_p2():
    test_groups = [["abc"], ["a", "b", "c"], ["ab", "ac"], ["a", "a", "a", "a"], ["b"]]
    actual = day_6.d6_p2(test_groups)
    expected = 6
    assert actual == expected, f"Expected {expected}, got {actual}"
