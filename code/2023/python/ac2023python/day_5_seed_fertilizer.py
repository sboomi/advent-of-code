from pathlib import Path
from ac2023python.settings import DATA_PATH

DATA_FILE = DATA_PATH / "day5"


def get_almanac(p: Path = DATA_FILE) -> str:
    with open(p, "r") as f:
        return f.read()


def main():
    almanac = get_almanac()
    print(almanac)


if __name__ == "__main__":
    main()
