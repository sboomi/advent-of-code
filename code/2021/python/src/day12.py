from src import DATA_DIR


def load_data():
    day_twelve_file = DATA_DIR / "day12"
    with open(day_twelve_file, "r") as f:
        return f.read()


def day12():
    print("--- Day 12: Passage Pathing ---")
    data = load_data()
    print(data)


if __name__ == "__main__":
    day12()
