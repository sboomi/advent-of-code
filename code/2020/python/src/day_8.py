def load_day_8():
    filename = "data/day8"
    with open(filename, "r") as file:
        list_instructions = [line.strip() for line in file.readlines()]
    return [tuple([instruc.split()[0], int(instruc.split()[1])]) for instruc in list_instructions]
