from src import day_2


def test_d2_p1():
    test_pw = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    actual = day_2.d2_p1(test_pw)
    expected = 2
    assert actual == expected, f"Expected {expected}, got {actual}"


def test_d2_p2():
    test_pw = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    actual = day_2.d2_p2(test_pw)
    expected = 1
    assert actual == expected, f"Expected {expected}, got {actual}"
