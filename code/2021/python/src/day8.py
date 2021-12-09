from src import DATA_DIR
from typing import List, Tuple
from collections import defaultdict, Counter


seven_segments = [
    " aaaa \nb    c\nb    c\n .... \ne    f\ne    f\n gggg ",
    " .... \n.    c\n.    c\n .... \n.    f\n.    f\n .... ",
    " aaaa \n.    c\n.    c\n dddd \ne    .\ne    .\n gggg ",
    " aaaa \n.    c\n.    c\n dddd \n.    f\n.    f\n gggg ",
    " .... \nb    c\nb    c\n dddd \n.    f\n.    f\n .... ",
    " aaaa \nb    .\nb    .\n dddd \n.    f\n.    f\n gggg ",
    " aaaa \nb    .\nb    .\n dddd \ne    f\ne    f\n gggg ",
    " aaaa \n.    c\n.    c\n .... \n.    f\n.    f\n .... ",
    " aaaa \nb    c\nb    c\n dddd \ne    f\ne    f\n gggg ",
    " aaaa \nb    c\nb    c\n dddd \n.    f\n.    f\n gggg ",
]

pattern_list = ["".join(sorted([s for s in list(set(seg)) if s not in ["\n", ".", " "]])) for seg in seven_segments]

n_digits = defaultdict(list)
for idx, pattern in enumerate(pattern_list):
    n_digits[len(pattern)].append(idx)


def load_data() -> Tuple[List[List[str]], List[List[str]]]:
    day_eight_file = DATA_DIR / "day8"
    signal_patterns = []
    digit_output_value = []
    with open(day_eight_file, "r") as f:
        for line in f.readlines():
            s_pats, sig_val = line.split("|")
            signal_patterns.append(s_pats.split())
            digit_output_value.append(sig_val.split())
    return signal_patterns, digit_output_value


def find_unique_n_digits(digit_output: List[str]) -> int:
    len_counter: Counter = Counter()
    for digit_sample in digit_output:
        len_counter += Counter([len(samp) for samp in digit_sample])

    unique_lens = [n_segs for n_segs, num in n_digits.items() if len(num) == 1]
    return sum([len_count for digit_len, len_count in len_counter.items() if digit_len in unique_lens])


def decode_signal(digit_output: List[str]) -> int:
    signal_output = ""
    for digit in digit_output:
        current_digit = pattern_list.index("".join(sorted(digit)))
        signal_output += str(current_digit)
    return int(signal_output)


def day8():
    print("--- Day 8: Seven Segment Search ---")
    signal_patterns, digit_output_value = load_data()
    print(pattern_list)
    print(n_digits)
    unique_n_digits = find_unique_n_digits(digit_output_value)
    print("Number of times we can find 1, 4, 7 or 8:", unique_n_digits)


if __name__ == "__main__":
    day8()
