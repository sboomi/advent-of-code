def load_day_6():
    filename = "data/day6"
    with open(filename, "r") as file:
        groups = file.read()
    return [[person for person in group.split("\n")] for group in groups.split("\n\n")]
