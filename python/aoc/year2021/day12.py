# Link: https://adventofcode.com/2021/day/12
from typing import Dict
from ..utils import AOCTestCase
from collections import defaultdict

START = "start"
END = "end"


class PassagePathing(AOCTestCase):
    day = 12
    year = 2021

    paths: Dict[str, set]

    def has_visited(self, node: str):
        return {node} if node.islower() else set()

    def find_paths(self, node: str, visited: set[str]) -> int:
        """DFS Path finding."""
        if node == "end":
            return 1

        if node.islower():
            visited = visited.copy() | {node}

        next_nodes = self.paths[node] - visited
        return sum(self.find_paths(next_node, visited) for next_node in next_nodes)

    def read(self, content) -> Dict[str, set]:
        lines = self.lines(content)
        paths = defaultdict(set)
        for line in lines:
            a, b = line.split("-")
            paths[a] |= {b}
            paths[b] |= {a}
        return paths

    def part1(self, content: str) -> int:
        self.paths = self.read(content)
        return self.find_paths(START, set())

    # def part2(self, content: str) -> int:
    #     paths = self.read(content)
    #     return self.dfs(paths, START, {START}, True)
