from utils.input_utils import (
    ParseType,
    get_sample_1_input,
    get_part_2_input,
    get_part_1_input,
    get_sample_2_input,
)
from pathlib import Path

PACKAGE_PATH = Path(__file__).parent


def get_first_and_last(input: str) -> tuple[int, int]:
    first_str, last_str = input.split("-")
    return int(first_str), int(last_str)


def is_valid(num: int) -> bool:
    str_num = str(num)
    if len(str_num) % 2 != 0:
        return False
    half = len(str_num) // 2
    return str_num[:half] == str_num[half:]


def part_one():
    sample_input = get_part_1_input(PACKAGE_PATH, ParseType.comma)
    total = 0
    for line in sample_input:
        first, last = get_first_and_last(line)
        for num in range(first, last + 1):
            if is_valid(num):
                total += num
    return total


def part_two():
    sample_input = get_sample_2_input(PACKAGE_PATH, ParseType.comma)
    for line in sample_input:
        print(get_first_and_last(line))


if __name__ == "__main__":
    print("Part One:")
    print(part_one())
    # print("Part Two:")
    # part_two()
