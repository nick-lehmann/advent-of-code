# Link: https://adventofcode.com/2022/day/3
from ..utils import AOCTestCase


class RucksackReorganization(AOCTestCase):
    day = 3
    year = 2022

    def priority(self, c: str) -> int:
        return ord(c) - ord("a") + 1 if c.islower() else ord(c) - ord("A") + 27

    def part1(self, content: str) -> int:
        lines = self.lines(content)
        s = 0
        for line in lines:
            middle = len(line) // 2
            first = line[:middle]
            second = line[middle:]

            common = ""
            for c in first:
                if c in second:
                    common = c
                    break

            priority = self.priority(common)
            # print(f"Common: {common} ({priority})")
            s += priority

        return s

    def part2(self, content: str) -> int:
        lines = self.lines(content)
        s = 0

        for i in range(0, len(lines), 3):
            (l1, l2, l3) = map(set, lines[i : i + 3])
            common = list(l1 & l2 & l3)[0]
            priority = self.priority(common)

            # print(f"Common: {common} ({priority})")
            s += priority

        return s
