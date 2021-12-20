from src import DATA_DIR


def load_data():
    day_fifteen_file = DATA_DIR / "day15"
    with open(day_fifteen_file, "r") as f:
        return f.read()


def day15():
    print()
    data = load_data()
    print(data)


if __name__ == "__main__":
    day15()
