"""Day 2: Rock Paper Scissors"""
from enum import Enum
from pathlib import Path

from rich import print

from ac2022python.solutions import DATA_PATH


class RPSOpponentEnum(str, Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"


class RPSPlayerEnum(str, Enum):
    ROCK = "X"
    PAPER = "Y"
    SCISSORS = "Z"


PUZZLE_INPUT = Path(DATA_PATH / "day2")


class RockPaperScissors:
    PLAYER_LIST = [member.value for member in RPSPlayerEnum]
    OPPONENT_LIST = [member.value for member in RPSOpponentEnum]

    @staticmethod
    def get_round_score(
        opponent_choice: RPSOpponentEnum, player_choice: RPSPlayerEnum
    ) -> int:
        """Calculates the score of the current round for the player

        Parameters
        ----------
        opponent_choice : RPSOpponentEnum
            The choice of the opponent (A, B or C)
        player_choice : RPSPlayerEnum
            The choice of the player (X, Y, Z)

        Returns
        -------
        int
            Player's score for the current round
        """
        player_index = RockPaperScissors.PLAYER_LIST.index(player_choice)
        score = player_index + 1
        opp_index = RockPaperScissors.OPPONENT_LIST.index(opponent_choice)

        if opp_index == 0 and player_index == len(RockPaperScissors.PLAYER_LIST) - 1:
            player_index = -1
        elif (
            player_index == 0 and opp_index == len(RockPaperScissors.OPPONENT_LIST) - 1
        ):
            opp_index = -1

        if player_index > opp_index:
            score += 6
        elif opp_index == player_index:
            score += 3

        return score

    @staticmethod
    def get_total_score(strategy_guide: Path, part_two: bool = False) -> int:
        total_score = 0
        with open(strategy_guide, "r") as f:
            while f:
                line = f.readline()
                if len(line.strip()) >= 1:
                    opponent_choice, player_choice = line.strip().split()
                    if part_two:
                        total_score += (
                            RockPaperScissors.get_round_score_from_plan_strategy(
                                opponent_choice, player_choice
                            )
                        )
                    else:
                        total_score += RockPaperScissors.get_round_score(
                            opponent_choice, player_choice
                        )
                if line.strip() == "":
                    break
        return total_score

    @staticmethod
    def get_round_score_from_plan_strategy(
        opponent_choice: RPSOpponentEnum, player_choice: RPSPlayerEnum
    ) -> int:
        opp_idx = RockPaperScissors.OPPONENT_LIST.index(opponent_choice)

        if player_choice == RPSPlayerEnum.ROCK:
            new_player_choice = RockPaperScissors.PLAYER_LIST[
                (opp_idx - 1) % len(RockPaperScissors.PLAYER_LIST)
            ]
        elif player_choice == RPSPlayerEnum.PAPER:
            new_player_choice = RockPaperScissors.PLAYER_LIST[opp_idx]
        elif player_choice == RPSPlayerEnum.SCISSORS:
            new_player_choice = RockPaperScissors.PLAYER_LIST[
                (opp_idx + 1) % len(RockPaperScissors.PLAYER_LIST)
            ]

        return RockPaperScissors.get_round_score(opponent_choice, new_player_choice)


def solve_first_part():
    res = RockPaperScissors.get_total_score(PUZZLE_INPUT)
    print(f"Your total score is {res}")


def solve_second_part():
    res = RockPaperScissors.get_total_score(PUZZLE_INPUT, part_two=True)
    print(f"Your total score after redefining your strategy is {res}")


def solve_all():
    solve_first_part()
    solve_second_part()


if __name__ == "__main__":
    solve_all()
