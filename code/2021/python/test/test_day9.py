import pytest
from src.day9 import (
    find_low_points,
    check_neighbors,
    compute_risk_level,
    determine_basin_size,
    find_basin_size_list,
    find_product_basins,
)


def test_check_neighbors_easy_case():
    test_heightmap = [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]

    n_rows = len(test_heightmap)
    n_cols = len(test_heightmap[0])

    act_neighbor_list = check_neighbors(test_heightmap, (2, 2), (n_rows, n_cols))
    exp_neighbor_list = [8, 6, 6, 8]

    assert len(exp_neighbor_list) == len(
        act_neighbor_list
    ), f"Expected {len(exp_neighbor_list)} points. Got {len(act_neighbor_list)} points."
    assert exp_neighbor_list == act_neighbor_list, f"Expected\n{exp_neighbor_list}\nGot\n{act_neighbor_list}"


def test_check_neighbors_upper_border_case():
    test_heightmap = [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]

    n_rows = len(test_heightmap)
    n_cols = len(test_heightmap[0])

    act_neighbor_list = check_neighbors(test_heightmap, (1, 0), (n_rows, n_cols))
    exp_neighbor_list = [9, 9, 2]

    assert len(exp_neighbor_list) == len(
        act_neighbor_list
    ), f"Expected {len(exp_neighbor_list)} points. Got {len(act_neighbor_list)} points."
    assert exp_neighbor_list == act_neighbor_list, f"Expected\n{exp_neighbor_list}\nGot\n{act_neighbor_list}"


def test_check_neighbors_lower_border_case():
    test_heightmap = [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]

    n_rows = len(test_heightmap)
    n_cols = len(test_heightmap[0])

    act_neighbor_list = check_neighbors(test_heightmap, (6, 4), (n_rows, n_cols))
    exp_neighbor_list = [6, 6, 6]

    assert len(exp_neighbor_list) == len(
        act_neighbor_list
    ), f"Expected {len(exp_neighbor_list)} points. Got {len(act_neighbor_list)} points."
    assert exp_neighbor_list == act_neighbor_list, f"Expected\n{exp_neighbor_list}\nGot\n{act_neighbor_list}"


def test_check_neighbors_upper_corner_case():
    test_heightmap = [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]

    n_rows = len(test_heightmap)
    n_cols = len(test_heightmap[0])

    act_neighbor_list = check_neighbors(test_heightmap, (9, 0), (n_rows, n_cols))
    exp_neighbor_list = [1, 1]

    assert len(exp_neighbor_list) == len(
        act_neighbor_list
    ), f"Expected {len(exp_neighbor_list)} points. Got {len(act_neighbor_list)} points."
    assert exp_neighbor_list == act_neighbor_list, f"Expected\n{exp_neighbor_list}\nGot\n{act_neighbor_list}"


def test_check_neighbors_lower_corner_case():
    test_heightmap = [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]

    n_rows = len(test_heightmap)
    n_cols = len(test_heightmap[0])

    act_neighbor_list = check_neighbors(test_heightmap, (0, 4), (n_rows, n_cols))
    exp_neighbor_list = [8, 8]

    assert len(exp_neighbor_list) == len(
        act_neighbor_list
    ), f"Expected {len(exp_neighbor_list)} points. Got {len(act_neighbor_list)} points."
    assert exp_neighbor_list == act_neighbor_list, f"Expected\n{exp_neighbor_list}\nGot\n{act_neighbor_list}"


def test_find_low_points():
    test_heightmap = [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]

    exp_low_points = [1, 0, 5, 5]
    act_low_points = find_low_points(test_heightmap)

    assert len(exp_low_points) == len(
        act_low_points
    ), f"Expected {len(exp_low_points)} points. Got {len(act_low_points)} points."
    assert exp_low_points == act_low_points, f"Expected\n{exp_low_points}\nGot\n{act_low_points}"


def test_compute_risk_level():
    test_heightmap = [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]

    exp_risk_level = 15
    act_risk_level = compute_risk_level(test_heightmap)

    assert exp_risk_level == act_risk_level, f"Expected {exp_risk_level}. Got {act_risk_level}."


def test_determine_basin_size_small_basin():
    test_heightmap = [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]

    act_basin_size = determine_basin_size([(0, 0)], test_heightmap, points_visited=[])
    exp_basin_size = 3

    assert act_basin_size == exp_basin_size, f"Expected {exp_basin_size}. Got {act_basin_size}."


def test_determine_basin_size_in_the_middle():
    test_heightmap = [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]

    act_basin_size = determine_basin_size([(2, 2)], test_heightmap, points_visited=[])
    exp_basin_size = 14

    assert act_basin_size == exp_basin_size, f"Expected {exp_basin_size}. Got {act_basin_size}."


def test_determine_basin_size_lower_corner():
    test_heightmap = [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]

    act_basin_size = determine_basin_size([(6, 4)], test_heightmap, points_visited=[])
    exp_basin_size = 9

    assert act_basin_size == exp_basin_size, f"Expected {exp_basin_size}. Got {act_basin_size}."


def test_find_basin_size_list():
    test_heightmap = [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]

    act_basin_size_list = find_basin_size_list(test_heightmap)
    exp_basin_size_list = [3, 9, 14, 9]

    assert len(exp_basin_size_list) == len(
        act_basin_size_list
    ), f"Expected {len(exp_basin_size_list)} points. Got {len(act_basin_size_list)} points."
    assert exp_basin_size_list == act_basin_size_list, f"Expected\n{exp_basin_size_list}\nGot\n{act_basin_size_list}"


def test_find_product_basins():
    test_heightmap = [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]

    act_basin_size_list = find_basin_size_list(test_heightmap)
    exp_basin_product = 1134
    act_basin_product = find_product_basins(act_basin_size_list)

    assert act_basin_product == exp_basin_product, f"Expected {exp_basin_product}. Got {act_basin_product}."
