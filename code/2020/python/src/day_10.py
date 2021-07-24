def load_day_10():
    filename = "data/day10"
    with open(filename, "r") as file:
        return [int(line.strip()) for line in file.readlines()]
