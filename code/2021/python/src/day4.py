from src import DATA_DIR
from typing import List, Tuple


class BingoBoard:
    BINGO_ROWS = 5
    BINGO_COLS = 5

    def __init__(self, bingo_list):
        if len(bingo_list) != 25:
            raise AttributeError(f"Bingo list's length must be {self.BINGO_COLS * self.BINGO_ROWS}")
        self.bingo_list = bingo_list
        self.checked = [False] * (self.BINGO_ROWS * self.BINGO_COLS)
        self.winning_board = False

    @classmethod
    def from_2d_array(cls, array_2d):
        return cls([num for line in array_2d for num in line])

    def reshape2d(self, bingo_array: List[int]) -> List[List[int]]:
        """Transforms a 1D array into a 2D array of N_ROWS x N_COLS

        Parameters
        ----------
        bingo_array : List[int]
            The bingo array to reshape (actual array or boolean checks)

        Returns
        -------
        List[List[int]]
            2D representation of the array
        """
        return [
            [bingo_array[row * self.BINGO_ROWS + col] for col in range(self.BINGO_COLS)]
            for row in range(self.BINGO_ROWS)
        ]

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.bingo_list[item]
        if isinstance(item, tuple):
            row, col = item
            if isinstance(row, int) and isinstance(col, int):
                return self.bingo_list[row * self.BINGO_ROWS + col]
            if isinstance(row, slice) and isinstance(col, int):
                selected_col = self.bingo_list[col : self.BINGO_COLS * self.BINGO_ROWS : self.BINGO_COLS]
                return selected_col[row]
            if isinstance(row, int) and isinstance(col, slice):
                selected_row = self.bingo_list[row * self.BINGO_COLS : (row + 1) * self.BINGO_COLS]
                return selected_row[col]
            if isinstance(row, slice) and isinstance(col, slice):
                reshaped_bingo_board = self.reshape2d(self.bingo_list)
                return [resh_line[col] for resh_line in reshaped_bingo_board[row]]

    def check_number(self, number: int) -> None:
        """Checks if the drawn number is on the bingo card and marks it as checked

        Parameters
        ----------
        number : int
            The drawn number
        """
        for idx, bingo_sq in enumerate(self.bingo_list):
            if number == bingo_sq:
                self.checked[idx] = True

    def check_if_winning(self) -> None:
        """Checks whether the board is winning or not by making sure all numbers
        from a row or column are checked (diagonals don't count).
        """
        for row_idx in range(self.BINGO_ROWS):
            if all(self.checked[row_idx * self.BINGO_COLS : (row_idx + 1) * self.BINGO_COLS]):
                self.winning_board = True
                return

        for col_idx in range(self.BINGO_COLS):
            if all(self.checked[col_idx : self.BINGO_COLS * self.BINGO_ROWS : self.BINGO_COLS]):
                self.winning_board = True
                return

    def get_unmarked_numbers_sum(self) -> int:
        """Finds the sum of unmarked numbers on the board

        Returns
        -------
        int
            The total sum of unmarked numbers
        """
        return sum([bingo_sq for bingo_sq, is_drawn in zip(self.bingo_list, self.checked) if not is_drawn])

    def __repr__(self):
        fmt_str = []
        fmt_str.append(f"Bingo list: {self.bingo_list}")
        fmt_str.append(f"Checked squares: {self.checked}")
        return "\n".join(fmt_str)

    def __str__(self):
        fmt_str = []
        for i in range(self.BINGO_ROWS):
            current_row = self.__getitem__((i, slice(None, None, None)))
            current_row_checked = self.checked[i * self.BINGO_COLS : (i + 1) * self.BINGO_COLS]
            fmt_str.append(
                " ".join([f"{num:2d}" if not sq_chk else "##" for num, sq_chk in zip(current_row, current_row_checked)])
            )
        return "\n".join(fmt_str)


def load_data() -> Tuple[List[int], List[BingoBoard]]:
    """Loads data as a 2d int array stored in BingoBoard instances

    Returns
    -------
    Tuple[List[int], List[BingoBoard]]
        [description]
    """
    day_four_file = DATA_DIR / "day4"
    bingo_boards = bingo_board = []
    with open(day_four_file, "r") as f:
        numbers_to_draw = [int(num) for num in f.readline().split(",")]
        while True:
            current_line = f.readline()
            if not current_line:
                break

            current_line = current_line.strip()
            if current_line:
                bingo_board.append([int(num) for num in current_line.split()])
            else:
                if bingo_board:
                    bingo_boards.append(BingoBoard.from_2d_array(bingo_board))
                bingo_board = []

    return numbers_to_draw, bingo_boards


def find_winner(numbers_to_draw: List[int], bingo_boards: List[BingoBoard]) -> Tuple[int, BingoBoard]:
    for number in numbers_to_draw:
        for bingo_board in bingo_boards:
            bingo_board.check_number(number)
            bingo_board.check_if_winning()
            if bingo_board.winning_board:
                return number, bingo_board

    return number, bingo_board


def day4():
    print("--- Day 4: Giant Squid ---")

    numbers_to_draw, bingo_boards = load_data()
    print("N° of numbers to draw:", len(numbers_to_draw))
    print("Bingo board dimensions:", len(bingo_boards))

    win_number, win_board = find_winner(numbers_to_draw, bingo_boards)
    print(f"The winning number was {win_number}.")
    print(win_board)
    unmarked_sum = win_board.get_unmarked_numbers_sum()
    print(f"The total unmarked sum was {unmarked_sum} / FINAL SCORE = {win_number * unmarked_sum}")


if __name__ == "__main__":
    day4()
