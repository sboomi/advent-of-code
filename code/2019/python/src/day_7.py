def load_day_7():
    filename = "data/day7"
    with open(filename, "r") as file:
        number_list = file.read()
    return [int(number) for number in number_list.split(",")]
