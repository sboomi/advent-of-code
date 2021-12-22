import pytest
from src.day14 import polymer_length, transform_polymer, chr_counter, chr_counter_optimized


def test_polymer_length():
    polymer = "NNCB"

    exp_len_vec = [4, 7, 13, 25, 49, 97, 193, 385, 769, 1537, 3073]
    act_len_vec = [polymer_length(i, len(polymer)) for i in range(11)]

    for idx, (act_len, exp_len) in enumerate(zip(act_len_vec, exp_len_vec)):
        assert act_len == exp_len, f"After step {idx}: expected length {exp_len}. Got length {act_len}"


def test_transform_polymer_first_step():
    init_polymer = "NNCB"
    rules = {
        "CH": "B",
        "HH": "N",
        "CB": "H",
        "NH": "C",
        "HB": "C",
        "HC": "B",
        "HN": "C",
        "NN": "C",
        "BH": "H",
        "NC": "B",
        "NB": "B",
        "BN": "B",
        "BB": "N",
        "BC": "B",
        "CC": "N",
        "CN": "C",
    }

    exp_polymer = "NCNBCHB"
    act_polymer = transform_polymer(init_polymer, rules)

    assert exp_polymer == act_polymer, f"Expected {exp_polymer}, got {act_polymer}."


def test_transform_polymer_first_five_steps():
    init_polymer = "NNCB"
    rules = {
        "CH": "B",
        "HH": "N",
        "CB": "H",
        "NH": "C",
        "HB": "C",
        "HC": "B",
        "HN": "C",
        "NN": "C",
        "BH": "H",
        "NC": "B",
        "NB": "B",
        "BN": "B",
        "BB": "N",
        "BC": "B",
        "CC": "N",
        "CN": "C",
    }

    exp_polymers = [
        "NCNBCHB",
        "NBCCNBBBCBHCB",
        "NBBBCNCCNBBNBNBBCHBHHBCHB",
        "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB",
    ]

    for step in range(len(exp_polymers)):
        init_polymer = transform_polymer(init_polymer, rules)
        assert (
            exp_polymers[step] == init_polymer
        ), f"After step {step+1}: expected {exp_polymers[step]}. Got {init_polymer}."


def test_chr_counter_simple_example_10_steps():
    init_polymer = "NNCB"
    rules = {
        "CH": "B",
        "HH": "N",
        "CB": "H",
        "NH": "C",
        "HB": "C",
        "HC": "B",
        "HN": "C",
        "NN": "C",
        "BH": "H",
        "NC": "B",
        "NB": "B",
        "BN": "B",
        "BB": "N",
        "BC": "B",
        "CC": "N",
        "CN": "C",
    }

    act_counter = sorted(chr_counter(10, init_polymer, rules).items())
    exp_counter = sorted({"B": 1749, "C": 298, "H": 161, "N": 865}.items())

    assert act_counter == exp_counter, f"Expected\n{exp_counter}\nGot\n{act_counter}"


def test_chr_counter_optimized_first_step():
    init_polymer = "NNCB"
    rules = {
        "CH": "B",
        "HH": "N",
        "CB": "H",
        "NH": "C",
        "HB": "C",
        "HC": "B",
        "HN": "C",
        "NN": "C",
        "BH": "H",
        "NC": "B",
        "NB": "B",
        "BN": "B",
        "BB": "N",
        "BC": "B",
        "CC": "N",
        "CN": "C",
    }

    act_result, act_pairs = chr_counter_optimized(1, init_polymer, rules)
    exp_result = {"N": 2, "C": 2, "B": 2, "H": 1}

    # "NCNBCHB"
    exp_pairs = {
        "BB": 0,
        "CB": 0,
        "CH": 1,
        "NC": 1,
        "CC": 0,
        "HH": 0,
        "BC": 1,
        "HC": 0,
        "HB": 1,
        "NN": 0,
        "BH": 0,
        "NB": 1,
        "BN": 0,
        "NH": 0,
        "CN": 1,
        "HN": 0,
    }

    assert exp_pairs == act_pairs, f"Expected\n{exp_pairs}\nGot\n{act_pairs}"
    assert exp_result == act_result, f"Expected\n{exp_result}\nGot\n{act_result}"


def test_chr_counter_optimized_first_four_steps():
    init_polymer = "NNCB"
    rules = {
        "CH": "B",
        "HH": "N",
        "CB": "H",
        "NH": "C",
        "HB": "C",
        "HC": "B",
        "HN": "C",
        "NN": "C",
        "BH": "H",
        "NC": "B",
        "NB": "B",
        "BN": "B",
        "BB": "N",
        "BC": "B",
        "CC": "N",
        "CN": "C",
    }

    act_result, act_pairs = chr_counter_optimized(4, init_polymer, rules)
    exp_result = {"N": 11, "B": 23, "C": 10, "H": 5}

    exp_pairs = {
        "BB": 9,
        "CB": 5,
        "CH": 0,
        "NC": 1,
        "CC": 2,
        "HH": 1,
        "BC": 4,
        "HC": 3,
        "HB": 0,
        "NN": 0,
        "BH": 3,
        "NB": 9,
        "BN": 6,
        "NH": 1,
        "CN": 3,
        "HN": 1,
    }

    # NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
    assert exp_pairs == act_pairs, f"Expected\n{sorted(exp_pairs.items())}\nGot\n{sorted(act_pairs.items())}"
    assert exp_result == act_result, f"Expected\n{sorted(exp_result.items())}\nGot\n{sorted(act_result.items())}"


def test_chr_counter_optimized_40_steps():
    init_polymer = "NNCB"
    rules = {
        "CH": "B",
        "HH": "N",
        "CB": "H",
        "NH": "C",
        "HB": "C",
        "HC": "B",
        "HN": "C",
        "NN": "C",
        "BH": "H",
        "NC": "B",
        "NB": "B",
        "BN": "B",
        "BB": "N",
        "BC": "B",
        "CC": "N",
        "CN": "C",
    }

    act_counter, _ = chr_counter_optimized(40, init_polymer, rules)
    act_counter = {"B": act_counter["B"], "H": act_counter["H"]}
    exp_counter = {"B": 2192039569602, "H": 3849876073}

    assert act_counter == exp_counter, f"Expected\n{exp_counter}\nGot\n{act_counter}"
