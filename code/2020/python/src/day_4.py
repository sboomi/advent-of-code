def load_day_4():
    filename = "data/day4"
    passports = []
    with open(filename, "r") as file:
        passport = {}
        for line in file.readlines():
            if line == "\n":
                passports.append(passport)
                passport = {}
            else:
                for el in line.strip().split():
                    passport[el.split(":")[0]] = el.split(":")[1]
    passport = {}
    for el in line.strip().split():
        passport[el.split(":")[0]] = el.split(":")[1]
    passports.append(passport)
    return passports
