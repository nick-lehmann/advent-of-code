# Link: https://adventofcode.com/2021/day/9
from typing import List
from ..utils import AOCTestCase
from dataclasses import dataclass
import math


@dataclass
class Point:
    row: int
    col: int
    value: int


class SmokeBasin(AOCTestCase):
    day = 9
    year = 2021

    def find_low_points(self, grid) -> List[Point]:
        height, width = len(grid), len(grid[0])

        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        low_points = []
        for row in range(height):
            for column in range(width):
                cell = grid[row][column]

                if all(
                    grid[row + x][column + y] > cell
                    for x, y in d
                    if 0 <= row + x < height and 0 <= column + y < width
                ):
                    low_points += [Point(row, column, cell)]

        return low_points

    def find_basin(self, grid, point: Point, height: int, width: int) -> List[Point]:
        basin = [point]
        wave = [point]

        while len(wave):
            new_wave = []
            for point in wave:
                for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if not (0 <= point.row + x < height and 0 <= point.col + y < width):
                        continue

                    other_point = Point(
                        point.row + x, point.col + y, grid[point.row + x][point.col + y]
                    )

                    if other_point in new_wave or other_point in basin:
                        continue

                    if other_point.value > point.value and other_point.value != 9:
                        new_point = Point(
                            point.row + x,
                            point.col + y,
                            grid[point.row + x][point.col + y],
                        )
                        new_wave += [new_point]
                        basin += [new_point]

            wave = new_wave

        return basin

    def part1(self, content: str) -> int:
        grid = self.intmap(content)
        low_points = self.find_low_points(grid)
        return sum(p.value + 1 for p in low_points)

    def part2(self, content: str) -> int:
        grid = self.intmap(content)
        height, width = len(grid), len(grid[0])

        low_points = self.find_low_points(grid)

        basins = [self.find_basin(grid, p, height, width) for p in low_points]
        basins = sorted(basins, key=lambda b: len(b))

        for row in range(height):
            for column in range(width):
                point = Point(row, column, grid[row][column])

                if any(point in basin for basin in basins):
                    print(f"\033[91m{point.value}\033[0m", end="")
                else:
                    print(point.value, end="")
            print()

        return math.prod(len(basin) for basin in basins[-3:])
