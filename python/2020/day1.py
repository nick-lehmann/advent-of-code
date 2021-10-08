from typing import Set
from itertools import combinations


def part1(numbers: Set[int]) -> int:
    for number in numbers:
        remainder = 2020 - number
        if remainder in numbers:
            return number * remainder


def part2(numbers: Set[int]):
    for combo in combinations(numbers, 2):
        remainder = 2020 - sum(combo)
        if remainder in numbers:
            return combo[0] * combo[1] * remainder


if __name__ == "__main__":
    with open("../../exercises/2020/01.txt") as file:
        numbers = set([int(line) for line in file.readlines()])
        print(part1(numbers))
        print(part2(numbers))
