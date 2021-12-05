import pytest
from src.day5 import filter_horizontal_lines, find_min_max_coords, tracing_diagram, count_overlaps


def test_filter_horizontal_lines():
    dummy_start_points = [(0, 9), (8, 0), (9, 4), (2, 2), (7, 0), (6, 4), (0, 9), (3, 4), (0, 0), (5, 5)]
    dummy_end_points = [(5, 9), (0, 8), (3, 4), (2, 1), (7, 4), (2, 0), (2, 9), (1, 4), (8, 8), (8, 2)]

    act_start_hor_lines, act_end_hor_lines = filter_horizontal_lines(dummy_start_points, dummy_end_points)
    exp_start_hor_lines = [(0, 9), (9, 4), (2, 2), (7, 0), (0, 9), (3, 4)]
    exp_end_hor_lines = [(5, 9), (3, 4), (2, 1), (7, 4), (2, 9), (1, 4)]

    assert len(act_start_hor_lines) == len(
        exp_start_hor_lines
    ), f"Expected {len(exp_start_hor_lines)}. Got {len(act_start_hor_lines)}"
    assert act_start_hor_lines == exp_start_hor_lines, f"Expected {exp_start_hor_lines}. Got {act_start_hor_lines}"
    assert act_end_hor_lines == exp_end_hor_lines, f"Expected {exp_end_hor_lines}. Got {act_end_hor_lines}"


def test_find_min_max_coords():
    dummy_start_points = [(0, 9), (9, 4), (2, 2), (7, 0), (0, 9), (3, 4)]
    dummy_end_points = [(5, 9), (3, 4), (2, 1), (7, 4), (2, 9), (1, 4)]

    exp_max_x = 9
    exp_max_y = 9
    act_max_x, act_max_y = find_min_max_coords(dummy_start_points, dummy_end_points)

    assert act_max_x == exp_max_x, f"Expected {exp_max_x}. Got {act_max_x}"
    assert act_max_y == exp_max_y, f"Expected {exp_max_y}. Got {act_max_y}"


def test_tracing_diagram():
    dummy_start_points = [(0, 9), (9, 4), (2, 2), (7, 0), (0, 9), (3, 4)]
    dummy_end_points = [(5, 9), (3, 4), (2, 1), (7, 4), (2, 9), (1, 4)]

    dummy_max_x = 9
    dummy_max_y = 9

    exp_diagram = [
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 1, 2, 1, 1, 1, 2, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 2, 2, 1, 1, 1, 0, 0, 0, 0],
    ]
    act_diagram = tracing_diagram(dummy_start_points, dummy_end_points, dummy_max_x, dummy_max_y)

    assert len(exp_diagram) == len(act_diagram), f"Expected {len(exp_diagram)}. Got {len(act_diagram)}"
    assert len(exp_diagram[0]) == len(act_diagram[0]), f"Expected {len(exp_diagram[0])}. Got {len(act_diagram[0])}"
    assert exp_diagram == act_diagram, f"Expected \n{exp_diagram}.\nGot \n{act_diagram}"


def test_count_overlaps():
    dummy_diagram = [
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 1, 2, 1, 1, 1, 2, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 2, 2, 1, 1, 1, 0, 0, 0, 0],
    ]

    actual_overlap_count = count_overlaps(dummy_diagram)
    expected_overlap_count = 5

    assert (
        actual_overlap_count == expected_overlap_count
    ), f"Expected {expected_overlap_count}. Got {actual_overlap_count}"


def test_tracing_diagram_with_diagonals():
    dummy_start_points = [(0, 9), (8, 0), (9, 4), (2, 2), (7, 0), (6, 4), (0, 9), (3, 4), (0, 0), (5, 5)]
    dummy_end_points = [(5, 9), (0, 8), (3, 4), (2, 1), (7, 4), (2, 0), (2, 9), (1, 4), (8, 8), (8, 2)]

    dummy_max_x = 9
    dummy_max_y = 9

    exp_diagram = [
        [1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
        [0, 1, 1, 1, 0, 0, 0, 2, 0, 0],
        [0, 0, 2, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 2, 0, 2, 0, 0],
        [0, 1, 1, 2, 3, 1, 3, 2, 1, 1],
        [0, 0, 0, 1, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [2, 2, 2, 1, 1, 1, 0, 0, 0, 0],
    ]

    act_diagram = tracing_diagram(dummy_start_points, dummy_end_points, dummy_max_x, dummy_max_y)

    assert len(exp_diagram) == len(act_diagram), f"Expected {len(exp_diagram)}. Got {len(act_diagram)}"
    assert len(exp_diagram[0]) == len(act_diagram[0]), f"Expected {len(exp_diagram[0])}. Got {len(act_diagram[0])}"
    assert exp_diagram == act_diagram, f"Expected \n{exp_diagram}.\nGot \n{act_diagram}"


def test_counts_overlaps_with_diagonals():
    dummy_diagram = [
        [1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
        [0, 1, 1, 1, 0, 0, 0, 2, 0, 0],
        [0, 0, 2, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 2, 0, 2, 0, 0],
        [0, 1, 1, 2, 3, 1, 3, 2, 1, 1],
        [0, 0, 0, 1, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [2, 2, 2, 1, 1, 1, 0, 0, 0, 0],
    ]

    actual_overlap_count = count_overlaps(dummy_diagram)
    expected_overlap_count = 12

    assert (
        actual_overlap_count == expected_overlap_count
    ), f"Expected {expected_overlap_count}. Got {actual_overlap_count}"
