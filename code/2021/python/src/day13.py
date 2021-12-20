from src import DATA_DIR


def load_data():
    day_thirteen_file = DATA_DIR / "day13"
    with open(day_thirteen_file, "r") as f:
        instructions = f.read().split("\n")
    split_idx = instructions.index("")
    return [tuple([int(coord) for coord in points.split(",")]) for points in instructions[:split_idx]], [
        (instr.lstrip("fold along ").split("=")[0], int(instr.lstrip("fold along ").split("=")[1]))
        for instr in instructions[split_idx + 1 :]
    ]


def day13():
    print("--- Day 13: Transparent Origami ---")
    points_list, folding_instructions = load_data()
    print(points_list)
    print(folding_instructions)


if __name__ == "__main__":
    day13()
