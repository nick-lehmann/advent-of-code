# Link: https://adventofcode.com/2020/day/15
from ..utils import AOCTestCase
from collections import *


class RambunctiousRecitation(AOCTestCase):
    day = 15
    year = 2020

    def part1(self, content: str) -> int:
        x = {}
        turn = 0
        current_number = 0
        for i, n in enumerate(content.strip("\n").split(",")):
            x[int(n)] = i+1
            turn += 1
            current_number = n

        while turn != 6:
            if current_number not in x:
                x[0] = turn
                current_number = 0
            else:
                current_number = x[current_number] - turn
                x[current_number] = turn
            turn += 1
            print(f"Step {turn}: {current_number} {x}")

        return current_number

    def part2(self, content: str) -> int:
        pass
