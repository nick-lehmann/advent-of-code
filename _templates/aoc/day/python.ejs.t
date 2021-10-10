---
to: python/aoc/year<%= year %>/day<%= dayPadded %>.py
unless_exists: true
---
from ..utils import AOCTestCase


class <%= name %>(AOCTestCase):
    day = <%= day %>
    year = <%= year %>

    def part1(self, content: str) -> int:
        pass

    def part2(self, content: str) -> int:
        pass
