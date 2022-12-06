# Link: https://adventofcode.com/2021/day/17
from ..utils import AOCTestCase
from dataclasses import dataclass
import re

@dataclass
class Range:
    lower: int
    upper: int


@dataclass
class Area:
    x: Range
    y: Range



def steps_for_dy(area: Area):
    y, steps, valid = 0, 0, []
    while y >= area.y.lower:
        if miny <= y <= maxy:
            valid += [steps]
        y += dy
        dy -= 1
        steps += 1
    return valid

def can_land_dx(step):
    total = set()
    for dx in range(0, maxx + 1):
        x = 0
        odx = dx
        for _ in range(step):
            x += dx
            if dx > 0:
                dx -= 1
        if minx <= x <= maxx:
            total.add(odx)
    return total


class TrickShot(AOCTestCase):
    day = 17
    year = 2021

    
    def read(self, content: str) -> Area:
        """
        Parse a string like "target area: x=20..30, y=-10..-5" into a Area 
        """
        m = re.match(r"target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)", content)
        return Area(Range(int(m[1]), int(m[2])), Range(int(m[3]), int(m[4])))
        

    def part1(self, content: str) -> int:
        area = self.read(content)
        dy = -area.y.lower

        while True:
            if any(can_land_dx(step) for step in steps_for_dy(dy)):
                return sum(range(1, dy + 1))
            dy -= 1

    def part2(self, content: str) -> int:
        area = self.read(content)

        total = 0

        for dy in range(miny - 1, -miny + 1):
            iter = set()
            for step in steps_for_dy(dy):
                iter |= can_land_dx(step)
            total += len(iter)

        return total
