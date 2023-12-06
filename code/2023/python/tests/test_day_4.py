import pytest
from ac2023python.day_4_scratchcards import get_cards, Card


EXAMPLE_INPUT = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
]


@pytest.fixture(scope="session")
def text_file(tmp_path_factory):
    txt = "\n".join(EXAMPLE_INPUT)
    fn = tmp_path_factory.mktemp("data") / "day4"
    with open(fn, "w") as f:
        f.write(txt)
    return fn


def test_get_cards(text_file):
    act_cards = get_cards(text_file)
    exp_cards = [
        Card(
            _id=1,
            winning_numbers=[41, 48, 83, 86, 17],
            my_numbers=[83, 86, 6, 31, 17, 9, 48, 53],
        ),
        Card(
            _id=2,
            winning_numbers=[13, 32, 20, 16, 61],
            my_numbers=[61, 30, 68, 82, 17, 32, 24, 19],
        ),
        Card(
            _id=3,
            winning_numbers=[1, 21, 53, 59, 44],
            my_numbers=[69, 82, 63, 72, 16, 21, 14, 1],
        ),
        Card(
            _id=4,
            winning_numbers=[41, 92, 73, 84, 69],
            my_numbers=[59, 84, 76, 51, 58, 5, 54, 83],
        ),
        Card(
            _id=5,
            winning_numbers=[87, 83, 26, 28, 32],
            my_numbers=[88, 30, 70, 12, 93, 22, 82, 36],
        ),
        Card(
            _id=6,
            winning_numbers=[31, 18, 13, 56, 72],
            my_numbers=[74, 77, 10, 23, 35, 67, 36, 11],
        ),
    ]

    assert act_cards == exp_cards


def test_card_points(text_file):
    cards = get_cards(text_file)
    act_points = [card.points() for card in cards]
    exp_points = [8, 2, 2, 1, 0, 0]

    assert act_points == exp_points
    assert sum(act_points) == 13
