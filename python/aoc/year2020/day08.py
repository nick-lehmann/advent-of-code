from dataclasses import dataclass
from enum import Enum
from typing import Iterable, List
from ..utils import AOCTestCase


class Operation(Enum):
    Accumulate = "acc"
    Jump = "jmp"
    Nop = "nop"

    @classmethod
    def value_of(cls, value: str) -> "Operation":
        for k, v in cls.__members__.items():
            if v.value == value:
                return v
        else:
            raise ValueError(f"'{cls.__name__}' enum not found for '{value}'")


@dataclass
class Instruction:
    operation: Operation
    value: int

    def __str__(self) -> str:
        return f"{self.operation.value} {self.value}"


def parse_instruction(line: str) -> Instruction:
    operation, value = line.split(" ")
    return Instruction(operation=Operation.value_of(operation), value=int(value))


def parse_instructions(lines: List[str]) -> Iterable[Instruction]:
    return map(parse_instruction, lines)


class HandheldHalting(AOCTestCase):
    day = 8
    year = 2020

    def part1(self, content: str) -> int:
        instructions = list(parse_instructions(self.lines(content)))

        accumulator = 0
        step = 0
        already_executed = set()

        while True:
            instruction = instructions[step]

            if step in already_executed:
                return accumulator

            already_executed |= {step}
            if instruction.operation == Operation.Accumulate:
                accumulator += instruction.value
                step += 1
            elif instruction.operation == Operation.Jump:
                step += instruction.value
            else:
                step += 1

    def part2(self, content: str) -> int:
        pass
