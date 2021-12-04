import pytest
from src.day4 import BingoBoard, find_winner, find_last_winner


def test_bingo_board_instance():
    dummy_board = [
        [22, 13, 17, 11, 0],
        [8, 2, 23, 4, 24],
        [21, 9, 14, 16, 7],
        [6, 10, 3, 18, 5],
        [1, 12, 20, 15, 19],
    ]
    actual = BingoBoard.from_2d_array(dummy_board)
    expected = [22, 13, 17, 11, 0, 8, 2, 23, 4, 24, 21, 9, 14, 16, 7, 6, 10, 3, 18, 5, 1, 12, 20, 15, 19]
    assert actual.bingo_list == expected, f"Got {actual.bingo_list}. Expected{expected}"


def test_multiple_boards():
    dummy_boards = [
        [
            [22, 13, 17, 11, 0],
            [8, 2, 23, 4, 24],
            [21, 9, 14, 16, 7],
            [6, 10, 3, 18, 5],
            [1, 12, 20, 15, 19],
        ],
        [
            [3, 15, 0, 2, 22],
            [9, 18, 13, 17, 5],
            [19, 8, 7, 25, 23],
            [20, 11, 10, 24, 4],
            [14, 21, 16, 12, 6],
        ],
        [
            [14, 21, 17, 24, 4],
            [10, 16, 15, 9, 19],
            [18, 8, 23, 26, 20],
            [22, 11, 13, 6, 5],
            [2, 0, 12, 3, 7],
        ],
    ]
    for idx, list_board in enumerate(dummy_boards):
        bingo_board = BingoBoard.from_2d_array(list_board)
        expected = [num for line in list_board for num in line]
        actual = bingo_board.bingo_list
        assert len(expected) == len(actual), f"EXAMPLE N°{idx}: Expected {len(expected)}. Got {len(actual)}."
        assert expected == actual, f"EXAMPLE N°{idx}: Expected {expected}. Got {actual}."


def test_find_winner():
    dummy_num_list = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
    dummy_boards = [
        [
            [22, 13, 17, 11, 0],
            [8, 2, 23, 4, 24],
            [21, 9, 14, 16, 7],
            [6, 10, 3, 18, 5],
            [1, 12, 20, 15, 19],
        ],
        [
            [3, 15, 0, 2, 22],
            [9, 18, 13, 17, 5],
            [19, 8, 7, 25, 23],
            [20, 11, 10, 24, 4],
            [14, 21, 16, 12, 6],
        ],
        [
            [14, 21, 17, 24, 4],
            [10, 16, 15, 9, 19],
            [18, 8, 23, 26, 20],
            [22, 11, 13, 6, 5],
            [2, 0, 12, 3, 7],
        ],
    ]

    dummy_bingo_list = [BingoBoard.from_2d_array(dummy_board) for dummy_board in dummy_boards]
    act_num, act_board = find_winner(dummy_num_list, dummy_bingo_list)
    exp_num = 24
    exp_board_list = [14, 21, 17, 24, 4, 10, 16, 15, 9, 19, 18, 8, 23, 26, 20, 22, 11, 13, 6, 5, 2, 0, 12, 3, 7]
    exp_checks = [
        True,
        True,
        True,
        True,
        True,
        False,
        False,
        False,
        True,
        False,
        False,
        False,
        True,
        False,
        False,
        False,
        True,
        False,
        False,
        True,
        True,
        True,
        False,
        False,
        True,
    ]
    assert act_num == exp_num, f"Expected {exp_num}. Got {act_num}."
    assert exp_board_list == act_board.bingo_list, f"Expected {exp_board_list}. Got {act_board.bingo_list}."
    assert exp_checks == act_board.checked, f"Expected {exp_checks}. Got {act_board.checked}."

    exp_sum = 188
    exp_result = 4512

    act_sum = act_board.get_unmarked_numbers_sum()
    assert act_sum == exp_sum, f"Expected {exp_sum}. Got {act_sum}."
    act_result = act_num * act_sum
    assert act_result == exp_result, f"Expected {exp_result}. Got {act_result}."


def test_find_last_winner():
    dummy_num_list = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
    dummy_boards = [
        [
            [22, 13, 17, 11, 0],
            [8, 2, 23, 4, 24],
            [21, 9, 14, 16, 7],
            [6, 10, 3, 18, 5],
            [1, 12, 20, 15, 19],
        ],
        [
            [3, 15, 0, 2, 22],
            [9, 18, 13, 17, 5],
            [19, 8, 7, 25, 23],
            [20, 11, 10, 24, 4],
            [14, 21, 16, 12, 6],
        ],
        [
            [14, 21, 17, 24, 4],
            [10, 16, 15, 9, 19],
            [18, 8, 23, 26, 20],
            [22, 11, 13, 6, 5],
            [2, 0, 12, 3, 7],
        ],
    ]

    dummy_bingo_list = [BingoBoard.from_2d_array(dummy_board) for dummy_board in dummy_boards]
    act_num, act_board = find_last_winner(dummy_num_list, dummy_bingo_list)
    exp_num = 13
    exp_board_list = [3, 15, 0, 2, 22, 9, 18, 13, 17, 5, 19, 8, 7, 25, 23, 20, 11, 10, 24, 4, 14, 21, 16, 12, 6]
    exp_checks = [
        False,
        False,
        True,
        True,
        False,
        True,
        False,
        True,
        True,
        True,
        False,
        False,
        True,
        False,
        True,
        False,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        False,
        False,
    ]
    assert act_num == exp_num, f"Expected {exp_num}. Got {act_num}."
    assert exp_board_list == act_board.bingo_list, f"Expected {exp_board_list}. Got {act_board.bingo_list}."
    assert exp_checks == act_board.checked, f"Expected {exp_checks}. Got {act_board.checked}."

    exp_sum = 148
    exp_result = 1924

    act_sum = act_board.get_unmarked_numbers_sum()
    assert act_sum == exp_sum, f"Expected {exp_sum}. Got {act_sum}."
    act_result = act_num * act_sum
    assert act_result == exp_result, f"Expected {exp_result}. Got {act_result}."
