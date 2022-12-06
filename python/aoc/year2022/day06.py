# Link: https://adventofcode.com/2022/day/6
from ..utils import AOCTestCase


class TuningTrouble(AOCTestCase):
    day = 6
    year = 2022

    def part1(self, content: str) -> int:
        input = self.lines(content)[0]
        for i in range(4, len(input)):
            chars = input[i - 4 : i]
            if len(chars) == len(set(chars)):
                return i

    def part2(self, content: str) -> int:
        input = self.lines(content)[0]
        for i in range(14, len(input)):
            chars = input[i - 14 : i]
            if len(chars) == len(set(chars)):
                return i
