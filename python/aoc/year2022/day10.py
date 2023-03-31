# Link: https://adventofcode.com/2022/day/10
from ..utils import AOCTestCase


class CathodeRayTube(AOCTestCase):
    day = 10
    year = 2022

    def signals(self, lines, cycle=0, register=1):
        for line in lines:
            if line.startswith("addx "):
                cycle += 2
                register += int(line[5:])
            else:
                cycle += 1
            yield cycle, register

    def part1(self, content: str) -> int:
        cycle, register = 0, 1
        signals = self.signals(self.lines(content))
        result = 0
        for i in [20, 60, 100, 140, 180, 220]:
            last_register = register
            while cycle < i:
                last_register = register
                cycle, register = next(signals)
            result += i * last_register
        return result

    def part2(self, content: str) -> int:
        cycle, register, last_register = 0, 1, 1
        signals = self.signals(self.lines(content))
        result = []
        for row in range(6):
            line = ""
            for col in range(40):
                while cycle <= 40 * row + col:
                    last_register = register
                    cycle, register = next(signals)
                line += "\u2593" if -1 <= last_register - col <= 1 else "\u2591"
            result.append(line)

        screen = "\n".join(result)
        print(screen)
        return screen
