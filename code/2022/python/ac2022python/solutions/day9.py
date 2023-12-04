"""Day 9: Rope Bridge"""
from pathlib import Path

from rich import print
from collections import Counter

from ac2022python.solutions import DATA_PATH

PUZZLE_INPUT = Path(DATA_PATH / "day9")


class RopeBridge:
    @staticmethod
    def count_visited_tail_positions(instructions: Path) -> int:
        visited_positions = []
        current_head_position = (0, 0)
        current_tail_position = ()
        with open(instructions, "r") as f:
            for line in f:
                direction, steps = line.split()
                x, y = current_head_position
                steps = int(steps.strip())

                if direction == "R":
                    for step in range(steps):
                        current_head_position = (x + step, y)
                        if current_tail_position == ():
                            current_tail_position == (0, 0)
                elif direction == "L":
                    for step in range(steps):
                        current_head_position = (x - step, y)
                        if current_tail_position == ():
                            current_tail_position == (0, 0)
                elif direction == "U":
                    for step in range(steps):
                        current_head_position = (x, y + step)
                        if current_tail_position == ():
                            current_tail_position == (0, 0)
                elif direction == "D":
                    for step in range(steps):
                        current_head_position = (x, y - step)
                        if current_tail_position == ():
                            current_tail_position == (0, 0)

        c = Counter(visited_positions)
        return sum([val > 1 for val in c.values()])


def solve_first_part():
    res = RopeBridge.get_total_score(PUZZLE_INPUT)
    print(f"Your total score is {res}")


def solve_second_part():
    print("jej")


def solve_all():
    solve_first_part()
    solve_second_part()


if __name__ == "__main__":
    solve_all()
