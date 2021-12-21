import pytest
from src.day13 import fold_paper, craft_paper


def test_craft_paper_small_sample():
    point_list = [
        (6, 10),
        (0, 14),
        (9, 10),
        (0, 3),
        (10, 4),
        (4, 11),
        (6, 0),
        (6, 12),
        (4, 1),
        (0, 13),
        (10, 12),
        (3, 4),
        (3, 0),
        (8, 4),
        (1, 10),
        (2, 14),
        (8, 10),
        (9, 0),
    ]

    exp_rep = "...#..#..#.\n....#......\n...........\n#..........\n...#....#.#\n...........\n...........\n...........\n...........\n...........\n.#....#.##.\n....#......\n......#...#\n#..........\n#.#........"
    act_rep = craft_paper(point_list)

    assert exp_rep == act_rep, f"Expected...\n{exp_rep}\nGot...\n{act_rep}"


def test_fold_paper_simple_fold():
    point_list = [
        (6, 10),
        (0, 14),
        (9, 10),
        (0, 3),
        (10, 4),
        (4, 11),
        (6, 0),
        (6, 12),
        (4, 1),
        (0, 13),
        (10, 12),
        (3, 4),
        (3, 0),
        (8, 4),
        (1, 10),
        (2, 14),
        (8, 10),
        (9, 0),
    ]

    fold = ("y", 7)

    act_folded_paper = fold_paper(point_list, fold)
    exp_folded_paper = "#.##..#..#.\n#...#......\n......#...#\n#...#......\n.#.#..#.###\n...........\n..........."
    act_rep = craft_paper(act_folded_paper, max_y=6)

    exp_point_number = 17
    act_point_number = len(act_folded_paper)

    assert exp_point_number == act_point_number, f"Expected {exp_point_number} points. Got {act_point_number}."
    assert exp_folded_paper == act_rep, f"Expected folded paper\n{exp_folded_paper}\nActual folded paper\n{act_rep}"


def test_fold_paper_two_folds():
    point_list = [
        (6, 10),
        (0, 14),
        (9, 10),
        (0, 3),
        (10, 4),
        (4, 11),
        (6, 0),
        (6, 12),
        (4, 1),
        (0, 13),
        (10, 12),
        (3, 4),
        (3, 0),
        (8, 4),
        (1, 10),
        (2, 14),
        (8, 10),
        (9, 0),
    ]

    fold = ("y", 7)
    second_fold = ("x", 5)

    act_folded_paper = fold_paper(point_list, fold)
    act_folded_paper = fold_paper(act_folded_paper, second_fold)
    act_rep = craft_paper(act_folded_paper, max_y=6, max_x=4)

    exp_folded_paper = "#####\n#...#\n#...#\n#...#\n#####\n.....\n....."

    exp_point_number = 16
    act_point_number = len(act_folded_paper)

    assert exp_point_number == act_point_number, f"Expected {exp_point_number} points. Got {act_point_number}."
    assert exp_folded_paper == act_rep, f"Expected folded paper\n{exp_folded_paper}\nActual folded paper\n{act_rep}"
