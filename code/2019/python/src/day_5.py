def load_day_5():
    filename = "data/day5"
    with open(filename, "r") as file:
        number_list = file.read()
    return [int(number) for number in number_list.split(",")]
