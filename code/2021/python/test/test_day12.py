from typing import List
import pytest
from src.day12 import init_paths, find_all_paths, count_all_paths


def format_paths(path_list: List[List[str]]) -> str:
    return "\n".join([",".join(path) for path in path_list])


def test_init_paths_simple_maze():
    maze = {
        "start": ["A", "b"],
        "A": ["start", "c", "b", "end"],
        "b": ["start", "A", "d", "end"],
        "c": ["A"],
        "d": ["b"],
        "end": ["A", "b"],
    }

    exp_init = [["start", "A"], ["start", "b"]]
    act_init = init_paths(maze)
    assert exp_init == act_init, f"Expected\n{exp_init}\nGot\n{act_init}"


def test_find_all_paths_simple_maze():
    maze = {
        "start": ["A", "b"],
        "A": ["start", "c", "b", "end"],
        "b": ["start", "A", "d", "end"],
        "c": ["A"],
        "d": ["b"],
        "end": ["A", "b"],
    }

    init_step = [["start", "A"], ["start", "b"]]

    act_paths = find_all_paths(maze, init_step)
    exp_paths = [
        ["start", "A", "b", "A", "c", "A", "end"],
        ["start", "A", "b", "A", "end"],
        ["start", "A", "b", "end"],
        ["start", "A", "c", "A", "b", "A", "end"],
        ["start", "A", "c", "A", "b", "end"],
        ["start", "A", "c", "A", "end"],
        ["start", "A", "end"],
        ["start", "b", "A", "c", "A", "end"],
        ["start", "b", "A", "end"],
        ["start", "b", "end"],
    ]

    assert sorted(act_paths) == sorted(
        exp_paths
    ), f"Expected\n{format_paths(sorted(exp_paths))}\nGot\n{format_paths(sorted(act_paths))}"


def test_find_all_paths_larger_example():
    maze = {
        "dc": ["end", "start", "HN", "LN", "kj"],
        "end": ["dc", "HN"],
        "HN": ["start", "dc", "end", "kj"],
        "start": ["HN", "kj", "dc"],
        "kj": ["start", "sa", "HN", "dc"],
        "LN": ["dc"],
        "sa": ["kj"],
    }

    init_step = [["start", "HN"], ["start", "kj"], ["start", "dc"]]

    act_paths = find_all_paths(maze, init_step)
    exp_paths = [
        ["start", "HN", "dc", "HN", "end"],
        ["start", "HN", "dc", "HN", "kj", "HN", "end"],
        ["start", "HN", "dc", "end"],
        ["start", "HN", "dc", "kj", "HN", "end"],
        ["start", "HN", "end"],
        ["start", "HN", "kj", "HN", "dc", "HN", "end"],
        ["start", "HN", "kj", "HN", "dc", "end"],
        ["start", "HN", "kj", "HN", "end"],
        ["start", "HN", "kj", "dc", "HN", "end"],
        ["start", "HN", "kj", "dc", "end"],
        ["start", "dc", "HN", "end"],
        ["start", "dc", "HN", "kj", "HN", "end"],
        ["start", "dc", "end"],
        ["start", "dc", "kj", "HN", "end"],
        ["start", "kj", "HN", "dc", "HN", "end"],
        ["start", "kj", "HN", "dc", "end"],
        ["start", "kj", "HN", "end"],
        ["start", "kj", "dc", "HN", "end"],
        ["start", "kj", "dc", "end"],
    ]

    assert sorted(act_paths) == sorted(
        exp_paths
    ), f"Expected\n{format_paths(sorted(exp_paths))}\nGot\n{format_paths(sorted(act_paths))}"


def test_count_all_paths_bigger_example():
    maze = {
        "fs": ["end", "he", "DX", "pj"],
        "end": ["fs", "zg"],
        "he": ["DX", "fs", "pj", "RW", "WI", "zg"],
        "DX": ["he", "start", "pj", "fs"],
        "start": ["DX", "pj", "RW"],
        "pj": ["DX", "zg", "he", "RW", "start", "fs"],
        "zg": ["end", "sl", "pj", "RW", "he"],
        "sl": ["zg"],
        "RW": ["he", "pj", "zg", "start"],
        "WI": ["he"],
    }

    exp_value = 226
    act_value = count_all_paths(maze)

    assert exp_value == act_value, f"Expected {exp_value} different paths. Got {act_value}."


