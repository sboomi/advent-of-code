from typing import List, Tuple
from src import DATA_DIR


def load_data() -> Tuple[str, List[str]]:
    day_twenty_file = DATA_DIR / "day20"
    with open(day_twenty_file, "r") as f:
        input = f.read().split("\n")
    return input[0], input[2:]


def day20():
    print("--- Day 20: Trench Map ---")
    iea, im = load_data()
    print(iea)
    print(im)


if __name__ == "__main__":
    day20()
