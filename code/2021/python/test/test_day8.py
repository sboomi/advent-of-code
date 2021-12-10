import pytest
from src.day8 import find_unique_n_digits, SegmentDecoder, sum_output_values


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


def test_show_pattern_formation():
    test_pattern = ["acedgfb", "cdfbe", "gcdfa", "fbcad", "dab", "cefabd", "cdfgeb", "eafb", "cagedb", "ab"]

    sd = SegmentDecoder(test_pattern)
    sd.guess_segments()
    act_pattern = sd.show_pattern()

    exp_pattern = " dddd \ne    a\ne    a\n ffff \ng    b\ng    b\n cccc "
    assert act_pattern == exp_pattern, f"Expected:\n{exp_pattern}\nGot:\n{act_pattern}"


def test_sort_patterns():
    test_pattern = ["acedgfb", "cdfbe", "gcdfa", "fbcad", "dab", "cefabd", "cdfgeb", "eafb", "cagedb", "ab"]

    sd = SegmentDecoder(test_pattern)
    sd.guess_segments()
    act_idx_pattern = sd.idx_patterns
    exp_idx_pattern = ["cagedb", "ab", "gcdfa", "fbcad", "eafb", "cdfbe", "cdfgeb", "dab", "acedgfb", "cefabd"]

    assert act_idx_pattern == exp_idx_pattern, f"Expected:\n{exp_idx_pattern}\nGot:\n{act_idx_pattern}"


def test_decode_signal_simple():
    test_pattern = ["acedgfb", "cdfbe", "gcdfa", "fbcad", "dab", "cefabd", "cdfgeb", "eafb", "cagedb", "ab"]
    test_signal = ["cdfeb", "fcadb", "cdfeb", "cdbaf"]

    sd = SegmentDecoder(test_pattern)
    sd.guess_segments()

    act_signal = sd.decode_signal(test_signal)
    exp_signal = 5353

    assert act_signal == exp_signal, f"Expected {exp_signal}. Got {act_signal}"


def test_decode_signal_multiple_instances():
    signal_instances = [
        ["be", "cfbegad", "cbdgef", "fgaecd", "cgeb", "fdcge", "agebfd", "fecdb", "fabcd", "edb"],
        ["edbfga", "begcd", "cbg", "gc", "gcadebf", "fbgde", "acbgfd", "abcde", "gfcbed", "gfec"],
        ["fgaebd", "cg", "bdaec", "gdafb", "agbcfd", "gdcbef", "bgcad", "gfac", "gcb", "cdgabef"],
        ["fbegcd", "cbd", "adcefb", "dageb", "afcb", "bc", "aefdc", "ecdab", "fgdeca", "fcdbega"],
        ["aecbfdg", "fbg", "gf", "bafeg", "dbefa", "fcge", "gcbea", "fcaegb", "dgceab", "fcbdga"],
        ["fgeab", "ca", "afcebg", "bdacfeg", "cfaedg", "gcfdb", "baec", "bfadeg", "bafgc", "acf"],
        ["dbcfg", "fgd", "bdegcaf", "fgec", "aegbdf", "ecdfab", "fbedc", "dacgb", "gdcebf", "gf"],
        ["bdfegc", "cbegaf", "gecbf", "dfcage", "bdacg", "ed", "bedf", "ced", "adcbefg", "gebcd"],
        ["egadfb", "cdbfeg", "cegd", "fecab", "cgb", "gbdefca", "cg", "fgcdab", "egfdb", "bfceg"],
        ["gcafb", "gcf", "dcaebfg", "ecagb", "gf", "abcdeg", "gaef", "cafbge", "fdbac", "fegbdc"],
    ]
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

    exp_signal_list = [8394, 9781, 1197, 9361, 4873, 8418, 4548, 1625, 8717, 4315]

    for idx, (test_pattern, test_signal) in enumerate(zip(signal_instances, digit_instances)):
        sd = SegmentDecoder(test_pattern)
        sd.guess_segments()

        act_signal = sd.decode_signal(test_signal)
        exp_signal = exp_signal_list[idx]

        assert act_signal == exp_signal, f"Instance {idx}. Expected {exp_signal}. Got {act_signal}"


def test_sum_output_values():
    signal_instances = [
        ["be", "cfbegad", "cbdgef", "fgaecd", "cgeb", "fdcge", "agebfd", "fecdb", "fabcd", "edb"],
        ["edbfga", "begcd", "cbg", "gc", "gcadebf", "fbgde", "acbgfd", "abcde", "gfcbed", "gfec"],
        ["fgaebd", "cg", "bdaec", "gdafb", "agbcfd", "gdcbef", "bgcad", "gfac", "gcb", "cdgabef"],
        ["fbegcd", "cbd", "adcefb", "dageb", "afcb", "bc", "aefdc", "ecdab", "fgdeca", "fcdbega"],
        ["aecbfdg", "fbg", "gf", "bafeg", "dbefa", "fcge", "gcbea", "fcaegb", "dgceab", "fcbdga"],
        ["fgeab", "ca", "afcebg", "bdacfeg", "cfaedg", "gcfdb", "baec", "bfadeg", "bafgc", "acf"],
        ["dbcfg", "fgd", "bdegcaf", "fgec", "aegbdf", "ecdfab", "fbedc", "dacgb", "gdcebf", "gf"],
        ["bdfegc", "cbegaf", "gecbf", "dfcage", "bdacg", "ed", "bedf", "ced", "adcbefg", "gebcd"],
        ["egadfb", "cdbfeg", "cegd", "fecab", "cgb", "gbdefca", "cg", "fgcdab", "egfdb", "bfceg"],
        ["gcafb", "gcf", "dcaebfg", "ecagb", "gf", "abcdeg", "gaef", "cafbge", "fdbac", "fegbdc"],
    ]
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

    act_sum = sum_output_values(signal_instances, digit_instances)
    exp_sum = 61229
    assert act_sum == exp_sum, f"Expected {exp_sum}. Got {act_sum}"
