from pathlib import Path
from ac2023python.settings import DATA_PATH
from dataclasses import dataclass

DATA_FILE = DATA_PATH / "day2"


@dataclass
class BagCubes:
    red: int = 0
    green: int = 0
    blue: int = 0

    def __lt__(self, other) -> bool:
        # Define the behavior for the less than operator
        return (
            self.red < other.red and self.green < other.green and self.blue < other.blue
        )

    def __le__(self, other) -> bool:
        # Define the behavior for the less than operator
        return (
            self.red <= other.red
            and self.green <= other.green
            and self.blue <= other.blue
        )

    def __eq__(self, __value: object) -> bool:
        return (
            self.red == __value.red
            and self.green == __value.green
            and self.blue == __value.blue
        )

    def product(self) -> int:
        return self.green * self.blue * self.red


@dataclass
class Game:
    _id: int
    bag_cubes: list[BagCubes]

    def is_game_config_valid(self, bag_config: BagCubes) -> bool:
        return all([bag_cube <= bag_config for bag_cube in self.bag_cubes])

    def best_bag_config(self) -> BagCubes:
        best_bag = self.bag_cubes[0]

        for bag in self.bag_cubes[1:]:
            best_bag = BagCubes(
                red=best_bag.red if best_bag.red >= bag.red else bag.red,
                blue=best_bag.blue if best_bag.blue >= bag.blue else bag.blue,
                green=best_bag.green if best_bag.green >= bag.green else bag.green,
            )

        return best_bag


def _record_to_bag_cube(rec: str) -> BagCubes:
    return BagCubes(
        **{item.split()[1]: int(item.split()[0]) for item in rec.split(", ")}
    )


def _extract_game_from_line(line: str) -> Game:
    game_id, game_records = line.split(": ")
    _, game_id = game_id.split()
    return Game(
        _id=int(game_id),
        bag_cubes=[_record_to_bag_cube(record) for record in game_records.split("; ")],
    )


def get_games(p: Path = DATA_FILE) -> list[Game]:
    with open(p, "r") as f:
        contents = [_extract_game_from_line(line.strip()) for line in f.readlines()]
    return contents


def possible_games(games: list[Game]) -> list[int]:
    game_conf = BagCubes(red=12, green=13, blue=14)

    return [game._id for game in games if game.is_game_config_valid(game_conf)]


def fewest_games(games: list[Game]) -> int:
    best_bags = [game.best_bag_config() for game in games]
    return sum([bag.product() for bag in best_bags])


def main():
    games = get_games()
    pos_games = possible_games(games)

    print(f"Number of possible games: {sum(pos_games)}")

    few_games = fewest_games(games)
    print(f"The sum of power of these sets is {few_games}")


if __name__ == "__main__":
    main()
