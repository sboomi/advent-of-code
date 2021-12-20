from src import DATA_DIR


def load_data():
    day_twentythree_file = DATA_DIR / "day23"
    with open(day_twentythree_file, "r") as f:
        return f.read()


def day23():
    print()
    data = load_data()
    print(data)


if __name__ == "__main__":
    day23()
