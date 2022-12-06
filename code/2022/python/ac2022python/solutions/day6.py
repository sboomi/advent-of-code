"""Day 6: Tuning Trouble"""
from pathlib import Path

from rich import print

from ac2022python.solutions import DATA_PATH

PUZZLE_INPUT = Path(DATA_PATH / "day6")


class TuningTrouble:
    LEN_SOP = 4
    LEN_SOM = 14

    @staticmethod
    def _find_start_of_packet_left_chrs(
        datastream_buffer: str, start_of_msgs: bool = False
    ) -> int:
        """Browses the string in packs of a certain length and
        returns the number of character before the start of
        packets/messages. The length depends of the problem:

        * A start of packet is a substring of 4 characters.
        * A start of message is a substring of 14 characters. Its
        length can be enabled by turning `start_of_msgs` on.

        The method only uses an index as well as the corresponding
        offset to produce a window in which we determine whether the
        characters are unique or not. If that's the case, then
        idx + offset is returned as the n° of chars before the start
        of packet/messages.

        Parameters
        ----------
        datastream_buffer : str
            A chain of characters (a-z) from the Elves' subroutine.
        start_of_msgs : bool, optional
            Flag to enable a start of messages search, by default False

        Returns
        -------
        int
            The number of chars before the start of packet/messages
        """
        pack_len = TuningTrouble.LEN_SOM if start_of_msgs else TuningTrouble.LEN_SOP
        for idx_char in range(len(datastream_buffer) - pack_len):
            chr_packet = datastream_buffer[idx_char : idx_char + pack_len]
            if len(list(set(chr_packet))) == pack_len:
                return idx_char + pack_len

        return -1

    @staticmethod
    def find_start_of_packet_left_chrs(
        datastream_buffer: Path, start_of_msgs: bool = False
    ) -> int:
        """Wraps `_find_start_of_packet_left_chrs` to make it
        more suitable for a file input.

        Parameters
        ----------
        datastream_buffer : Path
            _description_
        start_of_msgs : bool, optional
            _description_, by default False

        Returns
        -------
        int
            The number of chars before the start of packet/messages
        """
        with open(datastream_buffer, "r") as f:
            return TuningTrouble._find_start_of_packet_left_chrs(
                f.read().strip(), start_of_msgs=start_of_msgs
            )


def solve_first_part():
    res = TuningTrouble.find_start_of_packet_left_chrs(PUZZLE_INPUT)
    print(
        f"We need to process {res} characters before the first start-of-packet marker is detected."
    )


def solve_second_part():
    res = TuningTrouble.find_start_of_packet_left_chrs(PUZZLE_INPUT, start_of_msgs=True)
    print(
        f"We need to process {res} characters before the first start-of-message marker is detected."
    )


def solve_all():
    solve_first_part()
    solve_second_part()


if __name__ == "__main__":
    solve_all()
