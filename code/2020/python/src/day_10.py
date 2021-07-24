"""Day 10: Adapter Array"""
import logging
import time
from typing import Dict, List

import coloredlogs

from src import DATA_PATH

log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=log_fmt)
logger = logging.getLogger(__file__)
coloredlogs.install()


def load_day_10() -> List[int]:
    filename = DATA_PATH / "day10"
    with open(filename, "r") as file:
        return [int(line.strip()) for line in file.readlines()]


def d10_p1(joltage_r: List[int]) -> Dict[str, int]:
    eff_rating = 0
    results = {"1": 0, "3": 0}
    while eff_rating < max(joltage_r):
        if 1 + eff_rating in joltage_r:
            eff_rating += 1
            results["1"] += 1
        elif 3 + eff_rating in joltage_r:
            eff_rating += 3
            results["3"] += 1

    results["3"] += 1
    return results


def d10_p2():
    pass


def day_10() -> None:
    logger.info("Day 10: Adapter Array")
    joltage_ratings = load_day_10()
    t1 = time.time()
    diff_joltage = d10_p1(joltage_ratings)
    prod_voltage = diff_joltage["1"] * diff_joltage["3"]
    logger.info(f"N° joltage differences: {diff_joltage} / Product: {prod_voltage}")
    t2 = time.time()
    logger.info(f"Task 1 completed in {t2 - t1} seconds")
    _ = d10_p2()
    # logger.info(f": {}")
    logger.error("Not implemented.")
    t3 = time.time()
    logger.info(f"Task 2 completed in {t3 - t2} seconds")
