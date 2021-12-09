import pytest
from src.day8 import find_unique_n_digits, decode_signal


def test_find_unique_n_digits():
    digit_instances = [
        ["fdgacbe", "cefdb", "cefbgd", "gcbe"],
        ["fcgedb", "cgb", "dgebacf", "gc"],
        ["cg", "cg", "fdcagb", "cbg"],
        ["efabcd", "cedba", "gadfec", "cb"],
        ["gecf", "egdcabf", "bgf", "bfgea"],
        ["gebdcfa", "ecba", "ca", "fadegcb"],
        ["cefg", "dcbef", "fcge", "gbcadfe"],
        ["ed", "bcgafe", "cdgba", "cbgef"],
        ["gbdfcae", "bgc", "cg", "cgb"],
        ["fgae", "cfgab", "fg", "bagce"],
    ]

    exp_n_instances = 26
    act_n_instances = find_unique_n_digits(digit_instances)

    assert act_n_instances == exp_n_instances, f"Expected {exp_n_instances}. Got {act_n_instances}"


def test_decode_signal_simple():
    test_signal = ["cdfeb", "fcadb", "cdfeb", "cdbaf"]

    act_signal = decode_signal(test_signal)
    exp_signal = 5353

    assert act_signal == exp_signal, f"Expected {exp_signal}. Got {act_signal}"
