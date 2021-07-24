from src import day_1


def test_d1_p1():
    test_numbers = [1721, 979, 366, 299, 675, 1456]
    actual = day_1.d1_p1(test_numbers)
    expected = 514579
    assert actual == expected, f"Expected {expected}, got {actual}"


def test_d2_p2():
    test_numbers = [1721, 979, 366, 299, 675, 1456]
    actual = day_1.d1_p2(test_numbers)
    expected = 241861950
    assert actual == expected, f"Expected {expected}, got {actual}"
