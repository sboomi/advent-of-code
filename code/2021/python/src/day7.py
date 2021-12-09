from src import DATA_DIR
from typing import List, Tuple


def load_data() -> List[int]:
    day_seven_file = DATA_DIR / "day7"
    with open(day_seven_file, "r") as f:
        return [int(num) for num in f.read().split(",")]


def find_center_range(crab_position: List[int]) -> Tuple[int, int]:
    midway = (max(crab_position) - min(crab_position)) // 2
    return midway, min(crab_position) + midway


def total_sum(n: int) -> int:
    if n == 0:
        return n
    else:
        return n + total_sum(n - 1)


def crab_spaceship_spending(x_position: int, dest: int, mode: str) -> int:
    if mode == "basic":
        return abs(x_position - dest)
    elif mode == "advanced":
        return sum(list(range(abs(x_position - dest) + 1)))
    else:
        raise NotImplementedError("`mode` must only take the following values: `basic` or `advanced`")


def get_optimum_fuel_spendings(crab_position: List[int], mode: str) -> int:
    midway, center = find_center_range(crab_position)

    if mode == "basic":
        fuel_used = sum([max(crab_position) for _ in crab_position])
    elif mode == "advanced":
        fuel_used = sum([sum(list(range(max(crab_position)))) for _ in crab_position])
    else:
        raise NotImplementedError("`mode` must only take the following values: `basic` or `advanced`")

    for x in range(midway + 1):
        x_neg = center - x
        x_pos = center + x + (max(crab_position) % 2)

        fuel_used = min(fuel_used, sum([crab_spaceship_spending(x, x_neg, mode=mode) for x in crab_position]))
        fuel_used = min(fuel_used, sum([crab_spaceship_spending(x, x_pos, mode=mode) for x in crab_position]))

    return fuel_used


def day7():
    print("--- Day 7: The Treachery of Whales ---")
    crab_position = load_data()
    midway, center = find_center_range(crab_position)
    print(f"Starting from {center} on a range of {midway}")
    min_fuel_used = get_optimum_fuel_spendings(crab_position, "basic")
    print(f"Minimum fuel quantity used: {min_fuel_used}")
    print("PART 2: do more engineering")
    min_fuel_used_adv = get_optimum_fuel_spendings(crab_position, "advanced")
    print(f"Minimum fuel quantity used (with more research): {min_fuel_used_adv}")


if __name__ == "__main__":
    day7()
