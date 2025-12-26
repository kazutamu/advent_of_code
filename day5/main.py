from utils.input_utils import (
    ParseType,
    get_sample_1_input,
    get_part_2_input,
    get_part_1_input,
    get_sample_2_input,
)
from pathlib import Path
from collections import defaultdict

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
    inputs = get_part_2_input(PACKAGE_PATH, ParseType.two_section_lines)
    range_list, _ = inputs
    search = defaultdict(int)
    for start, end in get_ranges(range_list):
        search[start] += 1
        search[end] -= 1

    total_num = 0
    edge_nums = sorted(search.keys())
    start_edge_num = edge_nums[0]
    value = 0
    for i in range(len(edge_nums)):
        edge_num = edge_nums[i]
        value += search[edge_num]
        if value == 0:
            total_num += edge_num - start_edge_num + 1
            start_edge_num = edge_nums[i + 1] if i + 1 < len(edge_nums) else None

    return total_num


if __name__ == "__main__":
    # print("Part One:")
    # print(part_one())
    print("Part Two:")
    print(part_two())
