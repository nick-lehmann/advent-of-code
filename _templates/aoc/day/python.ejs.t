---
to: python/<%= year %>/day<%= day %>.py
---
from utils import AOCTestCase
import unittest


class <%= name %>(AOCTestCase):
    def part1(self) -> int:
        pass

    def part2(self) -> int:
        pass


if __name__ == "__main__":
    unittest.main()


