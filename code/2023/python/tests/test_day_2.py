import pytest
from ac2023python.day_2_cube_conundrum import get_games, possible_games, BagCubes

EXAMPLE_INPUT = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]


@pytest.fixture(scope="session")
def text_file(tmp_path_factory):
    txt = "\n".join(EXAMPLE_INPUT)
    fn = tmp_path_factory.mktemp("data") / "day2"
    with open(fn, "w") as f:
        f.write(txt)
    return fn


def test_possible_games(text_file):
    games = get_games(text_file)
    expected_games = [1, 2, 5]
    actual_games = possible_games(games)

    assert expected_games == actual_games
    assert 8 == sum(actual_games)


def test_best_bag_config(text_file):
    games = get_games(text_file)
    act_best_bags = [game.best_bag_config() for game in games]
    exp_best_bags = [
        BagCubes(red=4, green=2, blue=6),
        BagCubes(red=1, green=3, blue=4),
        BagCubes(red=20, green=13, blue=6),
        BagCubes(red=14, green=3, blue=15),
        BagCubes(red=6, green=3, blue=2),
    ]

    assert act_best_bags == exp_best_bags
