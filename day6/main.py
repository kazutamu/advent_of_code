from utils.input_utils import (
    ParseType,
    get_sample_1_input,
    get_part_2_input,
    get_part_1_input,
    get_sample_2_input,
)
from pathlib import Path

PACKAGE_PATH = Path(__file__).parent


def part_one():
    inputs = get_part_1_input(PACKAGE_PATH, ParseType.lines)
    operators = inputs[-1].split()
    values = [int(value) for value in inputs[0].split()]
    for input in inputs[1:-1]:
        input = input.split()
        for i, value in enumerate(input):
            if operators[i] == "+":
                values[i] += int(value)
            elif operators[i] == "*":
                values[i] *= int(value)
    return sum(values)


def part_two():
    inputs = get_sample_2_input(PACKAGE_PATH, ParseType.lines)
    print(inputs)


if __name__ == "__main__":
    print("Part One:")
    print(part_one())
    # print("Part Two:")
    # part_two()
