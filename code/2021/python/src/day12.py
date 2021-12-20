from collections import Counter, defaultdict
from typing import List

from src import DATA_DIR


def load_data() -> defaultdict[str, List]:
    nodes = defaultdict(list)
    day_twelve_file = DATA_DIR / "day12"
    with open(day_twelve_file, "r") as f:
        for line in f.readlines():
            first_cave, second_cave = line.strip().split("-")
            nodes[first_cave].append(second_cave)
            nodes[second_cave].append(first_cave)

    return nodes


def init_paths(nodes: defaultdict[str, List]) -> List[List[str]]:
    """Takes the first branches at `start` for the algorithm

    Parameters
    ----------
    nodes : defaultdict[str, List]
        [description]

    Returns
    -------
    List[List[str]]
        [description]
    """
    return [["start", cave] for cave in nodes["start"]]


def find_all_paths(
    nodes: defaultdict[str, List], list_paths: List[List[str]], visit_twice: bool = False
) -> List[List[str]]:
    """From a dictionnary containing nodes and their connections, find every path
    available according to a set of rules.

    Each path features a start point, and endpoint and a number of caves.
    If it's a small cave already visited or the start point, the path is dropped from
    the new branches.

    `verify_twice` allows the rules to change a bit and allow a revisiting of a small cave, if
    the prefix has it at least once

    The recursion stops when every path reaches `end`

    Parameters
    ----------
    nodes : defaultdict[str, List]
        [description]
    list_paths : List[List[str]]
        [description]
    visit_twice : bool, optional
        [description], by default False

    Returns
    -------
    List[List[str]]
        [description]
    """
    new_list_paths = []

    for path in list_paths:
        last_cave = path[-1]
        if last_cave == "end":
            new_list_paths.append(path)
            continue
        cave_prefix = path[:-1]
        path_expansions = [[last_cave, cave] for cave in nodes[last_cave]]
        for expansion in path_expansions:
            if expansion[-1] == "start":
                continue

            if visit_twice:
                count_caves = Counter(path)
                visited_twice = [v == 2 for k, v in count_caves.items() if k != expansion[-1] and k.islower()]
                add_condition = (
                    expansion[-1].isupper()
                    or expansion[-1].islower()
                    and (
                        count_caves[expansion[-1]] == 0 or (count_caves[expansion[-1]] == 1 and not any(visited_twice))
                    )
                )
            else:
                add_condition = expansion[-1].isupper() or expansion[-1].islower() and expansion[-1] not in cave_prefix

            if add_condition:
                new_list_paths.append(cave_prefix + expansion)

    if all([path[-1] == "end" for path in new_list_paths]):
        return new_list_paths

    return find_all_paths(nodes, new_list_paths, visit_twice=visit_twice)


def count_all_paths(nodes: defaultdict[str, List], visit_twice: bool = False) -> int:
    """Takes a list of possible paths and counts the result

    Parameters
    ----------
    nodes : defaultdict[str, List]
        [description]
    visit_twice : bool, optional
        [description], by default False

    Returns
    -------
    int
        [description]
    """
    list_paths_init = init_paths(nodes)

    full_path_list = find_all_paths(nodes, list_paths_init, visit_twice=visit_twice)

    return len(full_path_list)


def day12():
    print("--- Day 12: Passage Pathing ---")
    cave_network = load_data()
    n_paths = count_all_paths(cave_network)
    print("N° of different paths:", n_paths)
    n_paths_twice = count_all_paths(cave_network, visit_twice=True)
    print("N° of different paths if one cave is visited twice:", n_paths_twice)


if __name__ == "__main__":
    day12()
