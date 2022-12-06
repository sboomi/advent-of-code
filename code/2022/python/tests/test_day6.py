from ac2022python.solutions.day6 import TuningTrouble

EXAMPLE_INPUT = [
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
]


def test_find_n_chrs_before_sop():
    expected_result = [7, 5, 6, 10, 11]

    for inp, exp_res in zip(EXAMPLE_INPUT, expected_result):
        actual_result = TuningTrouble._find_start_of_packet_left_chrs(inp)
        assert exp_res == actual_result


def test_find_n_chrs_before_som():
    expected_result = [19, 23, 23, 29, 26]

    for inp, exp_res in zip(EXAMPLE_INPUT, expected_result):
        actual_result = TuningTrouble._find_start_of_packet_left_chrs(
            inp, start_of_msgs=True
        )
        assert exp_res == actual_result
