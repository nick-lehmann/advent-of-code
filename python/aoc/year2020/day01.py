from itertools import combinations
from ..utils import AOCTestCase


class ReportRepair(AOCTestCase):
    day = 1
    year = 2020

    def part1(self, content: str) -> int:
        numbers = self.ints(content)
        for number in numbers:
            remainder = 2020 - number
            if remainder in numbers:
                return number * remainder

    def part2(self, content: str) -> int:
        numbers = self.ints(content)
        for combo in combinations(numbers, 2):
            remainder = 2020 - sum(combo)
            if remainder in numbers:
                return combo[0] * combo[1] * remainder
