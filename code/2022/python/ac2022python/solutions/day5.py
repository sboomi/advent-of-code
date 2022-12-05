"""Day 5: Supply Stacks"""
from pathlib import Path
import re
from typing import Optional

from rich import print

from ac2022python.solutions import DATA_PATH

PUZZLE_INPUT = Path(DATA_PATH / "day5")


class CrateStack:
    """Wrapper meant to adapt the schema of a crate stack in a more convenient way"""

    def __init__(self, crate_stack_hash: dict[int, list[str]]) -> None:
        self.struct = crate_stack_hash

    @classmethod
    def create(cls, crate_str: list[str]) -> "CrateStack":
        """Factory method creating a CrateStack instance from a 1D array of strings.

        Here is an example of an acceptable input:
        ```
        [
            "    [D]    ",
            "[N] [C]    ",
            "[Z] [M] [P]",
            " 1   2   3 ",
        ]
        ```

        Parameters
        ----------
        crate_str : list[str]
            A list of strings containing the shape of the crates as well as their
            stack pile numbers.

        Returns
        -------
        CrateStack
            A CrateStack instance, wrapping each crate pile as a dict table.
        """
        idx_val = [(idx, int(c)) for idx, c in enumerate(crate_str[-1]) if c.isdigit()]

        crate_obj = {
            val: [
                crate_line[idx]
                for crate_line in crate_str[:-1]
                if crate_line[idx].isalnum()
            ][::-1]
            for idx, val in idx_val
        }

        return cls(crate_obj)

    def __str__(self) -> str:
        fmt = [" ".join([f" {stck} " for stck in self.struct])]
        n_iter = max([len(crates) for crates in self.struct.values()])
        for i in range(n_iter):
            fmt_row = []
            for crates in self.struct.values():
                try:
                    crate_name = crates[i]
                    fmt_row.append(f"[{crate_name}]")
                except IndexError:
                    fmt_row.append("   ")
            fmt.insert(0, " ".join(fmt_row))
        return "\n".join(fmt)

    def get_top_crates(self) -> str:
        """Returns the combination of the top crates

        Returns
        -------
        str
            A combination of all top crate letters (from A-Z)
        """
        return "".join(v[-1] for v in self.struct.values())


class SupplyStacks:
    def __init__(self) -> None:
        self.crate_stack: Optional[CrateStack] = None

    def move_crate(self, instruction: str, multiple_crates: bool = False):
        """Method taking an instruction on how to move the crates from a
        stack to another and modifies the crate stack structure.

        It parses the numbers of crates to move from a starting point to
        an end point and performs the appropriate slices depending of the
        situation.

        Enabling `multiple_crates` switches to the second part where multiple
        crates are selected and moved at once.

        Parameters
        ----------
        instruction : str
            A sentence from the instructions list, written in the following
            format: "move {qty} from {start_crate} to {end_crate}"
        multiple_crates : bool, optional
            Flag enabling the second part of the problem, by default False
        """
        m = re.search(r"move (\d+) from (\d+) to (\d+)", instruction, re.M)
        if m is not None:
            qty, start_crate, end_crate = [int(m.group(i_g)) for i_g in range(1, 4)]
            len_start_crate = len(self.crate_stack.struct[start_crate])
            crates_to_move = self.crate_stack.struct[start_crate][
                len_start_crate - qty : len_start_crate
            ]
            if not multiple_crates:
                crates_to_move = crates_to_move[::-1]
            self.crate_stack.struct[end_crate] += crates_to_move
            self.crate_stack.struct[start_crate] = self.crate_stack.struct[start_crate][
                : len_start_crate - qty
            ]

    def find_top_crate_combination(
        self, stacks_and_order: Path, multiple_crates: bool = False
    ) -> str:
        """Takes a file containing the crate structure and the list of
        instructions, instanciates a CrateStack object then read the
        instructions to move crates around. When every operation is done,
        the function returns the combination of the top crates as the output.

        Enabling `multiple_crates` switches to the second part where multiple
        crates are selected and moved at once.

        Parameters
        ----------
        stacks_and_order : Path
            A file containing the crate structure and the instructions
        multiple_crates : bool, optional
            Flag enabling the second part of the problem, by default False

        Returns
        -------
        str
            A combination of all top crate letters (from A-Z)
        """
        with open(stacks_and_order, "r") as bf:
            crate_str: list[str] = []
            for line in bf:
                if not line.strip():
                    self.crate_stack = CrateStack.create(crate_str)

                if self.crate_stack is None:
                    crate_str.append(line)
                else:
                    self.move_crate(line, multiple_crates=multiple_crates)

        return self.crate_stack.get_top_crates()


def solve_first_part():
    ss = SupplyStacks()
    res = ss.find_top_crate_combination(PUZZLE_INPUT)
    print(f"The top crate combination after rearrangement is {res}")


def solve_second_part():
    ss = SupplyStacks()
    res = ss.find_top_crate_combination(PUZZLE_INPUT, multiple_crates=True)
    print(
        f"The top crate combination after rearrangement using the CrateMover 9001 is {res}"
    )


def solve_all():
    solve_first_part()
    solve_second_part()


if __name__ == "__main__":
    solve_all()
