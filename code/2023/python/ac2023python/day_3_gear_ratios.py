from dataclasses import dataclass
from pathlib import Path
from ac2023python.settings import DATA_PATH

DATA_FILE = DATA_PATH / "day3"


@dataclass
class Number:
    value: int
    line: int
    position: tuple[int, int]

    def __eq__(self, __value: object) -> bool:
        return (
            self.value == __value.value
            and self.line == __value.line
            and self.position == __value.position
        )

    def symbols(self, schematic: list[str]) -> list[str]:
        n_rows, n_cols = len(schematic), len(schematic[0])
        return [
            schematic[pos_y][pos_x]
            for pos_y in range(max(self.line - 1, 0), min(self.line + 2, n_rows - 1))
            for pos_x in range(
                max(self.position[0] - 1, 0), min(self.position[1] + 2, n_cols - 1)
            )
            if (pos_y, pos_x)
            not in [
                (self.line, d_pos)
                for d_pos in range(self.position[0], self.position[1] + 1)
            ]
            and schematic[pos_y][pos_x] != "."
        ]

    def is_part_number(self, schematic: list[str]) -> bool:
        return bool(self.symbols(schematic))


def get_engine_schematic(p: Path = DATA_FILE) -> list[str]:
    with open(p, "r") as f:
        contents = [line.strip() for line in f.readlines()]
    return contents


def register_numbers(engine_schematic: list[str]) -> list[Number]:
    numbers, num_buffer, pos_start = [], "", 0

    for n_line, line in enumerate(engine_schematic):
        for n_col, col in enumerate(line):
            if col.isdigit():
                if not num_buffer:
                    pos_start = n_col
                num_buffer += col
            else:
                if num_buffer:
                    numbers.append(
                        Number(
                            value=int(num_buffer),
                            line=n_line,
                            position=(pos_start, n_col - 1),
                        )
                    )
                    num_buffer = ""
        if num_buffer:
            numbers.append(
                Number(
                    value=int(num_buffer),
                    line=n_line,
                    position=(pos_start, n_col - 1),
                )
            )
        num_buffer, pos_start = "", 0

    return numbers


def find_part_numbers(engine_schematic: list[str]) -> list[Number]:
    numbers = register_numbers(engine_schematic)
    return [number for number in numbers if number.is_part_number(engine_schematic)]


def main():
    engine_schematic = get_engine_schematic()

    part_numbers = find_part_numbers(engine_schematic)

    print(
        "The sum of all the part numbers of the engine schematic:",
        sum([num.value for num in part_numbers]),
    )


if __name__ == "__main__":
    main()
