from typing import List, Tuple
from collections import namedtuple

from src import DATA_DIR

START_POINT = (0, 0)
END_POINT = lambda cavern_map: (len(cavern_map[0]) - 1, len(cavern_map) - 1)

NodeValue = namedtuple("NodeValue", ["point", "value"])


def load_data() -> List[List[int]]:
    """Loads the map of the cavern, where
    each value represents the risk level.

    Returns
    -------
    List[List[int]]
        2D map of the cavern
    """
    day_fifteen_file = DATA_DIR / "day15"
    with open(day_fifteen_file, "r") as f:
        return [[int(el) for el in line] for line in f.read().split("\n")]


def next_nodes(point: Tuple[int, int], cavern_map: List[List[int]]) -> List[NodeValue]:
    x, y = point
    x_max, y_max = END_POINT(cavern_map)

    right_node = NodeValue((x + 1, y), cavern_map[y][x + 1]) if x <= x_max else None
    down_node = NodeValue((x, y + 1), cavern_map[y + 1][x]) if y <= y_max else None
    return [node for node in (right_node, down_node) if node]


def calculate_lowest_total_risk(cavern_map: List[List[int]]) -> int:
    return 0


def day15():
    print("--- Day 15: Chiton ---")
    cavern_map = load_data()
    print("\n".join(["".join([str(risk_lv) for risk_lv in cavern_row]) for cavern_row in cavern_map]))
    print(f"Map dims: {len(cavern_map[0])} x {len(cavern_map)}")


if __name__ == "__main__":
    day15()
