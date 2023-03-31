# Link: https://adventofcode.com/2020/day/20
from typing import List
from ..utils import AOCTestCase
from dataclasses import dataclass


@dataclass
class Tile:
    id: int
    content: List[str]

    @property
    def left_border(self) -> List[str]:
        return [line[0] for line in self.content]

    @property
    def right_border(self) -> List[str]:
        return [line[-1] for line in self.content]

    @property
    def top_border(self) -> List[str]:
        return self.content[0]

    @property
    def right_border(self) -> List[str]:
        return self.content[-1]


class JurassicJigsaw(AOCTestCase):
    day = 20
    year = 2020

    def part1(self, content: str) -> int:
        raw_tiles = content.split("\n\n")
        tiles = []
        for tile in raw_tiles:
            tiles.append(Tile(id=int(tile[0].split(" ")[1]), content=tile[1:]))

    def part2(self, content: str) -> int:
        pass
