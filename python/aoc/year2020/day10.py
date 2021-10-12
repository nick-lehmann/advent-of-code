# Link: https://adventofcode.com/2020/day/10
from typing import List
from ..utils import AOCTestCase


def neighborDifferences(numbers: List[int]) -> List[int]:
    return [y - x for x, y in zip(numbers, numbers[1:])]


class AdapterArray(AOCTestCase):
    day = 10
    year = 2020

    def part1(self, content: str) -> int:
        numbers = sorted(self.ints(content))
        numbers = [0] + numbers + [numbers[-1] + 3]
        differences = neighborDifferences(numbers)
        return differences.count(1) * differences.count(3)

    def part2(self, content: str) -> int:
        pass
