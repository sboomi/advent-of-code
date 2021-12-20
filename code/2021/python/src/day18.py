from src import DATA_DIR


def load_data():
    day_eighteen_file = DATA_DIR / "day18"
    with open(day_eighteen_file, "r") as f:
        return [eval(line) for line in f.readlines()]


def day18():
    print("--- Day 18: Snailfish ---")
    data = load_data()
    print(data)


if __name__ == "__main__":
    day18()
