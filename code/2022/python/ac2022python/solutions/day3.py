"""Day 3: Rucksack Reorganization"""
from pathlib import Path
import string
from rich import print

from ac2022python.solutions import DATA_PATH

PUZZLE_INPUT = Path(DATA_PATH / "day3")


class RucksackOrganization:
    @staticmethod
    def find_item_priority_in_both_compartments(rucksack: str) -> int:
        """Divides the rucksack in half to find the common item in
        both compartments by performing a set intersection. The result
        is the priority index stated by the rules.

        Parameters
        ----------
        rucksack : str
            The items from the rucksack. A string with characters from a to Z.

        Returns
        -------
        int
            The priority index from the duplicate item.
        """
        common_item = list(
            set(rucksack[: len(rucksack) // 2]) & set(rucksack[len(rucksack) // 2 :])
        )[0]
        return string.ascii_letters.index(common_item) + 1

    @staticmethod
    def get_priority_sum(rucksacks: Path) -> int:
        """Opens the list of rucksacks from a file and returns the
        total priority sum by performing `find_item_priority_in_both_compartments` on
        each line.

        Parameters
        ----------
        rucksacks : Path
            The file containing each rucksack item description.

        Returns
        -------
        int
            The total sum from each item's priority present in both compartments.
        """
        priority_sum = 0
        with open(rucksacks, "r") as f:
            for rucksack in f:
                priority_sum += (
                    RucksackOrganization.find_item_priority_in_both_compartments(
                        rucksack
                    )
                )
        return priority_sum

    @staticmethod
    def find_item_priority_in_group_of_three(rucksacks: list[str]) -> int:
        """Takes a group of elves (three rucksacks) and performs an intersection over
        the three bags to find the common item. The result is the priority index of this item.

        Parameters
        ----------
        rucksacks : list[str]
            A list of three rucksacks. Each rucksack is a string with characters from a to Z.

        Returns
        -------
        int
            The priority index from the common item.
        """
        common_item = list((set.intersection(*[set(rs) for rs in rucksacks])))[0]
        return string.ascii_letters.index(common_item) + 1

    @staticmethod
    def get_priority_sum_group_of_three(rucksacks: Path) -> int:
        """Reads a rucksack list, retains a group of three over the file's
        lecture and performs `find_item_priority_in_group_of_three` on this group of three.

        The result is the sum of the priorities index from the common items each group had in
        common.

        Parameters
        ----------
        rucksacks : Path
            The file containing each rucksack item description.

        Returns
        -------
        int
            The total sum from each item's priority present among a group of three elves.
        """
        priority_sum = 0
        with open(rucksacks, "r") as f:
            grp_rucksacks = ["", "", ""]
            for idx_l, rucksack in enumerate(f):
                grp_rucksacks[idx_l % 3] = rucksack.strip()
                if (idx_l + 1) % 3 == 0:
                    priority_sum += (
                        RucksackOrganization.find_item_priority_in_group_of_three(
                            grp_rucksacks
                        )
                    )

        return priority_sum


def solve_first_part():
    res = RucksackOrganization.get_priority_sum(PUZZLE_INPUT)
    print(
        f"The sum of the priority of the items present in both compartments is {res}."
    )


def solve_second_part():
    res = RucksackOrganization.get_priority_sum_group_of_three(PUZZLE_INPUT)
    print(
        f"The sum of the priority of the items present among a group of 3 elves is {res}."
    )


def solve_all():
    solve_first_part()
    solve_second_part()


if __name__ == "__main__":
    solve_all()
