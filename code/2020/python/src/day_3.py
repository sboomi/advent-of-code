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


def load_day_3() -> List[str]:
    filename = DATA_PATH / "day3"
    with open(filename, "r") as file:
        forest = file.readlines()
    return [line.strip() for line in forest]


def d3_p1(forest: List[str]) -> int:
    tree_count = 0
    i = 0
    j = 0
    while i < len(forest) - 1:
        j = (j + 3) % len(forest[0])
        i += 1
        if forest[i][j] == "#":
            tree_count += 1

    return tree_count


def count_trees(forest: List[str], slopey: int = 1, slopex: int = 3) -> int:
    tree_count = 0
    i = 0
    j = 0
    while i < len(forest) - 1:
        j = (j + slopex) % len(forest[0])
        i += slopey
        if forest[i][j] == "#":
            tree_count += 1
    return tree_count


def d3_p2(forest: List[str]) -> int:
    tree_product = 1
    list_slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    for slope in list_slopes:
        tree_product *= count_trees(forest, slopey=slope[1], slopex=slope[0])
    return tree_product


def day_3() -> None:
    logger.info("Day 2: Password Philosophy")
    forest = load_day_3()
    t1 = time.time()
    n_trees = d3_p1(forest)
    logger.info(f"Number of trees encountered: {n_trees}")
    t2 = time.time()
    logger.info(f"Task 1 completed in {t2 - t1} seconds")
    tree_product = d3_p2(forest)
    logger.info(f"Tree product: {tree_product}")
    t3 = time.time()
    logger.info(f"Task 2 completed in {t3 - t2} seconds")
