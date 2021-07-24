def load_day_1():
    filename = "data/day1"
    with open(filename, "r") as file:
        number_list = file.readlines()
    return [int(number) for number in number_list]
