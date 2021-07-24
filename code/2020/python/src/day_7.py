def load_day_7():
    filename = "data/day7"
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]
