from typing import List
from src import DATA_DIR


def load_data() -> List[int]:
    day_one_file = DATA_DIR / "day1"
    with open(day_one_file, "r") as f:
        return [int(line) for line in f.readlines()]


def count_depmes_increase(report: List[int]) -> int:
    return sum([el1 - el2 > 0 for el1, el2 in zip(report[1:], report[:-1])])


def count_by_three(report: List[int]) -> int:
    sliding_window = sum(report[:3])
    increase_count = 0

    for idx in range(1, len(report)):
        if idx + 1 < len(report) - 1:
            increase_count += int(sum(report[idx : idx + 3]) - sliding_window > 0)
            sliding_window = sum(report[idx : idx + 3])

    return increase_count


def day1():
    print("--- Day 1: Sonar Sweep ---")
    report = load_data()
    print("PART 1: Counting the number of times a depth measurement increases")
    count_depmes = count_depmes_increase(report)
    print("Result:", count_depmes)
    print("PART 2: Counting by three")
    count_three_depmes = count_by_three(report)
    print("Result:", count_three_depmes)


if __name__ == "__main__":
    day1()
