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


def part_one():
    input = get_part_1_input(PACKAGE_PATH, ParseType.comma)
    total = 0

    def is_valid(num: int) -> bool:
        str_num = str(num)
        if len(str_num) % 2 != 0:
            return False
        half = len(str_num) // 2
        return str_num[:half] == str_num[half:]

    for line in input:
        first, last = get_first_and_last(line)
        for num in range(first, last + 1):
            if is_valid(num):
                total += num
    return total


def part_two():
    input = get_part_2_input(PACKAGE_PATH, ParseType.comma)
    total = 0

    def is_valid(num: int) -> bool:
        str_num = str(num)
        for i in range(len(str_num) - 1):
            if len(str_num) % (i + 1) != 0:
                continue
            separated = [
                str_num[j : j + (i + 1)] for j in range(0, len(str_num), (i + 1))
            ]
            if all(part == separated[0] for part in separated):
                return True
        return False

    for line in input:
        first, last = get_first_and_last(line)
        for num in range(first, last + 1):
            if is_valid(num):
                total += num

    return total


if __name__ == "__main__":
    print("Part One:")
    print(part_one())
    print("Part Two:")
    print(part_two())
