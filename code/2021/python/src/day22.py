from src import DATA_DIR


def load_data():
    day_twentytwo_file = DATA_DIR / "day22"
    with open(day_twentytwo_file, "r") as f:
        return f.read()


def day22():
    print()
    data = load_data()
    print(data)


if __name__ == "__main__":
    day22()
