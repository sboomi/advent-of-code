def load_day_5():
    filename = "data/day5"
    with open(filename, "r") as file:
        seats = file.readlines()
    return [seat.strip() for seat in seats]
