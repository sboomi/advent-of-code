from src import DATA_DIR


def load_data():
    day_twentyone_file = DATA_DIR / "day21"
    with open(day_twentyone_file, "r") as f:
        return f.read()


def day21():
    print()
    data = load_data()
    print(data)


if __name__ == "__main__":
    day21()
