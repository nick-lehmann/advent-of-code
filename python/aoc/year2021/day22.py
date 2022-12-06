# Link: https://adventofcode.com/2021/day/22
from typing import List
from ..utils import AOCTestCase
import re
from dataclasses import dataclass


@dataclass
class Instruction:
    state: bool
    x: range
    y: range
    z: range


class ReactorReboot(AOCTestCase):
    day = 22
    year = 2021

    def read(self, content) -> List[Instruction]:
        pattern = r"(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)"
        ranges = re.findall(pattern, content)

        instructions = []
        for r in ranges:
            instructions += [
                Instruction(
                    state=r[0] == "on",
                    x=range(int(r[1]), int(r[2]) + 1),
                    y=range(int(r[3]), int(r[4]) + 1),
                    z=range(int(r[5]), int(r[6]) + 1),
                )
            ]

        return instructions

    def part1(self, content: str) -> int:
        ranges = self.read(content)
        maxX, maxY, maxZ = 50, 50, 50
        # TODO: Create helper function to create a 2D and 3D array with default value
        cubes = [[[False] * maxZ] * maxY] * maxX

        for r in ranges:
            print(r)

        total = 0
        for r in ranges:
            for x in r.x:
                for y in r.y:
                    for z in r.z:
                        cell = cubes[x][y][z]
                        if cell:
                            if not r.state:
                                pass
                                # total -= 1
                        if not cell:
                            if r.state:
                                total += 1
                        cubes[x][y][z] = r.state

        return total

    def part2(self, content: str) -> int:
        pass
