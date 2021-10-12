# Link: https://adventofcode.com/2020/day/5
from ..utils import AOCTestCase


class BinaryBoarding(AOCTestCase):
    day = 5
    year = 2020

    def part1(self, content: str) -> int:
        line = self.lines(content)[0]
        return int(
            line.replace("F", "0")
            .replace("B", "1")
            .replace("L", "0")
            .replace("R", "1"),
            2,
        )

    def part2(self, content: str):
        pass
