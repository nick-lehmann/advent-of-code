# Link: https://adventofcode.com/2021/day/9
from ..utils import AOCTestCase


class TheTreacheryOfWhales(AOCTestCase):
    day = 7
    year = 2021

    def part1(self, content: str) -> int:
        positions = [int(x) for x in self.lines(content)[0].split(',')]
        
        min_fuel = 10000000000
        for alignment in range(max(positions)):
            fuel = sum(abs(pos - alignment) for pos in positions)
            min_fuel = min(min_fuel, fuel) 
        return min_fuel
            
    def part2(self, content: str) -> int:
        positions = [int(x) for x in self.lines(content)[0].split(',')]
        
        min_fuel = 10000000000
        for alignment in range(max(positions)):
            fuel = sum((abs(alignment - pos) ** 2 + abs(alignment - pos)) // 2 for pos in positions)
            min_fuel = min(min_fuel, fuel) 
        return min_fuel
