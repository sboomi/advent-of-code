import pytest
from src.day2 import move_submarine, move_submarine_aim


def test_move_submarine():
    dummy_instructions = [("forward", 5), ("down", 5), ("forward", 8), ("up", 3), ("down", 8), ("forward", 2)]
    expected = (15, 10)
    actual = move_submarine(dummy_instructions)
    assert expected == actual
    assert actual[0] * actual[1] == 150


def test_move_submarine_aim():
    dummy_instructions = [("forward", 5), ("down", 5), ("forward", 8), ("up", 3), ("down", 8), ("forward", 2)]
    expected = (15, 60)
    act_x, act_y, _ = move_submarine_aim(dummy_instructions)
    assert expected == (act_x, act_y), f"Position was ({act_x}, {act_y}). Should be (15, 60)"
    assert 900 == act_x * act_y, f"Product was {act_x * act_y}. Should be 900"
