from typing import Tuple
from src import DATA_DIR


def load_data() -> Tuple[range, range]:
    day_seventeen_file = DATA_DIR / "day17"
    with open(day_seventeen_file, "r") as f:
        str_range_x, str_range_y = f.read().lstrip("target area:").split(", ")
        str_range_x, str_range_y = str_range_x.lstrip("x="), str_range_y.lstrip("y=")
        range_x, range_y = [
            range(int(data.split("..")[0]), int(data.split("..")[1])) for data in [str_range_x, str_range_y]
        ]
        return range_x, range_y


def day17():
    print("--- Day 17: Trick Shot ---")
    range_x, range_y = load_data()
    print(range_x)
    print(range_y)


if __name__ == "__main__":
    day17()
