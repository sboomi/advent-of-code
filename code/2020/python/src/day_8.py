"""Day 8: Handheld Halting"""
import logging
import time
from typing import List, Tuple

import coloredlogs

from src import DATA_PATH

log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=log_fmt)
logger = logging.getLogger(__file__)
coloredlogs.install()


def load_day_8() -> List[Tuple[str, int]]:
    filename = DATA_PATH / "day8"
    with open(filename, "r") as file:
        list_instructions = [line.strip() for line in file.readlines()]
    return [(instruc.split()[0], int(instruc.split()[1])) for instruc in list_instructions]


def apply_instruction(instruction: Tuple[str, int]) -> Tuple[int, int]:
    acc_inc = 0
    ind_inc = 0

    if instruction[0] == "acc":
        acc_inc += instruction[1]
        ind_inc += 1
    elif instruction[0] == "jmp":
        ind_inc += instruction[1]
    elif instruction[0] == "nop":
        ind_inc += 1

    return acc_inc, ind_inc


def d8_p1(instructions: List[Tuple[str, int]]) -> int:
    accumulator = 0
    past_instructions_ind = []
    i = 0
    while i not in past_instructions_ind:
        acc_inc, ind_inc = apply_instruction(instructions[i])
        past_instructions_ind.append(i)
        accumulator += acc_inc
        i += ind_inc
    return accumulator


def fix_kink(instructions: List[Tuple[str, int]], ind: int) -> List[Tuple[str, int]]:
    com, val = instructions[ind]
    if com == "nop":
        replacement = ("jmp", val)
    elif com == "jmp":
        replacement = ("nop", val)
    else:
        replacement = (com, val)
    new_instructions = instructions.copy()
    new_instructions[ind] = replacement
    return new_instructions


def d8_p2(instructions: List[Tuple[str, int]]) -> int:
    # Starting from the bottom as hinted by the problem
    list_indexes = [i for i, v in enumerate(instructions) if v[0] in ["nop", "jmp"]][::-1]
    counter = 0
    accumulator = 0
    past_instructions_ind: List[int] = []
    i = 0
    fixed_ins = fix_kink(instructions, list_indexes[counter])
    while i < len(instructions):
        if i in past_instructions_ind:
            counter += 1
            accumulator = 0
            past_instructions_ind = []
            i = 0
            fixed_ins = fix_kink(instructions, list_indexes[counter])
        acc_inc, ind_inc = apply_instruction(fixed_ins[i])
        past_instructions_ind.append(i)
        accumulator += acc_inc
        i += ind_inc
    return accumulator


def day_8() -> None:
    logger.info("Day 8: Handheld Halting")
    instructions = load_day_8()
    t1 = time.time()
    accumulator_value = d8_p1(instructions)
    logger.info(f"Value of the accumulator: {accumulator_value}")
    t2 = time.time()
    logger.info(f"Task 1 completed in {t2 - t1} seconds")
    acc_val_fix = d8_p2(instructions)
    logger.info(f"Value of the accumulator (fixed): {acc_val_fix}")
    t3 = time.time()
    logger.info(f"Task 2 completed in {t3 - t2} seconds")
