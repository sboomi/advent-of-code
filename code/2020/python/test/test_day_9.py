from src import day_9


def test_d9_p1():
    test_numbers = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
    actual = day_9.d9_p1(test_numbers, 5)
    expected = 127
    assert actual == expected, f"Expected {expected}, got {actual}"


def test_d9_p2():
    test_numbers = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
    actual = day_9.d9_p2(test_numbers, 127)
    expected = 62
    assert actual == expected, f"Expected {expected}, got {actual}"
