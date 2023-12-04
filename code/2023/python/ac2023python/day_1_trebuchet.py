from pathlib import Path
from ac2023python.settings import DATA_PATH

DATA_FILE = DATA_PATH / "day1"


def read_data(p: Path = DATA_FILE) -> list[str]:
    with open(p, "r") as f:
        contents = [line.strip() for line in f.readlines()]
    return contents


def main():
    puzzle_input = read_data()
    print(puzzle_input)


if __name__ == "__main__":
    main()
