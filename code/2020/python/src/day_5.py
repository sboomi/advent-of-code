"""Day 5: Binary Boarding"""
import logging
import time
from typing import List

import coloredlogs

from src import DATA_PATH

log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=log_fmt)
logger = logging.getLogger(__file__)
coloredlogs.install()


def load_day_5() -> List[str]:
    filename = DATA_PATH / "day5"
    with open(filename, "r") as file:
        seats = file.readlines()
    return [seat.strip() for seat in seats]


def find_seat(code: str, n_places: int, code_letter: List[str]) -> int:
    max_limit = n_places - 1
    min_limit = 0
    middle = n_places // 2
    for letter in code[:-1]:
        if letter == code_letter[0]:
            max_limit -= middle
        elif letter == code_letter[1]:
            min_limit += middle
        middle = middle // 2
    return min_limit if code[-1] == code_letter[0] else max_limit


def d5_p1(seats: List[str]) -> int:
    max_id = 0
    for seat in seats:
        row = find_seat(seat[:7], 128, ["F", "B"])
        column = find_seat(seat[7:], 8, ["L", "R"])
        max_id = max(max_id, row * 8 + column)

    return max_id


def get_id_list(seats: List[str]) -> List[int]:
    list_id = []
    for seat in seats:
        row = find_seat(seat[:7], 128, ["F", "B"])
        column = find_seat(seat[7:], 8, ["L", "R"])
        seat_id = row * 8 + column
        if seat_id not in ([i for i in range(8)] + [127 * 8 + i for i in range(8)]):
            list_id.append(seat_id)
    return sorted(list_id)


def d5_p2(seats: List[str]) -> int:
    list_id = get_id_list(seats)
    full_list = [i for i in range(list_id[0], list_id[-1] + 1)]
    missing_id = list(set(full_list).difference(set(list_id)))[0]
    return missing_id


def day_5() -> None:
    logger.info("Day 5: Binary Boarding")
    seats = load_day_5()
    t1 = time.time()
    max_id = d5_p1(seats)
    logger.info(f"Highest seat ID: {max_id}")
    t2 = time.time()
    logger.info(f"Task 1 completed in {t2 - t1} seconds")
    my_seat_id = d5_p2(seats)
    logger.info(f"My seat ID: {my_seat_id}")
    t3 = time.time()
    logger.info(f"Task 2 completed in {t3 - t2} seconds")
