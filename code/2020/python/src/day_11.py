def load_day_11():
    filename = "data/day11"
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]
