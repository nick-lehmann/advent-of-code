# Link: https://adventofcode.com/2021/day/01
from ..utils import AOCTestCase


class SonarSweep(AOCTestCase):
    day = 1
    year = 2021

    def part1(self, content: str) -> int:
        depths = self.ints(content)
        return sum([1 for x, y in zip(depths, depths[1:]) if x < y])

    def part2(self, content: str) -> int:
        depths = self.ints(content)
        return sum(
            1
            for i in range(len(depths) - 3)
            if sum(depths[i : i + 3]) < sum(depths[i + 1 : i + 4])
        )
