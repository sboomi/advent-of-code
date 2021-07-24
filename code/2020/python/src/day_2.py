"""Day 2: Password Philosophy"""
import logging
import time
from typing import List

import coloredlogs

from src import DATA_PATH

log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=log_fmt)
logger = logging.getLogger(__file__)
coloredlogs.install()


def load_day_2() -> List[str]:
    filename = DATA_PATH / "day2"
    with open(filename, "r") as file:
        passwords = file.readlines()
    return [password.strip() for password in passwords]


def d2_p1(pwds: List[str]) -> int:
    n_valid = 0
    for crit in pwds:
        ran, letter, pw = crit.split()
        n_letter = pw.count(letter[0])
        ran_down, ran_up = [int(i) for i in ran.split("-")]
        if ran_down <= n_letter <= ran_up:
            n_valid += 1
    return n_valid


def d2_p2(pwds: List[str]) -> int:
    n_valid = 0
    for crit in pwds:
        pos, letter, pw = crit.split()
        letter = letter[0]
        pos_1, pos_2 = [int(i) - 1 for i in pos.split("-")]
        if (pw[pos_1] == letter and pw[pos_2] != letter) or (pw[pos_2] == letter and pw[pos_1] != letter):
            n_valid += 1
    return n_valid


def day_2() -> None:
    logger.info("Day 2: Password Philosophy")
    pwds = load_day_2()
    t1 = time.time()
    n_valid_pwds = d2_p1(pwds)
    logger.info(f"Number of valid passwords: {n_valid_pwds}")
    t2 = time.time()
    logger.info(f"Task 1 completed in {t2 - t1} seconds")
    n_valid_pwds_plus = d2_p2(pwds)
    logger.info(f"Numbers of valid passwords (update): {n_valid_pwds_plus}")
    t3 = time.time()
    logger.info(f"Task 2 completed in {t3 - t2} seconds")
