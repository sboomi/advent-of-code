from src import DATA_DIR


def load_data():
    day_nineteen_file = DATA_DIR / "day19"
    with open(day_nineteen_file, "r") as f:
        return f.read()


def day19():
    print()
    data = load_data()
    print(data)


if __name__ == "__main__":
    day19()
