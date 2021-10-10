import re
from functools import cache
from collections import deque
from typing import Dict, List, Tuple

from ..utils import AOCTestCase

line_pattern = r"(\w+ \w+) bags contain (.*)"
single_item_pattern = r"(\d+) (\w+ \w+) bags?"

Color = str


class HandyHaversacks(AOCTestCase):
    day = 7
    year = 2020

    def parse(self, lines: str) -> Dict[Color, List[Tuple[int, Color]]]:
        bags = {}
        for line in lines:
            bag, items = re.match(line_pattern, line).groups()
            bags[bag] = [
                (int(match.group(1)), match.group(2))
                for match in re.finditer(single_item_pattern, items)
            ]
        return bags

    def part1(self, content: str) -> int:
        rules = self.parse(self.lines(content))

        @cache
        def is_gold(item):
            return any(
                subitem == "shiny gold" or is_gold(subitem)
                for _, subitem in rules.get(item, ())
            )

        return sum(map(is_gold, rules))

    def part2(self, content: str) -> int:
        rules = self.parse(self.lines(content))
        queue = deque(rules.get("shiny gold", ()))
        total = 0
        while queue:
            count, color = queue.popleft()
            total += count
            queue.extend(
                ((count * subcount, subcolor) for subcount, subcolor in rules[color])
            )
        return total
