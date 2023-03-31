# Link: https://adventofcode.com/2022/day/17
from dataclasses import dataclass
from ..utils import AOCTestCase


@dataclass
class Point:
    x: int
    y: int

RelativePoint = Point

@dataclass
class Block:
    points: set[RelativePoint]


blocks = [
    Block(points=[Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0)]),
    Block(points=[Point(0, 1), Point(0, 1), Point(1, 1), Point(1, 2)])
]


class PyroclasticFlow(AOCTestCase):
    day = 17
    year = 2022

    def part1(self, content: str) -> int:
        height = 0
        content = content.strip()
        movements = [1 if x == ">" else -1 for x in content.split(",")]

    def part2(self, content: str) -> int:
        pass
