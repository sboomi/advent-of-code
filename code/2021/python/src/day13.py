from typing import Dict, List, Tuple
from src import DATA_DIR


def load_data() -> Tuple[List[Tuple[int, ...]], List[Tuple[str, int]]]:
    day_thirteen_file = DATA_DIR / "day13"
    with open(day_thirteen_file, "r") as f:
        instructions = f.read().split("\n")
    split_idx = instructions.index("")
    return [tuple([int(coord) for coord in points.split(",")]) for points in instructions[:split_idx]], [
        (instr.lstrip("fold along ").split("=")[0], int(instr.lstrip("fold along ").split("=")[1]))
        for instr in instructions[split_idx + 1 :]
    ]


def find_paper_dims(points_list: List[Tuple[int, int]], folding_instructions: List[Tuple[str, int]]) -> Dict[str, int]:
    max_x, max_y = (0, 0)
    for points in points_list:
        x, y = points
        max_x, max_y = max(max_x, x), max(max_y, y)
    dims = {"x": max_x, "y": max_y}

    for fold in folding_instructions:
        dim, val = fold
        dims[dim] = min(dims[dim], val)

    return dims


def craft_paper(points_list: List[Tuple[int, int]], max_x: int = 0, max_y: int = 0) -> str:
    if not (max_x and max_y):
        for points in points_list:
            x, y = points
            max_x, max_y = max(max_x, x), max(max_y, y)
    elif not max_x:
        for points in points_list:
            max_x = max(max_x, points[0])
    elif not max_y:
        for points in points_list:
            max_y = max(max_y, points[1])

    paper = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for points in points_list:
        x, y = points
        paper[y][x] = "#"

    return "\n".join(["".join(paper_row) for paper_row in paper])


def fold_paper(points_list: List[Tuple[int, int]], fold: Tuple[str, int]) -> List[Tuple[int, int]]:
    new_point_list = []
    direction, line_idx = fold
    for point in sorted(points_list):
        x, y = point
        if direction == "x":
            if x <= line_idx:
                new_point_list.append((x, y))
            else:
                line_dist = x - line_idx
                if (x - (line_dist * 2), y) not in new_point_list:
                    new_point_list.append((x - (line_dist * 2), y))
        elif direction == "y":
            if y <= line_idx:
                new_point_list.append((x, y))
            else:
                line_dist = y - line_idx
                if (x, y - (line_dist * 2)) not in new_point_list:
                    new_point_list.append((x, y - (line_dist * 2)))

    return new_point_list


def serial_folding(
    points_list: List[Tuple[int, int]], folding_instructions: List[Tuple[str, int]]
) -> List[Tuple[int, int]]:
    pl_copy = points_list.copy()

    for folds in folding_instructions:
        pl_copy = fold_paper(pl_copy, folds)

    return pl_copy


def day13():
    print("--- Day 13: Transparent Origami ---")
    points_list, folding_instructions = load_data()
    points_first_fold = fold_paper(points_list, folding_instructions[0])
    print("N° of points after the first fold:", len(points_first_fold))
    final_folded_paper = serial_folding(points_list, folding_instructions)
    paper_dims = find_paper_dims(points_list, folding_instructions)
    fold_rep = craft_paper(final_folded_paper, max_x=paper_dims["x"], max_y=paper_dims["y"])
    print("Message:")
    print(fold_rep)


if __name__ == "__main__":
    day13()
