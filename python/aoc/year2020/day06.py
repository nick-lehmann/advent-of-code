from string import ascii_lowercase
from typing import List
from ..utils import AOCTestCase


def count_anyone_in_block(lines: List[str]) -> int:
    answers = set()
    for line in lines:
        answers |= set(line)
    return len(answers)


def count_everyone_in_block(lines: List[str]) -> int:
    answers = set(ascii_lowercase)
    for line in lines:
        answers &= set(line)
    return len(answers)


class CustomCustoms(AOCTestCase):
    day = 6
    year = 2020

    def part1(self, content: str) -> int:
        blocks = self.blocks(content)
        return sum(count_anyone_in_block(block.split("\n")) for block in blocks)

    def part2(self, content: str) -> int:
        blocks = self.blocks(content)
        blocks[-1] = blocks[-1].strip("\n")
        temp = [count_everyone_in_block(block.split("\n")) for block in blocks]
        return sum(temp)
