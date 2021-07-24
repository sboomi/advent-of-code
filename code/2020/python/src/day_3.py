def load_day_3():
    filename = "data/day3"
    with open(filename, "r") as file:
        forest = file.readlines()
    return [line.strip() for line in forest]
