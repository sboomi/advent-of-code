def load_day_6():
    filename = "data/day6"
    with open(filename, "r") as file:
        orbits = file.read()
    return [orbit.strip() for orbit in orbits.split("\n")]
