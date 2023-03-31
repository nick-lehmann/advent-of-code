# Link: https://adventofcode.com/2021/day/15
from ..utils import AOCTestCase


class Chiton(AOCTestCase):
    day = 15
    year = 2021

    grid: list[list[int]]
    height: int
    width: int
    directions = [(1, 0), (0, 1)]

    def get_neighbours(self, row, column) -> list[tuple[int, int]]:
        return [
            (row - drow, column - dcolumn)
            for drow, dcolumn in self.directions
            if 0 <= row - drow and 0 <= column - dcolumn
        ]

    def find_in_grid(self) -> int:
        self.grid[0][0] = 0
        for row in range(0, self.height):
            for column in range(0, self.width):
                neighbours = self.get_neighbours(row, column)

                if len(neighbours) == 0:
                    continue

                current_cell = self.grid[row][column]
                self.grid[row][column] = min(
                    current_cell + self.grid[nrow][ncolumn]
                    for nrow, ncolumn in neighbours
                )

        return self.grid[self.height - 1][self.width - 1]

    def part1(self, content: str) -> int:
        self.grid = self.intmap(content)
        self.height = len(self.grid)
        self.width = len(self.grid[0])

        return self.find_in_grid()

    def part2(self, content: str) -> int:
        grid = self.intmap(content)
        height, width = len(grid), len(grid[0])

        new_map = [line * 5 for line in grid * 5]
        for i in range(height * 5):
            for j in range(width * 5):
                new_map[i][j] = (new_map[i][j] + i // height + j // width - 1) % 9 + 1

        self.grid = new_map
        self.height = len(self.grid)
        self.width = len(self.grid[0])

        # print(f"Generated grid is {self.height}x{self.width}")
        # for row in self.grid:
        #     for cell in row:
        #         print(str(cell).rjust(2, " "), end="")
        #     print()

        return self.find_in_grid()
