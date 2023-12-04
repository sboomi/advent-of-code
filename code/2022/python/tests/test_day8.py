import pytest
from ac2022python.solutions.day8 import TreePatch, TreeTopTreeHouse

EXAMPLE_INPUT = ["30373", "25512", "65332", "33549", "35390"]


@pytest.fixture(scope="session")
def text_file(tmp_path_factory):
    txt = "\n".join(EXAMPLE_INPUT)
    fn = tmp_path_factory.mktemp("data") / "day8"
    with open(fn, "w") as f:
        f.write(txt)
    return fn


def test_read_tree_patch_from_file(text_file):
    tp = TreePatch.from_file(text_file)

    assert tp.n_cols == 5
    assert tp.n_rows == 5
    assert tp.grid[0][0].height == 3, f"{tp.grid[0][0]}"
    assert tp.grid[0][0].is_visible
    assert tp.to_list() == [
        [3, 0, 3, 7, 3],
        [2, 5, 5, 1, 2],
        [6, 5, 3, 3, 2],
        [3, 3, 5, 4, 9],
        [3, 5, 3, 9, 0],
    ]


# def test_count_visible_trees(text_file):
#     act_number = TreeTopTreeHouse.count_visible_trees(text_file)
#     exp_number = 21

#     assert act_number == exp_number
