from src import DATA_DIR

SCORE_TABLE = {")": 3, "]": 57, "}": 1197, ">": 25137}


def load_data():
    day_ten_file = DATA_DIR / "day10"
    with open(day_ten_file, "r") as f:
        return [line.strip() for line in f.readlines()]


def day10():
    print("--- Day 10: Syntax Scoring ---")
    navigation_subsystem = load_data()
    print(navigation_subsystem)


if __name__ == "__main__":
    day10()
