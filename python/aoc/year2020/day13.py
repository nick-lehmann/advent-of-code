# Link: https://adventofcode.com/2020/day/13
from ..utils import AOCTestCase
from functools import reduce


def chinese_remainder(residues, moduli):
    sum = 0
    prod = reduce(lambda a, b: a*b, moduli)
    for n_i, a_i in zip(moduli, residues):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


class ShuttleSearch(AOCTestCase):
    day = 13
    year = 2020

    def part1(self, content: str) -> int:
        lines = self.lines(content)
        timestamp = int(lines[0])
        buses = [int(bus) for bus in lines[1].split(",") if bus != 'x']

        next_bus = None
        next_time = 1000000000000

        for bus in buses:
            arrvies_at = (timestamp // bus + 1) * bus - timestamp
            if arrvies_at < next_time:
                next_time = arrvies_at
                next_bus = bus

        return next_bus * next_time

    def part2(self, content: str) -> int:
        lines = self.lines(content)

        mods = []
        residues = []
        for offset, bus in enumerate(lines[1].split(',')):
            if bus == 'x':
                continue
            mods += [int(bus)]
            residues += [int(bus)-offset]

        return chinese_remainder(residues, mods)
