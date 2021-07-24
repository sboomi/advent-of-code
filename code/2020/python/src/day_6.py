"""Day 6: Custom Customs"""
import logging
import time
from typing import List

import coloredlogs

from src import DATA_PATH

log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=log_fmt)
logger = logging.getLogger(__file__)
coloredlogs.install()


def load_day_6() -> List[List[str]]:
    filename = DATA_PATH / "day6"
    with open(filename, "r") as file:
        groups = file.read()
    return [[person for person in group.split("\n")] for group in groups.split("\n\n")]


def d6_p1(groups: List[List[str]]) -> int:
    counts = [len(set("".join(group))) for group in groups]
    return sum(counts)


def d6_p2(groups: List[List[str]]) -> int:
    count_yes = 0
    for group in groups:
        answers = list(set("".join(group)))
        for letter in answers:
            if all([letter in person for person in group]):
                count_yes += 1

    return count_yes


def day_6() -> None:
    logger.info("Day 6: Custom Customs")
    groups = load_day_6()
    t1 = time.time()
    counts = d6_p1(groups)
    logger.info(f"Total number of 'yes' answers: {counts}")
    t2 = time.time()
    logger.info(f"Task 1 completed in {t2 - t1} seconds")
    count_yes = d6_p2(groups)
    logger.info(f"Total number of 'yes' answers for every person: {count_yes}")
    t3 = time.time()
    logger.info(f"Task 2 completed in {t3 - t2} seconds")
