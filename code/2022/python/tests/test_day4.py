import pytest
from ac2022python.solutions.day4 import CampCleanup

EXAMPLE_INPUT = ["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"]


@pytest.fixture(scope="session")
def text_file(tmp_path_factory):
    txt = "\n".join(EXAMPLE_INPUT)
    fn = tmp_path_factory.mktemp("data") / "day4"
    with open(fn, "w") as f:
        f.write(txt)
    return fn


def test_camp_cleanup_part_one(text_file):

    expected_result = 2
    actual_result = CampCleanup.find_all_pairs(text_file)

    assert expected_result == actual_result


def test_camp_cleanup_part_two(text_file):
    expected_result = 4

    actual_result = CampCleanup.find_all_pairs(text_file, is_intersecting=True)

    assert expected_result == actual_result
