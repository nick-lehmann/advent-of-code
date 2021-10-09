from utils import AOCTestCase
import unittest


class BinaryBoarding(AOCTestCase):
    def part1(self) -> int:
        line = self.lines[0]
        return int(
            line.replace("F", "0")
            .replace("B", "1")
            .replace("L", "0")
            .replace("R", "1"),
            2,
        )

    def part2(self):
        pass


if __name__ == "__main__":
    unittest.main()
