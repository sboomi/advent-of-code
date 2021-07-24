from src import day_5


def test_find_row_seat():
    test_string = "FBFBBFF"
    actual = day_5.find_seat(test_string, 128, ["F", "B"])
    expected = 44
    assert actual == expected, f"Expected {expected}, got {actual}"


def test_find_column_seat():
    test_string = "RLR"
    actual = day_5.find_seat(test_string, 8, ["L", "R"])
    expected = 5
    assert actual == expected, f"Expected {expected}, got {actual}"


def test_compute_id():
    test_seat = "FBFBBFFRLR"
    actual = day_5.find_seat(test_seat[:7], 128, ["F", "B"]) * 8 + day_5.find_seat(test_seat[7:], 8, ["L", "R"])
    expected = 357
    assert actual == expected, f"Expected {expected}, got {actual}"


def test_d5_p1():
    test_seats = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
    actual = day_5.d5_p1(test_seats)
    expected = 820
    assert actual == expected, f"Expected {expected}, got {actual}"
