# Link: https://adventofcode.com/2020/day/4
from ..utils import AOCTestCase


class PassportProcessing(AOCTestCase):
    day = 4
    year = 2020

    def part1(self, content: str) -> int:
        lines = self.lines(content)
        required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
        valid = 0
        for lines in lines.join("\n").split("\n\n"):
            parts = {part.split(":")[0] for part in lines.replace("\n", " ").split(" ")}
            valid += int(not (required_fields - parts))
        return valid

    def part2(self, content: str) -> int:
        raise NotImplementedError()
