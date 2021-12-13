from src import DATA_DIR
from typing import List, Tuple


def load_data() -> List[List[int]]:
    day_nine_file = DATA_DIR / "day9"
    with open(day_nine_file, "r") as f:
        return [[int(letter) for letter in line.strip()] for line in f.readlines()]


def check_neighbors(heightmap: List[List[int]], current_point: Tuple[int, int], lims: Tuple[int, int]) -> List[int]:
    """Takes a heightmap and returns a list of all the neighbors located left, right, up and down the current point.

    It needs the map, current position (x, y) and map boundaries (n_rows, n_cols).
    The function checks out-of-bounds neighbors and assign -1 to the position if that's the case.

    Parameters
    ----------
    heightmap : List[List[int]]
        [description]
    current_point : Tuple[int, int]
        [description]
    lims : Tuple[int, int]
        [description]

    Returns
    -------
    List[int]
        [description]
    """
    x, y = current_point
    n_rows, n_cols = lims

    top = -1 if y - 1 < 0 else heightmap[y - 1][x]
    bottom = -1 if y + 1 >= n_rows else heightmap[y + 1][x]
    left = -1 if x - 1 < 0 else heightmap[y][x - 1]
    right = -1 if x + 1 >= n_cols else heightmap[y][x + 1]

    return [neighbor for neighbor in [top, right, bottom, left] if neighbor != -1]


def find_low_points(heightmap: List[List[int]]) -> List[int]:
    """Function checking all points from the maps and returning a list of all points who are lower than their neighbors

    The computation is done by checking whether or not the weighted sum is lower than the sum of all neighbors.

    Parameters
    ----------
    heightmap : List[List[int]]
        [description]

    Returns
    -------
    List[int]
        [description]
    """
    low_points = []

    n_rows = len(heightmap)
    n_cols = len(heightmap[0])

    for i, heightmap_row in enumerate(heightmap):
        for j, hm_point in enumerate(heightmap_row):
            neighbors = check_neighbors(heightmap, (j, i), (n_rows, n_cols))
            is_lowest = all([neighbor > hm_point for neighbor in neighbors])
            if is_lowest:
                low_points.append(hm_point)
    return low_points


def compute_risk_level(heightmap: List[List[int]]) -> int:
    """Computes risk-level based on lower points

    Parameters
    ----------
    heightmap : List[List[int]]
        [description]

    Returns
    -------
    int
        [description]
    """
    low_points = find_low_points(heightmap)

    return sum([point + 1 for point in low_points])


def determine_basin_size(
    basin_points: List[Tuple[int, int]], heightmap: List[List[int]], points_visited: List[Tuple[int, int]] = []
) -> int:
    n_rows = len(heightmap)
    n_cols = len(heightmap[0])

    if not basin_points:
        return len(points_visited)
    else:
        x, y = basin_points[0]
        if 0 <= x < n_cols and 0 <= y < n_rows and heightmap[y][x] != 9:
            points_visited.append((x, y))
            basin_points = basin_points[1:] + [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        else:
            basin_points = basin_points[1:]

        return determine_basin_size(
            [point for point in basin_points if point not in points_visited], heightmap, points_visited=points_visited
        )


def find_basin_size_list(heightmap: List[List[int]]) -> List[int]:
    low_points = []
    basin_size_list = []

    n_rows = len(heightmap)
    n_cols = len(heightmap[0])

    for i, heightmap_row in enumerate(heightmap):
        for j, hm_point in enumerate(heightmap_row):
            neighbors = check_neighbors(heightmap, (j, i), (n_rows, n_cols))
            is_lowest = all([neighbor > hm_point for neighbor in neighbors])
            if is_lowest:
                low_points.append((j, i))

    for point in low_points:
        x, y = point
        basin_size = determine_basin_size([(x, y)], heightmap, points_visited=[])
        basin_size_list.append(basin_size)

    return basin_size_list


def find_product_basins(basin_size_list: List[int]) -> int:
    order_basins = sorted(basin_size_list, reverse=True)
    return order_basins[0] * order_basins[1] * order_basins[2]


def day9():
    print("--- Day 9: Smoke Basin ---")
    heightmap = load_data()
    risk_level = compute_risk_level(heightmap)
    print("Risk level of the map:", risk_level)
    basin_size_list = find_basin_size_list(heightmap)
    product_basins = find_product_basins(basin_size_list)
    print("Product of size basins", product_basins)


if __name__ == "__main__":
    day9()
