from src import DATA_DIR
from src import DATA_DIR


def load_data():
    christmas_file = DATA_DIR / "day25"
    with open(christmas_file, "r") as f:
        return f.read()


def day25():
    print()
    data = load_data()
    print(data)


if __name__ == "__main__":
    day25()
