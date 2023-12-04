from ac2023python.day_1_trebuchet import get_calibration_values, get_calibration_values_with_letters

def test_get_calibration_values():
    puzzle_input = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]
    act_calibrations = get_calibration_values(puzzle_input)
    exp_calibrations = [12, 38, 15, 77]
    assert (
        act_calibrations == exp_calibrations
    ), f"Expected {exp_calibrations}. Got {act_calibrations}."
    assert sum(act_calibrations) == 142, f"Expected 142. Got {sum(act_calibrations)}"


def test_get_calibration_values_with_letters():
    puzzle_input = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]
    act_calibrations = get_calibration_values_with_letters(puzzle_input)
    exp_calibrations = [29, 83, 13, 24, 42, 14, 76]
    assert (
        act_calibrations == exp_calibrations
    ), f"Expected {exp_calibrations}. Got {act_calibrations}."
    assert sum(act_calibrations) == 281, f"Expected 281. Got {sum(act_calibrations)}"
