# Link: https://adventofcode.com/2022/day/8
from ..utils import AOCTestCase
from math import prod


def griditer(height, width):
    for row in range(height):
        for column in range(width):
            yield row, column


class TreetopTreeHouse(AOCTestCase):
    day = 8
    year = 2022

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    grid: list[list[int]]
    height: int
    width: int

    def part1(self, content: str) -> int:
        self.grid = self.intmap(content)
        self.height = len(self.grid)
        self.width = len(self.grid[0])

        total = 0
        visible = set()
        for row, column in griditer(self.height, self.width):
            for dx, dy in self.directions:
                if self.is_visible(row, column, dx, dy):
                    total += 1
                    visible.add((row, column))
                    continue

        return len(visible)

    def is_visible(self, row, column, dx, dy):
        i = 1
        h = self.grid[row][column]
        while True:
            x = row + i * dx
            y = column + i * dy

            if not (self.height > x >= 0 and self.width > y >= 0):
                return True

            neighbor = self.grid[x][y]
            if neighbor >= h:
                return False
            i += 1

    def part2(self, content: str) -> int:
        self.grid = self.intmap(content)
        self.height = len(self.grid)
        self.width = len(self.grid[0])

        max_score = 0
        for row, column in griditer(self.height, self.width):
            max_score = max(
                max_score,
                prod(
                    self.scenic_score(row, column, dx, dy) for dx, dy in self.directions
                ),
            )

        return max_score
