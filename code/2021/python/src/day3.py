from src import DATA_DIR
from typing import List, Literal, Tuple


def load_data() -> List[str]:
    day_three_file = DATA_DIR / "day3"
    with open(day_three_file, "r") as f:
        return f.read().splitlines()


def calculate_gamma_epsilon(diagnostic_report: List[str]) -> Tuple[str, str]:
    """Finds the binary representation for the gamma and epsilon value from a diagnosis report.

    The function runs over the report N times till it encounters an IndexError indicating the end
    of the diagnostic. It composes the gamma and epsilon numbers over the number of promenient bits.

    * `gamma` takes the major bit
    * `epsilon` takes the minor bit

    **NOTE:** the function returns binary representation strings. You need to convert them back to
    obtain the power consumption through `int(gamma, 2) * int(epsilon, 2)`.

    Parameters
    ----------
    diagnostic_report : List[str]
        list of binary representation strings like `"10110"`

    Returns
    -------
    Tuple[str, str]
        values of gamma and epsilon as binary representation strings
    """
    gamma = epsilon = ""
    n = 0
    count_ones = 0
    total_lines = len(diagnostic_report)
    while True:
        for line_report in diagnostic_report:
            try:
                bit = line_report[n]
                count_ones += int(bit == "1")
            except IndexError:
                return gamma, epsilon
        gamma += str(int(count_ones > (total_lines - count_ones)))
        epsilon += str(int(not count_ones > (total_lines - count_ones)))

        # Go to next bit
        n += 1
        count_ones = 0


def find_gas_rating(
    candidates: List[str], gas_name: Literal["co2_scrubber_rating", "oxygen_generator_rating"], current_bit_idx: int = 0
) -> str:
    """Finds one of the gases' best rating based over the most / least common bit

    Parameters
    ----------
    candidates : List[str]
        [description]
    gas_name : Literal[
        [description]
    current_bit_idx : int, optional
        [description], by default 0

    Returns
    -------
    str
        [description]
    """
    if len(candidates) == 1:
        return candidates[0]

    count_ones = 0
    total_lines = len(candidates)

    for candidate in candidates:
        try:
            bit = candidate[current_bit_idx]
            count_ones += int(bit == "1")
        except IndexError:
            return candidate

    cond = count_ones >= (total_lines - count_ones)
    if gas_name == "co2_scrubber_rating":
        cond = not cond

    if cond:
        new_candidates = [candidate for candidate in candidates if candidate[current_bit_idx] == "1"]
    else:
        new_candidates = [candidate for candidate in candidates if candidate[current_bit_idx] == "0"]

    return find_gas_rating(new_candidates, gas_name, current_bit_idx + 1)


def find_life_support(diagnostic_report: List[str]) -> int:
    oxygen_generator_rating = find_gas_rating(diagnostic_report, gas_name="oxygen_generator_rating")
    co2_scrubber_rating = find_gas_rating(diagnostic_report, gas_name="co2_scrubber_rating")
    return int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)


def day3():
    print("--- Day 3: Binary Diagnostic ---")
    diagnostic_report = load_data()
    gamma, epsilon = calculate_gamma_epsilon(diagnostic_report)
    print(f"Gamma value: {gamma} (base 10: {int(gamma, 2)}) / Epsilon value: {epsilon} (base 10: {int(epsilon, 2)})")
    print("Power consumption =", int(gamma, 2) * int(epsilon, 2))
    print("PART 2: life support")
    life_support_reserves = find_life_support(diagnostic_report)
    print("Life support reserves:", life_support_reserves)


if __name__ == "__main__":
    day3()
