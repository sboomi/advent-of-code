from src import DATA_DIR


def load_data():
    day_twentyfour_file = DATA_DIR / "day24"
    with open(day_twentyfour_file, "r") as f:
        return f.read()


def day24():
    print()
    data = load_data()
    print(data)


if __name__ == "__main__":
    day24()
