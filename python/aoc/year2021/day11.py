# Link: https://adventofcode.com/2021/day/11
from typing import Iterable, List, Tuple
from ..utils import AOCTestCase
from dataclasses import dataclass


@dataclass
class Cell:
    value: int
    neighbors: List["Cell"]
    row: int
    column: int


# Reads a grid of cells from a string
def read_grid(input_string: str, diagonal: bool) -> List[List[Cell]]:
    grid: List[List[Cell]] = []
    for row, line in enumerate(input_string.splitlines()):
        grid.append([])
        for column, char in enumerate(line):
            cell = Cell(value=int(char), neighbors=[], row=row, column=column)
            grid[row].append(cell)

    # Add neighbor relation
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    if diagonal:
        d += [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    for row in grid:
        for cell in row:
            for dx, dy in d:
                try:
                    cell.neighbors.append(grid[cell.row + dx][cell.column + dy])
                except IndexError:
                    pass

    rows = len(grid)
    columns = len(grid[0])

    return grid, rows, columns


def iterate_grid(rows: int, columns: int) -> Iterable[Tuple[int, int]]:
    for row in range(rows):
        for column in range(columns):
            yield row, column


class DumboOctopus(AOCTestCase):
    day = 11
    year = 2021

    def part1(self, content: str) -> int:
        # grid, rows, columns = read_grid(content, diagonal=True)

        # round = 0
        # flashes = 0
        # while round < 100:
        #     stack = []
        #     for row, column in iterate_grid(rows, columns):
        #         cell = grid[row][column]
        #         cell.value += 1
        #         if cell.value == 10:
        #             stack += [cell]

        #     while stack:
        #         cell = stack.pop()
        #         for neighbor in cell.neighbors:
        #             if neighbor.value == 10:
        #                 continue

        #             neighbor.value += 1
        #             if neighbor.value == 10:
        #                 stack += [neighbor]

        #     # TODO: Custom grid class with iterator
        #     for row, column in iterate_grid(rows, columns):
        #         cell = grid[row][column]
        #         if cell.value == 10:
        #             cell.value = 1
        #             flashes += 1

        #     print(f"Round {round}: {flashes}")
        #     round += 1

        # return flashes
        data = {}
        for y, row in enumerate(self.lines(content)):
            for x, n in enumerate(row.strip()):
                data[(x, y)] = int(n)

        border = ((1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1))
        step = 0
        total_flashes = 0
        while True:
            step += 1
            for key in data:
                data[key] += 1

            stack = [key for key in data if data[key] == 10]
            while stack:
                x, y = stack.pop()
                for dx, dy in border:
                    x_ = x + dx
                    y_ = y + dy
                    if (x_, y_) in data and data[x_, y_] < 10:
                        data[x_, y_] += 1
                        if data[x_, y_] == 10:
                            stack.append((x_, y_))

            flashes = 0
            for key in data:
                if data[key] == 10:
                    data[key] = 0
                    flashes += 1

            total_flashes += flashes
            if step == 100:
                return total_flashes

    def part2(self, content: str) -> int:
        data = {}
        for y, row in enumerate(self.lines(content)):
            for x, n in enumerate(row.strip()):
                data[(x, y)] = int(n)

        border = ((1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1))
        step = 0
        total_flashes = 0
        while True:
            step += 1
            for key in data:
                data[key] += 1

            stack = [key for key in data if data[key] == 10]
            while stack:
                x, y = stack.pop()
                for dx, dy in border:
                    x_ = x + dx
                    y_ = y + dy
                    if (x_, y_) in data and data[x_, y_] < 10:
                        data[x_, y_] += 1
                        if data[x_, y_] == 10:
                            stack.append((x_, y_))

            flashes = 0
            for key in data:
                if data[key] == 10:
                    data[key] = 0
                    flashes += 1

            total_flashes += flashes

            if flashes == 100:
                return step
