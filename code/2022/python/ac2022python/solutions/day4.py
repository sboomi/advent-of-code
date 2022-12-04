"""Day 4: Camp Cleanup"""
from pathlib import Path

from rich import print

from ac2022python.solutions import DATA_PATH

PUZZLE_INPUT = Path(DATA_PATH / "day4")


class CampCleanup:
    @staticmethod
    def find_all_pairs(pairs: Path, is_intersecting: bool = False) -> int:
        """Browses through every pair of elf assigned to a section range and
        computes the sum of englobed pairs (whether the first or the second
        englobes the other).

        Enabling `is_intersecting` triggers the second part of the problem,
        where the algorithm finds the pairs intersecting with each other.

        Parameters
        ----------
        pairs : Path
            The path to the file containing the pairs of elves (X,Y) with
            the range of section IDs to clean (Xmin-Xmax,Ymin-Ymax).
        is_intersecting : bool, optional
            Flag enabling the second part of the day, by default False

        Returns
        -------
        int
            The number of pairs englobed (or intersecting if `is_intersecting`
            is enabled).
        """
        n_pairs = 0
        with open(pairs, "r") as f_pairs:
            for pair in f_pairs:
                first, second = pair.strip().split(",")
                first_min, first_max = [int(n) for n in first.split("-")]
                second_min, second_max = [int(n) for n in second.split("-")]

                if is_intersecting:
                    if not (first_max < second_min or second_max < first_min):
                        n_pairs += 1
                else:
                    if (second_min <= first_min and second_max >= first_max) or (
                        first_min <= second_min and first_max >= second_max
                    ):
                        n_pairs += 1

        return n_pairs


def solve_first_part():
    res = CampCleanup.find_all_pairs(PUZZLE_INPUT)
    print(f"The number of pairs where one englobes the other is {res}")


def solve_second_part():
    res = CampCleanup.find_all_pairs(PUZZLE_INPUT, is_intersecting=True)
    print(f"The number of pairs intersecting is {res}")


def solve_all():
    solve_first_part()
    solve_second_part()


if __name__ == "__main__":
    solve_all()
