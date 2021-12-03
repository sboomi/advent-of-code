from typing import List, Tuple
from src import DATA_DIR


def load_data() -> List[Tuple[str, int]]:
    day_two_file = DATA_DIR / "day2"
    with open(day_two_file, "r") as f:
        return [(line.split()[0], int(line.split()[1])) for line in f.readlines()]


def move_submarine(instructions: List[Tuple[str, int]], position=(0, 0)) -> Tuple[int, int]:
    """Reads a list of instructions and returns the final position (X, Y).
    X = horizontal position in units
    Y = submarine depth in units

    The function can take 3 types of directions.
    * forward X increases the horizontal position by X units.
    * down X increases the depth by X units.
    * up X decreases the depth by X units.

    Parameters
    ----------
    instructions : List[Tuple[str, int]]
        list of directions and values for a submarine (ie. `forward 5`)
    position : tuple, optional
        initial position of the submarine, by default (0,0)

    Returns
    -------
    Tuple[int, int]
        final position of the submarine
    """
    for instruction in instructions:
        direction, units = instruction
        x, y = position
        if direction == "forward":
            position = (x + units, y)
        elif direction == "down":
            position = (x, y + units)
        elif direction == "up":
            position = (x, y - units)

    return position


def move_submarine_aim(instructions: List[Tuple[str, int]], position=(0, 0, 0)) -> Tuple[int, int, int]:
    """Reads a list of instructions and returns the final position (X, Y, Z).
    X = horizontal position in units
    Y = submarine depth in units
    Z = aim value in units

    The rules are slightly different as depth (Y) depends of the aim (Z)
    * down X increases your aim by X units.
    * up X decreases your aim by X units.
    * forward X does two things:
        * It increases your horizontal position by X units.
        * It increases your depth by your aim multiplied by X.

    Parameters
    ----------
    instructions : List[Tuple[str, int]]
        list of directions and values for a submarine (ie. `forward 5`)
    position : tuple, optional
        initial position of the submarine, by default (0, 0, 0)

    Returns
    -------
    Tuple[int, int, int]
        final position of the submarine
    """
    for instruction in instructions:
        direction, units = instruction
        x, y, aim = position
        if direction == "forward":
            position = (x + units, y + (units * aim), aim)
        elif direction == "down":
            position = (x, y, aim + units)
        elif direction == "up":
            position = (x, y, aim - units)
    return position


def day2():
    print("--- Day 2: Dive! ---")
    planned_course = load_data()
    print("PART 1: Moving submarine")
    submarine_position = move_submarine(planned_course)
    x, y = submarine_position
    print("Final position:", submarine_position, f"(product: {x*y})")
    print("PART 2: Taking aim in consideration")
    x_bis, y_bis, aim = move_submarine_aim(planned_course)
    print("Final position:", (x_bis, y_bis), "with aim of", aim, f"(product = {x_bis*y_bis})")


if __name__ == "__main__":
    day2()
