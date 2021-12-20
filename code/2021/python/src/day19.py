from collections import namedtuple
from typing import List
import re

from src import DATA_DIR

ScannerPointCoords = namedtuple("ScannerPointCoords", ["x", "y", "z"])


class Scanner:
    def __init__(self):
        self.coords: List[ScannerPointCoords] = []

    def add_coords(self, coords: ScannerPointCoords):
        self.coords.append(coords)

    def __repr__(self) -> str:
        return f"Scanner(coords:{self.coords})"

    def __str__(self) -> str:
        fmt_str = []
        for idx, point_coords in enumerate(self.coords):
            fmt_str.append(f"P{idx}({point_coords.x},{point_coords.y},{point_coords.z})")
        return "\n".join(fmt_str)


def load_data() -> List[Scanner]:
    scanner_pattern = re.compile(r"--- scanner \d+ ---")
    scanner_list = []
    day_nineteen_file = DATA_DIR / "day19"
    with open(day_nineteen_file, "r") as f:
        contents = [scan_contents.split("\n") for scan_contents in scanner_pattern.split(f.read())]

    for scan_contents in contents:
        scanner = Scanner()
        for scan_coords in scan_contents:
            if scan_coords:
                x, y, z = [int(coord) for coord in scan_coords.split(",")]
                scanner.add_coords(ScannerPointCoords(x, y, z))
        scanner_list.append(scanner)

    return scanner_list


def day19():
    print("--- Day 19: Beacon Scanner ---")
    data = load_data()
    print(data)


if __name__ == "__main__":
    day19()
