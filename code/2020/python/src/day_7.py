"""Day 7: Handy Haversacks"""
import logging
import time
from typing import Dict, List

import coloredlogs

from src import DATA_PATH

log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=log_fmt)
logger = logging.getLogger(__file__)
coloredlogs.install()


def load_day_7() -> List[str]:
    filename = DATA_PATH / "day7"
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]


def bag_contents(rules, list_of_bags):
    super_bags = []
    for rule in rules:
        target_bag, contents = [el.replace("bags", "").strip() for el in rule.split("contain")]
        if any([bag in contents for bag in list_of_bags]):
            super_bags.append(target_bag)
    return super_bags


def d7_p1(rules: List[str]) -> int:
    list_of_bags = ["shiny gold"]
    total_bags = ["shiny gold"]
    while list_of_bags:
        list_of_bags = bag_contents(rules, list_of_bags)
        if list_of_bags:
            total_bags.extend(list_of_bags)

    return len(set(total_bags)) - 1


def organize_bag_items(list_bags: List[str]) -> Dict[str, Dict[str, int]]:
    item_bags = {}
    for bag in list_bags:
        main_bag, contents = [el.replace("bags", "").replace("bag", "").strip() for el in bag[:-1].split("contain")]
        if "no other" in contents:
            items = {}
        else:
            item_list = [el.strip() for el in contents.split(",")]
            items = {" ".join(item.split()[1:]): int(item.split()[0]) for item in item_list}
        item_bags[main_bag] = items
    return item_bags


def pick_bags(items: Dict[str, Dict[str, int]], query: str) -> int:
    if not items[query]:
        return 0
    else:
        return sum(list(items[query].values()) + [v * pick_bags(items, k) for k, v in items[query].items()])


def d7_p2(rules: List[str]) -> int:
    item_bags = organize_bag_items(rules)
    total_bags = pick_bags(item_bags, "shiny gold")
    return total_bags


def day_7() -> None:
    logger.info("Day 7: Handy Haversacks")
    rules = load_day_7()
    t1 = time.time()
    n_bags = d7_p1(rules)
    logger.info(f"N° of bag colors: {n_bags}")
    t2 = time.time()
    logger.info(f"Task 1 completed in {t2 - t1} seconds")
    n_bags_2 = d7_p2(rules)
    logger.info(f"N° of bag colors (update): {n_bags_2}")
    t3 = time.time()
    logger.info(f"Task 2 completed in {t3 - t2} seconds")
