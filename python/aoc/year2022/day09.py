# Link: https://adventofcode.com/2022/day/9
from attr import dataclass
from ..utils import AOCTestCase


@dataclass
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


deltas = {
    "U": Point(0, 1),
    "D": Point(0, -1),
    "R": Point(1, 0),
    "L": Point(-1, 0),
}


class RopeBridge(AOCTestCase):
    day = 9
    year = 2022

    def part1(self, content: str) -> int:
        lines = [line.split() for line in self.lines(content)]

        head = Point(0, 0)
        tail = Point(0, 0)

        for direction, steps in lines:
            delta = deltas[direction]
            for _ in steps:
                head += delta
                diff = head - tail

                if diff.x < 2 and diff.y < 2:
                    continue

                if diff.x >= 2 and diff.y == 0:
                    pass

    def part2(self, content: str) -> int:
        pass
