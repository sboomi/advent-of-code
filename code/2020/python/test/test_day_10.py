from src import day_10


def test_d10_p1():
    test_jolts = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    actual = day_10.d10_p1(test_jolts)
    expected = {"1": 7, "3": 5}
    assert actual == expected, f"Expected {expected}, got {actual}"


def test_d10_p1_second():
    test_jolts = [
        28,
        33,
        18,
        42,
        31,
        14,
        46,
        20,
        48,
        47,
        24,
        23,
        49,
        45,
        19,
        38,
        39,
        11,
        1,
        32,
        25,
        35,
        8,
        17,
        7,
        9,
        4,
        2,
        34,
        10,
        3,
    ]
    actual = day_10.d10_p1(test_jolts)
    expected = {"1": 22, "3": 10}
    assert actual == expected, f"Expected {expected}, got {actual}"


def test_d10_p2():
    pass
