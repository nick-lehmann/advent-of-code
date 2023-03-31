# Link: https://adventofcode.com/2021/day/8
from typing import List
from ..utils import AOCTestCase
from itertools import permutations
from dataclasses import dataclass


@dataclass
class Part:
    input: List[str]
    output: List[str]


display = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}


class SevenSegmentSearch(AOCTestCase):
    day = 8
    year = 2021

    def read(self, content):
        parts = []
        for line in self.lines(content):
            input, output = line.split(" | ")
            parts += [Part(input.split(), output.split())]
        return parts

    def part1(self, content: str) -> int:
        parts = self.read(content)
        unique_lengths = [2, 3, 4, 7]
        total = 0
        for part in parts:
            for digit in part.output:
                if len(digit) in unique_lengths:
                    total += 1
        return total

    def part2(self, content: str) -> int:
        parts = self.read(content)
        total = 0
        for part in parts:
            for permutation in permutations("abcdefg"):
                to = str.maketrans("abcdefg", "".join(permutation))
                a = ["".join(sorted(code.translate(to))) for code in part.input]
                if all(code in display for code in a):
                    b = ["".join(sorted(code.translate(to))) for code in part.output]
                    total += int("".join(str(display[code]) for code in b))
                    break

        return total
