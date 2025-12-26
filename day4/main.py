from utils.input_utils import (
    ParseType,
    get_sample_1_input,
    get_part_2_input,
    get_part_1_input,
    get_sample_2_input,
)
from pathlib import Path

from utils.matrix_utils import OFFSETS, is_in_bounds

PACKAGE_PATH = Path(__file__).parent


def is_valid_position(i, j, matrix, removed=set()):
    if matrix[i][j] != "@" or (i, j) in removed:
        return False

    count = 0
    for dx, dy in OFFSETS:
        ni, nj = i + dx, j + dy
        if not is_in_bounds(ni, nj, matrix):
            continue
        if matrix[ni][nj] == "@" and (ni, nj) not in removed:
            count += 1
    if count < 4:
        return True

    return False


def part_one():
    inputs = get_part_1_input(PACKAGE_PATH, ParseType.matrix)
    count = 0
    for i in range(len(inputs)):
        for j in range(len(inputs[0])):
            if is_valid_position(i, j, inputs):
                count += 1
    return count


def part_two():
    inputs = get_part_2_input(PACKAGE_PATH, ParseType.matrix)
    count = 0
    total_removed = set()
    removed: set[int] = [-1]
    while len(removed) != 0:
        removed = set()
        for i in range(len(inputs)):
            for j in range(len(inputs[0])):
                if is_valid_position(i, j, inputs, total_removed):
                    removed.add((i, j))
                    count += 1
        total_removed.update(removed)
    return count


if __name__ == "__main__":
    print("Part One:")
    print(part_one())
    print("Part Two:")
    print(part_two())
