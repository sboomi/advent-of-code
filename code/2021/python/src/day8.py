from src import DATA_DIR
from typing import List, Tuple
from collections import Counter


class SegmentDigit:
    def __init__(self, *sargs):
        if len(sargs) != 7:
            raise ValueError("SegmentDigit must be initialized with 9 arguments")

        self.a, self.b, self.c, self.d, self.e, self.f, self.g = sargs
        self.digit_rep = [
            f" {self.a}{self.a}{self.a}{self.a} \n{self.b}    {self.c}\n{self.b}    {self.c}\n .... \n{self.e}    {self.f}\n{self.e}    {self.f}\n {self.g}{self.g}{self.g}{self.g} ",
            f" .... \n.    {self.c}\n.    {self.c}\n .... \n.    {self.f}\n.    {self.f}\n .... ",
            f" {self.a}{self.a}{self.a}{self.a} \n.    {self.c}\n.    {self.c}\n {self.d}{self.d}{self.d}{self.d} \n{self.e}    .\n{self.e}    .\n {self.g}{self.g}{self.g}{self.g} ",
            f" {self.a}{self.a}{self.a}{self.a} \n.    {self.c}\n.    {self.c}\n {self.d}{self.d}{self.d}{self.d} \n.    {self.f}\n.    {self.f}\n {self.g}{self.g}{self.g}{self.g} ",
            f" .... \n{self.b}    {self.c}\n{self.b}    {self.c}\n {self.d}{self.d}{self.d}{self.d} \n.    {self.f}\n.    {self.f}\n .... ",
            f" {self.a}{self.a}{self.a}{self.a} \n{self.b}    .\n{self.b}    .\n {self.d}{self.d}{self.d}{self.d} \n.    {self.f}\n.    {self.f}\n {self.g}{self.g}{self.g}{self.g} ",
            f" {self.a}{self.a}{self.a}{self.a} \n{self.b}    .\n{self.b}    .\n {self.d}{self.d}{self.d}{self.d} \n{self.e}    {self.f}\n{self.e}    {self.f}\n {self.g}{self.g}{self.g}{self.g} ",
            f" {self.a}{self.a}{self.a}{self.a} \n.    {self.c}\n.    {self.c}\n .... \n.    {self.f}\n.    {self.f}\n .... ",
            f" {self.a}{self.a}{self.a}{self.a} \n{self.b}    {self.c}\n{self.b}    {self.c}\n {self.d}{self.d}{self.d}{self.d} \n{self.e}    {self.f}\n{self.e}    {self.f}\n {self.g}{self.g}{self.g}{self.g} ",
            f" {self.a}{self.a}{self.a}{self.a} \n{self.b}    {self.c}\n{self.b}    {self.c}\n {self.d}{self.d}{self.d}{self.d} \n.    {self.f}\n.    {self.f}\n {self.g}{self.g}{self.g}{self.g} ",
        ]

    def __getitem__(self, idx) -> str:
        if not (0 <= idx <= 9):
            raise IndexError("Index must be in range [0,9]")

        return self.digit_rep[idx]


