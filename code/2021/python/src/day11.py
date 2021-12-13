from src import DATA_DIR


def load_data():
    day_eleven_file = DATA_DIR / "day11"
    with open(day_eleven_file, "r") as f:
        return f.read()


def day11():
    print("--- Day 11: Dumbo Octopus ---")
    data = load_data()
    print(data)


if __name__ == "__main__":
    day11()
