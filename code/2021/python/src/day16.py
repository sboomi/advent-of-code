from src import DATA_DIR


def load_data():
    day_sixteen_file = DATA_DIR / "day16"
    with open(day_sixteen_file, "r") as f:
        return f.read()


def day16():
    print()
    data = load_data()
    print(data)


if __name__ == "__main__":
    day16()