class SegmentDecoder:
    N_SEGMENTS = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    LEN_SEGMENT_DISTRIBUTION = {6: [0, 6, 9], 2: [1], 5: [2, 3, 5], 4: [4], 3: [7], 7: [8]}

    def __init__(self, signal_patterns):
        if len(signal_patterns) != 10:
            raise ValueError("SegmentDecoder's `signal_patterns` must have 10 arguments")
        self.signal_patterns = signal_patterns
        self.len_signal = [len(signal_pattern) for signal_pattern in signal_patterns]
        self.idx_patterns = ["" for _ in range(10)]

    def find_unique_digits(self):
        """Finds which patterns have a unique number of segments and associate them to
        positions 1, 4, 7 and 8.
        """
        for n_segs, num in self.LEN_SEGMENT_DISTRIBUTION.items():
            if len(num) == 1:
                idx_unique_digit = self.len_signal.index(n_segs)
                self.idx_patterns[num[0]] = self.signal_patterns[idx_unique_digit]

    def find_upper_segment(self):
        """Assign the first segment letter by comparing pattern 1 and 7"""
        pat_one = self.idx_patterns[1]
        pat_seven = self.idx_patterns[7]
        self.a = list(set(pat_seven).difference(set(pat_one)))[0]

    def find_right_segments(self):
        """Detects right segments from 1 by comparing digits 8 and 6."""
        pat_one = self.idx_patterns[1]
        pat_eight = self.idx_patterns[8]
        for one_letter in pat_one:
            pot_pat_six = "".join([letter for letter in pat_eight if letter != one_letter])
            for pattern in self.signal_patterns:
                if sorted(pattern) == sorted(pot_pat_six):
                    self.idx_patterns[6] = pattern
                    self.c = one_letter
                    self.f = [letter for letter in pat_one if letter != one_letter][0]
                    return

    def find_middle_top_left_segments(self):
        """Detects middle and top left segments from the difference between
        1 and 4 by comparing 0 and 8
        """
        pat_one = self.idx_patterns[1]
        pat_eight = self.idx_patterns[8]
        pat_four = self.idx_patterns[4]

        top_left_segments = "".join(list(set(pat_four).difference(set(pat_one))))
        for four_letter in top_left_segments:
            pot_pat_zero = "".join([letter for letter in pat_eight if letter != four_letter])
            for pattern in self.signal_patterns:
                if sorted(pattern) == sorted(pot_pat_zero):
                    self.idx_patterns[0] = pattern
                    self.d = four_letter
                    self.b = [letter for letter in top_left_segments if letter != four_letter][0]
                    return

    def find_bottom_left_segment(self):
        six_seg_pats = [self.idx_patterns[0], self.idx_patterns[6]]
        pat_nine = ""
        pat_eight = self.idx_patterns[8]
        for len_pattern, pattern in zip(self.len_signal, self.signal_patterns):
            if len_pattern == 6 and pattern not in six_seg_pats:
                pat_nine = pattern
                break
        self.idx_patterns[9] = pat_nine
        self.e = list(set(pat_eight).difference(set(pat_nine)))[0]
        pat_four = self.idx_patterns[4]
        top_bottom_segments = "".join(list(set(pat_nine).difference(set(pat_four))))
        self.g = [letter for letter in top_bottom_segments if letter != self.a][0]

    def reassociate_five_seg_patterns(self):
        for len_pattern, pattern in zip(self.len_signal, self.signal_patterns):
            if len_pattern == 5:
                if sorted("".join([self.a, self.c, self.d, self.e, self.g])) == sorted(pattern):
                    self.idx_patterns[2] = pattern
                elif sorted("".join([self.a, self.c, self.d, self.f, self.g])) == sorted(pattern):
                    self.idx_patterns[3] = pattern
                elif sorted("".join([self.a, self.b, self.d, self.f, self.g])) == sorted(pattern):
                    self.idx_patterns[5] = pattern

    def guess_segments(self):
        """Combine guessing signals in that order"""
        self.find_unique_digits()
        self.find_upper_segment()
        self.find_right_segments()
        self.find_middle_top_left_segments()
        self.find_bottom_left_segment()
        self.reassociate_five_seg_patterns()

    def create_segment_digit(self):
        self.segdig = SegmentDigit(self.a, self.b, self.c, self.d, self.e, self.f, self.g)

    def show_pattern(self):
        if not hasattr(self, "segdig"):
            self.create_segment_digit()
        return self.segdig[8]

    def decode_signal(self, signal: List[str]) -> int:
        """Decodes the signal using the complete list of patterns

        Parameters
        ----------
        signal : List[str]
            [description]

        Returns
        -------
        int
            [description]
        """
        arranged_patterns = ["".join(sorted(pattern)) for pattern in self.idx_patterns]
        output_value = ""
        for digit in signal:
            output_value += str(arranged_patterns.index("".join(sorted(digit))))

        return int(output_value)


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

    unique_lens = [n_segs for n_segs, num in SegmentDecoder.LEN_SEGMENT_DISTRIBUTION.items() if len(num) == 1]
    return sum([len_count for digit_len, len_count in len_counter.items() if digit_len in unique_lens])


def sum_output_values(signal_patterns: List[List[str]], digit_output: List[List[str]]) -> int:
    total_sum = 0
    for signal_pattern, digits in zip(signal_patterns, digit_output):
        sd = SegmentDecoder(signal_pattern)
        sd.guess_segments()

        total_sum += sd.decode_signal(digits)
    return total_sum


def day8():
    print("--- Day 8: Seven Segment Search ---")
    signal_patterns, digit_output_value = load_data()
    unique_n_digits = find_unique_n_digits(digit_output_value)
    print("Number of times we can find 1, 4, 7 or 8:", unique_n_digits)
    total_output = sum_output_values(signal_patterns, digit_output_value)
    print("Total output value", total_output)


if __name__ == "__main__":
    day8()
