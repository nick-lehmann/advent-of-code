# Link: https://adventofcode.com/2022/day/14
from ..utils import AOCTestCase


class RegolithReservoir(AOCTestCase):
    day = 14
    year = 2022
    blocks: set[tuple[int, int]]

    def read(self, content) -> set[tuple[int, int]]:
        blocks = set()
        for line in self.lines(content):
            points = [tuple(map(int, point.split(","))) for point in line.split(" -> ")]
            for point1, point2 in zip(points, points[1:]):
                x1, y1 = point1
                x2, y2 = point2
                blocks.update(
                    (x, y)
                    for x in range(min(x1, x2), max(x1, x2) + 1)
                    for y in range(min(y1, y2), max(y1, y2) + 1)
                )
        return blocks

    def simulate(self, x: int, y: int) -> list[tuple[int, int]]:
        print(f"Checking {x}, {y}")
        if (x, y) in self.blocks:
            return [(x, y)]

        results = (
            self.simulate(x, y + 1)
            + self.simulate(x - 1, y + 1)
            + self.simulate(x + 1, y + 1)
        )
        self.blocks |= {(x, y)}
        return results

    def part1(self, content: str) -> int:
        self.blocks = self.read(content)
        l = len(self.blocks)
        self.simulate(500, 0)
        return len(self.blocks) - l

    def part2(self, content: str) -> int:
        pass
