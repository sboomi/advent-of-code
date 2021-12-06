import pytest
from src.day6 import evolve_lanternfishes, run_population_evolution, track_pop_evolution


def test_evolve_lanternfishes_simple_example():
    lanternfish_example = [3]

    act_lfish_day_1 = evolve_lanternfishes(lanternfish_example)
    exp_lfish_day_1 = [2]
    assert act_lfish_day_1 == exp_lfish_day_1, f"Expected {exp_lfish_day_1}. Got {act_lfish_day_1}"

    act_lfish_day_2 = evolve_lanternfishes(act_lfish_day_1)
    exp_lfish_day_2 = [1]
    assert act_lfish_day_2 == exp_lfish_day_2, f"Expected {exp_lfish_day_2}. Got {act_lfish_day_2}"

    act_lfish_day_3 = evolve_lanternfishes(act_lfish_day_2)
    exp_lfish_day_3 = [0]
    assert act_lfish_day_3 == exp_lfish_day_3, f"Expected {exp_lfish_day_3}. Got {act_lfish_day_3}"

    act_lfish_day_4 = evolve_lanternfishes(act_lfish_day_3)
    exp_lfish_day_4 = [6, 8]
    assert act_lfish_day_4 == exp_lfish_day_4, f"Expected {exp_lfish_day_4}. Got {act_lfish_day_4}"

    act_lfish_day_5 = evolve_lanternfishes(act_lfish_day_4)
    exp_lfish_day_5 = [5, 7]
    assert act_lfish_day_5 == exp_lfish_day_5, f"Expected {exp_lfish_day_5}. Got {act_lfish_day_5}"


def test_run_population_evolution_simple_example():
    lanternfish_example = [3]

    act_lfish_day_5 = run_population_evolution(5, lanternfish_example)
    exp_lfish_day_5 = [5, 7]
    assert act_lfish_day_5 == exp_lfish_day_5, f"Expected {exp_lfish_day_5}. Got {act_lfish_day_5}"


def test_run_population_evolution_more_complex_example():
    sample_pop = [3, 4, 3, 1, 2]

    act_lfish_day_6 = run_population_evolution(6, sample_pop)
    exp_lfish_day_6 = [4, 5, 4, 2, 3, 4, 5, 6, 6, 7]
    assert act_lfish_day_6 == exp_lfish_day_6, f"Expected {exp_lfish_day_6}. Got {act_lfish_day_6}"

    act_lfish_day_12 = run_population_evolution(12, sample_pop)
    exp_lfish_day_12 = [5, 6, 5, 3, 4, 5, 6, 0, 0, 1, 5, 6, 7, 7, 7, 8, 8]
    assert act_lfish_day_12 == exp_lfish_day_12, f"Expected {exp_lfish_day_12}. Got {act_lfish_day_12}"

    act_lfish_day_18 = run_population_evolution(18, sample_pop)
    exp_lfish_day_18 = [6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6, 0, 1, 1, 1, 2, 2, 3, 3, 4, 6, 7, 8, 8, 8, 8]
    assert act_lfish_day_18 == exp_lfish_day_18, f"Expected {exp_lfish_day_18}. Got {act_lfish_day_18}"

    act_n_fish_day_80 = len(run_population_evolution(80, sample_pop))
    exp_n_fish_day_80 = 5934
    assert act_n_fish_day_80 == exp_n_fish_day_80, f"Expected {exp_n_fish_day_80}. Got {act_n_fish_day_80}"


def test_run_population_long_time():
    sample_pop = [3, 4, 3, 1, 2]

    act_n_fish_day_256 = track_pop_evolution(256, sample_pop)
    exp_n_fish_day_256 = 26984457539
    assert act_n_fish_day_256 == exp_n_fish_day_256, f"Expected {exp_n_fish_day_256}. Got {act_n_fish_day_256}"
