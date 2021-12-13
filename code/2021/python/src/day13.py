from src import DATA_DIR


def load_data():
    day_thirteen_file = DATA_DIR / "day13"
    with open(day_thirteen_file, "r") as f:
        return f.read()


def day13():
    print("--- Day 13: Transparent Origami ---")
    data = load_data()
    print(data)


if __name__ == "__main__":
    day13()
