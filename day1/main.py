from utils.input_utils import (
    get_sample_1_input,
    get_part_2_input,
    get_part_1_input,
    get_sample_2_input,
)
from pathlib import Path

PACKAGE_PATH = Path(__file__).parent


def get_dir_and_num(input: str) -> tuple[str, int]:
    return input[0], int(input[1:])


def part_one():
    inputs = get_part_1_input(PACKAGE_PATH)
    curret_position = 50
    count = 0
    for input in inputs:
        dir, num = get_dir_and_num(input)
        factor = 1 if dir == "R" else -1
        curret_position = (curret_position + factor * num) % 100
        if curret_position == 0:
            count += 1
    return count


def part_two():
    inputs = get_part_2_input(PACKAGE_PATH)
    cur_pos = 50
    count = 0

    for input in inputs:
        dir, num = get_dir_and_num(input)

        if dir == "R":
            end = cur_pos + num
            # Count multiples of 100 crossed in (cur_pos, end]
            count += end // 100 - cur_pos // 100
        else:
            end = cur_pos - num
            # Count multiples of 100 crossed in [end, cur_pos)
            count += (cur_pos - 1) // 100 - (end - 1) // 100

        cur_pos = end % 100

    return count


if __name__ == "__main__":
    print("Part One:")
    print(part_one())
    print("Part Two:")
    print(part_two())
