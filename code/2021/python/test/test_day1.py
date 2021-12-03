import pytest
from src.day1 import count_depmes_increase, count_by_three


def test_count_depmes_increase():
    dummy_report = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    expected = 7
    actual = count_depmes_increase(dummy_report)
    assert expected == actual


def test_count_by_three():
    dummy_report = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    actual = count_by_three(dummy_report)
    expected = 5
    assert expected == actual
