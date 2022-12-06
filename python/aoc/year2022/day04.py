# Link: https://adventofcode.com/2022/day/4
from ..utils import AOCTestCase


class CampCleanup(AOCTestCase):
    day = 4
    year = 2022

    def includes_completely(self, r1: range, r2: range) -> bool:
        return r1.start <= r2.start and r1.stop >= r2.stop

    def includes_partially(self, r1: range, r2: range) -> bool:
        return (
            r1.start <= r2.start
            and r1.stop >= r2.start
            or r1.stop >= r2.stop
            and r1.start <= r2.stop
        )

    def play(self, content: str, fn) -> int:
        lines = self.lines(content)
        s = 0
        for line in lines:
            (first, second) = line.split(",")
            first = range(*list(map(int, first.split("-"))))
            second = range(*list(map(int, second.split("-"))))

            if fn(first, second) or fn(second, first):
                s += 1
        return s

    def part1(self, content: str) -> int:
        return self.play(content, self.includes_completely)

    def part2(self, content: str) -> int:
        return self.play(content, self.includes_partially)
