def load_day_3():
    filename = "data/day3"
    with open(filename, "r") as file:
        fuses = file.read()
    return [[direction.strip() for direction in fuse.split(",")] for fuse in fuses.split("\n")]
