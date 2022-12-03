import pytest
from ac2022python.solutions.day3 import RucksackOrganization

EXAMPLE_INPUT = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]


@pytest.fixture(scope="session")
def text_file(tmp_path_factory):
    txt = "\n".join(EXAMPLE_INPUT)
    fn = tmp_path_factory.mktemp("data") / "day3"
    with open(fn, "w") as f:
        f.write(txt)
    return fn


def test_rucksack_organisation_part_one(text_file):

    expected_result = 157
    actual_result = RucksackOrganization.get_priority_sum(text_file)

    assert expected_result == actual_result


def test_rucksack_organisation_part_two(text_file):
    expected_result = 70
    actual_result = RucksackOrganization.get_priority_sum_group_of_three(text_file)

    assert expected_result == actual_result
