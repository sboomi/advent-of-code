def load_day_2():
    filename = "data/day2"
    with open(filename, "r") as file:
        passwords = file.readlines()
    return [password.strip() for password in passwords]
