# Link: https://adventofcode.com/2021/day/12
from typing import Dict
from ..utils import AOCTestCase
from collections import defaultdict

START = "start"
END = "end"

class PassagePathing(AOCTestCase):
    day = 12
    year = 2021

    def dfs(self, paths, start, visited, visit_twice) -> int:
        if start == END:
            return 1

        count = 0
        for end in paths[start]:
            if end not in visited:
                tmp = {end} if end == end.lower() else set()
                count += self.dfs(paths, end, visited | tmp, visit_twice)
            elif visit_twice and end != START:
                count += self.dfs(paths, end, visited, False)

        return count

    def read(self, content) -> Dict[str, set]:
        lines = self.lines(content)
        paths = defaultdict(set)
        for line in lines:
            a, b = line.split('-')
            paths[a] |= {b}
            paths[b] |= {a}
        return paths


    def part1(self, content: str) -> int:
        paths = self.read(content)           
        return self.dfs(paths, START, {START}, False)
        

    def part2(self, content: str) -> int:
        paths = self.read(content)           
        return self.dfs(paths, START, {START}, True)
