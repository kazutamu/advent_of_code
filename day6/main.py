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


def transform(inputs: list[str]) -> list[str]:
    result: list[str] = []
    result.append("")
    for j in range(len(inputs[0]) - 1, -1, -1):
        for i in range(len(inputs)):
            char = inputs[i][j]
            result[-1] += inputs[i][j]
            if char in ["+", "*"]:
                result.append("")

    return result


def part_two():
    inputs = get_part_2_input(PACKAGE_PATH, ParseType.lines)
    str_list = transform(inputs)
    total = 0
    for s in str_list:
        if len(s) == 0:
            continue
        op = s[-1]
        values = [int(value) for value in s[:-1].strip().split()]
        if op == "+":
            total += sum(values)
        elif op == "*":
            product = 1
            for v in values:
                product *= v
            total += product
    return total


if __name__ == "__main__":
    # print("Part One:")
    # print(part_one())
    print("Part Two:")
    print(part_two())
