from utils.input_utils import (
    ParseType,
    get_sample_1_input,
    get_part_2_input,
    get_part_1_input,
    get_sample_2_input,
)
from pathlib import Path

PACKAGE_PATH = Path(__file__).parent


def get_value(first: str, second: str) -> int:
    return int(first) * 10 + int(second)


def get_two_joltage(input: str) -> int:
    max_first = int(input[0])
    max_value = get_value(input[0], input[1])
    for i in range(len(input)):
        first = int(input[i])
        if first >= max_first:
            for j in range(i + 1, len(input)):
                second = int(input[j])
                value = get_value(first, second)
                if value > max_value:
                    max_value = value
                    max_first = first
    return max_value


def get_twelve_joltage(input: str) -> int:
    first_index = 0
    last_index = -12
    str_list = []
    for i in range(12):
        max_index = first_index
        for j in range(first_index, len(input) + last_index + 1):
            if input[j] > input[max_index]:
                max_index = j
        str_list.append(input[max_index])
        first_index = max_index + 1
        last_index += 1
    return int("".join(str_list))


def part_one():
    inputs = get_part_1_input(PACKAGE_PATH, ParseType.lines)
    total = 0
    for input in inputs:
        total += get_two_joltage(input)
    return total


def part_two():
    inputs = get_part_2_input(PACKAGE_PATH, ParseType.lines)
    total = 0
    for input in inputs:
        total += get_twelve_joltage(input)
    return total


if __name__ == "__main__":
    print("Part One:")
    print(part_one())
    print("Part Two:")
    print(part_two())
