from utils.input_utils import (
    ParseType,
    get_sample_1_input,
    get_part_2_input,
    get_part_1_input,
    get_sample_2_input,
)
from pathlib import Path

PACKAGE_PATH = Path(__file__).parent


def get_ranges(range_list) -> list[tuple[int, int]]:
    ranges = []
    for range_str in range_list:
        start_str, end_str = range_str.split("-")
        ranges.append((int(start_str), int(end_str)))
    return ranges


def within_ranges(value: int, ranges: list[tuple[int, int]]) -> bool:
    for start, end in ranges:
        if start <= value <= end:
            return True
    return False


def part_one():
    inputs = get_part_1_input(PACKAGE_PATH, ParseType.two_section_lines)
    range_list, ids = inputs
    count = 0
    for id in ids:
        if within_ranges(int(id), get_ranges(range_list)):
            count += 1
    return count


def part_two():
    inputs = get_sample_2_input(PACKAGE_PATH, ParseType.two_section_lines)
    range_list, ids = inputs


if __name__ == "__main__":
    print("Part One:")
    print(part_one())
    print("Part Two:")
    part_two()
