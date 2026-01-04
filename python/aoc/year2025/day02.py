# Link: https://adventofcode.com/2025/day/2
from ..utils import AOCTestCase


class CalorieCounting(AOCTestCase):
    day = 2
    year = 2025

    def part1(self, content: str) -> int:
        return len(content)
        # return self.process(content)[0]

    def part2(self, content: str) -> int:
        return len(content)
        # return sum(self.process(content)[:3])
