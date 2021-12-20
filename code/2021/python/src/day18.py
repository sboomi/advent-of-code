from src import DATA_DIR


def load_data():
    day_eightteen_file = DATA_DIR / "day18"
    with open(day_eightteen_file, "r") as f:
        return f.read()


def day18():
    print()
    data = load_data()
    print(data)


if __name__ == "__main__":
    day18()
