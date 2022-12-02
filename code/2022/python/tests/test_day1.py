from ac2022python.solutions.day1 import CalorieCounting
import pytest

EXAMPLE_INPUT = [
    "1000",
    "2000",
    "3000",
    "",
    "4000",
    "",
    "5000",
    "6000",
    "",
    "7000",
    "8000",
    "9000",
    "",
    "10000",
]


@pytest.fixture(scope="session")
def text_file(tmp_path_factory):
    txt = "\n".join(EXAMPLE_INPUT)
    fn = tmp_path_factory.mktemp("data") / "day1"
    with open(fn, "w") as f:
        f.write(txt)
    return fn


def test_calorie_counting_part_one(text_file):

    expected_result = 24000
    actual_result = CalorieCounting.elf_with_the_most_calories_from_list(text_file)

    assert expected_result == actual_result


def test_calorie_counting_part_two(text_file):
    expected_result = 45000
    actual_result = CalorieCounting.top_three_elves(text_file)

    assert expected_result == actual_result
