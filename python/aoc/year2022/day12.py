# Link: https://adventofcode.com/2022/day/12
from collections import deque
from ..utils import AOCTestCase
from typing import Generator


def bfs(start, neighbours) -> Generator[tuple[int, int], None, None]:
    seen = {start}
    queue = deque(((start, 0),))
    while queue:
        item, depth = queue.popleft()
        yield item, depth
        wave = list(neighbours(item))
        # print(f"Next cells: {wave}")
        for neighbor in wave:
            if neighbor in seen:
                continue
            seen.add(neighbor)
            queue.append((neighbor, depth + 1))


def norm(cell: str) -> str:
    if cell == "S":
        return "a"
    if cell == "E":
        return "z"
    return cell


class HillClimbingAlgorithm(AOCTestCase):
    """
    Grid
    --> x
    |
    v y
    """

    day = 12
    year = 2022

    def part1(self, content: str) -> int:
        grid = self.map(content)
        height, width = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def find(cell: str) -> tuple[int, int]:
            for y, row in enumerate(grid):
                for x, c in enumerate(row):
                    if c == cell:
                        return (x, y)
            raise ValueError(f"Cell {cell} not found")

        def in_bounds(x: int, y: int) -> bool:
            return 0 <= x < width and 0 <= y < height

        def reachable(cell1: str, cell2: str) -> bool:
            return abs(ord(cell1) - ord(cell2)) <= 1

        def neighbours(pos: tuple[int, int]) -> list[tuple[int, int]]:
            x, y = pos
            cell = norm(grid[y][x])
            for dy, dx in directions:
                new_x, new_y = x + dx, y + dy
                other = norm(grid[new_y][new_x])
                if in_bounds(new_x, new_y) and reachable(cell, other):
                    yield (x + dx, y + dy)

        end = find("E")
        print(f"End: {end}")
        print(list(bfs(end, neighbours)))
        for new in bfs(end, neighbours):
            print(new)
            (x, y), depth = new
            if grid[y][x] == "S":
                return depth
        raise Exception("Unable to come back to start")

    def part2(self, content: str) -> int:
        pass
