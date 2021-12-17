from typing import Tuple, List
from src import DATA_DIR
from collections import Counter


SCORE_TABLE = {")": 3, "]": 57, "}": 1197, ">": 25137}
SCORE_MIRROR_TABLE = {")": 1, "]": 2, "}": 3, ">": 4}
CORRUPTED_CHUNKS_COMBOS = [
    "(}",
    "(>",
    "(]",
    "{)",
    "{>",
    "{]",
    "<)",
    "<}",
    "<]",
    "[)",
    "[}",
    "[>",
]
PAIRS = {"(": ")", "{": "}", "<": ">", "[": "]"}


def load_data() -> List[str]:
    """Loads a list of lines of the navigation subsystem

    ex.
    ```
    [({(<(())[]>[[{[]{<()<>>
    [(()[<>])]({[<{<<[]>>(
    {([(<{}[<>[]}>{[]{[(<()>
    (((({<>}<{<{<>}{[]{[]{}
    [[<[([]))<([[{}[[()]]]
    [{[{({}]{}}([{[{{{}}([]
    {<[[]]>}<{[{[{[]{()[[[]
    [<(<(<(<{}))><([]([]()
    <{([([[(<>()){}]>(<<{{
    <{([{{}}[<[[[<>{}]]]>[]]
    ```

    Returns
    -------
    List[str]
        Navigation subsystem of N lines
    """
    day_ten_file = DATA_DIR / "day10"
    with open(day_ten_file, "r") as f:
        return [line.strip() for line in f.readlines()]


def check_legal_chunks(chunk: str) -> Tuple[str, str]:
    """Uses a recursion to determine whether a chunk is valid, incomplete or corrupted.

    It removes all pairs of `()`, `<>`, `[]` and `{}` until the string is empty or its length
    doesn't move anymore, then returns a status and the processed chunk.

    Incomplete processed chunks will only have opening characters while corrupted chunks
    will always feature at least one incorrect closing character.

    Parameters
    ----------
    chunk : str
        the initial chunk

    Returns
    -------
    Tuple[str, str]
        the status (`valid`, `incomplete` or `corrupted`) and the chunk
    """
    if not chunk:
        return "valid", chunk

    len_chunk = len(chunk)
    new_chunk = chunk.replace("()", "").replace("{}", "").replace("[]", "").replace("<>", "")
    if len_chunk == len(new_chunk):
        # Indicates corruption or incompleteness
        if all([chr in "({[<" for chr in chunk]):
            return "incomplete", chunk
        else:
            return "corrupted", chunk

    return check_legal_chunks(new_chunk)


def get_first_wrong_closing_chr(chunk: str) -> str:
    """Takes corrupted chunks and get the first incorrect closing character.

    Parameters
    ----------
    chunk : str
        [description]

    Returns
    -------
    str
        [description]
    """
    status, proc_chunk = check_legal_chunks(chunk)
    if status == "corrupted":
        for first_chr, second_chr in zip(proc_chunk[:-1], proc_chunk[1:]):
            if first_chr + second_chr in CORRUPTED_CHUNKS_COMBOS:
                return second_chr

    return ""


def syntax_score(nav_subsys: List[str]) -> int:
    """Computes the syntax score on the whole navigation subsystem

    Parameters
    ----------
    nav_subsys : List[str]
        [description]

    Returns
    -------
    int
        [description]
    """
    wrong_enclosing_chrs = ""

    for line in nav_subsys:
        wrong_closing_chr = get_first_wrong_closing_chr(line)
        wrong_enclosing_chrs += wrong_closing_chr

    chr_counter = Counter(wrong_enclosing_chrs)
    return sum([val * chr_counter[chr] for chr, val in SCORE_TABLE.items()])


def make_mirror_image(chunk: str) -> str:
    """Takes incomplete lines and makes a mirror image of the closing characters.

    Parameters
    ----------
    chunk : str
        [description]

    Returns
    -------
    str
        closed characters of the original processed chunk (empty string if the status is anything
        other than `incomplete`)
    """
    status, proc_chunk = check_legal_chunks(chunk)
    if status == "incomplete":
        return "".join([PAIRS[c] for c in proc_chunk])[::-1]

    return ""


def get_completion_score(chunk: str) -> int:
    """Computes the completion score from a mirror image issued from incomplete
    lines.

    Parameters
    ----------
    chunk : str
        [description]

    Returns
    -------
    int
        completion score (-1 if the chain isn't incomplete)
    """
    mirror_str = make_mirror_image(chunk)
    if not mirror_str:
        return -1

    total_score = 0
    for c in mirror_str:
        total_score = (total_score * 5) + SCORE_MIRROR_TABLE[c]

    return total_score


def middle_score(nav_subsys: List[str]) -> int:
    """Returns the middle score from incomplete lines

    Parameters
    ----------
    nav_subsys : List[str]
        [description]

    Returns
    -------
    int
        [description]
    """
    all_scores = []

    for line in nav_subsys:
        comp_score = get_completion_score(line)
        if comp_score != -1:
            all_scores.append(comp_score)

    return sorted(all_scores)[len(all_scores) // 2]


def day10():
    print("--- Day 10: Syntax Scoring ---")
    navigation_subsystem = load_data()
    full_score = syntax_score(navigation_subsystem)
    print("Navigation subsystem has a score of:", full_score)
    full_middle_score = middle_score(navigation_subsystem)
    print("Middle score for completion strings:", full_middle_score)


if __name__ == "__main__":
    day10()
