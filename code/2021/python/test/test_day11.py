import pytest
from src.day11 import find_neighbors, update_octo_grid, count_flashes


def make_printable_grid(grid):
    return "\n".join(["".join([str(n) for n in row]) for row in grid])


def show_diff(act_grid, exp_grid):
    return "\n".join(
        [
            "".join(["X" if act != exp else "_" for act, exp in zip(act_row, exp_row)])
            for act_row, exp_row in zip(act_grid, exp_grid)
        ]
    )


def test_find_neighbors_upper_left_corner():
    energy_lvs = [
        [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
        [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
        [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
        [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
        [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
        [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
        [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
        [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
        [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
        [5, 2, 8, 3, 7, 5, 1, 5, 2, 6],
    ]

    n_rows = len(energy_lvs)
    n_cols = len(energy_lvs[0])

    point = (0, 0)
    exp_neighbors = [(1, 0), (1, 1), (0, 1)]
    act_neighbors = find_neighbors(point, n_rows, n_cols)

    assert len(exp_neighbors) == len(
        act_neighbors
    ), f"Expected len of {len(exp_neighbors)}. Got len of {len(act_neighbors)}"
    assert sorted(exp_neighbors) == sorted(
        act_neighbors
    ), f"Expected\n{sorted(exp_neighbors)}\nGot\n{sorted(act_neighbors)}"


def test_find_neighbors_lower_right_corner():
    energy_lvs = [
        [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
        [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
        [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
        [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
        [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
        [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
        [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
        [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
        [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
        [5, 2, 8, 3, 7, 5, 1, 5, 2, 6],
    ]

    n_rows = len(energy_lvs)
    n_cols = len(energy_lvs[0])

    point = (9, 9)
    exp_neighbors = [(9, 8), (8, 8), (8, 9)]
    act_neighbors = find_neighbors(point, n_rows, n_cols)

    assert len(exp_neighbors) == len(
        act_neighbors
    ), f"Expected len of {len(exp_neighbors)}. Got len of {len(act_neighbors)}"
    assert sorted(exp_neighbors) == sorted(
        act_neighbors
    ), f"Expected\n{sorted(exp_neighbors)}\nGot\n{sorted(act_neighbors)}"


def test_find_neighbors_center():
    energy_lvs = [
        [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
        [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
        [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
        [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
        [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
        [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
        [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
        [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
        [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
        [5, 2, 8, 3, 7, 5, 1, 5, 2, 6],
    ]

    n_rows = len(energy_lvs)
    n_cols = len(energy_lvs[0])

    point = (4, 4)
    exp_neighbors = [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)]
    act_neighbors = find_neighbors(point, n_rows, n_cols)

    assert len(exp_neighbors) == len(
        act_neighbors
    ), f"Expected len of {len(exp_neighbors)}. Got len of {len(act_neighbors)}"
    assert sorted(exp_neighbors) == sorted(
        act_neighbors
    ), f"Expected\n{sorted(exp_neighbors)}\nGot\n{sorted(act_neighbors)}"


def test_find_neighbors_right_border():
    energy_lvs = [
        [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
        [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
        [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
        [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
        [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
        [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
        [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
        [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
        [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
        [5, 2, 8, 3, 7, 5, 1, 5, 2, 6],
    ]

    n_rows = len(energy_lvs)
    n_cols = len(energy_lvs[0])

    point = (9, 4)
    exp_neighbors = [(8, 4), (9, 3), (9, 5), (8, 3), (8, 5)]
    act_neighbors = find_neighbors(point, n_rows, n_cols)

    assert len(exp_neighbors) == len(
        act_neighbors
    ), f"Expected len of {len(exp_neighbors)}. Got len of {len(act_neighbors)}"
    assert sorted(exp_neighbors) == sorted(
        act_neighbors
    ), f"Expected\n{sorted(exp_neighbors)}\nGot\n{sorted(act_neighbors)}"


def test_update_octo_grid_one_center():
    simple_octo_grid = [[1, 1, 1, 1, 1], [1, 9, 9, 9, 1], [1, 9, 1, 9, 1], [1, 9, 9, 9, 1], [1, 1, 1, 1, 1]]

    exp_grid = [[3, 4, 5, 4, 3], [4, 0, 0, 0, 4], [5, 0, 0, 0, 5], [4, 0, 0, 0, 4], [3, 4, 5, 4, 3]]
    exp_flashes = 9
    act_grid, act_flashes = update_octo_grid(simple_octo_grid)

    assert (
        exp_grid == act_grid
    ), f"Expected\n{make_printable_grid(exp_grid)}\nGot\n{make_printable_grid(act_grid)}Diff:\n{show_diff(act_grid, exp_grid)}"
    assert exp_flashes == act_flashes, f"Expected {exp_flashes} flashes. Got {act_flashes} flashes"


def test_update_octo_grid_one_center_step_two():
    simple_octo_grid = [[1, 1, 1, 1, 1], [1, 9, 9, 9, 1], [1, 9, 1, 9, 1], [1, 9, 9, 9, 1], [1, 1, 1, 1, 1]]

    exp_grid = [[4, 5, 6, 5, 4], [5, 1, 1, 1, 5], [6, 1, 1, 1, 6], [5, 1, 1, 1, 5], [4, 5, 6, 5, 4]]
    exp_flashes = 9
    act_grid, act_flashes = update_octo_grid(simple_octo_grid)
    act_grid_two, act_flashes_two = update_octo_grid(act_grid)
    act_flashes += act_flashes_two

    assert (
        exp_grid == act_grid_two
    ), f"Expected\n{make_printable_grid(exp_grid)}\nGot\n{make_printable_grid(act_grid_two)}Diff:\n{show_diff(act_grid_two, exp_grid)}"
    assert exp_flashes == act_flashes, f"Expected {exp_flashes} flashes. Got {act_flashes} flashes"


def test_update_octo_grid_ten_times():
    energy_lvs = [
        [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
        [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
        [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
        [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
        [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
        [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
        [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
        [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
        [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
        [5, 2, 8, 3, 7, 5, 1, 5, 2, 6],
    ]

    exp_grid = [
        [
            [6, 5, 9, 4, 2, 5, 4, 3, 3, 4],
            [3, 8, 5, 6, 9, 6, 5, 8, 2, 2],
            [6, 3, 7, 5, 6, 6, 7, 2, 8, 4],
            [7, 2, 5, 2, 4, 4, 7, 2, 5, 7],
            [7, 4, 6, 8, 4, 9, 6, 5, 8, 9],
            [5, 2, 7, 8, 6, 3, 5, 7, 5, 6],
            [3, 2, 8, 7, 9, 5, 2, 8, 3, 2],
            [7, 9, 9, 3, 9, 9, 2, 2, 4, 5],
            [5, 9, 5, 7, 9, 5, 9, 6, 6, 5],
            [6, 3, 9, 4, 8, 6, 2, 6, 3, 7],
        ],
        [
            [8, 8, 0, 7, 4, 7, 6, 5, 5, 5],
            [5, 0, 8, 9, 0, 8, 7, 0, 5, 4],
            [8, 5, 9, 7, 8, 8, 9, 6, 0, 8],
            [8, 4, 8, 5, 7, 6, 9, 6, 0, 0],
            [8, 7, 0, 0, 9, 0, 8, 8, 0, 0],
            [6, 6, 0, 0, 0, 8, 8, 9, 8, 9],
            [6, 8, 0, 0, 0, 0, 5, 9, 4, 3],
            [0, 0, 0, 0, 0, 0, 7, 4, 5, 6],
            [9, 0, 0, 0, 0, 0, 0, 8, 7, 6],
            [8, 7, 0, 0, 0, 0, 6, 8, 4, 8],
        ],
        [
            [0, 0, 5, 0, 9, 0, 0, 8, 6, 6],
            [8, 5, 0, 0, 8, 0, 0, 5, 7, 5],
            [9, 9, 0, 0, 0, 0, 0, 0, 3, 9],
            [9, 7, 0, 0, 0, 0, 0, 0, 4, 1],
            [9, 9, 3, 5, 0, 8, 0, 0, 6, 3],
            [7, 7, 1, 2, 3, 0, 0, 0, 0, 0],
            [7, 9, 1, 1, 2, 5, 0, 0, 0, 9],
            [2, 2, 1, 1, 1, 3, 0, 0, 0, 0],
            [0, 4, 2, 1, 1, 2, 5, 0, 0, 0],
            [0, 0, 2, 1, 1, 1, 9, 0, 0, 0],
        ],
        [
            [2, 2, 6, 3, 0, 3, 1, 9, 7, 7],
            [0, 9, 2, 3, 0, 3, 1, 6, 9, 7],
            [0, 0, 3, 2, 2, 2, 1, 1, 5, 0],
            [0, 0, 4, 1, 1, 1, 1, 1, 6, 3],
            [0, 0, 7, 6, 1, 9, 1, 1, 7, 4],
            [0, 0, 5, 3, 4, 1, 1, 1, 2, 2],
            [0, 0, 4, 2, 3, 6, 1, 1, 2, 0],
            [5, 5, 3, 2, 2, 4, 1, 1, 2, 2],
            [1, 5, 3, 2, 2, 4, 7, 2, 1, 1],
            [1, 1, 3, 2, 2, 3, 0, 2, 1, 1],
        ],
        [
            [4, 4, 8, 4, 1, 4, 4, 0, 0, 0],
            [2, 0, 4, 4, 1, 4, 4, 0, 0, 0],
            [2, 2, 5, 3, 3, 3, 3, 4, 9, 3],
            [1, 1, 5, 2, 3, 3, 3, 2, 7, 4],
            [1, 1, 8, 7, 3, 0, 3, 2, 8, 5],
            [1, 1, 6, 4, 6, 3, 3, 2, 3, 3],
            [1, 1, 5, 3, 4, 7, 2, 2, 3, 1],
            [6, 6, 4, 3, 3, 5, 2, 2, 3, 3],
            [2, 6, 4, 3, 3, 5, 8, 3, 2, 2],
            [2, 2, 4, 3, 3, 4, 1, 3, 2, 2],
        ],
        [
            [5, 5, 9, 5, 2, 5, 5, 1, 1, 1],
            [3, 1, 5, 5, 2, 5, 5, 2, 2, 2],
            [3, 3, 6, 4, 4, 4, 4, 6, 0, 5],
            [2, 2, 6, 3, 4, 4, 4, 4, 9, 6],
            [2, 2, 9, 8, 4, 1, 4, 3, 9, 6],
            [2, 2, 7, 5, 7, 4, 4, 3, 4, 4],
            [2, 2, 6, 4, 5, 8, 3, 3, 4, 2],
            [7, 7, 5, 4, 4, 6, 3, 3, 4, 4],
            [3, 7, 5, 4, 4, 6, 9, 4, 3, 3],
            [3, 3, 5, 4, 4, 5, 2, 4, 3, 3],
        ],
        [
            [6, 7, 0, 7, 3, 6, 6, 2, 2, 2],
            [4, 3, 7, 7, 3, 6, 6, 3, 3, 3],
            [4, 4, 7, 5, 5, 5, 5, 8, 2, 7],
            [3, 4, 9, 6, 6, 5, 5, 7, 0, 9],
            [3, 5, 0, 0, 6, 2, 5, 6, 0, 9],
            [3, 5, 0, 9, 9, 5, 5, 5, 6, 6],
            [3, 4, 8, 6, 6, 9, 4, 4, 5, 3],
            [8, 8, 6, 5, 5, 8, 5, 5, 5, 5],
            [4, 8, 6, 5, 5, 8, 0, 6, 4, 4],
            [4, 4, 6, 5, 5, 7, 4, 6, 4, 4],
        ],
        [
            [7, 8, 1, 8, 4, 7, 7, 3, 3, 3],
            [5, 4, 8, 8, 4, 7, 7, 4, 4, 4],
            [5, 6, 9, 7, 6, 6, 6, 9, 4, 9],
            [4, 6, 0, 8, 7, 6, 6, 8, 3, 0],
            [4, 7, 3, 4, 9, 4, 6, 7, 3, 0],
            [4, 7, 4, 0, 0, 9, 7, 6, 8, 8],
            [6, 9, 0, 0, 0, 0, 7, 5, 6, 4],
            [0, 0, 0, 0, 0, 0, 9, 6, 6, 6],
            [8, 0, 0, 0, 0, 0, 4, 7, 5, 5],
            [6, 8, 0, 0, 0, 0, 7, 7, 5, 5],
        ],
        [
            [9, 0, 6, 0, 0, 0, 0, 6, 4, 4],
            [7, 8, 0, 0, 0, 0, 0, 9, 7, 6],
            [6, 9, 0, 0, 0, 0, 0, 0, 8, 0],
            [5, 8, 4, 0, 0, 0, 0, 0, 8, 2],
            [5, 8, 5, 8, 0, 0, 0, 0, 9, 3],
            [6, 9, 6, 2, 4, 0, 0, 0, 0, 0],
            [8, 0, 2, 1, 2, 5, 0, 0, 0, 9],
            [2, 2, 2, 1, 1, 3, 0, 0, 0, 9],
            [9, 1, 1, 1, 1, 2, 8, 0, 9, 7],
            [7, 9, 1, 1, 1, 1, 9, 9, 7, 6],
        ],
        [
            [0, 4, 8, 1, 1, 1, 2, 9, 7, 6],
            [0, 0, 3, 1, 1, 1, 2, 0, 0, 9],
            [0, 0, 4, 1, 1, 1, 2, 5, 0, 4],
            [0, 0, 8, 1, 1, 1, 1, 4, 0, 6],
            [0, 0, 9, 9, 1, 1, 1, 3, 0, 6],
            [0, 0, 9, 3, 5, 1, 1, 2, 3, 3],
            [0, 4, 4, 2, 3, 6, 1, 1, 3, 0],
            [5, 5, 3, 2, 2, 5, 2, 3, 5, 0],
            [0, 5, 3, 2, 2, 5, 0, 6, 0, 0],
            [0, 0, 3, 2, 2, 4, 0, 0, 0, 0],
        ],
    ]
    exp_flashes = [0, 35, 45, 16, 8, 1, 7, 24, 39, 29]
    act_grid = []
    act_flashes = []
    updated_grid = [[energy_point for energy_point in energy_row] for energy_row in energy_lvs]

    for _ in range(10):
        updated_grid, step_flashes = update_octo_grid(updated_grid)
        act_flashes.append(step_flashes)
        act_grid.append(updated_grid)

    for i in range(10):
        assert (
            exp_grid[i] == act_grid[i]
        ), f"STEP {i+1}: Expected\n{make_printable_grid(exp_grid[i])}\nGot\n{make_printable_grid(act_grid[i])}\nDiff:\n{show_diff(act_grid[i], exp_grid[i])}"
        assert (
            exp_flashes[i] == act_flashes[i]
        ), f"STEP {i+1}: Expected {exp_flashes[i]} flashes. Got {act_flashes[i]} flashes"


def test_count_flashes_full():
    energy_lvs = [
        [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
        [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
        [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
        [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
        [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
        [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
        [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
        [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
        [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
        [5, 2, 8, 3, 7, 5, 1, 5, 2, 6],
    ]

    exp_flashes = 1656
    act_flashes = count_flashes(100, energy_lvs)

    assert exp_flashes == act_flashes, f"Expected {exp_flashes}. Got {act_flashes}"
