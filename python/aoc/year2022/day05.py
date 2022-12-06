# Link: https://adventofcode.com/2022/day/5
from ..utils import AOCTestCase
from dataclasses import dataclass


@dataclass
class Instruction:
    count: int
    source: int
    destination: int


class SupplyStacks(AOCTestCase):
    day = 5
    year = 2022

    def parse_stacks(self, lines) -> list[list[int]]:
        description = lines[-1]
        l = len(description.replace(" ", ""))
        stacks = [[] for _ in range(l)]
        for line in lines[:-1]:
            for i, x in enumerate(range(1, len(line), 4)):
                if line[x] != " ":
                    stacks[i].append(line[x])

        print(stacks)
        return stacks

    def parse_instructions(self, lines: list[str]) -> list[Instruction]:
        instructions = []
        for line in lines:
            parts = line.split(" ")
            instructions.append(
                Instruction(
                    count=int(parts[1]),
                    source=int(parts[3]) - 1,
                    destination=int(parts[5]) - 1,
                )
            )
        return instructions

    def part1(self, content: str) -> str:
        (stacks, instructions) = content.split("\n\n")
        stacks = self.lines(stacks)[1:]
        instructions = self.lines(instructions)

        stacks = self.parse_stacks(stacks)
        instructions = self.parse_instructions(instructions)

        for instruction in instructions:
            for _ in range(instruction.count):
                stacks[instruction.destination] = [
                    stacks[instruction.source].pop(0)
                ] + stacks[instruction.destination]

        return "".join([stack[0] for stack in stacks])

    def part2(self, content: str) -> str:
        (stacks, instructions) = content.split("\n\n")
        stacks = self.lines(stacks)[1:]
        instructions = self.lines(instructions)

        stacks = self.parse_stacks(stacks)
        instructions = self.parse_instructions(instructions)

        for i in instructions:
            stacks[i.destination] = stacks[i.source][: i.count] + stacks[i.destination]
            stacks[i.source] = stacks[i.source][i.count :]

        return "".join([stack[0] for stack in stacks])
