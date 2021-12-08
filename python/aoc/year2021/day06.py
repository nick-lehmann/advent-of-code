# Link: https://adventofcode.com/2021/day/6
from ..utils import AOCTestCase
from collections import defaultdict


class Lanternfish(AOCTestCase):
    day = 6
    year = 2021

    def read(self, content):
        fishesList = [int(x) for x in content.strip().split(',')]
        
        fishes = defaultdict(int)
        for fish in fishesList:
            fishes[fish] += 1
        
        return fishes

    def play(self, fishes, rounds):
        for day in range(1,rounds+1):
            new_fishes = defaultdict(int)
            
            for age, count in fishes.items(): 
                if age == 0:
                    new_fishes[6] += count
                    new_fishes[8] += count
                else:
                    new_fishes[age - 1] += count

            fishes = new_fishes
            
        return sum(fish for fish in fishes.values())

        

    def part1(self, content: str) -> int:
        fishes = self.read(content)
        return self.play(fishes, 80)

    def part2(self, content: str) -> int:
        fishes = self.read(content)
        return self.play(fishes, 256)
