import pytest
from ac2022python.solutions.day2 import RockPaperScissors

EXAMPLE_INPUT = ["A Y", "B X", "C Z"]


@pytest.fixture(scope="session")
def text_file(tmp_path_factory):
    txt = "\n".join(EXAMPLE_INPUT)
    fn = tmp_path_factory.mktemp("data") / "day2"
    with open(fn, "w") as f:
        f.write(txt)
    return fn


def test_rock_paper_scissors_part_one(text_file):

    expected_result = 15
    actual_result = RockPaperScissors.get_total_score(text_file)

    assert expected_result == actual_result


def test_rock_paper_scissors_part_two(text_file):
    expected_result = 12
    actual_result = RockPaperScissors.get_total_score(text_file, part_two=True)

    assert expected_result == actual_result
