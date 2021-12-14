from typing import Tuple, List
from src import DATA_DIR
from collections import Counter

SCORE_TABLE = {")": 3, "]": 57, "}": 1197, ">": 25137}
CORRUPTED_CHUNKS_COMBOS = [
    "()",
    "(}",
    "(>",
    "(]",
    "{)",
    "{}",
    "{>",
    "{]",
    "<)",
    "<}",
    "<>",
    "<]",
    "[)",
    "[}",
    "[>",
    "[]",
]


def load_data() -> List[str]:
    day_ten_file = DATA_DIR / "day10"
    with open(day_ten_file, "r") as f:
        return [line.strip() for line in f.readlines()]


def check_legal_chunks(chunk: str) -> Tuple[str, str]:
    if not chunk:
        return "valid", chunk
    if len(chunk) == 1:
        print("Incomplete chunk", chunk)
        return "incomplete", chunk

    len_chunk = len(chunk)
    new_chunk = chunk.replace("()", "").replace("{}", "").replace("[]", "").replace("<>", "")
    if len_chunk == len(new_chunk):
        # Indicates corruption
        print("corrupted chunk", chunk)
        return "corrupted", chunk

    return check_legal_chunks(new_chunk)


def day10():
    print("--- Day 10: Syntax Scoring ---")
    navigation_subsystem = load_data()
    print(navigation_subsystem)


if __name__ == "__main__":
    day10()
