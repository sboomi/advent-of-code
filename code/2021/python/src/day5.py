from src import DATA_DIR
from typing import List, Tuple


def load_data() -> Tuple[List[Tuple[int, ...]], List[Tuple[int, ...]]]:
    day_five_file = DATA_DIR / "day5"
    start_points = []
    end_points = []
    with open(day_five_file, "r") as f:
        for line in f.readlines():
            start_point, end_point = [el.strip() for el in line.split("->")]
            start_points.append(tuple([int(coord) for coord in start_point.split(",")]))
            end_points.append(tuple([int(coord) for coord in end_point.split(",")]))

    return start_points, end_points


def filter_horizontal_lines(
    start_points: List[Tuple[int, int]], end_points: List[Tuple[int, int]]
) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
    """Filters non-diagonal lines from the set of points by making sure either
    x1 and x2 are equal or y1 and y2 are equal.

    Parameters
    ----------
    start_points : List[Tuple[int, int]]
        [description]
    end_points : List[Tuple[int, int]]
        [description]

    Returns
    -------
    Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]
        [description]
    """
    new_start_points = []
    new_end_points = []
    for ((x1, y1), (x2, y2)) in zip(start_points, end_points):
        if x1 == x2 or y1 == y2:
            new_start_points.append((x1, y1))
            new_end_points.append((x2, y2))

    return new_start_points, new_end_points


def find_min_max_coords(start_points: List[Tuple[int, int]], end_points: List[Tuple[int, int]]) -> Tuple[int, int]:
    """Determines the boundary of the diagram by checking max X and max Y

    Parameters
    ----------
    start_points : List[Tuple[int, int]]
        [description]
    end_points : List[Tuple[int, int]]
        [description]

    Returns
    -------
    Tuple[int, int]
        [description]
    """
    max_x = max_y = 0
    for ((x1, y1), (x2, y2)) in zip(start_points, end_points):
        max_x = max(max_x, x1)
        max_x = max(max_x, x2)

        max_y = max(max_y, y1)
        max_y = max(max_y, y2)

    return max_x, max_y


def abs_incl_range(start: int, stop: int) -> range:
    if start > stop:
        return range(start, stop - 1, -1)
    else:
        return range(start, stop + 1)


def tracing_diagram(
    start_points: List[Tuple[int, int]], end_points: List[Tuple[int, int]], max_x: int, max_y: int
) -> List[List[int]]:
    """[summary]

    Parameters
    ----------
    start_points : List[Tuple[int, int]]
        [description]
    end_points : List[Tuple[int, int]]
        [description]
    max_x : int
        [description]
    max_y : int
        [description]

    Returns
    -------
    List[List[int]]
        [description]
    """

    diagram = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for ((x1, y1), (x2, y2)) in zip(start_points, end_points):
        if x1 == x2:
            segm_y = list(abs_incl_range(y1, y2))
            segm_x = [x1] * len(segm_y)
        elif y1 == y2:
            segm_x = list(abs_incl_range(x1, x2))
            segm_y = [y1] * len(segm_x)
        else:
            segm_x = list(abs_incl_range(x1, x2))
            segm_y = list(abs_incl_range(y1, y2))

        for j, i in zip(segm_y, segm_x):
            diagram[j][i] += 1

    return diagram


def count_overlaps(diagram: List[List[int]]) -> int:
    """[summary]

    Parameters
    ----------
    diagram : List[List[int]]
        [description]

    Returns
    -------
    int
        [description]
    """
    count_overlap = 0
    for diagram_row in diagram:
        for el in diagram_row:
            if el >= 2:
                count_overlap += 1
    return count_overlap


def day5():
    print("--- Day 5: Hydrothermal Venture ---")
    start_points, end_points = load_data()
    print("Part 1: determining intersections")
    start_hori_points, end_hori_points = filter_horizontal_lines(start_points, end_points)
    max_x, max_y = find_min_max_coords(start_hori_points, end_hori_points)
    print(f"Field dimensions: {max_x} x {max_y}")
    diagram = tracing_diagram(start_hori_points, end_hori_points, max_x, max_y)
    overlap_count = count_overlaps(diagram)
    print("Number of points where at least 2 lines overlap:", overlap_count)
    print("PART 2: now with diagonals")
    full_max_x, full_max_y = find_min_max_coords(start_points, end_points)
    diag_diagram = tracing_diagram(start_points, end_points, full_max_x, full_max_y)
    full_overlap_count = count_overlaps(diag_diagram)
    print("Number of points where at least 2 lines overlap (with diagonals):", full_overlap_count)


if __name__ == "__main__":
    day5()
