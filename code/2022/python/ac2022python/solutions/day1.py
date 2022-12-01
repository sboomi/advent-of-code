"""Day 1: Calorie Counting """
from ac2022python.solutions import DATA_PATH
from pathlib import Path

PUZZLE_INPUT = Path(DATA_PATH / "day1")


class CalorieCounting:
    @staticmethod
    def elf_with_the_most_calories_from_list(calories: Path) -> int:
        """Takes the list of calories and retains the elf carrying the heaviest load before returning it

        Parameters
        ----------
        calories : Path
            The list of calories

        Returns
        -------
        int
            The heaviest load one elf can carry
        """
        current_elf, heaviest_elf = 0, 0
        with open(calories, "r") as f:
            while f:
                line = f.readline()
                if line.strip().isdigit():
                    current_elf += int(line.strip())
                else:
                    heaviest_elf = max(current_elf, heaviest_elf)
                    current_elf = 0
                if line == "":
                    break
        return heaviest_elf

    @staticmethod
    def top_three_elves(calories: Path) -> int:
        top_three = [0, 0, 0]
        current_elf = 0

        with open(calories, "r") as f:
            while f:
                line = f.readline()
                if line.strip().isdigit():
                    current_elf += int(line.strip())
                else:
                    top_three = [current_elf] + top_three
                    top_three.sort()
                    top_three = top_three[1:]
                    current_elf = 0
                if line == "":
                    break

        return sum(top_three)


def solve_first_part():
    res = CalorieCounting.elf_with_the_most_calories_from_list(PUZZLE_INPUT)
    print(f"The most calories being carried by an elf is {res}.")


def solve_second_part():
    res = CalorieCounting.top_three_elves(PUZZLE_INPUT)
    print(f"The most calories being carried by the three first elves is {res}.")


def solve_all():
    solve_first_part()
    solve_second_part()


if __name__ == "__main__":
    solve_all()
