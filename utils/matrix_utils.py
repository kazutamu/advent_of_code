OFFSETS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def is_in_bounds(x: int, y: int, matrix: list[list]) -> bool:
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])
