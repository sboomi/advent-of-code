def load_day_9():
    filename = "data/day9"
    with open(filename, "r") as file:
        return [int(line.strip()) for line in file.readlines()]
