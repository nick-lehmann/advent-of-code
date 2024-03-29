# Link: https://adventofcode.com/2020/day/2
from typing import List
import re
from operator import xor

from ..utils import AOCTestCase

# https://regex101.com/r/RTevsV/1/
PASSWORD_REGEX = r"(\d+)\-(\d+) (\w)\: (\w+)"


class PasswordPhilosophy(AOCTestCase):
    day = 2
    year = 2020

    def part1(self, content: str) -> int:
        valid = 0
        for line in self.lines(content):
            match = re.match(PASSWORD_REGEX, line, re.M | re.I)
            minimum, maximum, letter, password = match.groups()
            minimum = int(minimum)
            maximum = int(maximum)

            count = password.count(letter)
            if minimum <= count <= maximum:
                valid += 1
        return valid

    def part2(self, content: str) -> int:
        valid = 0
        for line in self.lines(content):
            match = re.match(PASSWORD_REGEX, line, re.M | re.I)
            first, second, letter, password = match.groups()
            if xor(
                password[int(first) - 1] == letter, password[int(second) - 1] == letter
            ):
                valid += 1
        return valid
