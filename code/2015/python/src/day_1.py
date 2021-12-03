"""Day 1: Not Quite Lisp"""
import logging
import time
from typing import List

import coloredlogs

from src import DATA_PATH

log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=log_fmt)
logger = logging.getLogger(__file__)
coloredlogs.install()


def load_day_1() -> str:
    filename = DATA_PATH / "day1"
    if not filename.exists():
        raise FileNotFoundError("'day1' not found.", f"Your path was {filename.resolve().as_posix()}")
    with open(filename, "r") as file:
        directions = file.read()
    return directions


def d1_p1(numbers: List[int]) -> int:
    for i in numbers:
        if 2020 - i in numbers:
            return (2020 - i) * i
    return 0


def d1_p2(numbers: List[int]) -> int:
    for i in numbers:
        for j in numbers:
            if 2020 - (i + j) in numbers:
                return i * j * (2020 - (i + j))
    return 0


def day_1() -> None:
    logger.info("Day 1: Not Quite Lisp")
    directions = load_day_1()
    t1 = time.time()
    total_expenses = d1_p1(numbers)
    logger.info(f"Total expenses: {total_expenses}")
    t2 = time.time()
    logger.info(f"Task 1 completed in {t2 - t1} seconds")
    total_expenses_three = d1_p2(numbers)
    logger.info(f"Total expenses (3): {total_expenses_three}")
    t3 = time.time()
    logger.info(f"Task 2 completed in {t3 - t2} seconds")
