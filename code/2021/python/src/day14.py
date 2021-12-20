from src import DATA_DIR


def load_data():
    day_fourteen_file = DATA_DIR / "day14"
    with open(day_fourteen_file, "r") as f:
        return f.read()


def day14():
    print("--- Day 14: Extended Polymerization ---")
    data = load_data()
    print(data)


if __name__ == "__main__":
    day14()
