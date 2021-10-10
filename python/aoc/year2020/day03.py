from dataclasses import dataclass
from typing import List
from ..utils import AOCTestCase


@dataclass
class Point:
    x: int = 0
    y: int = 0


Map = List[List[chr]]


def find_trees(map: Map, slope: Point) -> int:
    row = 0
    column = 0
    width = len(map[0])
    trees = 0
    while row < len(map):
        trees += int(map[row][column] == "#")
        row += slope.x
        column = (column + slope.y) % width
    return trees


class TobogganTrajectory(AOCTestCase):
    day = 3
    year = 2020

    def part1(self, content: str) -> int:
        return find_trees(self.map(content), Point(x=1, y=3))

    def part2(self, content: str) -> int:
        points = [
            Point(x=1, y=1),
            Point(x=3, y=1),
            Point(x=5, y=1),
            Point(x=7, y=1),
            Point(x=1, y=2),
        ]
        product = 1
        map = self.map(content)
        for point in points:
            product *= find_trees(map, point)
        return product
