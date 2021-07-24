"""Day 4: Passport Processing"""
import logging
import time
import re
from typing import List, Dict

import coloredlogs

from src import DATA_PATH

log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=log_fmt)
logger = logging.getLogger(__file__)
coloredlogs.install()


def load_day_4() -> List[Dict[str, str]]:
    filename = DATA_PATH / "day4"
    passports = []
    with open(filename, "r") as file:
        passport: Dict = {}
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


def d4_p1(passports: List[Dict[str, str]]) -> int:
    count = 0
    for passport in passports:
        if (len(list(passport.keys())) == 8) or (len(list(passport.keys())) == 7 and "cid" not in passport):
            count += 1
    return count


def d4_p2(passports: List[Dict[str, str]]) -> int:
    count = 0
    for passport in passports:
        if (len(list(passport.keys())) == 8) or (len(list(passport.keys())) == 7 and "cid" not in passport):
            # Insert instructions
            if (
                1920 <= int(passport["byr"]) <= 2002
                and 2010 <= int(passport["iyr"]) <= 2020
                and 2020 <= int(passport["eyr"]) <= 2030
            ):
                if (passport["hgt"][-2:] == "cm" and 150 <= int(passport["hgt"][:-2]) <= 193) or (
                    passport["hgt"][-2:] == "in" and 59 <= int(passport["hgt"][:-2]) <= 76
                ):
                    if (
                        re.search(r"#[a-f0-9]{6}", passport["hcl"])
                        and re.search(r"amb|blu|brn|gry|grn|hzl|oth", passport["ecl"])
                        and len(passport["pid"]) == 9
                    ):
                        count += 1

    return count


def day_4() -> None:
    logger.info("Day 4: Passport Proceeding")
    passports = load_day_4()
    t1 = time.time()
    n_valid_passports = d4_p1(passports)
    logger.info(f"Number of valid passports: {n_valid_passports}")
    t2 = time.time()
    logger.info(f"Task 1 completed in {t2 - t1} seconds")
    n_valid_passports_plus = d4_p2(passports)
    logger.info(f"Numbers of valid passports (update): {n_valid_passports_plus}")
    t3 = time.time()
    logger.info(f"Task 2 completed in {t3 - t2} seconds")
