# Link: https://adventofcode.com/2021/day/20
from typing import List
from ..utils import AOCTestCase
from itertools import product


def print_grid(grid: List[List[int]]):
    for row in grid:
        print("".join(["#" if x else "." for x in row]))
    print()


class TrenchMap(AOCTestCase):
    day = 20
    year = 2021

    def part1(self, content: str) -> int:
        algorithm, rawImage = content.split("\n\n")
        algorithm = [1 if x == "#" else 0 for x in algorithm]

        image = set()
        for rowIndex, row in enumerate(rawImage.split("\n")):
            for columnIndex, cell in enumerate(row):
                if cell == "#":
                    image.add((rowIndex, columnIndex))
        print("Working on image:")

        STEPS = 2
        for step in range(STEPS):
            new_image = set()
            minx = min(x for x, y in image)
            maxx = max(x for x, y in image)
            miny = min(y for x, y in image)
            maxy = max(y for x, y in image)

            for rowIndex in range(minx - 1, maxx + 2):
                for columnIndex in range(miny - 1, maxy + 2):
                    window = product(
                        range(rowIndex - 1, rowIndex + 2),
                        range(columnIndex - 1, columnIndex + 2),
                    )
                    enhancement_input = [0] * 9

                    for i, (x, y) in enumerate(window):
                        if (
                            (x, y) in image
                            or minx <= rowIndex <= maxx
                            and miny <= columnIndex <= maxy
                            and step % 2
                        ):
                            enhancement_input[i] = 1

                    enhancement_input = int("".join(map(str, enhancement_input)), 2)
                    if algorithm[enhancement_input] == 1:
                        image.add((rowIndex, columnIndex))

            print(f"Done with step {step}")
            # print_grid(new_image)
            image = new_image

        return sum(char for line in image for char in line)

    def part2(self, content: str) -> int:
        pass
