from typing import List, Tuple
from src import DATA_DIR

DIM_GRID = 10


def load_data() -> List[List[int]]:
    day_eleven_file = DATA_DIR / "day11"
    with open(day_eleven_file, "r") as f:
        return [[int(n) for n in line.strip()] for line in f.readlines()]


def find_neighbors(point: Tuple[int, int], n_rows: int, n_cols: int):
    x, y = point
    return [
        (x + j, y + i)
        for i in range(-1, 2)
        for j in range(-1, 2)
        if (x + j, y + i) != (x, y) and (0 <= x + j < n_cols and 0 <= y + i < n_rows)
    ]


def add_flash_contributions(
    octo_grid: List[List[int]], flash_list=List[Tuple[int, int]], visited_flash_points: List[Tuple[int, int]] = []
) -> List[List[int]]:
    """Takes a list of shining points and adds +1 to its neighborhood

    If a neighbor point shines, this one is added to the list.

    Parameters
    ----------
    octo_grid : List[List[int]]
        [description]
    flash_list : [type], optional
        [description], by default List[Tuple[int, int]]
    visited_flash_points : List[Tuple[int, int]], optional
        [description], by default []

    Returns
    -------
    List[List[int]]
        [description]
    """
    if not flash_list:
        return octo_grid

    flash_x, flash_y = flash_list[0]
    neighbors = find_neighbors((flash_x, flash_y), len(octo_grid), len(octo_grid[0]))
    visited_flash_points.append((flash_x, flash_y))
    for neighbor in neighbors:
        neigh_x, neigh_y = neighbor
        octo_grid[neigh_y][neigh_x] += 1
        if octo_grid[neigh_y][neigh_x] > 9:
            # It becomes a flashing point
            flash_list.append((neigh_x, neigh_y))

    return add_flash_contributions(
        octo_grid,
        [flash_point for flash_point in flash_list[1:] if flash_point not in visited_flash_points],
        visited_flash_points,
    )


def update_octo_grid(octo_grid: List[List[int]]) -> Tuple[List[List[int]], int]:
    """Takes a grid of octopi and returns the grid after transformation and number of flashes

    For each step:
    1. Does a first loop where it adds 1 to each energy level
    2. Runs the loop a second time to compute every neighbor on octopi whose energy
    level is above 9 and add 1 to them
    3. Runs a third and last time to update the flash counter and reset any energy
    level above 9 to 0 for the next round

    Parameters
    ----------
    octo_grid : List[List[int]]
        [description]

    Returns
    -------
    Tuple[List[List[int]], int]
        [description]
    """
    n_flashes = 0
    shining_points = []
    # Add 1 to each energy lv
    new_octo_grid = [[energy_lv + 1 for energy_lv in line] for line in octo_grid]

    # Adds flashing octopi's contributions
    # Get neighbor list first
    for i, octo_row in enumerate(new_octo_grid):
        for j, energy_lv in enumerate(octo_row):
            if energy_lv > 9:
                shining_points.append((j, i))

    new_octo_grid = add_flash_contributions(new_octo_grid, shining_points, [])
    # Reset positions and update counter
    for i, octo_row in enumerate(new_octo_grid):
        for j, energy_lv in enumerate(octo_row):
            if energy_lv > 9:
                n_flashes += 1
                new_octo_grid[i][j] = 0

    return new_octo_grid, n_flashes


def count_flashes(n_steps: int, octo_grid: List[List[int]]) -> int:
    """Takes a grid of octopi and returns the number of flashes after `n_steps`

    For each step:
    1. Does a first loop where it adds 1 to each energy level
    2. Runs the loop a second time to compute every neighbor on octopi whose energy
    level is above 9 and add 1 to them
    3. Runs a third and last time to update the flash counter and reset any energy
    level above 9 to 0 for the next round

    Parameters
    ----------
    n_steps : int
        [description]
    octo_grid : List[List[int]]
        [description]

    Returns
    -------
    int
        [description]
    """
    n_flashes = 0
    new_octo_grid = [[energy_lv for energy_lv in line] for line in octo_grid]

    for _ in range(n_steps):
        new_octo_grid, step_flashes = update_octo_grid(new_octo_grid)
        n_flashes += step_flashes

    return n_flashes


def day11():
    print("--- Day 11: Dumbo Octopus ---")
    octopi_energy_lv = load_data()
    octopi_flashes_100 = count_flashes(100, octopi_energy_lv)
    print("N° of flashes after 100 steps:", octopi_flashes_100)


if __name__ == "__main__":
    day11()
