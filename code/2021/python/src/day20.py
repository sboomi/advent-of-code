from src import DATA_DIR


def load_data():
    day_twenty_file = DATA_DIR / "day20"
    with open(day_twenty_file, "r") as f:
        return f.read()


def day20():
    print()
    data = load_data()
    print(data)


if __name__ == "__main__":
    day20()
