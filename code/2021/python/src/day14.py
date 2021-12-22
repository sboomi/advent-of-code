from typing import Dict, Tuple
from collections import Counter

from src import DATA_DIR


def load_data() -> Tuple[str, Dict[str, str]]:
    """Loads the data into a template polymer
    and a dictionnary of rules.

    Returns
    -------
    Tuple[str, Dict[str, str]]
        initial polymer and dictionary of (rule, letter) elements
    """
    day_fourteen_file = DATA_DIR / "day14"
    with open(day_fourteen_file, "r") as f:
        data = f.read().split("\n")

    return data[0], {rule.split(" -> ")[0]: rule.split(" -> ")[1] for rule in data[2:]}


def polymer_length(n_steps: int, init_polymer_len: int):
    """Predicts the length of the polymer after `n_steps`

    It assumes each step will expand the polymer's length at `(2 * L) + 1`

    Parameters
    ----------
    n_steps : int
        [description]
    init_polymer_len : int
        [description]

    Returns
    -------
    [type]
        [description]
    """
    for _ in range(n_steps):
        init_polymer_len = (init_polymer_len * 2) - 1

    return init_polymer_len


def transform_polymer(polymer: str, rules: Dict[str, str]) -> str:
    """Updates the polymer according to a certain set of rules
    Takes two characters and checks which character should be inserted in the middle

    The resulting string should have a length of `(2 * len(polymer)) - 1`

    Parameters
    ----------
    polymer : str
        [description]
    rules : Dict[str, str]
        [description]

    Returns
    -------
    str
        [description]
    """
    new_polymer = ""

    for letter_1, letter_2 in zip(polymer[:-1], polymer[1:]):
        new_polymer += letter_1 + rules[letter_1 + letter_2]

    return new_polymer + polymer[-1]


def chr_counter(n_steps: int, init_polymer: str, rules: Dict[str, str]) -> Dict[str, int]:
    """Counts every character in a string after we obtained the final result.

    ⚠ NOT SUITED FOR BIG NUMBERS ⚠

    Parameters
    ----------
    n_steps : int
        [description]
    init_polymer : str
        [description]
    rules : Dict[str, str]
        [description]

    Returns
    -------
    Dict[str, int]
        [description]
    """

    for _ in range(n_steps):
        init_polymer = transform_polymer(init_polymer, rules)

    d_counter = Counter(init_polymer)

    return dict(d_counter)


def diff_most_least_common_elements(n_steps: int, init_polymer: str, rules: Dict[str, str]) -> int:
    letter_counter = chr_counter(n_steps, init_polymer, rules)

    sorted_counter = sorted(letter_counter.items(), key=lambda item: item[1], reverse=True)

    return sorted_counter[0][1] - sorted_counter[-1][1]


def update_letter_pair_count(
    letters: Dict[str, int], pairs: Dict[str, int], rules: Dict[str, str]
) -> Tuple[Dict[str, int], Dict[str, int]]:
    """Updates dicts of pairs and letters seen in the polymer by iterating
    over the seen pairs.

    Each pair checks for the letter corresponding to the approriate rule and adds
    `n_pairs` to the count. Once it's done, the pairs are split up between the new pairs created.

    Parameters
    ----------
    letters : Dict[str, int]
        [description]
    pairs : Dict[str, int]
        [description]
    rules : Dict[str, str]
        [description]

    Returns
    -------
    Tuple[Dict[str, int], Dict[str, int]]
        [description]
    """
    new_pairs = {k: v for k, v in pairs.items()}
    new_letters = {k: v for k, v in letters.items()}
    for pair, pair_count in pairs.items():
        if pair_count:
            new_letter = rules[pair]
            new_letters[new_letter] += pair_count
            new_pairs[pair] -= pair_count
            new_pairs[pair[0] + new_letter] += pair_count
            new_pairs[new_letter + pair[1]] += pair_count

    return new_letters, new_pairs


def chr_counter_optimized(
    n_steps: int, init_polymer: str, rules: Dict[str, str]
) -> Tuple[Dict[str, int], Dict[str, int]]:
    """Optimized version of `chr_counter`.

    Instead of generating a new polymer that exponentially takes more memory
    and computation time, this version initializes two counter dictionnaries
    for elements and pairs respectively, based over the `rules` parameter.

    Each dictionary is updated in the instance loop, resulting in variables of
    N-elements and M-pairs, which is useful for obtaining reduced information
    on longer loops.

    Parameters
    ----------
    n_steps : int
        number of required iterations
    init_polymer : str
        the initial polymer to be iterated on
    rules : Dict[str, str]
        a dict of element addition rules based on pairs

    Returns
    -------
    Tuple[Dict[str, int], Dict[str, int]]
        N-element letters and M-element pairs
    """
    letters = {v: 0 for v in list(set(list(rules.values())))}
    pairs = {k: 0 for k in list(set(list(rules.keys())))}

    # init letters and pairs
    for l1, l2 in zip(init_polymer[:-1], init_polymer[1:]):
        pairs[l1 + l2] += 1
        letters[l1] += 1
    letters[init_polymer[-1]] += 1

    # iterate over n_steps
    for _ in range(n_steps):
        letters, pairs = update_letter_pair_count(letters, pairs, rules)

    return letters, pairs


def day14():
    print("--- Day 14: Extended Polymerization ---")
    polymer_template, insertion_rules = load_data()
    print("Length of polymer after 10 steps:", polymer_length(10, len(polymer_template)))
    diff_most_least = diff_most_least_common_elements(10, polymer_template, insertion_rules)
    print("Most common element vs least common element after 10 steps:", diff_most_least)
    print("Length of polymer after 40 steps:", polymer_length(40, len(polymer_template)))
    element_count, _ = chr_counter_optimized(40, polymer_template, insertion_rules)
    diff_ml_40 = max(element_count.values()) - min(element_count.values())
    print("Difference of most common vs least common element after 40 steps:", diff_ml_40)


if __name__ == "__main__":
    day14()
