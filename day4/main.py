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
    inputs = get_sample_1_input(PACKAGE_PATH, ParseType.matrix)
    print(inputs)


def part_two():
    inputs = get_sample_2_input(PACKAGE_PATH, ParseType.matrix)
    print(inputs)


if __name__ == "__main__":
    print("Part One:")
    part_one()
    print("Part Two:")
    part_two()
