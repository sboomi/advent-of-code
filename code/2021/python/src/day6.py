from src import DATA_DIR
from typing import List


def load_data() -> List[int]:
    day_six_file = DATA_DIR / "day6"
    with open(day_six_file, "r") as f:
        return [int(age) for age in f.read().split(",")]


def evolve_lanternfishes(lanternfishes: List[int]) -> List[int]:
    """Takes a list of lanternfish timers from T iteration (in days) and returns it at T+1

    Every day, each timer from the list decreases by 1 and resets to 6 after it hits 0 as
    controlled by the `% 7` operator. Before decreasing, the function checks whether the
    population increased and adds 8 to the list everytime it finds a timer value of 0.

    Parameters
    ----------
    lanternfishes : List[int]
        List of lanternfish timers at T

    Returns
    -------
    List[int]
        List of lanternfish timers at T+1
    """
    newborn_lanternfishes = sum([lanternfish == 0 for lanternfish in lanternfishes])
    return [(lanternfish - 1) % 7 if lanternfish < 7 else lanternfish - 1 for lanternfish in lanternfishes] + [
        8 for _ in range(newborn_lanternfishes)
    ]


def run_population_evolution(max_iter: int, initial_population: List[int]) -> List[int]:
    """Evolves population of lanternfishes given a max number of days and returns the list
    at `max_iter`

    Parameters
    ----------
    max_iter : int
        The maximum number of days
    initial_population : List[int]
        [description]

    Returns
    -------
    List[int]
        [description]
    """
    end_population = initial_population[:]

    for _ in range(max_iter):
        end_population = evolve_lanternfishes(end_population)

    return end_population


def track_pop_evolution(max_iter: int, initial_population: List[int]) -> int:
    """This solution optimizes memory and keeps the algorithm O1

    Parameters
    ----------
    max_iter : int
        [description]
    initial_population : List[int]
        [description]

    Returns
    -------
    int
        [description]
    """

    timer_tracker = {i: 0 for i in range(9)}
    for pop in initial_population:
        timer_tracker[pop] += 1

    for n in range(max_iter):
        newborns = timer_tracker[0]
        for k, v in timer_tracker.items():

            if k - 1 >= 0:
                timer_tracker[k - 1] = v
            else:
                resetters = v

        timer_tracker[6] += resetters
        timer_tracker[8] = newborns

    return sum([v for v in timer_tracker.values()])


def day6():
    print("--- Day 6: Lanternfish ---")
    lanternfish_ages = load_data()
    print(f"Population of lanternfishes at day 0: {len(lanternfish_ages)}")
    day_80_lfish_pop = run_population_evolution(80, lanternfish_ages)
    print(f"Population after 80 days: {len(day_80_lfish_pop)}")
    print("PART 2: optimization challenge")
    print("Don't attempt the first function at home, kids")
    day_256_lfish_pop = track_pop_evolution(256, lanternfish_ages)
    print(f"Population after 256 days: {day_256_lfish_pop}")


if __name__ == "__main__":
    day6()
