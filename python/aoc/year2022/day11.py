# Link: https://adventofcode.com/2022/day/11
from ..utils import AOCTestCase
from dataclasses import dataclass
from pprint import pprint
import math


class MonkeyInTheMiddle(AOCTestCase):
    day = 11
    year = 2022

    @dataclass
    class Monkey:
        items: list[int]
        operation: str
        modulo: int

        interactions = 0
        transitions: tuple[int, int]

    def read(self, content: str) -> list[Monkey]:
        monkeys = []
        for lines in content.split("\n\n"):
            lines = lines.split("\n")
            monkeys += [
                self.Monkey(
                    items=[int(item) for item in lines[1].split(":")[1].split(", ")],
                    operation=lines[2].split(" = ")[1],
                    modulo=int(lines[3].split("by ")[1]),
                    transitions=[
                        int(lines[5].split(" ")[-1]),
                        int(lines[4].split(" ")[-1]),
                    ],
                )
            ]
        return monkeys

    def play(self, monkeys: list[Monkey], rounds: int) -> int:
        for round in range(1, rounds + 1):
            print(f"# Round {round}")
            for monkey in monkeys:
                for item in monkey.items:
                    monkey.interactions += 1
                    new_item = eval(monkey.operation.replace("old", str(item))) // 3
                    test = new_item % monkey.modulo == 0
                    new_monkey = monkey.transitions[test]
                    monkeys[new_monkey].items += [new_item]
                monkey.items = []

            for i, monkey in enumerate(monkeys):
                print(f"Monkey {i}: {monkey.items}")

        interactions = sorted([monkey.interactions for monkey in monkeys], reverse=True)
        return interactions[0] * interactions[1]

    def part1(self, content: str) -> int:
        monkeys = self.read(content)
        pprint(monkeys)
        result = self.play(monkeys, 20)
        print(f"Result: {result}")
        return result

    def play2(self, monkeys: list[Monkey], rounds: int) -> int:
        x = math.lcm(*[monkey.modulo for monkey in monkeys])
        for round in range(1, rounds + 1):
            # print(f"# Round {round}")
            for monkey in monkeys:
                for item in monkey.items:
                    monkey.interactions += 1
                    new_item = eval(monkey.operation.replace("old", str(item))) % x
                    test = new_item % monkey.modulo == 0
                    new_monkey = monkey.transitions[test]
                    monkeys[new_monkey].items += [new_item]
                monkey.items = []

            # for i, monkey in enumerate(monkeys):
            #     print(f"Monkey {i}: {monkey.items}")

        interactions = sorted([monkey.interactions for monkey in monkeys], reverse=True)
        return interactions[0] * interactions[1]

    def part2(self, content: str) -> int:
        monkeys = self.read(content)
        pprint(monkeys)
        result = self.play2(monkeys, 10000)
        print(f"Result: {result}")
        return result