def test_find_all_paths_count_twice_simple_maze():
    maze = {
        "start": ["A", "b"],
        "A": ["start", "c", "b", "end"],
        "b": ["start", "A", "d", "end"],
        "c": ["A"],
        "d": ["b"],
        "end": ["A", "b"],
    }

    init_step = [["start", "A"], ["start", "b"]]

    act_paths = find_all_paths(maze, init_step, visit_twice=True)
    exp_paths = [
        ["start", "A", "b", "A", "b", "A", "c", "A", "end"],
        ["start", "A", "b", "A", "b", "A", "end"],
        ["start", "A", "b", "A", "b", "end"],
        ["start", "A", "b", "A", "c", "A", "b", "A", "end"],
        ["start", "A", "b", "A", "c", "A", "b", "end"],
        ["start", "A", "b", "A", "c", "A", "c", "A", "end"],
        ["start", "A", "b", "A", "c", "A", "end"],
        ["start", "A", "b", "A", "end"],
        ["start", "A", "b", "d", "b", "A", "c", "A", "end"],
        ["start", "A", "b", "d", "b", "A", "end"],
        ["start", "A", "b", "d", "b", "end"],
        ["start", "A", "b", "end"],
        ["start", "A", "c", "A", "b", "A", "b", "A", "end"],
        ["start", "A", "c", "A", "b", "A", "b", "end"],
        ["start", "A", "c", "A", "b", "A", "c", "A", "end"],
        ["start", "A", "c", "A", "b", "A", "end"],
        ["start", "A", "c", "A", "b", "d", "b", "A", "end"],
        ["start", "A", "c", "A", "b", "d", "b", "end"],
        ["start", "A", "c", "A", "b", "end"],
        ["start", "A", "c", "A", "c", "A", "b", "A", "end"],
        ["start", "A", "c", "A", "c", "A", "b", "end"],
        ["start", "A", "c", "A", "c", "A", "end"],
        ["start", "A", "c", "A", "end"],
        ["start", "A", "end"],
        ["start", "b", "A", "b", "A", "c", "A", "end"],
        ["start", "b", "A", "b", "A", "end"],
        ["start", "b", "A", "b", "end"],
        ["start", "b", "A", "c", "A", "b", "A", "end"],
        ["start", "b", "A", "c", "A", "b", "end"],
        ["start", "b", "A", "c", "A", "c", "A", "end"],
        ["start", "b", "A", "c", "A", "end"],
        ["start", "b", "A", "end"],
        ["start", "b", "d", "b", "A", "c", "A", "end"],
        ["start", "b", "d", "b", "A", "end"],
        ["start", "b", "d", "b", "end"],
        ["start", "b", "end"],
    ]

    assert sorted(act_paths) == sorted(
        exp_paths
    ), f"Expected\n{format_paths(sorted(exp_paths))}\nGot\n{format_paths(sorted(act_paths))}\nExpected n°:{len(exp_paths)} vs actual n°{len(act_paths)}"


def test_count_all_paths_count_twice_larger_example():
    maze = {
        "dc": ["end", "start", "HN", "LN", "kj"],
        "end": ["dc", "HN"],
        "HN": ["start", "dc", "end", "kj"],
        "start": ["HN", "kj", "dc"],
        "kj": ["start", "sa", "HN", "dc"],
        "LN": ["dc"],
        "sa": ["kj"],
    }

    exp_value = 103
    act_value = count_all_paths(maze, visit_twice=True)

    assert exp_value == act_value, f"Expected {exp_value} different paths. Got {act_value}."


def test_count_all_paths_count_twice_bigger_example():
    maze = {
        "fs": ["end", "he", "DX", "pj"],
        "end": ["fs", "zg"],
        "he": ["DX", "fs", "pj", "RW", "WI", "zg"],
        "DX": ["he", "start", "pj", "fs"],
        "start": ["DX", "pj", "RW"],
        "pj": ["DX", "zg", "he", "RW", "start", "fs"],
        "zg": ["end", "sl", "pj", "RW", "he"],
        "sl": ["zg"],
        "RW": ["he", "pj", "zg", "start"],
        "WI": ["he"],
    }

    exp_value = 3509
    act_value = count_all_paths(maze, visit_twice=True)

    assert exp_value == act_value, f"Expected {exp_value} different paths. Got {act_value}."
