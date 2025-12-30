from pathlib import Path
from enum import StrEnum


class ParseType(StrEnum):
    comma = "comma"
    lines = "lines"
    matrix = "matrix"
    two_section_lines = "two_section_lines"


def get_list_from_line_file(file_path: Path) -> list[str]:
    with open(file_path, "r") as file:
        return file.read().splitlines()


def get_list_from_comma_file(file_path: Path) -> list[str]:
    with open(file_path, "r") as file:
        content = file.read().replace("\n", "").strip()
        return [value for value in content.split(",") if value]


def get_matrix_from_file(file_path: Path) -> list[list[str]]:
    with open(file_path, "r") as file:
        lines = file.read().strip().splitlines()
        return [list(line) for line in lines]


def get_two_section_lines_from_file(file_path: Path) -> tuple[list[str], list[str]]:
    with open(file_path, "r") as file:
        content = file.read().strip()
        sections = content.split("\n\n")
        if len(sections) != 2:
            raise ValueError("Input file does not contain exactly two sections.")
        section1 = sections[0].splitlines()
        section2 = sections[1].splitlines()
        return section1, section2


def parse_input(file_path: Path, parse_type: ParseType) -> list[str]:
    if parse_type == ParseType.lines:
        return get_list_from_line_file(file_path)
    elif parse_type == ParseType.comma:
        return get_list_from_comma_file(file_path)
    elif parse_type == ParseType.matrix:
        return get_matrix_from_file(file_path)
    elif parse_type == ParseType.two_section_lines:
        return get_two_section_lines_from_file(file_path)
    else:
        raise ValueError(f"Unknown parse type: {parse_type}")


def get_sample_1_input(package_path: Path, parse_type: ParseType) -> list[str]:
    file_path = package_path / "sample1.txt"
    return parse_input(file_path, parse_type)


def get_sample_2_input(package_path: Path, parse_type: ParseType) -> list[str]:
    file_path = package_path / "sample2.txt"
    return parse_input(file_path, parse_type)


def get_part_1_input(package_path: Path, parse_type: ParseType) -> list[str]:
    file_path = package_path / "part1.txt"
    return parse_input(file_path, parse_type)


def get_part_2_input(package_path: Path, parse_type: ParseType) -> list[str]:
    file_path = package_path / "part2.txt"
    return parse_input(file_path, parse_type)
