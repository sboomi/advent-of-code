def load_day_2():
    filename = "data/day2"
    with open(filename, "r") as file:
        number_list = file.read()
    return [int(number) for number in number_list.split(",")]
