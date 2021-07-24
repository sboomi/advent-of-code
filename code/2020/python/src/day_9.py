"""Day 9: Encoding Error"""
import logging
import time
from typing import List

import coloredlogs

from src import DATA_PATH

log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=log_fmt)
logger = logging.getLogger(__file__)
coloredlogs.install()


def load_day_9() -> List[int]:
    filename = DATA_PATH / "day9"
    with open(filename, "r") as file:
        return [int(line.strip()) for line in file.readlines()]


def d9_p1(numbers: List[int], size_preamble: int) -> int:
    for i in range(len(numbers) - size_preamble):
        preamble = numbers[0 + i : size_preamble + i]
        next_num = numbers[size_preamble + i]
        pairs = [(n, next_num - n) for i, n in enumerate(preamble) if next_num - n in preamble[:i] + preamble[i + 1 :]]
        if not pairs:
            return next_num
    return -1


def d9_p2(numbers: List[int], intruder: int) -> int:
    ind = numbers.index(intruder)
    list_subset = numbers[:ind]
    for i in range(len(list_subset)):
        list_portion = list_subset[i:]
        for j in range(len(list_portion)):
            if sum(list_portion[:j]) == intruder:
                encryption_list = list_portion[:j]
    return max(encryption_list) + min(encryption_list)


def day_9() -> None:
    logger.info("Day 9: Encoding Error")
    numbers = load_day_9()
    t1 = time.time()
    first_num = d9_p1(numbers, 25)
    logger.info(f"First number that doesn't fit: {first_num}")
    t2 = time.time()
    logger.info(f"Task 1 completed in {t2 - t1} seconds")
    encryption_error = d9_p2(numbers, first_num)
    logger.info(f"Encryption weakness: {encryption_error}")
    t3 = time.time()
    logger.info(f"Task 2 completed in {t3 - t2} seconds")
