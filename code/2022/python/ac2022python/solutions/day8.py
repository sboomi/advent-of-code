"""Day 8: Treetop Tree House"""
from pathlib import Path
from rich import print

from ac2022python.solutions import DATA_PATH

PUZZLE_INPUT = Path(DATA_PATH / "day8")


class TreeCell:
    def __init__(self, x: int, y: int, height: int, is_visible: bool) -> None:
        self.x = x
        self.y = y
        self.height = height
        self.is_visible = is_visible


class TreePatch:
    def _init_visible_cells(self):
        for i_row in range(self.n_rows):
            self.grid[0][i_row].is_visible = True
            self.grid[-1][i_row].is_visible = True

        for i_col in range(self.n_cols):
            self.grid[i_col][0].is_visible = True
            self.grid[i_col][-1].is_visible = True

    def __init__(self, grid: list[list[TreeCell]]):
        self.grid = grid
        self.n_rows = len(grid)
        self.n_cols = len(grid[0])
        self._init_visible_cells()

    def to_list(self) -> list[list[int]]:
        return [[cell.height for cell in grid_row] for grid_row in self.grid]

    def find_visible_cells(self):
        pass

    def n_visible_cells(self) -> int:
        return sum([cell.is_visible for row in self.grid for cell in row])

    @classmethod
    def from_file(cls, file: Path) -> "TreePatch":
        grid = []
        with open(file, "r") as f:
            for i_row, line in enumerate(f.readlines()):
                grid_row = []
                for i_col, height in enumerate(line.strip()):
                    grid_row.append(TreeCell(i_row, i_col, int(height), False))
                grid.append(grid_row)
        return cls(grid)


class TreeTopTreeHouse:
    @staticmethod
    def count_visible_trees(tree_patch_file: Path) -> int:
        tp = TreePatch.from_file(tree_patch_file)

        for i in range(1, tp.n_rows - 1):
            for j in range(1, tp.n_cols - 1):
                tp.is_tree_visible((i, j))

        return tp.n_visible_cells


def solve_first_part():
    print("lef")


def solve_second_part():
    print("hf")


def solve_all():
    solve_first_part()
    solve_second_part()


if __name__ == "__main__":
    solve_all()
