# Link: https://adventofcode.com/2022/day/1
from ..utils import AOCTestCase


class CalorieCounting(AOCTestCase):
    day = 1
    year = 2022

    def process(self, content: str) -> int:
        calories = []
        current = 0
        for line in content.split("\n"):
            if line == "":
                calories += [current]
                current = 0
                continue
            current += int(line)

        return sorted(calories, reverse=True)

    def part1(self, content: str) -> int:
        return self.process(content)[0]

    def part2(self, content: str) -> int:
        return sum(self.process(content)[:3])
