from pathlib import Path


def get_list_from_file(file_path: Path) -> list[str]:
    with open(file_path, "r") as file:
        return file.read().strip().splitlines()


def get_sample_1_input(package_path: Path) -> list[str]:
    file_path = package_path / "sample1.txt"
    return get_list_from_file(file_path)


def get_sample_2_input(package_path: Path) -> list[str]:
    file_path = package_path / "sample2.txt"
    return get_list_from_file(file_path)


def get_part_1_input(package_path: Path) -> list[str]:
    file_path = package_path / "part1.txt"
    return get_list_from_file(file_path)


def get_part_2_input(package_path: Path) -> list[str]:
    file_path = package_path / "part2.txt"
    return get_list_from_file(file_path)
