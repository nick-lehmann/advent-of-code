# Link: https://adventofcode.com/2021/day/02
from ..utils import AOCTestCase


class Dive(AOCTestCase):
    day = 2
    year = 2021

    def part1(self, content: str) -> int:
        lines = self.lines(content)
        pos, depth = 0, 0
        for line in lines:
            command, value = line.split(" ")
            if command == "forward":
                pos += int(value)
            elif command == "up":
                depth -= int(value)
            elif command == "down":
                depth += int(value)
        return pos * depth

    def part2(self, content: str) -> int:
        lines = self.lines(content)
        pos, depth, aim = 0, 0, 0
        for line in lines:
            command, value = line.split(" ")
            if command == "forward":
                pos += int(value)
                depth += aim * int(value)
            elif command == "up":
                aim -= int(value)
            elif command == "down":
                aim += int(value)

        return pos * depth
