"""Day 3: Toboggan Trajectory"""
import logging
import time
from typing import List

import coloredlogs

from src import DATA_PATH

log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=log_fmt)
logger = logging.getLogger(__file__)
coloredlogs.install()


def load_day_11() -> List[str]:
    filename = DATA_PATH / "day11"
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]


# def day_() -> None:
#     logger.info("")
#     groups = load_day_()
#     t1 = time.time()
#     = d_p1()
#     logger.info(f": {}")
#     t2 = time.time()
#     logger.info(f"Task 1 completed in {t2 - t1} seconds")
#     = d_p2()
#     logger.info(f": {}")
#     t3 = time.time()
#     logger.info(f"Task 2 completed in {t3 - t2} seconds")
