import pytest
from src.day3 import calculate_gamma_epsilon, find_gas_rating, find_life_support


def test_calculate_gamma_epsilon():
    dummy_diagnostic = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
    act_gamma, act_epsilon = calculate_gamma_epsilon(dummy_diagnostic)
    assert (act_gamma, act_epsilon) == (
        "10110",
        "01001",
    ), f"Your gamma/epsilon pair: ({act_gamma}, {act_epsilon}), expected ('10110', '01001')"
    assert (
        int(act_gamma, 2) * int(act_epsilon, 2) == 198
    ), f"Actual power consumption: {int(act_gamma, 2) * int(act_epsilon, 2)}, expected 198."


def test_find_oxygen_generator_rating():
    dummy_diagnostic = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
    expected = "10111"
    actual = find_gas_rating(dummy_diagnostic, gas_name="oxygen_generator_rating")
    assert expected == actual, f"Expected 10111, got {actual}"


def test_find_co2_scrubber_rating():
    dummy_diagnostic = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
    expected = "01010"
    actual = find_gas_rating(dummy_diagnostic, gas_name="co2_scrubber_rating")
    assert expected == actual, f"Expected 01010, got {actual}"


def test_find_life_support():
    dummy_diagnostic = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
    expected = 230
    actual = find_life_support(dummy_diagnostic)
    assert expected == actual, f"Expected {expected}, got {actual}"
