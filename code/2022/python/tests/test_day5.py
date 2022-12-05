import pytest
from ac2022python.solutions.day5 import CrateStack, SupplyStacks

EXAMPLE_INPUT = [
    "    [D]    ",
    "[N] [C]    ",
    "[Z] [M] [P]",
    " 1   2   3 ",
    "",
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2",
]


@pytest.fixture(scope="session")
def text_file(tmp_path_factory):
    txt = "\n".join(EXAMPLE_INPUT)
    fn = tmp_path_factory.mktemp("data") / "day5"
    with open(fn, "w") as f:
        f.write(txt)
    return fn


def test_crate_stack_cs_creation():
    cs = CrateStack.create(EXAMPLE_INPUT[:4])

    expected_result = {1: ["Z", "N"], 2: ["M", "C", "D"], 3: ["P"]}

    assert cs.struct == expected_result

    assert str(cs) == "\n".join(EXAMPLE_INPUT[:4])


def test_find_top_crate_combination(text_file):
    expected = "CMZ"

    ss = SupplyStacks()
    actual_result = ss.find_top_crate_combination(text_file)

    assert expected == actual_result


def test_find_top_crate_combination_multiple_crates(text_file):
    expected = "MCD"

    ss = SupplyStacks()
    actual_result = ss.find_top_crate_combination(text_file, multiple_crates=True)

    assert expected == actual_result
