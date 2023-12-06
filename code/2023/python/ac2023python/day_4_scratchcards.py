from dataclasses import dataclass
from pathlib import Path
from ac2023python.settings import DATA_PATH

DATA_FILE = DATA_PATH / "day4"


@dataclass
class Card:
    _id: int
    winning_numbers: list[int]
    my_numbers: list[int]

    def __eq__(self, __value: object) -> bool:
        return (
            self._id == __value._id
            and self.winning_numbers == __value.winning_numbers
            and self.my_numbers == __value.my_numbers
        )

    def points(self) -> int:
        points = 0
        for number in self.my_numbers:
            if number in self.winning_numbers:
                if points == 0:
                    points += 1
                else:
                    points *= 2

        return points


def get_cards(p: Path = DATA_FILE) -> list[Card]:
    with open(p, "r") as f:
        contents = [line.strip() for line in f.readlines()]

    cards = []
    for linecard in contents:
        card_id, card_contents = linecard.split(": ")
        card_id = int(card_id.lstrip("Card "))
        winning_nums, nums = card_contents.split(" | ")

        cards.append(
            Card(
                _id=card_id,
                winning_numbers=[int(n) for n in winning_nums.split()],
                my_numbers=[int(n) for n in nums.split()],
            )
        )

    return cards


def main():
    cards = get_cards()
    points = [card.points() for card in cards]
    print(f"The scratching cards are worth in total {sum(points)} points")


if __name__ == "__main__":
    main()
