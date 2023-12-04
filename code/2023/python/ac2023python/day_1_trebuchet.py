from pathlib import Path
from ac2023python.settings import DATA_PATH

DATA_FILE = DATA_PATH / "day1"


def read_data(p: Path = DATA_FILE) -> list[str]:
    with open(p, "r") as f:
        contents = [line.strip() for line in f.readlines()]
    return contents


def get_calibration_values(puzzle_input: list[str]) -> list[int]:
    calibrations = []

    for line_input in puzzle_input:
        first_pos, last_pos = 0, -1
        first_letter, last_letter = line_input[first_pos], line_input[last_pos]
        while not first_letter.isdigit() or not last_letter.isdigit():
            if not last_letter.isdigit():
                last_pos -= 1
            if not first_letter.isdigit():
                first_pos += 1
            first_letter, last_letter = line_input[first_pos], line_input[last_pos]

        calibrations.append(int(first_letter + last_letter))

    return calibrations


def _find_number(letters: str, mapping_digits: dict[str, str], at_start: bool):
    number = letters[0] if at_start else letters[-1]

    if not number.isdigit():
        for k, v in mapping_digits.items():
            if at_start:
                if letters.startswith(k):
                    return v
            else:
                if letters.endswith(k):
                    return v
        return None

    return number


def get_calibration_values_with_letters(puzzle_input: list[str]) -> list[int]:
    letter_mapper = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    calibrations = []

    for line_input in puzzle_input:
        first_pos, last_pos = 0, -1
        first_segment, last_segment = line_input[first_pos], line_input[last_pos]
        while (
            _find_number(first_segment, letter_mapper, False) is None
            or _find_number(last_segment, letter_mapper, True) is None
        ):
            if _find_number(last_segment, letter_mapper, True) is None:
                last_pos -= 1
                last_segment = line_input[last_pos] + last_segment
            if _find_number(first_segment, letter_mapper, False) is None:
                first_pos += 1
                first_segment = first_segment + line_input[first_pos]

        calibrations.append(
            int(
                _find_number(first_segment, letter_mapper, False)
                + _find_number(last_segment, letter_mapper, True)
            )
        )

    return calibrations


def main():
    # read data
    # solve puzzle
    puzzle_input = read_data()
    calibrations = get_calibration_values(puzzle_input)
    print("The sum of all calibration values is", sum(calibrations))
    print("PART 2")
    new_calibrations = get_calibration_values_with_letters(puzzle_input)
    print("The sum of all calibration values (revised) is", sum(new_calibrations))


if __name__ == "__main__":
    main()
