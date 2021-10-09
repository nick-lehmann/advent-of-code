from itertools import combinations
from ..utils import AOCTestCase


class ReportRepair(AOCTestCase):
    def part1(self) -> int:
        numbers = self.ints
        for number in numbers:
            remainder = 2020 - number
            if remainder in numbers:
                return number * remainder

    def part2(self):
        numbers = self.ints
        for combo in combinations(numbers, 2):
            remainder = 2020 - sum(combo)
            if remainder in numbers:
                return combo[0] * combo[1] * remainder
