# Link: https://adventofcode.com/2020/day/11
from typing import List
from ..utils import AOCTestCase
from copy import deepcopy


Board = List[List[chr]]


class SeatingSystem(AOCTestCase):
    day = 11
    year = 2020

    def iterate(self, seats):
        new_seats = deepcopy(seats)
        for row in range(len(seats)):
            for column in range(len(seats[0])):
                if seats[row][column] == ".":
                    new_seats[row][column] = "."
                    continue

                occupied = 0
                for nRow in [row - 1, row, row + 1]:
                    for nColumn in [column - 1, column, column + 1]:
                        if nRow == 0 and nColumn == 0:
                            continue
                        try:
                            neighbor = seats[nRow][nColumn]
                            occupied += int(neighbor == "#")
                            print(f"{occupied} seats were occupied")
                        except:
                            continue

                new_seats[row][column] = "L" if occupied >= 4 else "#"

        return new_seats

    def part1(self, content: str) -> int:
        seats = [list(line) for line in content]

        step = 0
        while True:
            step += 1
            print(f"Step {step}")
            new_seats = self.iterate(seats)

            if seats == new_seats:
                return sum(line.count("#") for line in seats)
            seats = new_seats

    def part2(self, content: str) -> int:
        pass
