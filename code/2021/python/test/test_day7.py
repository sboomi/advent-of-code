import pytest
from src.day7 import find_center_range, get_optimum_fuel_spendings, crab_spaceship_spending


def test_find_center_range():
    example_positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

    exp_midway = 8
    exp_center = 8

    act_midway, act_center = find_center_range(example_positions)
    assert exp_midway == act_midway, f"Expected {exp_midway}. Got {act_midway}."
    assert exp_center == act_center, f"Expected {exp_center}. Got {act_center}."


def test_crab_space_ship_spendings_wrong_mode_value():
    x_pos = 16
    dest = 2
    with pytest.raises(NotImplementedError):
        crab_spaceship_spending(x_pos, dest, mode="rgjngtrgtilh")


def test_crab_space_ship_spendings_basic_values():
    dest = 2
    crab_pos_list = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    mode = "basic"

    exp_fuel = [14, 1, 0, 2, 2, 0, 5, 1, 0, 12]
    act_fuel = [crab_spaceship_spending(x, dest, mode) for x in crab_pos_list]

    exp_fuel_sum = 37
    act_fuel_sum = sum(act_fuel)

    assert act_fuel == exp_fuel, f"Expected \n{exp_fuel}.\nGot \n{act_fuel}."
    assert act_fuel_sum == exp_fuel_sum, f"Expected {exp_fuel_sum}. Got {act_fuel_sum}"


def test_crab_space_ship_spendings_advanced_values():
    dest = 5
    crab_pos_list = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    mode = "advanced"

    exp_fuel = [66, 10, 6, 15, 1, 6, 3, 10, 6, 45]
    act_fuel = [crab_spaceship_spending(x, dest, mode) for x in crab_pos_list]

    exp_fuel_sum = 168
    act_fuel_sum = sum(act_fuel)

    assert act_fuel == exp_fuel, f"Expected \n{exp_fuel}.\nGot \n{act_fuel}."
    assert act_fuel_sum == exp_fuel_sum, f"Expected {exp_fuel_sum}. Got {act_fuel_sum}"


def test_crab_space_ship_spendings_advanced_values_previous_position():
    dest = 2
    crab_pos_list = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    mode = "advanced"

    act_fuel = [crab_spaceship_spending(x, dest, mode) for x in crab_pos_list]

    exp_fuel_sum = 206
    act_fuel_sum = sum(act_fuel)

    assert act_fuel_sum == exp_fuel_sum, f"Expected {exp_fuel_sum}. Got {act_fuel_sum}"


def test_get_optimum_fuel_spendings():
    example_positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

    act_fuel = get_optimum_fuel_spendings(example_positions, mode="basic")
    exp_fuel = 37
    assert act_fuel == exp_fuel, f"Expected {exp_fuel}. Got {act_fuel}"


def test_get_optimum_fuel_spendings_advanced():
    example_positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

    act_fuel = get_optimum_fuel_spendings(example_positions, mode="advanced")
    exp_fuel = 168
    assert act_fuel == exp_fuel, f"Expected {exp_fuel}. Got {act_fuel}"
